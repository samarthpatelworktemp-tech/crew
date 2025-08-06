from typing import List
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from pydantic import BaseModel, Field
from tools.markdown_saver import MarkdownSaverTool

markdown_saver = MarkdownSaverTool()


class TechnicalDesignDoc(BaseModel):
    title: str = Field(..., description="Title of the technical design document")
    summary: str = Field(..., description="Summary of the system or module")
    components: List[str] = Field(..., description="Key components involved")
    sequence_of_steps: List[str] = Field(..., description="Logical flow or step-by-step breakdown")
    constraints: List[str] = Field(..., description="Any known limitations or boundaries")
    assumptions: List[str] = Field(..., description="Any assumptions made in the design")

@CrewBase
class CodeTranslatorCrew():
    """CodeTranslator Crew"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def code_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['code_analyst'],
            verbose=True,
            memory=False,
        )

    @agent
    def tdd_generator(self) -> Agent:
        return Agent(
            config=self.agents_config['tdd_generator'],
            verbose=True,
            memory=False,
        )

    @agent
    def code_generator(self) -> Agent:
        return Agent(
            config=self.agents_config['code_generator'],
            verbose=True,
            memory=False,
        )

    @task
    def code_analysis_task(self) -> Task:
        return Task(
            config=self.tasks_config['code_analysis'],
            agent=self.code_analyst()
        )

    @task
    def tdd_generation_task(self) -> Task:
        return Task(
            config=self.tasks_config['tdd_generation'],
            agent=self.tdd_generator(),
            context=[self.code_analysis_task()],
            output_pydantic=TechnicalDesignDoc
        )

    @task
    def tdd_save_task(self) -> Task:
        return Task(
            config=self.tasks_config['tdd_save'],
            agent=self.tdd_generator(),
            tools=[],
            context=[self.tdd_generation_task()],
        )

    @task
    def code_generation_task(self) -> Task:
        return Task(
            config=self.tasks_config['code_generation'],
            agent=self.code_generator(),
            context=[self.tdd_generation_task()],
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
        )