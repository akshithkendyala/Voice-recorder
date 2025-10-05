import sounddevice as sd
import numpy as np

duration = int(input("Enter number of seconds you want to record: "))  
fs = 48000    # sample rate (samples per second) 
#fs can be 44100(CD quality) | 48000(Studio quality) | 22050(lower quality)

print("\U0001F3A4 Recording...")
recording = sd.rec(int(duration * fs), samplerate=fs, channels=2, dtype='float64') 
#channels can be set to 1 or 2; 1 -> mono(single channel), 2 -> stereo(left + right)
#for most modern recordings we use 2, if you're doing voice-only capture we use 1 to save space
#'float64' | 'float32' | 'int16' => 'float32' is enough in most of the cases 
sd.wait()
print("\U00002705 Recording complete!")

# Playback
print("\U0001F50A Playing back...")
sd.play(recording, fs)
sd.wait()
print("\U00002705 Playback done!")
