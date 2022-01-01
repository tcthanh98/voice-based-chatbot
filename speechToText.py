import speech_recognition as sr

def speech_to_text():
	r = sr.Recognizer()
	mic = sr.Microphone() # use Microphone input


	with mic as source:
		r.pause_threshold = 1
		r.adjust_for_ambient_noise(source, duration = 1) # process noice 
		audio = r.listen(source)

	try:
		question = r.recognize_google(audio, language = "vi_VN").lower()

	#loop back to continue to listen for commands if unrecognizable speech is received
	except: 
		print("\n.............\n")
		question = speech_to_text()
	return question


