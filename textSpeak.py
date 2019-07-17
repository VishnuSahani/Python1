from gtts import gTTS
from playsound import playsound
tts = gTTS('hello vishnu sahani son of mr. suraj sahani')
#tts = gTTS(input("write for listening"))
tts.save('textSpeak.mp3')
playsound('textSpeak.mp3')
