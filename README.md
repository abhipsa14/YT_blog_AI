# YouTube Blog AI

This project uses CrewAI and local Ollama models to research videos from a
YouTube channel and generate a blog post.

## Requirements

- Python 3.10 or later
- [Ollama](https://ollama.com/)
- A YouTube channel URL supported by the CrewAI YouTube loader

## Setup

Create and activate a virtual environment on Windows:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Start Ollama and download the models used by the project:

```powershell
ollama serve
ollama pull llama3.2
ollama pull nomic-embed-text
```

The project uses:

- `llama3.2` for the CrewAI agents
- `nomic-embed-text` for YouTube content search and CrewAI memory

## Configure the channel

Update the URL in [tools.py](tools.py). Use the complete channel URL, for
example:

```python
yt_tool.adapter.add(
    "https://www.youtube.com/@krishnaik06",
    data_type=DataType.YOUTUBE_CHANNEL,
)
```

Supported channel URL formats include:

- `https://www.youtube.com/@channel_handle`
- `https://www.youtube.com/channel/CHANNEL_ID`
- `https://www.youtube.com/c/channel_name`
- `https://www.youtube.com/user/username`

The Ollama embedding endpoint is:

```text
http://localhost:11434/api/embeddings
```

The agent LLM endpoint is:

```text
http://localhost:11434
```

## Run

With Ollama running, execute:

```powershell
python crew.py
```

The generated blog post is written to `new-blog-post.md`.

To change the subject researched by the crew, update the `topic` value in
[crew.py](crew.py).

## Troubleshooting

### Ollama connection errors

Confirm that Ollama is running and that both models are installed:

```powershell
ollama list
```

### `OPENAI_API_KEY` errors

The YouTube search tool and CrewAI memory require embeddings. This project
configures Ollama embeddings explicitly, so an OpenAI key should not be
required. Make sure `nomic-embed-text` is installed and that the embedding
endpoint is `http://localhost:11434/api/embeddings`.