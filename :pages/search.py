
import streamlit as st

def app():
    st.title("🔎 Search Results")
    st.text_input("Search query", value="constitutional law")
    
    st.markdown("##### Filter by:")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.selectbox("Court", ["All", "Constitutional Court", "High Court", "Supreme Court of Appeal"])
    with col2:
        st.selectbox("Year", ["All", "2024", "2023", "2022", "2021"])
    with col3:
        st.selectbox("Topic", ["All", "Housing", "Labour", "Administrative Law"])

    st.markdown("### 📄 Case List")
    for i in range(3):
        with st.expander(f"Smith v Minister of Justice (Constitutional Court, 2023-06-12)"):
            st.write("This case involved a constitutional challenge to procedural fairness under the Immigration Act.")
            st.button("View Case Detail", key=f"view_case_{i}")
