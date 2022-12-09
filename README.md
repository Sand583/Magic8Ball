# Take-me-out-to-the-8-ball-game
Magic 8 ball team project for 3720 
Meeting Notes: https://docs.google.com/document/d/1gcicHMWvXZIwKz-5-sFnKCrD5gy73rB16Ij3maD42tw/edit?usp=sharing 

Idea:
    When you think of a magic 8 ball you think of a ball that you ask a question, then shake and wait for an answer to appear in the ball. For our project we took that idea and enhanced it.

API's Used:
    Our Project integrates three API's: Speech to text API, a Youtube music API, and a text to speech API. 


How the API's in Talking8Ball.py work individually:
    The Music API works by first creating an object and setting that object to a Youtube URL. Next we extract the audio stream from the url. We then download the audio into an mp3 file and set a variable to call pyglet.media.Player(). We set the file path for the mp3 file, and finaly we load that file using pyglet.media.load(<file-path>) and queue it. With this set up we can now use the variable that was set to pyglet.media.Player() to play and pause the sound.

    The Speech to text API works by using speech_recognition, pyaudio, and wave modules. First the wav file, chunk size, sample format, channel,sample rate, and pyaudio.PyAudio() are initialized. Next a stream object is opened using the previously initialized data(format, channel, sample rate, chunk, and pyaudio.PyAudio()) and  input and output variable.

    The text to speech API works by using gtts, os, and playsound modules. Using gtts.gTTS the API takes a line of text, converts it to speech and sets this to a new variable. Next the new variable saves to a mp3 file. Next the mp3 file speech is played using the playsound module.Finally the mp3 file is cleared using os for repeated use.

How The magic 8 ball gif and GUI pop up work:






How all parts work together:

    The music begins when the magic8ball.py file is run.The gif also begins at this time and continues throughout the program. The music stops when the button is clicked to ask a question. The text to speech API (TTS) uses a generated message to ask for the user question. The Speech to text API (STT) then listens for the question and converts it to text. Next the TTS repeats the question and responds with a randomly generated response. Finally the music api begins playing the sound again and the whole process is repeated.

    This entire process is visualized using GUI.
