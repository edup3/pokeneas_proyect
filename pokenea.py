from flask import Flask, jsonify, render_template
import os
import random


app = Flask(__name__)

pokeneas = [
    "Greninja",
    "Clauncher",
    "Kingambit",
    "Houndoom",
    "Beedril",
    "Zangoose",
    "Lopunny",
    "Buzzwhole",
    "Rillaboom",
    "WeezinYandel"
]


@app.route('/json/pokenea')
def get_random_pokenea():
    pokenea = random.choice(pokeneas)
    container_id = os.uname()[1]
    return jsonify(name=pokenea, container=container_id)


@app.route('/show/pokenea')
def show_random_pokenea():
    pokenea = random.choice(pokeneas)
    container_id = os.uname()[1]
    image_url = f"https://taller2bucketedup3.s3.us-east-1.amazonaws.com/pokeneas/{pokenea}.jpg"
    return render_template('pokedex.html', image=image_url)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
