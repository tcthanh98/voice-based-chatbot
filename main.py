import pandas as pd
import speechToText
import preprocess
import knn
import response
import textToSpeech
import speechAnswer
import pygame as pg
import time
import urllib.request
import os


# load dataset
dataset = pd.read_csv('dataset.csv') # file 'dataset.csv' contain all the questions for each label
dataset2 = pd.read_csv('response.csv') # file 'response.csv' contain the answer for each label

#run file 'opening.mp3' when start program
speechAnswer.play_music('mp3/opening.mp3', volume = 0.8)

# record the question
question = ""
question = speechToText.speech_to_text()

# preprocess the question
question = preprocess.remove_accents(question)
flag = 0;
cnt = 0

while (flag != 1):
	cnt += 1
	label_predict = knn.KNNClassifier(dataset, question)
	if (label_predict != 20):
		answer = response.response(dataset2, label_predict) # find the answer respectively the label predict
		
		link_mp3 = textToSpeech.text_to_speech(answer) # convert string "answer" to file .mp3
		time.sleep(3) # wait for FPT server create link mp3
		
		try:
			urllib.request.urlretrieve(link_mp3, 'mp3/answer'+ str(cnt) +'.mp3') # download file answer.mp3 from FPT server
		except:
			time.sleep(3)
			urllib.request.urlretrieve(link_mp3, 'mp3/answer'+ str(cnt) +'.mp3')

		speechAnswer.play_music('mp3/answer'+ str(cnt) +'.mp3', volume = 0.8) # play file "answer.mp3"
		
		# prepare to listen the next question
		question = speechToText.speech_to_text() 
		question = preprocess.remove_accents(question)
	else:
		speechAnswer.play_music('mp3/ending.mp3')

		for i in range(1, cnt+1):
			file_path = 'mp3/answer'+ str(cnt) + '.mp3'
			if os.path.exists(file_path):
				os.remove(file_path)

		flag = 1


"""
while (flag != 1):
	if ('dung' or 'ngung' not in question):
		label_predict = knn.KNNClassifier(dataset, question)

		# if file answer for label predict exists, then play it. Else download and play it
		file_path = 'mp3/answer'+ str(label_predict) +'.mp3'
		if os.path.exists(file_path):
			speechAnswer.play_music('mp3/answer'+ str(label_predict) +'.mp3', volume = 0.8)

		else:	
			answer = response.response(dataset2, label_predict) # find the answer respectively the label predict
		
			link_mp3 = textToSpeech.text_to_speech(answer) # convert string "answer" to file .mp3
			time.sleep(3) # wait for FPT server create link mp3
	
			urllib.request.urlretrieve(link_mp3, 'mp3/answer'+ str(label_predict) +'.mp3') # download file answer.mp3 from FPT server

			speechAnswer.play_music('mp3/answer'+ str(label_predict) +'.mp3', volume = 0.8) # play file "answer.mp3"

		# prepare to listen the next question
		question = speechToText.speech_to_text() 
		question = preprocess.remove_accents(question)
	else:
		speechAnswer.play_music('mp3/ending.mp3')
		flag = 1	
"""