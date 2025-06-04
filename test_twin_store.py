from twin_store import TwinStore
from survey_processor import build_cognitive_twin, neurotransmitter_vector


input_1 = {
    "name": "Alejandro Ruiz",
    "job_title": "Software Engineer",
    "daily_routine": "I wake up at 6 AM and go for a jog.",
    "workplace_limitation": "Too many meetings and not enough time to focus.",
    "favorite_scent": "Versace Eros",
    "childhood_scent_memory": "The smell of rain on wood always reminded me of home."
}

input_2 = {
    "name": "Emily Tran",
    "job_title": "Product Manager",
    "daily_routine": "I meditate every morning before work.",
    "workplace_limitation": "Rushed deadlines and lack of creative freedom.",
    "favorite_scent": "Lavender Breeze",
    "childhood_scent_memory": "Baking cookies with my grandmother every Sunday."
}


store = TwinStore()


uuid1, vec1 = store.add_twin(input_1)
uuid2, vec2 = store.add_twin(input_2)

print(f"Added twin 1: {uuid1}")
print(f"Added twin 2: {uuid2}")


print("\nTop similar twins to Alejandro:")
results = store.search_similar(vec1)
for r in results:
    print(r["uuid"], "| distance:", round(r["distance"], 4))

