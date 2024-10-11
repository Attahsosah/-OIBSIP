import speech_recognition as sr
import pyttsx3
import openai
from openai import OpenAI
import time
import schedule
from datetime import datetime, timedelta
import dateparser
import smtplib
import os
import webbrowser
import requests
from dotenv import load_dotenv
# from bs4 import BeautifulSoup

load_dotenv()

client = OpenAI(api_key='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')



def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.5  # Shorten time before recognizing a phrase
        r.energy_threshold = 300
        audio = r.listen(source)
        try:
            print("Processing what you said ...")
            text = r.recognize_google(audio)
            print(f"Okay you said: {text}")
            return text
        except sr.UnknownValueError:
            print("")
            return None

engine = pyttsx3.init()

# def search_web(query):
#     search_url = f"https://www.google.com/search?q={query}"
#     response = requests.get(search_url)
#     soup = BeautifulSoup(response.text, 'html.parser')

#     # Extract the first few search results (titles and links)
#     results = []
#     for g in soup.find_all('div', class_='BNeawe vvjwJb AP7Wnd'):
#         title = g.get_text()
#         link = g.find_previous('a')['href']
#         results.append((title, link))

#     return results

# def get_search_results(query):
#     search_results = search_web(query)

#     if search_results:
#         speak("Here are the top search results.")
#         for index, (title, link) in enumerate(search_results[:5]):  # Limit to top 5 results
#             print(f"{index + 1}. {title}: {link}")
#             speak(f"Result {index + 1}: {title}")

#     else:
#         speak("Sorry, I couldn't find any results for your search.")


def speak(text):
    engine.say(text)
    engine.runAndWait()


def get_openai_response(prompt):
    response = client.completions.create(engine="gpt-3.5-turbo",
    prompt=prompt,
    max_tokens=5000)
    return response.choices[0].text.strip()

# Functionality to send emails---------------------------------------------------------
def send_email(receiver_email, subject, body):
    sender_email = os.getenv("EMAIL")
    password = os.getenv("EMAIL_PASSWORD")  
    message = f"Subject: {subject}\n\n{body}"

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)
        return "Email sent successfully!"
    except Exception as e:
        print(f"Failed to send email: {e}")
        return "Failed to send email."

# The reminder section:--------------------------------------------------------------------------------------------

def set_reminder(reminder_text, reminder_time):
    speak(f"Your reminder is  set for {reminder_time}. I will remind you  {reminder_text}.")
    schedule.every().day.at(reminder_time).do(speak, f"It's time  : {reminder_text}")
    while True:
        schedule.run_pending()
        time.sleep(1)

def parse_time_command(command):
    
    words = command.split()

    # Try to find the part that indicates time
    time_keywords = ["at", "in"]
    for keyword in time_keywords:
        if keyword in words:
            time_part = " ".join(words[words.index(keyword):])  # Extract time part
            reminder_text = " ".join(words[:words.index(keyword)])  # Everything before time
            break
    else:
        return None, None  # If no valid time keyword was found
    
    reminder_text = reminder_text.replace("remind me", " ")
    reminder_text = reminder_text.replace("my","your")


    # Use dateparser to understand the time part
    reminder_time = dateparser.parse(time_part)
    
    # Convert the parsed time to the required string format (e.g., "14:30")
    if reminder_time:
        formatted_time = reminder_time.strftime("%H:%M")
        return formatted_time, reminder_text

    return None, None





def GPT_response(prompt):
    
    response = client.chat.completions.create(
        messages=[
            {
                "role":"user",
                "content":prompt, 
            }
            
        ], 
        model="gpt-3.5-turbo", 
        
    )
    
    return response.choices[0].message.content

def main():
    while True:
        command = get_audio()
        query = get_audio()
        if command:
            if any(say in command for say in ["Hello", "Hi there", "Greetings"]):
                speak("Hello there how are you. ")
                speak("My name is Arthur")
                speak("I am your AI voice Assitant")
                speak("I can remind you of things, send emails and more")
                speak("How may I be of assistance?")

            
                
            # elif "search for" in query:
            #     search_term = query().replace("search for", "").strip()
            #     get_search_results(search_term)
                
                


            elif any(word in command for word in ["say","tell","who","I", "No","Can", "Set", "what", "when", "where", "how", "should", "why", "will", "would", "can", "could", "do", "does", "is", "are", "am", "was", "were", "have", "has", "had", "which","tell","wow", "thank you"]):
               # Gets a response from GPT-3
               response = GPT_response(command)

               # Converts the response to speech
               speak(response)
               print(response)

            elif "email" in command:
                # Instead of speaking, ask the user to type the email, subject, and body
                speak("Who do you want to send the email to?")
                speak("Would you mind typing it out? thanks")
                receiver = input("Type the recipient's email address: ")
                speak("What is the subject?")
                subject = input("Type the subject of the email: ")
                speak("What should I say in the email?")
                body = input("Type the email body: ")
                if receiver and subject and body:
                    send_email(receiver, subject, body)
                    speak("Email sent.")
            elif "remind me" in command:
                try:
                     # Parse the time and reminder message
                    reminder_time, reminder_text = parse_time_command(command)
                            
                    # Set the reminder
                    set_reminder(reminder_text, reminder_time)
                except Exception as e:
                    speak("..")
                    print(f"Error: {e}")
            elif "stop" in command:
                speak("Okay goodbye")
                break
            else:
                speak("how may I help")

if __name__ == "__main__":
    main()





