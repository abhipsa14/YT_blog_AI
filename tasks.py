from crewai import Task
from tools import yt_tool

from agents import blog_researcher, blog_writer


## Research task

research_task=Task(
    description=(
        "Identify the video {topic}."
        "Get detailed information about the video from the channel."
    ),
    expected_output='A comprehensive 3 paragraphs long report based on the {topic} of video from the channel',
    tools=[yt_tool],
    agent=blog_researcher,
)

write_task=Task(
    description=(
        "get the info from the youtube channel on the topic {topic}."
    ),
    expected_output='Summarize the info from the youtube channel video on the topic{topic} and create a compelling blog post in 3 paragraphs with a catchy title and a meta description for the blog post',
    tools=[yt_tool],
    agent=blog_writer,
    async_execution=False,
    output_file='new-blog-post.md' # Example of output customization
)