from ingest import load_documents, preprocess_documents, chunk_documents
from retriever import Retriever
from generator import Generator

DATA_PATH = "data/sample_docs/"


def main():
    print("Loading documents...")
    docs = load_documents(DATA_PATH)

    print("Preprocessing documents...")
    docs = preprocess_documents(docs)

    print("Chunking documents...")
    chunks = chunk_documents(docs)

    print(f"Total chunks created: {len(chunks)}")

    print("Building retriever...")
    retriever = Retriever()
    retriever.build_index(chunks)

    print("Loading generator model (CPU)...")
    generator = Generator()

    print("\n=== Sanskrit RAG System Ready ===\n")

    while True:
        query = input("Enter your query (or type 'exit'): ")

        if query.lower() == "exit":
            print("Exiting...")
            break

        retrieved_chunks = retriever.retrieve(query)

        print("\n--- Retrieved Context ---\n")
        for i, chunk in enumerate(retrieved_chunks):
            print(f"[{i+1}] {chunk[:200]}...\n")

        response = generator.generate(query, retrieved_chunks)

        print("\n--- Generated Answer ---\n")
        print(response)
        print("\n" + "="*60 + "\n")


if __name__ == "__main__":
    main()