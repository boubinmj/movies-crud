from flask import Flask, render_template, request
import pickle, time, os, json
from flask_apscheduler import APScheduler

app = Flask(__name__)

global dictionary
dictionary = {}
file = open("dictionary_file.pkl", 'wb')
pickle.dump(dictionary, file)
file.close()

execute_clear_dictionary = APScheduler()

# Homepage
@app.route("/")
def crud_page():
    return render_template("/home.html")

@app.route("/about/")
def about():
    return render_template("/about.html")

@app.route("/home/")
def home():
    return render_template("/home.html")

@app.route("/contact/")
def contact():
    return render_template("/contact.html")

@app.route('/get_page')
def get_page():
    with open('db/data.json', 'r') as f:
        resp = json.load(f)
        return json.dumps(resp, indent=4)

def clear_dictionary():
    os.remove("dictionary_file.pkl")
    dictionary = json.loads("data.json")
    file = open("dictionary_file.pkl", 'wb')
    pickle.dump(dictionary, file)
    file.close()

if __name__== '__main__':
    #execute_clear_dictionary.add_job(id = 'Scheduled Task', func=clear_dictionary, trigger="interval", seconds=10)
    #execute_clear_dictionary.start()
    app.run(host="0.0.0.0", debug=True, port=8888)