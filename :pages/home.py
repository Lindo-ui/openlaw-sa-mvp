
import streamlit as st

def app():
    st.set_page_config(page_title="OpenLaw SA", layout="wide")
    st.title("📚 OpenLaw SA")
    st.subheader("South Africa's Unified Legal Intelligence Platform")
    st.markdown("_Making case law, legislation, and precedent maps accessible to all._")

    st.text_input("🔍 Search the legal database", placeholder="e.g. eviction, constitutional rights, housing")

    st.markdown("### 📂 Quick Access")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.button("📄 Recent Cases")
    with col2:
        st.button("📚 New Legislation")
    with col3:
        st.button("🧠 Browse by Topic")
    with col4:
        st.button("🕸 Precedent Maps")
