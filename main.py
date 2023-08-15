from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def index():
    return render_template('index.html')

@app.route("/transcribe", methods = ['POST'] )
def transcribe():
    urlValue = request.form['mediaUrl']
    return urlValue