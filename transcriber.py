import whisper

def transcribe(data):
    print(data)
    url = data['url']
    jobID = data['jobID']
    model = whisper.load_model("tiny.en")
    #result = model.transcribe("./test/micro-machines.wav")
    result = model.transcribe(url)
    transcription = result["text"]
    with open(f"assets/{jobID}.txt", "w") as transcriptFile:
        # Writing data to a file
        transcriptFile.write(transcription)