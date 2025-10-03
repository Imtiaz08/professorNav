# 📡 professorNAV – The GNSS Code & Theory Tutor

**professorNAV** is a RAG-powered (Retrieval-Augmented Generation) AI tutor and coding assistant for **Global Navigation Satellite Systems (GNSS)**. Whether you’re working with GPS, GLONASS, Galileo, BeiDou, QZSS, or IRNSS, professorNAV provides instant explanations of GNSS concepts and generates reliable, optimized code in **Python, C, C++**, and **Rust** for building positioning software, SDRs, and integrated navigation systems.

---

## 🌍 GNSS Constellations Supported

professorNAV is built with a **global scope**, supporting:

| Constellation    | Region / Origin       | Signal Formats             |
|------------------|------------------------|-----------------------------|
| **GPS**          | USA                    | L1 C/A, L2C, L5             |
| **GLONASS**      | Russia                 | L1OF, L2OF, CDMA            |
| **Galileo**      | Europe (EU)            | E1, E5a, E5b, E6            |
| **BeiDou**       | China                  | B1I, B1C, B2a, B2b          |
| **QZSS**         | Japan (regional)       | L1C/A, L1S, L2C, L5, L6     |
| **IRNSS (NavIC)**| India (regional)       | L5, S-band                  |

professorNAV is capable of answering questions, generating code in various programming languges including C, C++, Python, Rust, and Go across **multi-constellation** and **multi-frequency** environments.

---

## 📚 Embedded GNSS Literature

professorNAV uses a **vector database** populated with curated content from the most authoritative GNSS books and specifications:

1. **Global Positioning System: Signals, Measurements, and Performance** – *Misra & Enge*
2. **Understanding GPS/GNSS: Principles and Applications** – *Kaplan & Hegarty*
3. **Principles of GNSS, Inertial, and Multisensor Integrated Navigation Systems** – *Paul Groves*
4. **GNSS, Inertial Navigation, and Integration** – *Grewal, Weill & Andrews*
5. **Galileo Open Service SIS ICD** – *European GNSS Agency (GSA)*
6. **GLONASS Interface Control Document**
7. **BeiDou Signal in Space ICD**
8. **QZSS Interface Specifications (IS-QZSS)**
9. **IRNSS ICD** – *ISRO*

🧠 The vector DB is used in combination with a language model to deliver **contextual, source-grounded answers** to GNSS queries.

---

## 🧠 Features

- 💬 Ask complex GNSS theory questions (e.g. “How is dilution of precision computed?”)
- 💻 Generate GNSS receiver code in **Python, C, C++, or Rust**
- 📡 Understand signal structures for GPS, Galileo, BeiDou, and more
- 🧭 Integrated Inertial + GNSS theory with Kalman Filter examples
- 🧠 RAG engine with citation-backed answers from textbook chunks
- ⚙️ Uses `uv` as a fast and reproducible package manager
- 🧪 Modular testing, linting, and CI-ready

---

## 🛠️ Tech Stack

| Component        | Tool/Library                     |
|------------------|----------------------------------|
| Package Manager  | [uv](https://github.com/astral-sh/uv) |
| LLM Backend      | OpenAI GPT-4 / LLaMA / Mistral (Pluggable) |
| RAG Engine       | LangChain / LlamaIndex           |
| Vector DB        | FAISS / Chroma / Weaviate        |
| Embedding Model  | OpenAI ADA / Sentence Transformers |
| Frontend         | Typer (CLI), Streamlit (Web UI)  |
| Language Support | Python, C, C++, Rust             |

---

## 🧪 Quickstart (with uv)

```bash
# Setup
uv venv
uv pip install .

# Run the assistant (CLI)
python app.py

# Dev mode
uv pip install --dev
pytest

🤖 Example Prompts
Q: How does GLONASS implement FDMA and what are the implications for multi-constellation receivers?
→ (Detailed response from textbook with code implications in C++)

Q: Write a Python function to compute Galileo pseudoranges using E1-B/C signals
→ (Returns numpy-based code with explanations)

🧠 Roadmap
 Add L5/E5a dual-frequency ionosphere-free code support

 SDR integration (e.g. RTL-SDR, USRP support)

 Real-time GNSS simulation visualization

 Web deployment (Gradio/Hugging Face)

 Export RAG citations + answer to LaTeX/PDF

🛡️ License & Attribution
License: MIT
Disclaimer: Educational use only. Books and standards are used under fair use to build AI-based assistants. All content remains copyright of original authors.

🙋‍♂️ Author
Built by: Your Name
Purpose: To assist developers, researchers, and learners in mastering GNSS and building reliable navigation software.
🔨🤖🔧 AI meets Satellite Navigation. The future of GNSS tutoring is here."# professorNav" 
