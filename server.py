from flask import Flask, request, render_template
from Oski import *
app = Flask(__name__)

answer_output = ''

@app.route("/")
def hello():
	return app.send_static_file('index.html')

@app.route("/api/ReadTextInput", methods=["POST"])
def receive_cheep():
	print(request.form)
	return "Sucess"

@app.route("/api/GetQuestion", methods=["POST"])
def get_question():
	transcribed_audio = request.get_json(force=True)
	print(transcribed_audio)
	found_answer = answer(request.get_json(force=True)['data'])
	url_speech = text_to_voice_url(found_answer)
	print(found_answer)
	return render_template('answer.html', oski_answer=found_answer, speak=url_speech)

	# = request.POST['data'].json()

@app.route("/api/StartRecording", methods=["POST"])
def receive_recording_cue():
	print(request.form)
	transcribed_audio = get_audio().capitalize()
	print(transcribed_audio)
	found_answer = answer(transcribed_audio)
	url_speech = text_to_voice_url(found_answer)
	print(found_answer)
	return render_template('oski_answer.html', name=transcribed_audio, oski_answer=found_answer, speak=url_speech)

if __name__ == "__main__":
	app.run(debug=True)
