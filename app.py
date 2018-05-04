import json
from flask import Flask, jsonify, render_template, request


app = Flask(__name__)


with open('Dragon.json') as json_data:
    d = json.load(json_data)
    character_list = []
    for data in d['DragonBallZ']:
    	character_list.append(data)
    	
for character in character_list:
    print(type(character))

@app.route('/', methods =['GET'])
def test():
	return render_template("index.html")

@app.route('/DragonBallZ', methods =['GET'])
def test1():
	return render_template("index.html",list_data=character_list)

@app.route('/DragonBallZ/<int:idd>', methods =['GET'])
def test2(idd):
    g=[]
    for character in character_list:
        if character['id'] == idd:
            g.append(character)
        else:
            if character['PowerLevel'] <= idd:
                g.append(character)
    return render_template("index.html",list_data=g)

if __name__ == '__main__':
	 app.run(debug=True, host='0.0.0.0')
