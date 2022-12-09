#Magic 8 Ball
import json
import random 
import time

import speech_recognition as sr

r = sr.Recognizer()

import pyaudio
import wave


# pip3 install playsound pyaudio pydub ffmpeg-python
# pip3 install SpeechRecognition pydub

# Need to add component that asks user to indicate when
# ready to ask quesiton.

# For text-to-speech API
import gtts
import os
from playsound import playsound

# pip3 install gTTS pyttsx3 playsound
# pip uninstall playsound
# pip install playsound==1.2.2

# Dictionary to store all magic 8 ball responses
responses = {
    # Positive Respones
    1: "It is certain.",
    2: "It is decidedly so.",
    3: "Without a doubt.",
    4: "Yes definitely.",
    5: "You may rely on it.",
    6: "As I see it, yes.",
    7: "Most likely.",
    8: "Outlook good.",
    9: "Yes.",
    10: "Signs point to yes.",
    # Neutral Responses
    11: "Reply hazy, try again.",
    12: "Ask again later.",
    13: "Better not tell you now.",
    14: "Cannot predict now.",
    15: "Concentrate and ask again.",
    # Negative Responses
    16: "Don't count on it.",
    17: "My reply is no.",
    18: "My sources say no.",
    19: "Outlook not so good.",
    20: "Very doubtful."
}

# Prints a random value from the 'reponses' dictionary
def getResponse():
    randomNumber = random.randrange(1, len(responses))
    print(responses[randomNumber])
    tts = gtts.gTTS(responses[randomNumber])
    tts.save("response.mp3")
    playsound("response.mp3")
    os.remove("response.mp3")

# Prompts the user to ask a question
# Take in user input
# Wait before providing a response
# Repeat steps indefinitely
def magic8ball():
    while True:
        print("Please ask a question.")


        # the file name output you want to record into
        filename = "recorded.wav"
        # set the chunk size of 1024 samples
        chunk = 1024
        # sample format
        FORMAT = pyaudio.paInt16
        # mono, change to 2 if you want stereo
        channels = 1
        # 44100 samples per second
        sample_rate = 44100
        record_seconds = 5
        # initialize PyAudio object
        p = pyaudio.PyAudio()
        # open stream object as input & output
        stream = p.open(format=FORMAT,
                channels=channels,
                rate=sample_rate,
                input=True,
                output=True,
                frames_per_buffer=chunk)
        frames = []
        print("Listening...")
        for i in range(int(sample_rate / chunk * record_seconds)):
            data = stream.read(chunk)
            # if you want to hear your voice while recording
            # stream.write(data)
            frames.append(data)
        print("Finished listening.")
        # stop and close stream
        stream.stop_stream()
        stream.close()
        # terminate pyaudio object
        p.terminate()
        # save audio file
        # open the file in 'write bytes' mode
        wf = wave.open(filename, "wb")
        # set the channels
        wf.setnchannels(channels)
        # set the sample format
        wf.setsampwidth(p.get_sample_size(FORMAT))
        # set the sample rate
        wf.setframerate(sample_rate)
        # write the frames as bytes
        wf.writeframes(b"".join(frames))
        # close the file
        wf.close()

        filename = "recorded.wav"
        with sr.AudioFile(filename) as source:
            # listen for the data (load audio to memory)
            audio_data = r.record(source)
            # recognize (convert from speech to text)
            question = r.recognize_google(audio_data)
        print(question + "?")
        # question = input()
        print("Thinking...")
        time.sleep(10.5)   #random.randrange(3, 5)     <--- alternative code to have randomized time
        getResponse()
        time.sleep(3)

# Main function
if __name__ == "__main__":
    magic8ball()