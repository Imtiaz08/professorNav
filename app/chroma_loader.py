import os
import uuid
import time
from langchain.text_splitter import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer
import chromadb

# === CONFIGURATION ===
DOCS_DIR = "docs"  # folder with your .txt files
CHROMA_COLLECTION_NAME = "gnss_knowledge_base"
CHROMA_DB_DIR = "chroma_storage"  # persistent storage
MAX_BATCH_SIZE = 5000  # keep below Chroma's internal limit

# === INIT CHROMADB ===
# Persistent client so DB survives restarts
chroma_client = chromadb.PersistentClient(path=CHROMA_DB_DIR)
collection = chroma_client.get_or_create_collection(name=CHROMA_COLLECTION_NAME)

# === EMBEDDING MODEL ===
embed_model = SentenceTransformer("all-MiniLM-L6-v2")

# === TEXT SPLITTER ===
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)

# === HELPER: check if already embedded ===
def already_embedded(doc_name: str) -> bool:
    results = collection.get(where={"source": doc_name})
    return len(results["ids"]) > 0

# === HELPER: chunk any list into batches ===
def chunked(iterable, size):
    for i in range(0, len(iterable), size):
        yield iterable[i:i + size]

# === MAIN FUNCTION ===
def load_and_embed_all_txt():
    for filename in os.listdir(DOCS_DIR):
        if not filename.endswith(".txt"):
            continue

        if already_embedded(filename):
            print(f"Skipping {filename} (already embedded)")
            continue

        path = os.path.join(DOCS_DIR, filename)
        print(f"\nProcessing {filename}...")
        start_time = time.time()

        with open(path, "r", encoding="utf-8") as f:
            raw_text = f.read()

        # Split into chunks
        chunks = splitter.split_text(raw_text)
        print(f"Chunked into {len(chunks)} segments")

        # Batch embed chunks
        embeddings = embed_model.encode(chunks, show_progress_bar=True)
        ids = [str(uuid.uuid4()) for _ in chunks]
        metadatas = [{"source": filename} for _ in chunks]

        # Add to ChromaDB in safe batches
        for doc_batch, embed_batch, id_batch, meta_batch in zip(
            chunked(chunks, MAX_BATCH_SIZE),
            chunked(embeddings, MAX_BATCH_SIZE),
            chunked(ids, MAX_BATCH_SIZE),
            chunked(metadatas, MAX_BATCH_SIZE),
        ):
            collection.add(
                documents=doc_batch,
                embeddings=embed_batch,
                ids=id_batch,
                metadatas=meta_batch
            )

        elapsed = time.time() - start_time
        print(f"Embedded {len(chunks)} chunks from {filename} in {elapsed:.2f} seconds")

if __name__ == "__main__":
    load_and_embed_all_txt()
