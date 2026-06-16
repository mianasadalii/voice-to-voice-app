# 🎙️ Voice-to-Voice AI Assistant

This is a simple AI-powered voice assistant built with Python, Gradio, and Groq API.  
It takes your voice input, converts it into text, generates an AI response, and then converts the response back into speech.

---

## 🚀 Features

- 🎤 Voice input using microphone  
- 🧠 Speech-to-text using Groq Whisper model  
- 💬 AI response using Llama 3 model  
- 🔊 Text-to-speech using Google TTS  
- 🌐 Simple web UI using Gradio  
- ☁️ Ready to deploy on Hugging Face Spaces  

---

## 🛠️ Tech Stack

- Python  
- Gradio  
- Groq API  
- gTTS (Google Text-to-Speech)  
- Whisper (via Groq)  

---

🧠 How It Works
You speak into the microphone
Audio is converted to text using Whisper (Groq API)
Text is sent to Llama 3 model
AI generates a response
Response is converted into speech
You hear the AI voice reply 🎧

---

## 📦 Installation

Install required libraries:

```bash
pip install gradio groq gtts
