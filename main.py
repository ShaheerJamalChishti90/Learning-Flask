from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
# def greet():
#     return '<h1>Yes Shaheer, This is very exciting to learn Flask in 2025</h1>' 

@app.route('/')
def home():
    return render_template("index.html", name = "Shaheer")

@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)


