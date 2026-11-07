from crewai import Crew,Process
from agents import blog_researcher, blog_writer
from tasks import research_task, write_task


## Forming the tech-focued crew with some enhanced configurations

crew=Crew(
    agents=[blog_researcher, blog_writer],
    tasks=[research_task, write_task],
    process=Process.sequential, # Sequential execution of tasks
    memory=True, # Enable memory for the crew
    cache=True, # Enable caching for the crew
    max_rpm=100,
    share_crew=True
)


## Start the task execution process with enhanced feedback

result=crew.kickoff(inputs={'topic':'AI, Data Science, Machine Learning and GenAI and Deep learning'})
print(result)