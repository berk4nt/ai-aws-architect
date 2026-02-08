from crewai import Task
from crew.agents import requirements_agent, architect_agent, security_agent, cost_agent

requirements_task = Task(
    description = """
    Analyze the user input and extract clear AWS requirements.
    Identify : 
    - Application type
    - Expected scale
    - Data sensitivity
    - Data sensitivity
    - Availability needs
    Output a structured bullet points.
    """,

    expected_output = """
    Structured AWS requirements in bullet points.
""",
    agent = requirements_agent,
)

architect_task = Task(
    description = """
    Design a production-ready AWS architecture.
    Use only official AWS services.
    Focus on scalability, availability, and cost efficiency.
    Avoid over-engineering.
    Explain service choices clearly.
    """,
    expected_output = """
    AWS Architecture description
""",
    agent = architect_agent,
)

security_task = Task(
    description = """
    Review the AWS architecture and list security best practices.
    Focus on IAM, networking, encryption, and access control.
    """,
    expected_output = """
    Security recommendations
    """,
    agent = security_agent,
)

cost_task = Task(
    description = """
    Estimate the approximate monthly AWS cost.
    Provide a reasonable cost range and optimization suggestions.
    """,
    expected_output = "Estimated AWS monthly cost",
    agent=cost_agent
)