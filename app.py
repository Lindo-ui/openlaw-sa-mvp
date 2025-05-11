import streamlit as st
import json

st.set_page_config(page_title="OpenLaw SA", layout="wide")

# --- Beta Ribbon ---
st.info("🧪 This is a public beta — features are evolving. [Join the Beta Waiting List](https://forms.gle/9wnqR9jbRy6M5SMi8)", icon="⚠️")

# --- Hero Section ---
st.title("📚 OpenLaw SA")
st.markdown("**Making South African law searchable, understandable, and open to all.**")

# --- Primary Action: Search ---
st.markdown("### 🔍 Search Case Law")
query = st.text_input("Search by judgment, topic, or keyword...", placeholder="e.g. eviction, constitutional rights")

import time

# --- Page Visit Logging ---
if "page_load_logged" not in st.session_state:
    try:
        with open("usage_log.txt", "a") as f:
            f.write(f"{time.time()} | visit\n")
        st.session_state["page_load_logged"] = True
    except:
        pass

# --- Search Query Logging ---
if query:
    try:
        with open("search_log.txt", "a") as log:
            log.write(f"{time.time()} | {query}\n")
    except:
        st.warning("Logging failed.")

import time

if query:
    try:
        with open("search_log.txt", "a") as log:
            log.write(f"{time.time()} | {query}\n")
    except Exception as e:
        st.warning("Logging failed.")

try:
    with open("sample_cases.json", "r") as f:
        data = json.load(f)
except:
    st.error("Could not load case data.")
    st.stop()

results = [
    case for case in data
    if query.lower() in case.get("title", "").lower()
    or query.lower() in case.get("summary", "").lower()
    or any(query.lower() in tag.lower() for tag in case.get("tags", []))
] if query else data

st.markdown(f"### 📄 {len(results)} Result(s) Found")


for case in results:
    with st.expander(f"{case.get('title')} ({case.get('court')}, {case.get('date')})"):
        try:
            with open("interaction_log.txt", "a") as f:
                f.write(f"{time.time()} | expanded | {case.get('title')}\n")
        except:
            pass

        st.write("**Summary:**", case.get("summary"))
        st.write("**Court:**", case.get("court"))
        st.write("**Tags:**", ", ".join(case.get("tags", [])))
        st.write("**Citations:**", ", ".join(case.get("citations", [])))
        st.write("**Precedents Cited:**")
        for p in case.get("precedents_cited", []):
            st.write(f"- {p}")
        st.write("**Full Text:**", case.get("source_link"))
        if case.get("pdf_link"):
            st.write("**PDF:**", case.get("pdf_link"))
# --- CTA: Join Beta ---
st.markdown("""
### 🚀 Join the Beta Waiting List
OpenLaw SA is launching soon with advanced legal search, citation networks, watchlists, and structured case data.

Be the first to access premium features like:
- Smart precedent mapping
- Saved research trails
- Legal-grade API endpoints

📬 [Join the Waiting List](https://forms.gle/9wnqR9jbRy6M5SMi8)
""", unsafe_allow_html=True)

# --- Expandable Info Cards ---
with st.expander("📘 What is OpenLaw SA?"):
    st.markdown("""
    OpenLaw SA is South Africa’s first unified legal intelligence platform.  
    Built for lawyers, students, researchers, and citizens — it makes legal information more accessible, structured, and actionable.
    """)

with st.expander("🌍 Vision & Values"):
    st.markdown("""
    - **Access for All** – Legal knowledge should be open and understandable.  
    - **Plain Language First** – We prioritise human-friendly summaries.  
    - **Legal Data + Evidence** – Connecting law to lived realities.  
    - **Open Infrastructure** – Built for integration and community contribution.
    """)

with st.expander("🏛️ Data Sources & Scope of Coverage"):
    st.markdown("""
    We source data from:
    - [**SAFLII**](https://www.saflii.org/)
    - [**Laws.Africa**](https://laws.africa)
    - [**AfricanLII**](https://www.africanlii.org)
    - [**Government Gazette Archives**](https://www.gov.za/documents/publications/government-gazette)

    **Current coverage includes:**
    - Constitutional Court and landmark judgments
    - National and provincial legislation
    - Public notices and government gazettes

    **Not yet included:**
    - Proprietary legal commentaries (Juta, Lexis)
    - Academic journals
    - Practice manuals or court directives
    """)

with st.expander("🔐 Privacy & Legal Disclaimer"):
    st.markdown("""
    We do not track you or require login — your searches stay private.  
    This platform provides **legal information**, not legal advice.  
    Always consult a qualified legal professional for formal decisions.
    """)

with st.expander("❓ FAQs"):
    st.markdown("""
    **Q: Is this free to use?**  
    Yes — core features are free during beta. Premium features will launch soon.

    **Q: How can I contribute or request features?**  
    [Join the waitlist](https://forms.gle/9wnqR9jbRy6M5SMi8) or email feedback.

    **Q: Can I rely on this for legal submissions?**  
    Only the full court judgment is legally binding. Use summaries to aid — not replace — formal review.
    """)

# --- Footer ---
st.markdown("""
---
© 2025 **Dotsimple Holdings (Pty) Ltd**  
OpenLaw SA is a product of Dotsimple, built to make law accessible, open, and actionable.  
[Join the Waiting List](https://forms.gle/9wnqR9jbRy6M5SMi8)
""", unsafe_allow_html=True)