import streamlit as st
import json

st.set_page_config(page_title="OpenLaw SA", layout="wide", initial_sidebar_state="collapsed")

# --- Title ---
st.title("OpenLaw SA – Legal Case Explorer")
st.caption("Explore landmark Constitutional Court decisions in South Africa")

# --- Load JSON data ---
try:
    with open("sample_cases.json", "r", encoding="utf-8") as f:
        case_data = json.load(f)
except Exception as e:
    st.error("Error loading case data. Please check your JSON file.")
    st.stop()

# --- Render cases ---
for case in case_data:
    with st.expander(f"📄 {case['title']} ({case['date']})"):
        st.markdown(f"**Court**: {case['court']}")
        st.markdown(f"**Case ID**: {case['case_id']}")
        st.markdown(f"**Jurisdiction**: {case['jurisdiction']}")
        st.markdown(f"**Tags**: {', '.join(case['tags'])}")
        st.markdown(f"**Summary:**\n\n{case['summary']}")
        
        st.markdown("**Citations:**")
        for cite in case["citations"]:
            st.markdown(f"- {cite}")

        st.markdown("**Precedents Cited:**")
        for precedent in case["precedents_cited"]:
            st.markdown(f"- {precedent}")
        
        if case.get("pdf_link"):
            st.markdown(f"[🔗 View Full Judgment (PDF)]({case['pdf_link']})", unsafe_allow_html=True)

### 📘 Scope of Coverage

OpenLaw SA is built on publicly accessible, high-integrity sources -- including SAFLII, Laws.Africa, the Government Gazette, and AfricanLII. This gives you reliable access to court judgments, legislation, and official legal notices across South Africa.

We focus on providing structured, plain-language insight into South African law -- but we currently do **not** include:
- Proprietary headnotes or annotations from commercial databases
- Academic legal commentary or treatises
- Procedural practice directives or Bar circulars

Our mission is to bridge that gap over time -- starting with transparent, structured law that everyone can access and understand.



### 📘 Scope of Coverage
OpenLaw SA is committed to providing accessible and reliable legal information to South African legal professionals. Our platform currently includes:

- **Case Law**: Judgments from various South African courts, sourced from the Southern African Legal Information Institute (SAFLII).
- **Legislation**: National and provincial legislation, as well as municipal by-laws, obtained through partnerships with organizations like Laws.Africa.
- **Government Gazettes**: Official notices and publications from the Government Gazette Archives.

While we strive to offer comprehensive legal resources, please note that our platform does not currently include:

- **Proprietary Legal Commentaries**: Such as those found in subscription-based services like LexisNexis or Juta.
- **Academic Legal Journals**: Articles and analyses published in legal journals and periodicals.
- **Practice Manuals and Directives**: Internal guidelines and procedural manuals used within specific legal institutions.

We are continually working to expand our database and welcome feedback on additional resources that would benefit our users.



### 👥 Who's Behind This?
OpenLaw SA is built by Dotsimple Holdings (Pty) Ltd -- a South African company focused on creating technology for public good.  
We work with legal researchers and technologists to improve access to justice through open legal data.

### 🔐 Privacy Commitment
We do not require logins or collect personal data. Your searches stay private and no analytics are used to track your activity at this stage of the beta.

### ⚠️ Legal Notice
OpenLaw SA provides legal information -- not legal advice.  
Please consult a qualified legal professional before making legal decisions. Our summaries are for reference and should always be cross-checked with the full judgment.
