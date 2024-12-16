import tkinter as tk
from gtts import gTTS
import os
from playsound import playsound

def text_to_speech():
    text = entry.get()
    if text:
        tts = gTTS(text=text, lang='en')
        tts.save("output.mp3")
        playsound("output.mp3")

root = tk.Tk()
root.title("Text to Speech Converter")

label = tk.Label(root, text="Enter text to convert to speech:", font=("Arial", 16))
label.pack(pady=10)

entry = tk.Entry(root, width=30)
entry.pack(pady=10)

play_button = tk.Button(root, text="Play", command=text_to_speech, width=20, height=2)  # Bigger button
play_button.pack(pady=10)


exit_button = tk.Button(root, text="Exit", command=root.quit, width=20, height=2)  # Bigger button
exit_button.pack(pady=10)

root.mainloop()