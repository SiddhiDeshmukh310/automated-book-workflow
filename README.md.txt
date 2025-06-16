# 📘 Automated Book Publication Workflow

## 🚀 Objective
An AI-powered app to fetch chapters from a website, rewrite them using LLMs, allow human-in-the-loop edits, and store version-controlled outputs using ChromaDB.

---

## 🧠 Key Features
- ✅ **Web Scraping**: Fetch content and screenshots from [WikiSource](https://en.wikisource.org/wiki/The_Gates_of_Morning/Book_1/Chapter_1)
- ✅ **AI Writer**: Rewrites content using local LLM (Ollama: Mistral)
- ✅ **AI Reviewer**: Reviews rewritten text for clarity, grammar, and meaning
- ✅ **Human-in-the-Loop**: Allows humans to review/edit rewritten chapters
- ✅ **ChromaDB**: Stores and retrieves version-controlled documents
- ✅ **RL-style Search**: Searches relevant versions using embeddings

---

## 🛠 Tech Stack
- `Python`  
- `Streamlit` – For user interface  
- `Playwright` – For scraping & screenshots  
- `Ollama (Mistral)` – Local LLM for writing & reviewing  
- `ChromaDB` – Vector database for storing versions  
- `OpenAIEmbeddingFunction` – For semantic search  
- `UUID` – For version tracking

---

## 🧪 How to Run the App

1. **Install dependencies**
   ```bash
   pip install -r requirements.txt
