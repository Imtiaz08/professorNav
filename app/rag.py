import chromadb
from sentence_transformers import SentenceTransformer
import requests

# === CONFIG ===
CHROMA_DB_DIR = "chroma_storage"
COLLECTION_NAME = "gnss_knowledge_base"
OLLAMA_MODEL = "phi3"  # Change to your preferred GPT-OSS model name
OLLAMA_API_URL = "http://localhost:11434/api/generate"

# === INIT ===
chroma_client = chromadb.PersistentClient(path=CHROMA_DB_DIR)
collection = chroma_client.get_or_create_collection(name=COLLECTION_NAME)
embed_model = SentenceTransformer("all-MiniLM-L6-v2")

# === RAG Function ===
def query_with_rag(user_query, k=3, temperature=0.7):
    print(f"\nQuery: {user_query}")
    
    # Step 1: Embed user query
    query_embedding = embed_model.encode(user_query)

    # Step 2: Retrieve top-k matching chunks
    results = collection.query(query_embeddings=[query_embedding], n_results=3)
    retrieved_docs = results["documents"][0]
    sources = results["metadatas"][0]

    # Step 3: Format context
    context = "\n---\n".join(retrieved_docs)

    prompt = f"""
    I am ProfessorNav, your dedicated GNSS assistant — trained and developed by Imtiaz Nabi. I specialize in satellite navigation theory, positioning algorithms, and multiple programming languages for GNSS applications.

    You can rely on me to provide technically accurate, concise, and easy-to-understand answers based **only** on the trusted materials provided in the context below. I won’t speculate or guess. If the answer is not found in the context, I will say so honestly.

    Use this assistant as a guide for your studies, coding assignments, research, or engineering work to make this world a better place through accurate and reliable positioning, navigation and timing (PNT).
    
    Use the context below to answer the user's question. You are allowed to include:
    - Detailed explanations
    - Mathematical expressions (in Markdown/LaTeX)
    - Code blocks if relevant

    Be accurate and helpful, but don't be afraid to explore complex answers if needed. If information is missing, say so politely.

    Context:
    {context}

    Question:
    {user_query}

    Answer:
    """

    # Step 4: Call Ollama (local LLM)
    response = requests.post(
        OLLAMA_API_URL,
        json={
            "model": OLLAMA_MODEL,
            "prompt": prompt,
            "stream": True,
            "options": {
                "temperature": temperature
            }
        },
        stream=True
    )

    if response.status_code != 200:
        raise RuntimeError(f"Ollama error: {response.status_code} - {response.text}")

    answer = response.json().get("response", "").strip()
    print("Response received from LLM\n")
    return answer, sources

# === Example Usage ===
if __name__ == "__main__":
    while True:
        query = input("Ask a GNSS question (or 'exit'): ").strip()
        if query.lower() == "exit":
            break

        answer, metadata = query_with_rag(query)
        print("\nAnswer:\n", answer)
        print("\nSources:")
        for meta in metadata:
            print(" -", meta.get("source", "Unknown"))
