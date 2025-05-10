
import streamlit as st

def app():
    st.title("📄 Case Detail: Smith v Minister of Justice")
    st.markdown("**Court**: Constitutional Court  
**Date**: 2023-06-12")
    st.markdown("### 🧾 Summary")
    st.write("This case involved a constitutional challenge to the procedural fairness of administrative detention under the Immigration Act.")
    st.markdown("### 📌 Precedents Cited")
    st.markdown("- Minister of Home Affairs v Watchenuka 2004 (4) SA 326 (SCA)")
    st.markdown("- Masetlha v President of the RSA 2008 (1) SA 566 (CC)")
    st.button("🕸 View Precedent Map")
