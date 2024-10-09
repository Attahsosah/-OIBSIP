# VOICE ASSISTANT BY Attah Sosah 
from gtts import gTTS
import os 
import openai
import webbrowser
import pyautogui
from pydub import AudioSegment 
from dotenv import load_dotenv 
import speech_recognition as speech_r

# Loads environment variables from a .env file
load_dotenv()

# Retrieves the OpenAI API key from environment variables
KEY_AI = os.getenv("OPENAI_KEY")

# Sets the OpenAI API key for use in the program
openai.api_key = KEY_AI 



def get_audio():
    r = speech_r.Recognizer()
    with speech_r.Microphone() as source:
        print("Listening for your commands...")
        audio = r.listen(source)
        try:
            print("Processing...")
            prompt = r.recognize_google(audio)
            print(f"I think you  said: {prompt}")
            return prompt
        except speech_r.UnknownValueError:
            print("Sorry, I did not understand.")
            return None
        
        
#Time to convert the text command to speech 


def text_to_speech(response_text):
   print(response_text)
   tts = gTTS(text=response_text, lang="en")
   
   #Here we save the spoken text to mp3 format 

   tts.save("response.mp3")

    #converted into audio segment 
   sound = AudioSegment.from_mp3("response.mp3")

   # Exports the audio segment as a wav file
   sound.export("response.wav", format="wav")

   # Plays the wav file using the system's default audio player
   os.system("afplay response.wav")
   
#retrieving the response from GPT-3 
def GPT_response(prompt):
    
    response = openai.chat.completions.create(
        messages=[
            {
                "role":"user",
                "content":"prompt", 
            }
            
        ], 
        model="gpt-3.5-turbo", 
        
    )
    
    return response.choices[0].message.content

# Main function that runs the program
def main():
   text_to_speech("Hello What Can I Do For You Today?")
   while True:
       # Listens for a voice command
       command = get_audio()
       if command:
           # Checks if the command contains certain keywords
           if any(word in command for word in ["who", "what", "when", "where", "how", "should", "why", "will", "would", "can", "could", "do", "does", "is", "are", "am", "was", "were", "have", "has", "had", "which",]):
               # Gets a response from GPT-3
               response = GPT_response(command)

               # Converts the response to speech
               text_to_speech(response)

           # open chrome if user says open chrome
           if "open chrome" in command:
               text_to_speech("Opening Chrome.")

               # Opens Google Chrome to the Google homepage
               webbrowser.open('http://google.com')

           # exit if user says exit
           if "exit" in command:
               text_to_speech("Goodbye.")

               # Breaks the loop, ending the program
               break
           else:
               text_to_speech("Sorry, I don't understand that command.")


if __name__ == '__main__':
   main()