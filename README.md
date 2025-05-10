# OpenLaw SA – Legal Intelligence MVP

OpenLaw SA is a unified legal intelligence platform for South Africa. It aggregates landmark Constitutional Court decisions and presents them in a searchable, user-friendly interface.

## 🔍 Features

- Smart search through titles, summaries, and topic tags
- Plain-language summaries of major cases
- Expandable case cards with citations and precedents
- Direct links to full judgments and downloadable PDFs
- Fully responsive Streamlit frontend

## 📂 Project Structure

```
├── app.py                     # Streamlit app entry point
├── sample_cases.json          # Richly structured legal case data
├── requirements.txt           # Python dependencies
```

## 🛠 Installation

```bash
git clone https://github.com/Lindo-ui/openlaw-sa-mvp.git
cd openlaw-sa-mvp
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

## 📄 Data Format

Each entry in `sample_cases.json` contains:

- `title`, `summary`, `court`, `date`
- `citations` and `precedents_cited`
- `tags`, `source_link`, and `pdf_link`

## 🚀 Future Enhancements

- Advanced filtering by court, tag, year
- Dynamic citation graph visualization
- API endpoints for legal tech developers
- Summary generator integration

---

Built with ❤️ by Dotsimple.