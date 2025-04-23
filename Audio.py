from pathlib import Path
from agno.agent import Agent
from agno.media import Audio
from agno.models.google import Gemini

agent = Agent(
    model=Gemini(id="gemini-2.0-flash-exp", api_key="Your_api_key"),
    markdown=True,
)

# Please download a sample audio file to test this Agent and upload using:
audio_path = Path(__file__).parent.joinpath(r"path_to _the _audio_file")

agent.print_response(
    "Analyze and Predict the Emotion of the audio file",
    audio=[Audio(filepath=audio_path)],
    stream=True,
)
