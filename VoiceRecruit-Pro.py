
"""------------------------------ VoiceRecruit Pro --------------------------- """

"""------------------this code is when interviewer ask any question, this program using chatgpt, retrieve answer and 
display in a transparent tkinter window. with that this program, record the applicants answer and review it---------"""

import azure.cognitiveservices.speech as speechsdk
from tkinter import *
from threading import Thread 
import requests

exit_flag = False

def on_close():
    global exit_flag
    exit_flag = True
    root.destroy() 

    

root = Tk()
root.wm_attributes('-transparentcolor', '#abcdef')
root.protocol("WM_DELETE_WINDOW", on_close)
root.config(bg='#abcdef')

# Set the window size and position
window_width = 500
window_height = root.winfo_screenheight()  # Set the height to match the screen height
x_coordinate = root.winfo_screenwidth() - window_width  # Set the x-coordinate to place it on the right

root.geometry(f'{window_width}x{window_height}+{x_coordinate}+0')

# due to this line, the "root" window will stay on top of all other opened applicaation
root.wm_attributes('-topmost', 1)

# Function to create a label with its own background color and a delete button
def messages(text,places,bg_color):
    #bg_color="lightblue"
    label_frame = Frame(root, bg=bg_color)
    label_frame.pack(pady=5, padx=10, anchor=places)


    label = Label(label_frame, text=text, bg=bg_color,wraplength=450,justify="left",font=("Times New Roman", 13) )
    label.pack(side=LEFT, padx=5)

def generate_completion(prompt):
    try:
        response = requests.post(
            url="https://api.binjie.fun/api/generateStream",
            headers={
                "origin": "https://chat.jinshutuan.com",
                "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.79 Safari/537.36",
            },
            json={
                "prompt": prompt,
                "system": "Always talk in English.",
                "withoutContext": True,
                "stream": False,
            },
        )
        return response.text
    except:
        return "check your connection"

def is_question(s):
    interrogatives = ["Am", "How", "Were","Weren’t","Are", "How Come", "What","How Far","Aren’t", "How Long",
    "Can", "How Many", "What Kind","How Much", "What Time","Can’t", "How Often", "When","Could", "How Old",
    "Couldn’t", "Huh", "Where","Did", "Is", "Which","Didn’t", "Isn’t","Do", "May", "Who","Mayn’t","Might", "Whom",
    "Mightn’t", "Whose","Mustn’t","Neither", "Why","Needn’t","Oughtn’t", "Why Don’t","Will","Should", "Won’t",
    "Shouldn’t", "Would","Was","Wasn’t", "Wouldn’t", "tell us", "tell me","introduce"]
    return s.endswith('?') or any(s.lower().startswith(i) for i in interrogatives)

def recognize_from_microphone():
    sk="5c8a7b93496949df9bd149b9af6a566b"
    sr="centralindia"
    # This example requires environment variables named "SPEECH_KEY" and "SPEECH_REGION"
    speech_config = speechsdk.SpeechConfig(subscription=sk, region=sr)
    speech_config.speech_recognition_language="en-US"

    audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

    print("Speak into your microphone.")
    while not exit_flag:
        speech_recognition_result = speech_recognizer.recognize_once_async().get()
        try:
            if speech_recognition_result.reason == speechsdk.ResultReason.RecognizedSpeech:
                
                if is_question(speech_recognition_result.text): #if it is a question or not

                    question1=speech_recognition_result.text
                    messages(question1,"e","lightgreen")
                    with open("history_and_review_of_interview.txt","a") as file :
                        file.write("__________________INTERVIEWER ASKED: __________________\n        ")
                        file.write(speech_recognition_result.text)
                        file.write("\n \n")
                    file.close()

                    question = "interviewer is asking me " + speech_recognition_result.text + ". answer this question as if you are applicant"
                    interview_answer= generate_completion(question)
                    print("\n")
                    print(interview_answer)
                    messages(interview_answer,"w","lightblue")
                    print("\n")

                    # to register chatgpt answer
                    with open("history_and_review_of_interview.txt","a") as file :
                        file.write("__________________CHATGPT ANSWER: __________________ \n        ")
                        file.writelines(interview_answer)
                        file.write("\n \n")
                    file.close()

                else: # to register applicant answer
                    with open("history_and_review_of_interview.txt","a") as file :
                        file.write("__________________YOU ANSWERED: __________________\n        ")
                        file.write(speech_recognition_result.text)
                        file.write("\n \n")
                    file.close()

                    if(interview_answer != speech_recognition_result.text):

                        commenting = "interviewer asked me '" +question1+ "' \n and i answered it as '" + speech_recognition_result.text + "'\n review my answer"

                        comments = generate_completion(commenting)

                        with open("history_and_review_of_interview.txt","a") as file :
                            file.write("__________________COMMENT ON IT: __________________\n        ")
                            file.write(comments)
                            file.write("\n \n \n \n ")
                        file.close()
                        
        except:
            pass

def start_recognition_thread():
    global recognition_thread
    recognition_thread = Thread(target=recognize_from_microphone)
    recognition_thread.start()

# Start the recognition thread
start_recognition_thread()

root.mainloop()