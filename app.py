# app.py — DataMatchAI: Dataset Suitability Checker
import streamlit as st
import pandas as pd
import os
import json
from generator import query_suitable_datasets

st.set_page_config(page_title="DataMatchAI - Dataset Finder", page_icon="🔍", layout="wide")
st.title("🔍 DataMatchAI: Find Relevant Datasets for Your Research Goal")

st.markdown("Enter your research objective below. DataMatchAI will find and explain public datasets that match your goal.")

if "history" not in st.session_state:
    st.session_state.history = []

query = st.text_input("🧠 Your Research Goal", placeholder="e.g. detecting depression via social media text")

col1, col2 = st.columns([1, 2])
with col1:
    if st.button("🔎 Find Datasets") and query:
        st.session_state.history.append(query)
        with st.spinner("Searching for relevant datasets using AI..."):
            results = query_suitable_datasets(query)
            st.session_state.results = results

with col2:
    if st.session_state.get("results"):
        st.subheader("📄 Suggested Datasets")
        df = pd.DataFrame(st.session_state.results)
        st.dataframe(df, use_container_width=True)
        csv = df.to_csv(index=False).encode("utf-8")
        st.download_button("⬇️ Download Results as CSV", csv, file_name="dataset_matches.csv")

st.markdown("---")
st.markdown("### 📜 Search History")
for i, q in enumerate(reversed(st.session_state.history)):
    if st.button(q, key=f"past_query_{i}"):
        with st.spinner("Re-analyzing..."):
            results = query_suitable_datasets(q)
            st.session_state.results = results
