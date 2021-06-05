from flask import render_template, url_for,flash,redirect , request, session
from backend import app
from backend.Image_to_voice.snap import take_shot

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/takePicture')
def listen_picture():
    playsound('sound/welcome.mp3')
    speech = list()
    s = take_shot()
    speech.append(s)
    playsound('sound/nextPage.mp3')
    ch = input()
    while(ch == 'q'):
        s = take_shot()
        speech.append(s)
        playsound('sound/nextPage.mp3')
        ch = input()
    return render_template('take_pic.html', speech = speech)