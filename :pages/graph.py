
import streamlit as st

def app():
    st.title("🕸 Precedent Map")
    st.markdown("Visual representation of case law relationships:")
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Graph_structure.svg/800px-Graph_structure.svg.png", width=700)
    st.caption("Example: 'Smith v Minister of Justice' cites prior cases and is cited by newer decisions.")
