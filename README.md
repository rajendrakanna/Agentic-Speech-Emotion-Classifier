# Audio Emotion Analyzer

## Overview
Audio Emotion Analyzer is a Python application that uses Google's Gemini 2.0 Flash model to analyze audio files and predict the emotional content. This tool can identify emotions such as happiness, sadness, anger, excitement, and more from spoken audio.

## Features
- Emotional analysis of audio files
- Support for various audio formats
- Real-time streaming results
- Simple command-line interface
- Powered by Google's Gemini 2.0 Flash multimodal AI model

## Requirements
- Python 3.8+
- Google API key (for Gemini 2.0 Flash model)
- Internet connection
- Supported audio files (WAV, MP3, etc.)

## Installation

### 1. Install the required package

```bash
pip install agno
```

### 2. Set up your API credentials
You'll need a Google API key to use the Gemini 2.0 Flash model. Replace "Your_api_key" in the code with your actual Google API key.

## Usage

1. Save the script to a file (e.g., `audio_emotion_analyzer.py`)
2. Download or prepare an audio file you want to analyze
3. Update the path to your audio file in the script
4. Run the script:
   ```bash
   python audio_emotion_analyzer.py
   ```
5. The application will analyze the audio and output the detected emotions

## Code Explanation

The script uses the following components:

- `Agent` from the `agno` library to handle AI interactions
- Gemini 2.0 Flash as the AI model for audio analysis
- `pathlib` for file path handling
- `Audio` class to process the audio file
- Streaming response for real-time feedback

## Example

```
$ python audio_emotion_analyzer.py
Analyzing audio file...

Detected Emotion: Excitement
Confidence: High

The audio contains excited speech with elevated pitch and increased speaking rate.
Notable characteristics:
- Higher than average volume
- Animated tone
- Occasional laughter
- Rapid speech patterns
```

## Customization

You can modify the prompt to request different types of analysis:

```python
agent.print_response(
    "Identify the speaker's accent and emotional state in this recording",
    audio=[Audio(filepath=audio_path)],
    stream=True,
)
```

## Troubleshooting

If you encounter issues:

1. Ensure your audio file is in a supported format
2. Verify that the audio file path is correct (use absolute paths if needed)
3. Check that your Google API key is valid and has the necessary permissions
4. Make sure the au
