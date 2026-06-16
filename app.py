# for colab
# !pip install -q groq gradio gtts pydub    

import os
import tempfile
from groq import Groq
from gtts import gTTS
import gradio as gr

GROQ_API_KEY = os.environ.get("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY not found. Please set it in Hugging Face Secrets.")
    
client = Groq(api_key=GROQ_API_KEY)

def speech_to_text(audio_path):

    with open(audio_path, "rb") as audio_file:

        transcription = client.audio.transcriptions.create(
            file=audio_file,
            model="whisper-large-v3-turbo"
        )

    return transcription.text

def generate_response(user_text):

    completion = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful AI assistant."
            },
            {
                "role": "user",
                "content": user_text
            }
        ],
        temperature=0.7,
        max_tokens=512
    )

    return completion.choices[0].message.content

def text_to_speech(text):

    temp_audio = tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".mp3"
    )

    tts = gTTS(text=text, lang="en")

    tts.save(temp_audio.name)

    return temp_audio.name

def voice_assistant(audio):
    try:
        if audio is None:
            return None, "", ""

        user_text = speech_to_text(audio)

        ai_response = generate_response(user_text)

        output_audio = text_to_speech(ai_response)

        return output_audio, user_text, ai_response

    except Exception as e:
        print("ERROR:", e)
        return None, f"Error: {e}", f"Error: {e}"

with gr.Blocks() as demo:

    gr.Markdown("# Voice to Voice AI Assistant")

    audio_input = gr.Audio(
        sources=["microphone"],
        type="filepath",
        label="Speak"
    )

    output_audio = gr.Audio(
        label="AI Voice Response"
    )

    user_text = gr.Textbox(
        label="Your Speech"
    )

    ai_text = gr.Textbox(
        label="AI Response"
    )

    btn = gr.Button("Generate Response")

    btn.click(
        fn=voice_assistant,
        inputs=audio_input,
        outputs=[
            output_audio,
            user_text,
            ai_text
        ]
    )

demo.launch(debug=True)
