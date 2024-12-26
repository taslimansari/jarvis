# Jarvis Virtual Assistant

**Jarvis** is a personal virtual assistant built using Python that can perform tasks such as voice recognition, web browsing, music control, and more. The assistant responds to voice commands and uses various APIs to provide enhanced functionality.

## Features
- **Voice recognition**: Interact with the assistant through speech.
- **Text-to-speech**: The assistant speaks back to you using `pyttsx3` and `gTTS`.
- **Web browsing**: Open websites directly via voice commands.
- **Music control**: Play and control music using the custom `musicLibrary`.
- **API integration**: Fetch data from external sources like news and weather (using `requests` and `cohere`).
- **Customizable**: Add more features as needed.

## Dependencies
This project requires the following Python libraries:

- `speech_recognition`
- `pyttsx3`
- `webbrowser`
- `musicLibrary`
- `requests`
- `cohere`
- `gTTS`
- `pygame`
- `os`

These libraries can be installed by running:

```bash
pip install -r requirements.txt
