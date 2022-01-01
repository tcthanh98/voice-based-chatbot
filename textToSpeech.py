import requests
import urllib.request
import random
import os
import time


def text_to_speech(answer):
	url = 'https://api.fpt.ai/hmi/tts/v5'
	payload = answer

	keys = ['0F80Qz2Kpp8a0bFyJI0RZapMr9sUmkAb',
			'r1a2uWmuBEygH4jKB8rv5pxeVxWZjMFp',
			'4MHB9f2xmvEHEdvT8isJJ2tQVS080xqr',
			'Y6g3Nvx4BZ6xtAmHyeyy2uyHvkWs1ueE'
			]

	headers = {
	    'api-key': random.choice(keys),
	    'speed': '',
	    'voice': 'banmai'
	    #'prosody': '1'
	}

	response = requests.request('POST', url, data=payload.encode('utf-8'), headers=headers)
	response = response.json()

	link_mp3 = response['async']
	return link_mp3
	

# test
answer = "Xin lỗi, câu hỏi không có trong tập dữ liệu"

link_mp3 = text_to_speech(answer)
print(link_mp3)
time.sleep(3)

if os.path.exists("mp3/answer.mp3"):
	os.remove("mp3/answer.mp3")

urllib.request.urlretrieve(link_mp3, 'mp3/noneLabel.mp3')