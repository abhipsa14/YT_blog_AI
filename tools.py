from crewai_tools import YoutubeChannelSearchTool
from crewai_tools.rag.data_types import DataType

yt_tool = YoutubeChannelSearchTool(
    config={
        "embedding_model": {
            "provider": "ollama",
            "config": {
                "model_name": "nomic-embed-text",
                "url": "http://localhost:11434/api/embeddings",
            },
        },
    },
)

yt_tool.adapter.add(
    "https://www.youtube.com/@krishnaik06",
    data_type=DataType.YOUTUBE_CHANNEL,
)