
import streamlit as st
from pathlib import Path

st.set_page_config(page_title="OpenLaw SA", layout="wide")

# Optional: Logo or header
st.title("📚 OpenLaw SA")
st.subheader("Navigate using the menu on the left →")

st.markdown(
    '''
Welcome to the demo version of OpenLaw SA.

Use the left sidebar to access:
- 🔍 Search results
- 📄 Case detail
- 🕸 Precedent maps
'''
)
