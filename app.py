import streamlit as st
import requests

st.set_page_config(page_title="Cognitive Twin Builder")

st.title(" Cognitive Twin Builder")

st.markdown("Fill in the form below to generate your cognitive twin and find similar ones.")

# --- Form ---
with st.form("twin_form"):
    name = st.text_input("Full Name")
    email = st.text_input("Email Address")
    job_title = st.text_input("Job Title")
    routine = st.text_area("Describe your daily routine")
    limitation = st.text_area("What limits your productivity?")
    scent = st.text_input("Favorite perfume, cologne, or candle")
    memory = st.text_area("Describe a childhood memory associated with scent")
    submitted = st.form_submit_button("Generate Cognitive Twin")

# --- On Submit ---
if submitted:
    payload = {
        "name": name,
        "email": email,
        "job_title": job_title,
        "daily_routine": routine,
        "workplace_limitation": limitation,
        "favorite_scent": scent,
        "childhood_scent_memory": memory
    }

    # POST to Flask API
    try:
        create_res = requests.post("http://127.0.0.1:8000/create_twin", json=payload)
        search_res = requests.post("http://127.0.0.1:8000/search_similar", json=payload)

        if create_res.status_code == 200:
            st.success(" Cognitive Twin created!")
            st.json(create_res.json())

        if search_res.status_code == 200:
            st.subheader("🔍 Similar Twins:")
            for twin in search_res.json()["results"]:
                st.markdown(f"**UUID**: {twin['uuid']}")
                st.markdown(f"**Distance**: {round(twin['distance'], 4)}")
                st.markdown(f"**Profile Summary**: {twin['profile']}")
                st.markdown("---")
        else:
            st.error("Could not fetch similar twins.")
    except Exception as e:
        st.error(f"Error connecting to API: {e}")

