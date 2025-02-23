from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from src.crewai_test.tools.query_executer import SqlQueryExecuter

@CrewBase
class SrcCrewai():
	"""Src/Crewai crew"""

	def __init__(self , db_config):
		
		self.query_exec_tool = SqlQueryExecuter(db_config)


	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'


	@agent
	def query_creator(self) -> Agent:
		return Agent(
			config=self.agents_config['query_creator'],
			verbose=True
		)
	@agent
	def query_executer(self) -> Agent:
		return Agent(
			config=self.agents_config['query_executer'],
			verbose=True,
			tools = [self.query_exec_tool]
		)

	
	# To learn more about structured task outputs, 
	# task dependencies, and task callbacks, check out the documentation:
	# https://docs.crewai.com/concepts/tasks#overview-of-a-task
	@task
	def query_creation_task(self) -> Task:
		return Task(
			config=self.tasks_config['query_creation_task'],
		)
	
	@task
	def query_execution_task(self) -> Task:
		return Task(
			config=self.tasks_config['query_execution_task'],
		)

	
	@crew
	def crew(self) -> Crew:
		"""Creates the Src/Crewai crew"""
		# To learn how to add knowledge sources to your crew, check out the documentation:
		# https://docs.crewai.com/concepts/knowledge#what-is-knowledge

		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)
