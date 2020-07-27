from flask import Flask
from flask import render_template
from flask import json
from flask import request
import requests
import os

app = Flask(__name__)

game_1 = os.getenv('EASY_GAME_SERVER_IP')
game_2 = os.getenv('HARD_GAME_SERVER_IP')

@app.route('/')
def hello_world():
    game = request.args.get('game')

    if game:
        game = int(game)
        if game == 1:
            #res = requests.get("http://game_1:3000")
            res = requests.get(game_1)
            text = json.loads(res.text)
            if 'val' in text:
                if text['val'] == 4:
                    return render_template('won.html',amount="KSH. 5,000")
                else:
                    return render_template('lost.html', rolled=str(text['val']))
        elif game == 2:
            #res = requests.get("http://game_2:3000")
            res = requests.get(game_2)
            text = json.loads(res.text)
            if 'val' in text:
                if text['val'] == 27:
                    return render_template('won.html',amount="KSH. 50,000")
                else:
                    return render_template('lost.html', rolled=str(text['val']))

    return render_template('index.html')