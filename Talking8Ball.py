#Magic 8 Ball
import random
import time
import sys
import pyaudio
import wave
import pyglet
import speech_recognition as sr
import gtts
import os

from PySide6.QtWidgets import (
    QMainWindow, QApplication,
    QLabel, QCheckBox, QComboBox, QListWidget, QLineEdit,
    QLineEdit, QSpinBox, QDoubleSpinBox, QSlider, QWidget,
    QPushButton, QVBoxLayout,
)
from PySide6.QtCore import *
from PySide6.QtUiTools import QUiLoader
from PySide6.QtGui import *

from PySide6 import QtCore, QtGui

from pytube import YouTube
from playsound import playsound
r = sr.Recognizer()

from pathlib import Path

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

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.magicQuestion = "Your question will display here."
        self.magicAnswer = "Your answer will display here."

        # Create a YouTube object with the video URL
        yt = YouTube("https://www.youtube.com/watch?v=n61ULEU7CO0&t=9s")
        # Get the audio stream from the YouTube video
        audio_stream = yt.streams.filter(only_audio=True).first()
        # Download the audio file
        audio_stream.download()
        self.player = pyglet.media.Player()
        # Load the audio file using pyglet
        self.filePath = r"Best of lofi hip hop 2021 ✨ - beats to relaxstudy to.mp4"
        # https://www.youtube.com/watch?v=26nsBfLXwSQ
        self.music = pyglet.media.load(self.filePath)
        self.player.queue(self.music)
        # Play the audio file
        self.player.play()

        # Create a QApplication instance
        #self.app = QApplication([])
        # Create a QWidget instance
        self.widget = QWidget()
        self.widget.setStyleSheet("* {color: qlineargradient(spread:pad, x1:0 y1:0, x2:0 y2:1, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));""background: qlineargradient( x1:0 y1:0, x2:0 y2:1, stop:0 cyan, stop:1 purple);}")
        #  Create a QPushButton instance
        self.button = QPushButton('Ask the Magic 8 Ball')
        # Set the text and size of the button
        self.button.setText('Ask the Magic 8 Ball')
        self.button.resize(200, 100)
        self.button.setStyleSheet("* {color: qlineargradient(spread:pad, x1:0 y1:0, x2:0 y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));""background: qlineargradient( x1:0 y1:0, x2:0 y2:0, stop:0 white, stop:1 white);}")
        layout = QVBoxLayout()
        self.image = QLabel()
        self.image.setAlignment(Qt.AlignCenter)
        ag_file = "magic8ball-animated"
        self.movie = QMovie(ag_file, QByteArray(), self) 
        self.movie.setCacheMode(QMovie.CacheAll) 
        self.movie.setSpeed(200) 
        self.image.setMovie(self.movie) 
        # optionally display first frame
        self.movie.start()
        #self.movie.stop()

        #self.pixmap = QPixmap('8ballimage.png')
        #self.image.setPixmap(self.pixmap)
        self.magicQuestionText = QLabel(self.magicQuestion)
        self.magicAnswerText = QLabel(self.magicAnswer)
        #self.setCentralWidget(self.magicAnswerText)
        font = self.magicAnswerText.font()
        self.magicQuestionText.setAlignment(Qt.AlignCenter)
        self.magicAnswerText.setAlignment(Qt.AlignCenter)
        # Set the layout of the widget and add the button to it
        self.widget.setLayout(layout)
        self.widget.layout().addWidget(self.image)
        self.widget.layout().addWidget(self.button)
        self.widget.layout().addWidget(self.magicQuestionText)
        self.widget.layout().addWidget(self.magicAnswerText)
        # Set the title and size of the widget
        self.widget.setWindowTitle('Magic 8 Ball')
        self.widget.resize(400, 300)
        # Connect the clicked signal of the button to the magic8ball function
        self.button.clicked.connect(self.listening)
        # Show the widget
        self.widget.show()
        # Execute the QApplication
        #self.app.exec()

    def listening(self):
        ####self.magicAnswerText.setText("Listening...")
        ###self.statusMessage = QLabel("Listening...")
        ###self.statusMessage.setAlignment(Qt.AlignCenter)
        ###self.widget.layout().addWidget(self.statusMessage)
        ###self.widget.show()
        #self.start()
        self.player.pause()
        tts = gtts.gTTS("Please ask me a question. You will have 5 seconds. I will start listening in 1 second.")
        tts.save("response.mp3")
        playsound("response.mp3")
        os.remove("response.mp3")
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
        self.magicQuestionText.setText(question + "?")
        self.start()
        self.thinking(question)

    def thinking(self, question):
        #self.movie.start()
        tts = gtts.gTTS("I am done listening. You asked " + question + ". I am thinking of an answer.")
        tts.save("response.mp3")
        playsound("response.mp3")
        os.remove("response.mp3")
        ###self.magicAnswerText.setText("Thinking...")
        randomNumber = random.randrange(1, len(responses))
        response = responses[randomNumber]
        time.sleep(4)
        self.responding(response)

    def responding(self, response):
        #self.movie.stop()
        self.magicAnswerText.setText(response)
        tts = gtts.gTTS(response)
        tts.save("response.mp3")
        playsound("response.mp3")
        os.remove("response.mp3")
        self.player.play()
    
    def start(self):
        """start animnation"""
        self.movie.start()
        
    def stop(self):
        """stop the animation"""
        self.movie.stop()

app = QApplication(sys.argv)
window = MainWindow()
#window.show()
sys.exit(app.exec())
