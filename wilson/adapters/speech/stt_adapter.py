import speech_recognition as sr
from wilson.core.ports.ports import STTPort

class SpeechRecognitionAdapter(STTPort):
    def __init__(self):
        self.recognizer = sr.Recognizer()
        
    async def listen_and_transcribe(self) -> str:
        with sr.Microphone() as source:
            print("Listening...")
            self.recognizer.adjust_for_ambient_noise(source)
            try:
                # Capture audio
                audio = self.recognizer.listen(source, timeout=5, phrase_time_limit=10)
                print("Processing audio...")
                
                # Transcribe
                text = self.recognizer.recognize_google(audio)
                print(f"Recognized: {text}")
                return text
            except sr.WaitTimeoutError:
                print("No speech detected.")
                return ""
            except sr.UnknownValueError:
                print("Could not understand audio.")
                return ""
            except sr.RequestError as e:
                print(f"Could not request results; {e}")
                return ""
