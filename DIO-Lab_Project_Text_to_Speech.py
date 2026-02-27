# !pip install gTTS

from gtts import gTTS
from IPython.display import Audio, display

# Create the audio object
gtts_object = gTTS(
    text="Ao verme que primeiro roeu as frias carnes do meu cadáver dedico como saudosa lembrança estas memórias póstumas.", 
    lang="pt", 
    slow=False
)

# Save the audio file
audio = "/content/audio.wav"
gtts_object.save(audio)

# Display the audio player
display(Audio(audio, autoplay=True))
