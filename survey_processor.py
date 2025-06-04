import spacy
import requests
import numpy as np


nlp = spacy.load("en_core_web_sm")

def extract_gender(name):
    try:
        first_name = name.split()[0]
        response = requests.get(f"https://api.genderize.io/?name={first_name}")
        return response.json().get("gender", "unknown")
    except:
        return "unknown"


def infer_profession_stress(job_title):
    title = job_title.lower()
    if "manager" in title or "analyst" in title:
        return {"cortisol": 0.7, "dopamine": 0.6}
    elif "engineer" in title or "developer" in title:
        return {"dopamine": 0.8, "gaba": 0.4}
    return {"cortisol": 0.5, "dopamine": 0.5}


def analyze_routine(routine_text):
    if "6 AM" in routine_text or "morning" in routine_text:
        return {"cortisol": 0.6, "serotonin": 0.3}
    return {"cortisol": 0.3, "serotonin": 0.2}

def sentiment_keywords(text):
    doc = nlp(text)
    sentiment_map = {"stress": 0, "focus": 0}
    for token in doc:
        if token.text.lower() in ["stress", "rushed", "overwhelmed"]:
            sentiment_map["stress"] += 1
        elif token.text.lower() in ["focus", "productive"]:
            sentiment_map["focus"] += 1
    return sentiment_map





scent_to_neuro = {
    "vanilla": "oxytocin",
    "mint": "serotonin",
    "tonka bean": "oxytocin",
    "lavender": "gaba",
    "citrus": "dopamine",
    "wood": "gaba",
    "cinnamon": "dopamine",
    "bergamot": "serotonin"
}

def map_scent_to_neuro(scent_name):
    scent_notes = []

    scent_name = scent_name.lower()
    if "versace eros" in scent_name:
        scent_notes = ["vanilla", "tonka bean", "mint"]
    elif "lavender" in scent_name:
        scent_notes = ["lavender"]
    elif "lemon" in scent_name or "citrus" in scent_name:
        scent_notes = ["citrus"]
    elif "wood" in scent_name or "oak" in scent_name:
        scent_notes = ["wood"]
    elif "cinnamon" in scent_name:
        scent_notes = ["cinnamon"]


    neuro_map = {}
    for note in scent_notes:
        neuro = scent_to_neuro.get(note)
        if neuro:
            neuro_map[neuro] = neuro_map.get(neuro, 0) + 0.4  

    return neuro_map


def analyze_childhood_scent_memory(memory_text):
    memory_notes = []

    memory_text = memory_text.lower()
    if "bread" in memory_text or "baking" in memory_text:
        memory_notes = ["vanilla", "cinnamon"]
    if "wood" in memory_text or "rain" in memory_text:
        memory_notes = ["wood"]
    if "flowers" in memory_text or "roses" in memory_text:
        memory_notes = ["lavender"]


    neuro_map = {}
    for note in memory_notes:
        neuro = scent_to_neuro.get(note)
        if neuro:
            neuro_map[neuro] = neuro_map.get(neuro, 0) + 0.5  

    return neuro_map






def neurotransmitter_vector(profile):
    neurotransmitters = ["dopamine", "serotonin", "oxytocin", "gaba", "cortisol"]
    vector = []

    for nt in neurotransmitters:
        total = 0
        for section in profile.values():
            if isinstance(section, dict):
                total += section.get(nt, 0)
        vector.append(total)

    return np.array([vector], dtype='float32')



def build_cognitive_twin(data):
    profile = {}


    profile["gender"] = extract_gender(data.get("name", ""))
    profile["profession_stress"] = infer_profession_stress(data.get("job_title", ""))
    profile["routine_effects"] = analyze_routine(data.get("daily_routine", ""))
    profile["workplace_stress"] = sentiment_keywords(data.get("workplace_limitation", ""))
    profile["scent_profile"] = map_scent_to_neuro(data.get("favorite_scent", ""))
    profile["childhood_memory"] = analyze_childhood_scent_memory(data.get("childhood_scent_memory", ""))

    return profile
