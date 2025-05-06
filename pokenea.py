from flask import Flask, jsonify, render_template
import os
import random


app = Flask(__name__)

pokeneas = [
    {'id':1,'name': "Neaninja",'ability':'Puñalada Multiple','phrase':'Su mamá sabe coser?','height':150},
    {'id':2,'name': "Camareta",'ability':'Humo Espontaneo','phrase':'Camaron que se parcha se lo lleva la recocha','height':50},
    {'id':3,'name': "Kingnea",'ability':'Atraco Instantaneo','phrase':'Hermano me regala la hora?','height':200},
    {'id':4,'name': "Princesa",'ability':'Comer niños','phrase':'Perro que ladra no muerde','height':60},
    {'id':5,'name': "Machampeta",'ability':'Los prohibidos','phrase':'Chawa Chawa!','height':1500},
    {'id':6,'name': "JynxG",'ability':'Bichotear','phrase':'Que mas moooooor!','height':110},
    {'id':7,'name': "OmareepCourtz",'ability':'Auto-tune Shock','phrase':'No todos los rayos iluminan, algunos solo te despiertan para que no te duermas en tu propio flow pah!','height':60},
    {'id':8,'name': "Buzzchimbita",'ability':'Hipertrofia','phrase':'No pain no gain!','height':240},
    {'id':9,'name': "WeezinYandel",'ability':'Perreo','phrase':'EL DUO DE LA HISTORIA!','height':120}
]


@app.route('/json/pokenea')
def get_random_pokenea():
    pokenea = random.choice(pokeneas)
    container_id = os.uname()[1]
    pokenea.update({'container': container_id})
    return jsonify(id=pokenea.get('id'),name = pokenea.get('name'),height=pokenea.get('height'),ability=pokenea.get('ability'),container_id = container_id)


@app.route('/show/pokenea')
def show_random_pokenea():
    pokenea = random.choice(pokeneas)
    frase = pokenea.get('phrase')
    container_id = os.uname()[1]
    image_url = f"https://taller2bucketedup3.s3.us-east-1.amazonaws.com/pokeneas/{pokenea.get('name')}.jpg"
    return render_template('pokedex.html', image=image_url, container=container_id, frase=frase)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
