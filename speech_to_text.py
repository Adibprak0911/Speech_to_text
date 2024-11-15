import assemblyai as aai

# Replace with your API key
aai.settings.api_key = "8cfe77df62894433a60760057aaed62d"

FILE_URL = "output.wav"

transcriber = aai.Transcriber()
transcript = transcriber.transcribe(FILE_URL)

if transcript.status == aai.TranscriptStatus.error:
    print(transcript.error)
else:
    print(transcript.text)
