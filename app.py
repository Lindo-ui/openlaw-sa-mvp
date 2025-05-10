
import streamlit as st
import json

st.set_page_config(page_title="OpenLaw SA", layout="wide")

# --- Landing Section ---
st.title("📚 OpenLaw SA")
st.subheader("South Africa's Unified Legal Intelligence Platform")

st.markdown("""
### 🧾 About OpenLaw SA
OpenLaw SA is building South Africa’s first unified legal intelligence platform.  
Our mission is to make law more **accessible**, **transparent**, and **usable** — by everyone.

### 🌍 Vision & Values
- **Access for All**: Legal knowledge should be open and understandable.  
- **Plain Language First**: We prioritise human-friendly summaries.  
- **Legal Data + Evidence**: Connecting law to lived realities.  
- **Open Infrastructure**: Built for integration and community input.

### 🚧 Beta Notice
This app is currently in **public beta**.  
Some features are still being built — but we’d love your feedback!

👉 [Send us feedback](mailto:feedback.dotsimple@gmail.com)
""", unsafe_allow_html=True)

# --- Search Input ---
st.markdown("### 🔍 Search Legal Content")
query = st.text_input("Enter a topic, case name, or keyword", placeholder="e.g. eviction, constitutional rights")

# --- Load JSON Data ---
try:
    with open("sample_cases.json", "r") as file:
        data = json.load(file)
except FileNotFoundError:
    st.error("sample_cases.json not found.")
    st.stop()

# --- Filter Results ---
if query:
    results = [
        case for case in data
        if query.lower() in case.get("title", "").lower()
        or query.lower() in case.get("summary", "").lower()
        or any(query.lower() in tag.lower() for tag in case.get("tags", []))
    ]
else:
    results = data

st.markdown(f"### 📄 {len(results)} Result(s) Found")

for case in results:
    title = case.get("title", "Untitled")
    court = case.get("court", "Unknown Court")
    date = case.get("date", "Unknown Date")

    with st.expander(f"{title} ({court}, {date})"):
        st.write("**Summary:**", case.get("summary", "No summary available."))
        st.write("**Court:**", court)
        st.write("**Tags:**", ", ".join(case.get("tags", [])))
        st.write("**Citations:**", ", ".join(case.get("citations", [])))
        st.write("**Precedents Cited:**")
        for p in case.get("precedents_cited", []):
            st.write(f"- {p}")
        st.write("**Full Text:**", case.get("source_link", "N/A"))
        if case.get("pdf_link"):
            st.write("**PDF Download:**", case["pdf_link"])

# --- Footer ---
st.markdown(
    """
---
© 2025 **Dotsimple Holdings (Pty) Ltd**  
OpenLaw SA is a product of Dotsimple, built to make law accessible, open, and actionable.  
Questions or ideas? [Send us feedback](mailto:feedback.dotsimple@gmail.com)
""", unsafe_allow_html=True
)
