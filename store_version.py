# store_version.py

import uuid
from datetime import datetime
from chroma_client import get_chroma_collection

def store_version(rewritten_text: str, reviewed_text: str, chapter_number: str, user: str):
    """
    Stores both rewritten and reviewed versions in ChromaDB with metadata:
    - source (rewrite/review)
    - timestamp
    - chapter number
    - user
    """
    collection = get_chroma_collection()
    timestamp = datetime.now().isoformat()

    # Save to ChromaDB
    documents = [rewritten_text, reviewed_text]
    metadatas = [
        {
            "source": "rewrite",
            "timestamp": timestamp,
            "chapter": chapter_number,
            "user": user
        },
        {
            "source": "review",
            "timestamp": timestamp,
            "chapter": chapter_number,
            "user": user
        }
    ]
    ids = [str(uuid.uuid4()), str(uuid.uuid4())]
    collection.add(documents=documents, metadatas=metadatas, ids=ids)

    # Save reviewed version to file
    with open("final_output.txt", "a", encoding="utf-8") as f:
        f.write(f"\n\n--- Chapter {chapter_number} by {user} ({timestamp}) ---\n")
        f.write(reviewed_text + "\n")
