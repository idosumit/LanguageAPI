import googletrans
import speech_recognition as sr
import gtts
import playsound

recognizer = sr.Recognizer()
translator = googletrans.Translator()
input_lang = 'ja'
output_lang = 'en'

try:
    with sr.Microphone() as source:
        print("You can speak now")
        voice = recognizer.listen(source)
        text = recognizer.recognize_google(voice, language=input_lang)
        print(text)
        translated = translator.translate(text, dest=output_lang)
        print(translated.text)
        converted_audio = gtts.gTTS(translated.text, lang=output_lang)
        converted_audio.save('converted_voice.mp3')
        playsound.playsound('converted_voice.mp3')

except:
    pass