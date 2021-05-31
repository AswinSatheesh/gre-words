from flask import Flask, render_template, request, redirect, jsonify, redirect, url_for, flash
import json

app = Flask(__name__)

USERS_JSONPATH = "words.json"

@app.route('/') #Second Node
def start():

    word_dict = get_json()

    return render_template('index.html', json = word_dict["words"] , len = len(word_dict["words"]))    

def get_json():

    json_file = open(USERS_JSONPATH)
    json_data = json.load(json_file)

    return json_data

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080, debug=True) #Port is Set to 8080 and Host is set to Global