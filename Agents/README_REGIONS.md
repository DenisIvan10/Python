# Multi-Region PDF Question Answering System (CrewAI Approach)

## Overview

This project implements a modular, AI-powered pipeline for **automatic routing and answering questions about regional PDF documents**.  
It uses CrewAI to coordinate a set of Large Language Model (LLM) agents, each specialized in searching a PDF document for a specific geographical region.

---

## Key Features

- **Automated Region Detection:**  
  The main agent (“manager”) analyzes each user question and automatically determines which world region it refers to (e.g., Latin America, US, Canada, Europe, Asia-Pacific, Middle East & Africa).
- **Specialized Sub-Agents:**  
  Each region has a dedicated agent, equipped with a `PDFSearchTool` pointing to the respective document.
- **Delegation and Orchestration:**  
  The manager agent delegates questions to the right sub-agent, and composes the final answer.
- **Extensible Design:**  
  You can easily add more regions or document types by creating additional agents and tools.
- **Clear Fallbacks:**  
  If an answer cannot be found for a region, the system clearly reports that fact.

---

## How It Works

1. **User Input:**  
   The user enters a natural language question about any supported region.
2. **Region Identification:**  
   The `manager` agent determines the relevant region by parsing the question content (countries, keywords, etc.).
3. **Document Search:**  
   The matching regional agent uses `PDFSearchTool` to find answers in the corresponding PDF.
4. **Answer Composition:**  
   The system returns a detailed, region-specific answer, or notifies if the answer could not be found.

---

## Project Structure
```
├── regiuni.py # Main script (CrewAI pipeline with region agents)
├── pdf/ # Folder containing regional PDF files (not included)
│ ├── m_lac_inc_customer_en-us 1.pdf
│ ├── m_us_inc_customer_en-us 1.pdf
│ ├── m_can_inc_en-us 1.pdf
│ ├── m_eur_inc_customer_en-us 1.pdf
│ ├── m_ap_inc_customer_en-us 1.pdf
│ └── m_mea_inc_customer_en-us 1.pdf
├── .env # Environment variables (e.g. OpenAI API key)
└── requirements.txt # Python dependencies
```

---

## Installation

1. Clone the repository
```bash
git clone <repo_url>
cd <repo_folder>
```
2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Add PDF documents
Place your region-specific PDF files inside the pdf/ directory.

4. Configure environment
Add your OpenAI API key and any other necessary credentials in a .env file.

5. Usage
- Run the main script:
- Then enter your question when prompted, e.g.:
Enter a question about the PDF documents:
> What is the customer onboarding process in Canada?
The system will respond with the answer found in the relevant PDF, or state if no answer was found.

---
