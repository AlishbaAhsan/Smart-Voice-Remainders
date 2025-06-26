import streamlit as st
from ai_remainders import text_to_speech, ai_text

st.title("Magical Reminder Generator 🪄")

st.write("""
Enter your name and a short event description. The app will generate a delightful, personality-rich reminder and an audio file for you!
""")

user_name = st.text_input("Your Name")
event_text = st.text_area("Event Description", height=100)

if st.button("Generate Reminder"):
    if not user_name or not event_text:
        st.warning("Please enter both your name and an event description.")
    else:
        with st.spinner("Generating your magical reminder and audio..."):
            # Get the AI text first
            reminder_text = ai_text(user_name, event_text)
            if reminder_text:
                st.markdown(f"**Generated Reminder:**\n\n> {reminder_text}")
                audio_url, file_path = text_to_speech(user_name, event_text, final_text=reminder_text)
                if file_path:
                    st.success("Your reminder audio is ready!")
                    st.audio(file_path, format="audio/mp3")
                    st.download_button(
                        label="Download MP3",
                        data=open(file_path, "rb").read(),
                        file_name=file_path.split("/")[-1],
                        mime="audio/mp3"
                    )
                else:
                    st.error("Failed to generate audio. Please check your API keys and try again.")
            else:
                st.error("Failed to generate reminder text. Please try again.") 