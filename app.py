import streamlit as st
import json

st.set_page_config(page_title="OpenLaw SA", layout="wide")

# --- Mission ---
st.title("📚 OpenLaw SA")
st.markdown("**Making South African law searchable, understandable, and open to all.**")

# --- What is OpenLaw SA ---
st.markdown("""
OpenLaw SA is South Africa’s first unified legal intelligence platform.  
It’s built for lawyers, students, researchers, and citizens who need structured, reliable access to case law, legislation, and legal insights — all in one place.
""")

# --- Vision & Values ---
st.markdown("""
### 🌍 Vision & Values
- **Access for All** – Legal knowledge should be open and understandable.  
- **Plain Language First** – We prioritise human-friendly summaries.  
- **Legal Data + Evidence** – Connecting law to lived realities.  
- **Open Infrastructure** – Built for integration and community contribution.
""")

# --- Beta Notice ---
st.markdown("""
### 🚧 Beta Notice
This app is currently in **public beta**.  
Some features are still being built -- but we'd love your feedback!

👉 [Join the Beta Waiting List](https://forms.gle/9wnqR9jbRy6M5SMi8)
""", unsafe_allow_html=True)

# --- Data Provenance ---
st.markdown("""
### 🏛️ Data Provenance
OpenLaw SA draws its data from well-established and publicly available legal repositories, including:

- [**SAFLII**](https://www.saflii.org/)
- [**Laws.Africa**](https://laws.africa)
- [**AfricanLII**](https://www.africanlii.org)
- [**Government Gazette Archives**](https://www.gov.za/documents/publications/government-gazette)
""", unsafe_allow_html=True)

# --- Search ---
st.markdown("### 🔍 Search Legal Content")
query = st.text_input("Enter a topic, case name, or keyword", placeholder="e.g. eviction, constitutional rights")

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

# --- Join Beta CTA ---
st.markdown("""
### 🚀 Join the Beta Waiting List

OpenLaw SA is launching soon with advanced legal search, citation networks, watchlists, and structured case data.

Be the first to access premium features like:
- Smart precedent mapping
- Saved research trails
- Legal-grade API endpoints

📬 [Join the Waiting List](https://forms.gle/9wnqR9jbRy6M5SMi8)  
We’ll contact you as soon as new slots open.
""", unsafe_allow_html=True)

# --- Trust Sections ---
st.markdown("""
### 👥 Who's Behind This?
OpenLaw SA is built by Dotsimple Holdings (Pty) Ltd -- a South African company focused on creating technology for public good.  
We work with legal researchers and technologists to improve access to justice through open legal data.

### 🔐 Privacy Commitment
We do not require logins or collect personal data. Your searches stay private and no analytics are used to track your activity at this stage of the beta.

### ⚠️ Legal Notice
OpenLaw SA provides legal information -- not legal advice.  
Please consult a qualified legal professional before making legal decisions. Our summaries are for reference and should always be cross-checked with the full judgment.
""")

# --- FAQ Section ---
st.markdown("### ❓ Frequently Asked Questions (FAQs)")

with st.expander("🔎 What makes OpenLaw SA different from other legal search tools?"):
    st.markdown("OpenLaw SA is built exclusively for South African legal professionals. It combines verified court judgments with plain-language summaries, structured citation mapping, and topic tags -- all tailored for speed, clarity, and local relevance.")

with st.expander("📘 What does OpenLaw SA cover (and not cover)?"):
    st.markdown("""
    OpenLaw SA is committed to providing accessible and reliable legal information to South African legal professionals. Our platform currently includes:

    - **Case Law**: Judgments from various South African courts, sourced from the Southern African Legal Information Institute (SAFLII).
    - **Legislation**: National and provincial legislation, as well as municipal by-laws, obtained through partnerships with organizations like Laws.Africa.
    - **Government Gazettes**: Official notices and publications from the Government Gazette Archives.

    While we strive to offer comprehensive legal resources, please note that our platform does not currently include:

    - **Proprietary Legal Commentaries**: Such as those found in subscription-based services like LexisNexis or Juta.
    - **Academic Legal Journals**: Articles and analyses published in legal journals and periodicals.
    - **Practice Manuals and Directives**: Internal guidelines and procedural manuals used within specific legal institutions.

    We are continually working to expand our database and welcome feedback on additional resources that would benefit our users.
    """)

with st.expander("🆓 Is this free to use?"):
    st.markdown("The core search and summary features are free during public beta. Premium features (like citation graphs, watchlists, and API access) will be available through a paid beta tier, launching soon.")

with st.expander("📚 Where does your legal data come from?"):
    st.markdown("All case data is sourced from open-access legal repositories including SAFLII, Laws.Africa, and the Government Gazette -- ensuring transparency and accuracy.")

with st.expander("⚖️ Can I rely on this for formal legal work?"):
    st.markdown("Yes -- all summaries are linked directly to the original, cited judgments. While summaries assist with research, only the full text of the judgment should be relied on for legal submissions or litigation.")

with st.expander("🔐 Do you store my personal data?"):
    st.markdown("We currently do not require user accounts. If/when account features launch, your email or usage info will be stored securely and never sold or shared without consent.")

with st.expander("📬 How do I give feedback or join the beta?"):
    st.markdown("Submit your details via our [beta waiting list form](https://forms.gle/9wnqR9jbRy6M5SMi8)")

# --- Footer ---
st.markdown("""
---
© 2025 **Dotsimple Holdings (Pty) Ltd**  
OpenLaw SA is a product of Dotsimple, built to make law accessible, open, and actionable.  
Questions or ideas? [Join the Waiting List](https://forms.gle/9wnqR9jbRy6M5SMi8)
""", unsafe_allow_html=True)