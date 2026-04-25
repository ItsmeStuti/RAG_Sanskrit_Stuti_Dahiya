# Sanskrit RAG System (CPU-Based)

## 📌 Overview
This project implements a Retrieval-Augmented Generation (RAG) system specifically designed for Sanskrit documents. The system uses CPU-based inference with TinyLlama model and provides accurate question-answering capabilities for Sanskrit texts.

## 🚀 Features
- **Multi-format Support**: Processes `.pdf`, `.txt`, and `.docx` documents
- **Sanskrit-Compatible**: Specialized text preprocessing for Sanskrit language
- **Efficient Retrieval**: FAISS-based vector similarity search
- **CPU-Optimized**: No GPU required, runs on standard hardware
- **Context Management**: Smart context truncation to handle token limits
- **Bilingual Output**: Supports responses in both Sanskrit and English

## 🏗️ System Architecture

### Components:
1. **Document Ingestion** (`ingest.py`): Loads and processes multiple document formats
2. **Text Processing**: Cleans and chunks Sanskrit text with appropriate overlap
3. **Vector Retrieval** (`retriever.py`): FAISS-based similarity search using sentence embeddings
4. **LLM Generation** (`generator.py`): TinyLlama model for answer generation
5. **Main Orchestrator** (`main.py`): Coordinates the entire RAG pipeline

### Data Flow:
```
Documents → Ingestion → Chunking → Embedding → FAISS Index → Retrieval → Generation → Answer
```

## ⚙️ System Requirements
- **Python**: 3.8+
- **RAM**: Minimum 4GB (8GB recommended)
- **Storage**: 2GB free space for models
- **OS**: Windows/Linux/macOS

## 📦 Installation

### 1. Clone Repository
```bash
git clone https://github.com/ItsmeStuti/RAG_Sanskrit_Stuti_Dahiya.git
cd RAG_Sanskrit_Stuti_Dahiya
```

### 2. Create Virtual Environment
```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# Linux/Mac
python -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirement.txt
```

### 4. Download Models (Automatic)
Models are downloaded automatically on first run:
- **Sentence Transformers**: `paraphrase-multilingual-MiniLM-L12-v2`
- **TinyLlama**: `TinyLlama-1.1B-Chat-v1.0-GGUF`

## 🎯 Usage

### Basic Usage
```bash
python code/main.py
```

### Interactive Mode
1. Place your Sanskrit documents in `data/sample_docs/`
2. Run the main script
3. Enter your questions in natural language
4. Get AI-powered answers based on your documents

### Example Queries
```
"What is the documentation about?"
"Explain this concept in Sanskrit"
"Summarize the main points in both Hindi and English"
```

## 📁 Project Structure
```
RAG_Sanskrit_Stuti_Dahiya/
├── code/
│   ├── main.py          # Main orchestrator script
│   ├── ingest.py        # Document ingestion pipeline
│   ├── retriever.py     # FAISS-based retrieval system
│   ├── generator.py     # LLM inference with TinyLlama
│   ├── config.py        # Configuration parameters
│   └── utils.py         # Text preprocessing utilities
├── data/
│   └── sample_docs/     # Place your Sanskrit documents here
├── report/              # Final PDF report
├── README.md           # This file
└── requirement.txt     # Python dependencies
```

## 🔧 Configuration

Key parameters in `code/config.py`:
- `CHUNK_SIZE`: Text chunk size (default: 300)
- `CHUNK_OVERLAP`: Overlap between chunks (default: 50)
- `TOP_K`: Number of retrieved chunks (default: 1)
- Model paths and token limits

## 📊 Performance Optimization

### CPU Optimization Features:
- **Quantized Models**: GGUF format for efficient inference
- **Context Truncation**: Prevents token limit errors
- **Batch Processing**: Efficient document chunking
- **Memory Management**: Controlled memory usage

### Benchmarks:
- **Model Load Time**: ~30 seconds (first run)
- **Inference Speed**: ~2-5 seconds per query
- **Memory Usage**: ~2-3GB RAM during operation

## 🧪 Testing

### Run Tests
```bash
# Test individual components
python -c "from code.generator import Generator; g = Generator(); print('✓ Generator works')"

# Test full pipeline
python code/main.py
```

### Sample Data
- Place test documents in `data/sample_docs/`
- Supported formats: PDF, TXT, DOCX
- Recommended: Sanskrit religious texts, academic papers

## 🤝 Contributing

1. Fork the repository
2. Create feature branch
3. Test thoroughly on CPU
4. Submit pull request

## 📄 License

This project is developed for educational purposes.

## 📞 Support

For issues or questions:
- Check the troubleshooting section
- Ensure all dependencies are installed
- Verify document formats are supported

---

**Note**: This system is optimized for CPU inference and may take longer to load models on first run. Subsequent runs are faster due to model caching.