from flask import Flask, request, render_template
from Oski import *
app = Flask(__name__)

@app.route("/")
def hello():
	return app.send_static_file('index.html')

@app.route("/api/ReadTextInput", methods=["POST"])
def receive_cheep():
	print(request.form)
	return "Sucess"


@app.route("/api/StartRecording", methods=["POST"])
def receive_recording_cue():
	print(request.form)
	transcribed_audio = get_audio().capitalize()
	found_answer = answer(transcribed_audio)
	url_speech = text_to_voice_url(found_answer)
	return render_template('oski_answer.html', name=transcribed_audio, oski_answer=found_answer, speak=url_speech)

if __name__ == "__main__":
	app.run(debug=True)
