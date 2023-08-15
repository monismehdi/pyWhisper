from flask import Flask, request, render_template, jsonify
import transcriber

from redis import Redis
from rq import Queue
import uuid


queue = Queue(connection=Redis())

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def index():
    return render_template('index.html')

@app.route("/transcribe", methods = ['POST'] )
def transcribe():
    urlValue = request.form['mediaUrl']
    jobID = str(uuid.uuid1())
    # download the file, send it to a different backend for processing
    # transcription = transcriber.transcribe(urlValue,jobID)
    job = queue.enqueue(transcriber.transcribe, {"url": urlValue, "jobID": jobID})
    return jsonify({"url":urlValue, "id": jobID})


@app.route("/fetchTranscription", methods = ['GET'] )
def fetchTranscription():
    jobID = request.args.get('jobID')
    with open(f'assets/{jobID}.txt') as transcriptFile:
        transcription = transcriptFile.readlines()
        return {'transcription': transcription}


if __name__=='__main__':
    app.run(debug=True)