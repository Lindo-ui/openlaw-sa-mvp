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
