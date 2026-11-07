from crewai import Agent
from tools import yt_tool

ollama_llm=LLM(
    model="ollama/llama3.2",
    base_url="http://localhost:11434",
    temperature=0.7,
)

## Create a senior blog content researcher

blog_researcher=Agent(
    role='Blog Researcher from Youtube Videos',
    goal='get the relevant video content for the topic{topic} from YT channel',
    verbose=True,
    memory=True,
    backstory=(
        "Expert in understanding videos in AI, Data Science, Machine Learning and GenAI and Deep learning"
    ),
    tools=[],
    llm=ollama_llm,
    allow_delegation=True
)
## Creating a senior blog writer agent with YT tool

blog_writer=Agent(
    role='Writer',
    goal='Narrate compelling tech stories about the video {topic} from YT channel',
    verbose=True,
    memory=True,
    backstory=("With a flair for simplfying complex topics, you craft engaging narratives that captivate and educate, bringing new discoveries to lght in an accesible manner."),
    tools=[],
    llm=ollama_llm,
    allow_delegationn=False
)