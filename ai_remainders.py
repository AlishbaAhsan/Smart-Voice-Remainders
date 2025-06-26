import os
import re
import requests
from openai import OpenAI
from dotenv import load_dotenv
from datetime import datetime

# Load API key from .env file
load_dotenv(override=True)

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

### ollama client
API_KEY = os.getenv("OLLAMA_API_KEY")
BASE_URL = os.getenv("OLLAMA_BASE_URL")

ollama_client = OpenAI(
    api_key=API_KEY,
    base_url=BASE_URL
)

def ai_text(user_name, text):
    prompt = f"""
    You are a cheerful, whimsical reminder assistant — think of yourself as a warm-hearted, magical best friend who turns ordinary reminders into little bursts of joy. 
    Your job is to rewrite plain event texts into delightful, emotionally expressive, and personality-rich reminders that feel like they're from someone who truly cares.

    Instructions:
    1. Clearly and naturally include the event details (e.g., type of appointment and time), but avoid sounding robotic.
    2. Limit the reminder to 15–20 words max — must be short enough to fit in a 10-second audio clip. Make every word count!
    3. Weave the user's name ({user_name}) into the reminder in a fun, unexpected way (but not always at the start).
    4. Use playful humor, joyful language, and a light touch of sarcasm to make the reminder sparkle with personality.
    5. Sometimes add suitable expressive interjections to make the message feel warm, spontaneous, and human.
    6. The tone should always feel like it's coming from a supportive, slightly mischievous friend who wants to make {user_name} smile.
    7. Do not add emojis EVER. Instead, use punctuations or words to convey the emotions and expressions.
    
    Now, take the following event description and transform it into one of these magical, smile-inducing reminders:
    Event: {text}
    """

    try:
        response = ollama_client.chat.completions.create(
            model="openchat:latest",
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
        )

        return response.choices[0].message.content

    except Exception as e:
        print("Error generating social media post:", e)
        return None

def sanitize_filename(filename):
    """
    Replace characters that are not safe for filenames.
    """
    return re.sub(r'[^\w\-_\.]', '_', filename.strip())

def text_to_speech(user_name, text, final_text=None):
    """
    Generate an audio file (MP3) of the AI-generated text using OpenAI's TTS API.
    The audio file will be saved in the "remainders" folder with the filename based on the provided text.
    """
    if final_text is None:
        final_text = ai_text(user_name, text)
    print("AI Text:", final_text)
    
    if final_text is None:
        return None, None

    # OpenAI TTS API configuration
    url = "https://api.openai.com/v1/audio/speech"
    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "model": "gpt-4o-mini-tts",
        "voice": "nova",
        "input": final_text,
        "instructions": (
           """
           Affect/personality: A cheerful guide \n\n
           Tone: Friendly, clear, and reassuring, creating a calm atmosphere and making the listener feel confident and comfortable.\n\n
           Pronunciation: Clear, articulate, and steady, ensuring each instruction is easily understood while maintaining a natural, conversational flow.\n\n
           Pause: Brief, purposeful pauses after key instructions (e.g., "cross the street" and "turn right") to allow time for the listener to process the information and follow along.\n\n
           Emotion: Warm and supportive, conveying empathy and care, ensuring the listener feels guided and safe throughout the journey.
           """
        ),
        "response_format": "mp3"  # Request an MP3 file
    }
    
    # Send the POST request to create speech audio
    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 200:
        remainders_dir = "remainders"
        if not os.path.exists(remainders_dir):
            os.makedirs(remainders_dir)

        # Sanitize user name and text
        safe_user_name = sanitize_filename(user_name)
        # Get current timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_filename = os.path.join(remainders_dir, f"{safe_user_name}_{timestamp}.mp3")
        with open(output_filename, "wb") as f:
            f.write(response.content)
        # Return None for audio_url (as we're saving locally) and the file path
        return None, output_filename
    else:
        print(f"Error: {response.status_code}")
        print(response.text)
        return None, None

# Uncomment the following code block to test the functionality
# if __name__ == "__main__":

#     test_inputs = [
#         ("John", "Dentist's Appointment--Routine check-up, Date: 2025-04-15 10:00:00 +0000"),
#         ("Alishba", "Sprint meeting with the team at 10:00 AM")
#     ]
    
#     for user_name, event_text in test_inputs:
#         print(f"\nProcessing reminder for {user_name}:")
#         audio_url, file_path = text_to_speech(user_name, event_text)
#         print("Generated Audio URL:", audio_url)
#         print("Saved Audio File Path:", file_path)
#         print("-" * 50)
