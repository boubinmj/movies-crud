from flask import Flask, render_template, request
import pickle, time, os
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
    return render_template("/index.html")

def clear_dictionary():
    os.remove("dictionary_file.pkl")
    dictionary = {}
    file = open("dictionary_file.pkl", 'wb')
    pickle.dump(dictionary, file)
    file.close()

if __name__== '__main__':
    execute_clear_dictionary.add_job(id = 'Scheduled Task', func=clear_dictionary, trigger="interval", seconds=300)
    execute_clear_dictionary.start()
    app.run(host="0.0.0.0", debug=True, port=8888)