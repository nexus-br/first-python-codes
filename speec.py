import speech_recognition as sr
from time import sleep
recmic = sr.Recognizer()
listmic = [(sr.Microphone().list_microphone_names())]
for mics in listmic:
  print(mics)
def tospeech():
 with sr.Microphone(1) as source:
  recmic.adjust_for_ambient_noise(source)
  print("não se esqueça de configurar o microfone de maneira correta antes de rodar o app")
  print("lembre-s que é nescessario estar online para converter o audio em texto")
  print("estou ouvindo pode falar...")
  audio = recmic.listen(source)
  recmic.energy_threshold = 300
  recmic.pause_threshold = 1
  try:
   frase = recmic.recognize_google(audio, language='pt-BR')
   print("eu ouvi você dizer...",frase)
   return frase
  except:
   print("erro, não consegui entender, fale mais pausadamente")	
tospeech()
