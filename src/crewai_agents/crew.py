from crewai import Agent, Crew, Process, Task # type: ignore
from crewai.project import CrewBase, agent, crew, task # type: ignore

# Uncomment the following line to use an example of a custom tool
# from crewai_agents.tools.custom_tool import MyCustomTool

# Check our tools documentations for more information on how to use them
# from crewai_tools import SerperDevTool

@CrewBase
class CrewaiAgentsCrew():
	"""CrewaiAgents crew"""
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	@agent
	def researcher(self) -> Agent:
		return Agent(
			config=self.agents_config['researcher'],
			# tools=[MyCustomTool()], # Example of custom tool, loaded on the beginning of file
			verbose=True
		)

	@agent
	def reporting_analyst(self) -> Agent:
		return Agent(
			config=self.agents_config['reporting_analyst'],
			verbose=True
		)

	@task
	def research_task(self) -> Task:
		return Task(
			config=self.tasks_config['research_task'],
			agent=self.researcher()
		)

	@task
	def reporting_task(self) -> Task:
		return Task(
			config=self.tasks_config['reporting_task'],
			agent=self.reporting_analyst(),
			output_file='report.md'
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the CrewaiAgents crew"""
		return Crew(
			agents=[self.researcher(), self.reporting_analyst()], # Automatically created by the @agent decorator
			tasks=[self.research_task(), self.reporting_task()], # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=2,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)