Voice Recognition with Python & pyttsx3

A basic Python project that listens to your voice, converts speech to text, and responds using text-to-speech. This project uses SpeechRecognition for voice input and pyttsx3 for offline speech output.

📝 Features

🎙️ Speech-to-Text using SpeechRecognition

🔊 Text-to-Speech using pyttsx3 (works offline)

🧠 Simple and beginner-friendly code

⚙️ Works on Windows, macOS, and Linux

📦 Requirements

Install the required libraries:

pip install SpeechRecognition pyttsx3 pyaudio


Some systems may also need additional audio drivers for pyaudio.

▶️ How to Run

Clone the repository:

git clone https://github.com/your-username/Voice-recognition-with-pyttsx3.git


Navigate into the folder:

cd Voice-recognition-with-pyttsx3


Run the Python script:

python main.py

📁 Project Structure
Voice-recognition-with-pyttsx3/
│
├── main.py        # Main script for voice recognition + TTS
├── README.md      # Documentation
└── requirements.txt (optional)

📚 How It Works

The program listens to the microphone.

It converts your speech to text using Google Speech Recognition (free tier).

The recognized text is spoken back using pyttsx3, an offline text-to-speech engine.

🔧 Use Cases

Simple voice assistants

Learning STT + TTS basics

Automation using voice commands

Accessibility tools

🤝 Contributing

Feel free to submit issues or pull requests to improve the project.
