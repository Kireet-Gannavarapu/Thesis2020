import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
  print("Speak something: ")
  audio = r.listen(source)

  try:
    text = r.recognize_google(audio)
    print(text)
  except:
    print("Could not recognize")
