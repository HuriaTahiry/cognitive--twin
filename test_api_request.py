import requests

payload = {
    "name": "Huria Tahiry",
    "job_title": "Cybersecurity Analyst",
    "daily_routine": "I wake up at 7 AM and read threat reports.",
    "workplace_limitation": "Too much alert fatigue and constant context switching.",
    "favorite_scent": "Lavender Breeze",
    "childhood_scent_memory": "The smell of wood reminds me of swing."
}

res = requests.post("http://127.0.0.1:8000/create_twin", json=payload)
print("Create Twin Response:", res.json())

search = requests.post("http://127.0.0.1:8000/search_similar", json=payload)
print("Search Similar Response:", search.json())

