#The SpeechRecognition Library is uded for performing speech recognition, with support for several engines and APIs, online and offline.
#It library needs the PyAudio package to be installed in order for it to interact with the microphone input. 
import speech_recognition as sr
#urllib3 is a powerful, sanity-friendly HTTP client for Python.
#It provides Thread safety. Client-side SSL/TLS verification. Helpers for retrying requests and dealing with HTTP redirects. Proxy support for HTTP and SOCKS.
import urllib3
#disables the endless 'insecurerequest' warning which arises while trying to connect to the internet.
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

while (True == True):
#The primary purpose of a Recognizer instance is to recognize speech.
#Here Each instance comes with a variety of settings and functionality for recognizing speech from an audio source.
#This class helps obtain audio from the microphone
  r = sr.Recognizer()
  with sr.Microphone() as source:
    # listen for 1 second and create the ambient noise energy level
    r.adjust_for_ambient_noise(source, duration=1)
    print("Say something!")
    #listens for the user's input
    #here source is the microphone as already assigned to the variable source. phrase_time_limit determines the time period microphone will take user input
    #which here is set to 5 seconds.
    audio = r.listen(source,phrase_time_limit=5)
 
# recognize speech using Sphinx/Google
#Google API Client Library for Python is required if and only if you want to use the Google Cloud Speech API (recognizer_instance.recognize_google_cloud).
  try:
    #response = r.recognize_sphinx(audio)
    response = r.recognize_google(audio)
    #creates a output.txt names file if it doesn't exist and appends the speech data to the file.
    f=open('output.txt','a')
    f.write(response + ".")
    f.close()

 #here we ask the user if he/she wants to continue the recognition part or end the program.
    while True:
        answer = input('Do you want to continue?:')
        if answer.lower().startswith("n"):
            print("Exiting The Program!")
            exit()#exits the program
        else:
            print("Listening Again...")
            break #continues asking for more input from the user.
   #error occurs when google could not understand what was said
  except sr.UnknownValueError:
    print("Sphinx could not understand audio") #Sphinx cannot understand the user input because of the ambience in the background.
  except sr.RequestError as e:
    print("Sphinx error; {0}".format(e)) #this error occurs when some of the libraries required for running sphinx are missing from python.


