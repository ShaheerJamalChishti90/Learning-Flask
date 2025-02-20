from flask import Flask

app = Flask(__name__)

@app.route('/')

def shaheer():
    return 'Hey Mimi, Im your friend Shaheer!'

app.run(debug=True)   



