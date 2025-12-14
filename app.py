import streamlit as st
from github_fetcher import fetch_repo_data
from evaluator import evaluate_repo
from roadmap import generate_feedback

st.title("📊 Repository Mirror – AI Code Evaluator")

repo_url = st.text_input("Enter GitHub Repository URL")

if st.button("Analyze Repository"):
    data = fetch_repo_data(repo_url)
    score, level = evaluate_repo(data)
    summary, roadmap = generate_feedback(data)

    st.subheader(f"Score: {score}/100")
    st.write(f"Level: {level}")
    st.write("### Summary")
    st.write(summary)

    st.write("### Personalized Roadmap")
    for step in roadmap:
        st.write("•", step)
