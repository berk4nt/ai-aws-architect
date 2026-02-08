from crewai import Agent
from llm.openai_llm import get_llm

llm=get_llm()

requirements_agent = Agent(
    role = "AWS Cloud Architect",
    goal = "Extract structured AWS requirements from user input",
    backstory = "An AWS consultant who clarifies vague requriements",
    llm=llm
)

architect_agent = Agent(
    role = "AWS Cloud Architect",
    goal = "Design a scalable and cost-efficient AWS architecture ",
    backstory = "Senior AWS Solutions Architect with production experience",
    llm = llm
)

security_agent = Agent(
    role = "Security Reviewer",
    goal = "Ensure AWS security best practices are applied",
    backstory = "AWS security specialist",
    llm = llm
)

cost_agent = Agent(
    role = "Cost Estimator",
    goal = "Estimate AWS costs and suggest optimizations",
    backstory = "AWS cost optimization expert",
    llm = llm
)
