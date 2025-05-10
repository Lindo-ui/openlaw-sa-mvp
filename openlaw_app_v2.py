
import streamlit as st
import json

# Load sample data
with open("sample_cases.json", "r") as file:
    data = json.load(file)

st.set_page_config(page_title="OpenLaw SA", layout="wide")

# Hero Section
st.markdown("""
# 📚 OpenLaw SA
### South Africa's Unified Legal Intelligence Platform  
_“Summaries that save hours. Search that works. For lawyers who want clarity, fast.”_
""")
st.divider()

# Search bar
query = st.text_input("🔍 Search case titles or summaries:", "")

# Filter cases based on query
if query:
    results = [
        case for case in data["cases"]
        if query.lower() in case["title"].lower() or query.lower() in case["summary"].lower()
    ]
else:
    results = data["cases"]

# Display results
for case in results:
    with st.expander(f"{case['title']} ({case['court']}, {case['date']})"):
        st.write("**🧾 Summary:**", case["summary"])
        st.write("**🔗 Full Text:**", f"[Read Full Case]({case['full_text_url']})")
        st.write("**📌 Precedents Cited:**")
        for p in case["precedents_cited"]:
            st.markdown(f"- {p}")

# Mock Summary Generator (Manual Demo)
st.divider()
st.markdown("### ✍️ Try the Summary Generator")
user_input = st.text_area("Paste a legal excerpt or judgment text below:")

if st.button("Generate Summary (Mock)"):
    if user_input.strip():
        st.success("🧠 Summary:")
        st.markdown("This case concerns the application of constitutional principles to the conduct of public officials, particularly regarding procedural fairness and the rights of affected individuals under administrative law.")
    else:
        st.warning("Please paste some text to summarize.")
