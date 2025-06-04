
from survey_processor import extract_gender, infer_profession_stress, analyze_routine, sentiment_keywords

sample_data = {
    "name": "Alejandro Ruiz",
    "job_title": "Software Engineer",
    "daily_routine": "I wake up at 6 AM and go for a jog. Then I work until evening.",
    "workplace_limitation": "Too many meetings and not enough time to focus."
}

print("Gender:", extract_gender(sample_data["name"]))
print("Job Stress:", infer_profession_stress(sample_data["job_title"]))
print("Routine Neuro Map:", analyze_routine(sample_data["daily_routine"]))
print("Workplace Limitation Sentiments:", sentiment_keywords(sample_data["workplace_limitation"]))



from survey_processor import map_scent_to_neuro, analyze_childhood_scent_memory

scent = "Versace Eros"
childhood_memory = "The smell of rain on wood always reminded me of home."

print("Scent Profile:", map_scent_to_neuro(scent))
print("Childhood Memory Profile:", analyze_childhood_scent_memory(childhood_memory))


from survey_processor import build_cognitive_twin, neurotransmitter_vector

sample_input = {
    "name": "Alejandro Ruiz",
    "job_title": "Software Engineer",
    "daily_routine": "I wake up at 6 AM and go for a jog.",
    "workplace_limitation": "Too many meetings and not enough time to focus.",
    "favorite_scent": "Versace Eros",
    "childhood_scent_memory": "The smell of rain on wood always reminded me of home."
}

profile = build_cognitive_twin(sample_input)
vector = neurotransmitter_vector(profile)

print("Cognitive Twin Profile:", profile)
print("Neurotransmitter Vector:", vector)
