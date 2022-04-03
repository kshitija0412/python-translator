#importing libraries
import speech_recognition as sr
import pyttsx3
from gtts import gTTS
from googletrans import Translator
from playsound import playsound

#defining the recognizer
r = sr.Recognizer()

print("\nPlease select the language you'll be speaking in")

def getLanguage(language):
    switcher = {
        1: "zh"
        2: "en-IN"
        3: "fr-FR"
        }
    return switcher.get(language, 0)

def getSelection():
    while True:
        try:
            userInput = int(input())
            if (userInput < 1 or userInput > 3):
                print("Invalid option!! Try again!!")
                continue
            except ValueError:
                print("Invalid option!! Try again!!")
                continue
            else:
                return userInput
                break
        
        
#instructing to start the translation
print("\nPlease speak!!")


#defining the microphone
mic = sr.Microphone(device_index=0)

#recognizing speech
with mic as source:
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)

print("\nConverting the audio to text!!")    

#https://hashedin.com/blog/how-to-convert-different-language-audio-to-text-using-python/
#https://pypi.org/project/SpeechRecognition/1.2.3/


#printing the audio input
result = r.recognize_google(audio)
print(f"You spoke in {language} language")
print("\n\nAudio Input")
print(result)



#building the translator


#define translator
p = Translator()
k = p.translate(str(result), dest='es')


translated = str(k.text)
print("\n\nTranslated Output")
print(translated)


#taking translated text as input to convert to audio
mytext = translated

#language in which you want the audio output
language = 'es'

#passing the desired text and language to the engine
#we have marked slow=false which tells the module that the speed of the converted audio is high
myobj = gTTS(text = mytext, lang = language, slow = False)

#saving the converted audio output in a mp3 file format
myobj.save("outputAudio.mp3")

#playing the saved audio output file
playsound(f'E:\SEM 4\SBL\Python Programs\outputAudio.mp3')

#marking the end of the program
print('\n\nHope you had a great time using our translator!!')





























