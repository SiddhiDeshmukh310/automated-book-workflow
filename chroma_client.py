import chromadb
from chromadb.config import Settings
from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction

# Use SentenceTransformer for local embeddings
embedding_function = SentenceTransformerEmbeddingFunction(
    model_name="all-MiniLM-L6-v2"  # You can change this to any SentenceTransformer model
)

# Setup ChromaDB client
chroma_client = chromadb.PersistentClient(path="./chroma_store")

# Get or create collection
def get_chroma_collection(name="book_collection"):
    return chroma_client.get_or_create_collection(
        name=name,
        embedding_function=embedding_function
    )
