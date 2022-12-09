# Take-me-out-to-the-8-ball-game

Team Members: Emily Sandstrom, Liam Leahy, Kristina Zuniga, Harrison Tun, Stephen Sams

Magic 8 ball team project for 3720 
Meeting Notes: https://docs.google.com/document/d/1gcicHMWvXZIwKz-5-sFnKCrD5gy73rB16Ij3maD42tw/edit?usp=sharing 

Idea:
    When you think of a magic 8 ball you think of a ball that you ask a question, then shake and 
    wait for an answer to appear in the ball. For our project we took that idea and enhanced it.

How to use:
    First, make sure to have python downloaded (https://www.python.org/downloads/), pyside6 downloaded (https://pypi.org/project/PySide6/), and any promted pySide6 imports. To run, in the terminal type: "python3 magic8ball.py" 

API's Used:
    Our Project integrates three API's: Speech to text API, a Youtube music API, and a text to 
    speech API. 


How all parts work together:

    The music begins when the magic8ball.py file is run.The gif also begins at this time. The music and gif stop
    when the button is clicked to ask a question. The text to speech API (TTS) uses a generated message to ask for 
    the user question. The Speech to text API (STT) then listens for the question and converts it to text. Next the 
    TTS repeats the question and responds with a randomly generated response. Finally the music api and gif begin to 
    the sound and visuals again and the whole process is repeated.T his entire process is visualized using GUI.


How the API's in Talking8Ball.py function individually:

    The Music API works by first creating an object and setting that object to a Youtube URL. Next we extract 
    the audio stream from the url. We then download the audio into an mp3 file and set a variable to call 
    pyglet.media.Player(). We set the file path for the mp3 file, and finaly we load that file using 
    pyglet.media.load(<file-path>) and queue it. With this set up we can now use the variable that was set to 
    pyglet.media.Player() to play and pause the sound.

    The Speech to text API works by using speech_recognition (SRM), pyaudio, and wave modules. Step 1, the wav 
    file, chunk size, sample format, channel, sample rate, and pyaudio.PyAudio() are initialized. Step 2, a stream 
    object is opened using the previously initialized data(format, channel, sample rate, chunk, and pyaudio.PyAudio()) 
    and a input and output variable. Second we loop through a range of sample_rate / chunk * record_seconds. In that 
    loop we set the data using the stream object we created earlier (stream.read()) and append that data to an empty 
    array.Step 3, we stop  the stream, and close the stream and pyaudio. Step 4, a wav file is opened in write bytes 
    mode using the wav file we initialized earlier. The channels, sample format, sample rate, and frames (as bytes) 
    are set for the new wav file. Step 5,  listen for the data from the wav file using the (SRM). Step 6, convert from 
    speech to text using the the SRM function recognize_google. Finally you save the newly created text to a new 
    variable and now you have text derived from speech.

    The text to speech API works by using gtts, os, and playsound modules. Using gtts.gTTS the API takes a line of text, 
    converts it to speech and sets this to a new variable. Next the new variable saves to a mp3 file. Next the mp3 file 
    speech is played using the playsound module.Finally the mp3 file is cleared using os for repeated use.

How The magic 8 ball gif and GUI pop up function:

    The magic 8 ball gif was created by a friend of one of our teamates.

    The popup GUI was created using pySide6. Specifically we used functions such as QTwidgets, QtCore, QtGui, and QtUiTools. 
    First, we created a Qtwidget instance. Second, in the widget we set the background color and set the layout of the items 
    in the widget to center. Third, we added a button to the widget using Qtpushbutton and set the size and text for it. Fourth,
    we set our gif to a variable using QtMovie, we cache it, set the speed for the gif, and finally we set the gif in the widget 
    using QLabel. Now we can play and stop the gif using self.<variable>.start() and .stop(). Fifth, we set both the speech to 
    text result, and the text to speech result to a variable and inserted it inside of the widget using QLabel. Finally we set the 
    layout, the size, and the title of the widget using the initialized instance of a widget we created earlier. 



ScreenShots:

1. <img width="595" alt="Picture1" src="https://user-images.githubusercontent.com/112186297/206731502-b4327a11-6abd-44f6-8faf-1f06babc1c52.png">
2. <img width="609" alt="Picture2" src="https://user-images.githubusercontent.com/112186297/206731505-8a565375-4476-4821-a8f6-ff36299aa4eb.png">

Video:
https://user-images.githubusercontent.com/112186297/206733740-04bb09ec-16dc-4d75-a7f3-facab84108ef.mp4

