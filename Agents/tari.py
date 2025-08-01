from dotenv import load_dotenv
import os
import sys
from langchain_community.document_loaders import PyPDFLoader
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

load_dotenv()

# -------------------------------
# 1. Region Extraction via LLM
# -------------------------------
def extract_region_with_llm(question, llm, region_list):
    region_string = ", ".join(region_list)

    prompt = PromptTemplate(
        input_variables=["question", "regions"],
        template="""
You are a smart assistant that extracts a Region name from a user's question.
Pick the region mentioned in the question from the list below:

Regions: {regions}

Question: {question}

The region can be: Asia_Pacific, Canada, Europa, Latin_America, Middle_East_Africa and US.
Return ONLY the region name. If none found, return "Unknown".
"""
    )

    chain = LLMChain(llm=llm, prompt=prompt)
    result = chain.invoke({"question": question, "regions": region_string})
    return result["text"].strip()


# -------------------------------
# 2. Load Only Relevant PDF
# -------------------------------
def load_pdf_by_keyword(folder_path, keyword):
    for filename in os.listdir(folder_path):
        if filename.endswith(".pdf") and keyword.lower() in filename.lower():
            file_path = os.path.join(folder_path, filename)
            print(f"Using PDF: {file_path}")
            loader = PyPDFLoader(file_path)
            return loader.load()
    raise FileNotFoundError(f"No PDF found for keyword: {keyword}")


# -------------------------------
# 3. Main Flow
# -------------------------------
def main():
    try:
        question = (
            "what is the World(USD) for Full UCAF Group for IRD 53 for the US region mastercard consumer credit rates."
        )

        pdf_folder = "pdf"
        available_countries = [
            file.replace(".pdf", "") for file in os.listdir(pdf_folder) if file.endswith(".pdf")
        ]

        llm = ChatOpenAI(model_name="gpt-4-turbo", temperature=0, max_tokens=2048)
        region_keyword = extract_region_with_llm(question, llm, available_countries)
        print(f"[LLM Extracted Region] → {region_keyword}")

        if region_keyword == "Unknown":
            print("Could not detect region from question.")
            return

        documents = load_pdf_by_keyword(pdf_folder, region_keyword)

        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1500,
            chunk_overlap=200,
            separators=["\n\n", "\n", ".", "!", "?", ",", " ", ""]
        )
        texts = text_splitter.split_documents(documents)

        embeddings = OpenAIEmbeddings()
        vectorstore = Chroma.from_documents(texts, embeddings)

        retriever = vectorstore.as_retriever(search_kwargs={"k": 6})

        template = """Use the following pieces of context to answer the question at the end. 
If you don't know the answer, just say that you don't know — don't make up an answer.
If the question requests a table, return the answer in markdown table format.

{context}

Question: {question}
Answer:
"""
        QA_CHAIN_PROMPT = PromptTemplate(input_variables=["context", "question"], template=template)

        qa_chain = RetrievalQA.from_chain_type(
            llm,
            retriever=retriever,
            chain_type_kwargs={"prompt": QA_CHAIN_PROMPT}
        )

        result = qa_chain.invoke({"query": question})
        print("\n✅ Final Answer:\n")
        print(result["result"])

    except Exception as e:
        print(f"An error occurred: {e}")
        print("Python version:", sys.version)


if __name__ == "__main__":
    main()
