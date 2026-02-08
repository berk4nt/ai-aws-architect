from crewai import Crew 
from crew.tasks import requirements_task, architect_task, security_task, cost_task
from crew.agents import requirements_agent, architect_agent, security_agent, cost_agent

def get_crew():
    return Crew(
        agents=[requirements_agent, architect_agent, security_agent, cost_agent],
        tasks=[requirements_task, architect_task, security_task, cost_task],
        verbose=True
    )

