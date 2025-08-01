from crewai_tools import PDFSearchTool
from crewai import Agent, Task, Crew, Process, LLM
from dotenv import load_dotenv
import os

load_dotenv()

tool_latin = PDFSearchTool(pdf="pdf\m_lac_inc_customer_en-us 1.pdf")
tool_us = PDFSearchTool(pdf="pdf\m_us_inc_customer_en-us 1.pdf")
tool_canada = PDFSearchTool(pdf="pdf\m_can_inc_en-us 1.pdf")
tool_europa = PDFSearchTool(pdf="pdf\m_eur_inc_customer_en-us 1.pdf")
tool_ap = PDFSearchTool(pdf="pdf\m_ap_inc_customer_en-us 1.pdf")
tool_mea = PDFSearchTool(pdf="pdf\m_mea_inc_customer_en-us 1.pdf")

manager_llm = LLM(model="gpt-4o")

manager = Agent(
    role="Document Routing Manager",
    goal="Route questions to the appropriate region specialist based on query content. Always detect region from question.",
    backstory="You are responsible for identifying which region is being referred to in the user's question." \
    "If the word Latin America appears or any country from Latin America - use the agent_latin." \
    "If the word US appears or any state from US - use the agent_us." \
    "If the word Canada appears or anything related to Canada - use the agent_canada." \
    "If the word Europa appears or anything related to Europa - use the agent_europa." \
    "If the words Asia or Pacific appears or any country related to Asia or Pacific - use the agent_ap." \
    "If the words Middel East or Africa appears or any country related to Middel East or Africa - use the agent_mea." \
    "Based on the region, assign the correct agent to answer.",
    llm=manager_llm,
    allow_delegation=True,
    verbose=True
)

agent_latin = Agent(
    role="Latin America PDF Search Agent",
    goal="Search the Latin America PDF for answers. Only answer if the region is Latin America.",
    backstory="You specialize in extracting answers from the Latin America document. If you can not find the answear in the Latin America document say so expicitly.",
    tools=[tool_latin],
    verbose=True,
    allow_delegation=False
)

agent_us = Agent(
    role="US PDF Search Agent",
    goal="Search the US PDF for answers. Only answer if the region is the US.",
    backstory="You specialize in extracting answers from the US document. If you can not find the answear in the US document say so expicitly.",
    tools=[tool_us],
    verbose=True,
    allow_delegation=False
)

agent_canada = Agent(
    role="Canada PDF Search Agent",
    goal="Search the Canada PDF for answers. Only answer if the region is the Canada.",
    backstory="You specialize in extracting answers from the Canada document. If you can not find the answear in the Canada document say so expicitly.",
    tools=[tool_canada],
    verbose=True,
    allow_delegation=False
)

agent_europa = Agent(
    role="Europa PDF Search Agent",
    goal="Search the Europa PDF for answers. Only answer if the region is the Europa.",
    backstory="You specialize in extracting answers from the Europa document. If you can not find the answear in the Europa document say so expicitly.",
    tools=[tool_europa],
    verbose=True,
    allow_delegation=False
)

agent_ap = Agent(
    role="Asia and Pacific PDF Search Agent",
    goal="Search the Asia and Pacific PDF for answers. Only answer if the region is the Asia or Pacific.",
    backstory="You specialize in extracting answers from the Asia and Pacific document. If you can not find the answear in the Asia and Pacific document say so expicitly.",
    tools=[tool_ap],
    verbose=True,
    allow_delegation=False
)

agent_mea = Agent(
    role="Middel East and Africa PDF Search Agent",
    goal="Search the Middel East and Africa PDF for answers. Only answer if the region is the Middel East or Africa.",
    backstory="You specialize in extracting answers from the Middel East and Africa document. If you can not find the answear in the Middel East and Africa document say so expicitly.",
    tools=[tool_mea],
    verbose=True,
    allow_delegation=False
)

task_latin = Task(
    description="Answer this question about the Latin America PDF: {question}.",
    expected_output="A detailed answer extracted from the Latin America document.",
    agent=agent_latin,
    async_execution=True
)

task_us = Task(
    description="Answer this question about the US PDF: {question}.",
    expected_output="A detailed answer extracted from the US document.",
    agent=agent_us,
    async_execution=True
)

task_canada = Task(
    description="Answer this question about the Canada PDF: {question}.",
    expected_output="A detailed answer extracted from the Canada document.",
    agent=agent_canada,
    async_execution=True
)

task_europa = Task(
    description="Answer this question about the Europa PDF: {question}.",
    expected_output="A detailed answer extracted from the Europa document.",
    agent=agent_europa,
    async_execution=True
)

task_ap = Task(
    description="Answer this question about the Asia and Pacific PDF: {question}.",
    expected_output="A detailed answer extracted from the Asia and Pacific document.",
    agent=agent_ap,
    async_execution=True
)

task_mea = Task(
    description="Answer this question about the Middel East and Africa PDF: {question}.",
    expected_output="A detailed answer extracted from the Middel East and Africa document.",
    agent=agent_mea,
    async_execution=True
)

task_final = Task(
    description="Based on previous results, determine the most appropriate and complete final answer to the user's question: {question}",
    expected_output="A final, clear and accurate answer based on region-specific data.",
    agent=manager,
    context=[task_latin, task_us, task_canada, task_europa, task_ap, task_mea]
)

crew = Crew(
    agents=[manager, agent_latin, agent_us, agent_canada, agent_europa, agent_ap, agent_mea],
    tasks=[task_latin, task_us, task_canada, task_europa, task_ap, task_mea, task_final],
    manager_llm=manager_llm,
    manager_agent=manager,
    verbose=True,
    #process=Process.sequential
)

while True:
    question = input("\nEnter a question about the PDF documents:\n> ")
    result = crew.kickoff(inputs={"question": question})
    print("\n📄 Answer:\n", result)
