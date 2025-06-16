def search_versions(query, collection):
    results = collection.query(
        query_texts=[query],
        n_results=3  # get top 3 results
    )

    if not results["documents"]:
        return []

    output = []
    for doc, metadata in zip(results["documents"][0], results["metadatas"][0]):
        display = f"""### 📘 Chapter: {metadata.get('chapter_number', 'N/A')}  
👤 Author: {metadata.get('user', 'Unknown')}  

**✍️ Rewritten Text:**  
{doc}

**🧐 Review:**  
{metadata.get('review', 'No review available')}  

---"""
        output.append(display)

    return output
