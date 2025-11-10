import speech_recognition as sr
import pyttsx3

# Initialisation du moteur vocal
engine = pyttsx3.init()

def parler(texte):
    engine.say(texte)
    engine.runAndWait()

def ecouter():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Parle maintenant...")
        audio = recognizer.listen(source)
        try:
            texte = recognizer.recognize_google(audio, language="fr-FR")
            print("🗣️ Tu as dit :", texte)
            return texte
        except:
            print("❌ Je n'ai pas compris...")
            return ""

# Test
parler("Bonjour, je suis ton assistant vocal.")
texte = ecouter()
if texte:
    parler(f"Tu as dit {texte}")
