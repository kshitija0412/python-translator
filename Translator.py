#importing libraries
import speech_recognition as sr
from gtts import gTTS
from googletrans import Translator
from playsound import playsound


#defining the recognizer 
r = sr.Recognizer()

#instructing to start the translation
print("\nPlease speak!!")


#defining the microphone
mic = sr.Microphone(device_index=0)

#recognizing speech
with mic as source:
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)
    

#printing the audio input
result = r.recognize_google(audio)
print("\n\nAudio Input")
print(result)


#building the translator

#define translator
p = Translator()
#k = p.translate(str(result), dest='es')
k = p.translate(str(result), dest='en')


#detecting the audio input language
print("\nAudio input language: ", k.src)


#translating the text into destination language
translated = str(k.text)
print("\n\nTranslated Output in Spanish")
print(translated)


#taking translated text as input to convert to audio
mytext = translated

#language in which you want the audio output
#language = 'es'
language = 'en'

#passing the desired text and language to the engine
#we have marked slow=false which tells the module that the speed of the converted audio is high
myobj = gTTS(text = mytext, lang = language, slow = False)


#saving the converted audio output in a mp3 file format
myobj.save(f"outputAudio.mp3")


#playing the saved audio output file
playsound(f'E:\SEM 4\SBL\Python Programs\outputAudio.mp3')

#marking the end of the program
print('\n\nHope you had a great time using our translator!!')





























