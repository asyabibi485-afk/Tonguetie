from pathlib import Path

KB = Path(__file__).parent / "data" / "knowledge_base.txt"

def retrieve_context(query: str, top_k: int = 4) -> str:
    text = KB.read_text(encoding="utf-8") if KB.exists() else ""
    chunks = [c.strip() for c in text.split("\n\n") if c.strip()]
    terms = set(query.lower().split())
    ranked = sorted(chunks, key=lambda c: sum(t in c.lower() for t in terms), reverse=True)
    return "\n\n".join(ranked[:top_k])

# This intentionally keeps retrieval lightweight and dependency-free.
# For production, replace it with FAISS/Chroma/pgvector + embeddings.
