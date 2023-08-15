## Pytranscribe


### A service for audio transcription for multiple languages


### Python backend

  - POST /transcribe API to accept a url for a media file, this api returns a job id. Returns 200

  - GET /fetch API to fetch the transcription made by the server. Returns 200


### Python frontend

  - A textbox to accept a URL for a media file with basic validations, on submitted calls the /transcribe API, saves the returned job id. Updates a label saying "waiting for transcription"

  - In the background do a long polling on /fetch API with the returned job id




brew install redis
