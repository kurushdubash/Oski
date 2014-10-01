from flask import Flask, request, render_template
from Oski import *
import os
app = Flask(__name__)

answer_output = ''

@app.route("/")
def hello():
	return app.send_static_file('index.html')

@app.route('/<path:path>')
def static_proxy(path):
    # send_static_file will guess the correct MIME type
    return app.send_static_file(os.path.join('jcss', path))

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
	while(transcribed_audio == ''):
		transcribed_audio = get_audio.capitalize()
	print(transcribed_audio)
	found_answer = answer(transcribed_audio)
	print(found_answer)
	url_speech = text_to_voice_url(found_answer)
	return render_template('oski_answer.html', name=transcribed_audio, oski_answer=found_answer, speak=url_speech)

if __name__ == "__main__":
	app.run(debug=True)
