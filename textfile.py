from gtts import gTTS 
file = open('demo.txt','r').read().replace("\n"," ")
language = 'en'
speech = gTTS(text=str(file),lang=language,slow=False)
speech.save('final.mp3')
