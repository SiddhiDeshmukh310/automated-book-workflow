import sys
import types
import uuid
import torch
import streamlit as st

# Fix for torch/classes bug in Streamlit
torch.classes = types.SimpleNamespace()
sys.modules["torch.classes"] = torch.classes
from chromadb.utils.embedding_functions import OpenAIEmbeddingFunction
import chromadb

from chroma_client import get_chroma_collection
from rewriter import rewrite_text
from reviewer import review_text
from store_version import store_version
from search_version import search_versions

# ✅ Get Chroma collection with embedding
collection = get_chroma_collection()

# 🖼️ Streamlit UI
st.set_page_config(page_title="📘 Automated Book Workflow")
st.title("📚 Automated Book Workflow")

# 📋 Sidebar
menu = st.sidebar.selectbox("Choose Action", ["Rewrite & Review", "Search Versions"])

if menu == "Rewrite & Review":
    user_input = st.text_area(
        label="✍️ Please write or paste the chapter content below:",
        placeholder="Type or paste your chapter/paragraph here...",
        height=300
    )

    # ✅ Define these BEFORE the if condition
    chapter_number = st.text_input("📘 Chapter Number")
    user = st.text_input("👤 Your Name")

    if st.button("🔁 Rewrite") and user_input.strip() and chapter_number and user:
        rewritten = rewrite_text(user_input)
        st.success("✅ Rewritten Text:")
        st.write(rewritten)

        collection.add(
        documents=[rewritten],
        metadatas=[{
            "source": "rewrite",
            "chapter": chapter_number,
            "author": user
        }],
        ids=[str(uuid.uuid4())]
    )
        # Review the rewritten version
        reviewed = review_text(user_input, rewritten)
        st.info("🧐 Reviewed Version:")
        st.write(reviewed)

        # Store original + rewritten + reviewed
        store_version(rewritten, reviewed, chapter_number, user)


elif menu == "Search Versions":
    query = st.text_input("🔍 Enter search query")

    if st.button("Search") and query.strip():
        results = search_versions(query, collection)
        if results:
            st.write("📄 Most Relevant Match:")
            for r in results:
                st.markdown(f"- {r}")
        else:
            st.warning("❌ No matches found.")
