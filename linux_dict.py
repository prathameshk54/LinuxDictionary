import requests 
from urllib.parse import urlencode
import re

def strprint(string_):
	string_ = re.sub('{bc}', ': ', string_)
	string_ = re.sub('{ldquo}', '"', string_)
	string_ = re.sub('{rdquo}', '"', string_)
	string_ = re.sub("{([^{])*}", "", string_)
	print(string_)

def print_meaning(res):
	#differnt verb dividers
	for dicts in res['def']:
		#different sn's
		for lists in dicts['sseq']:
			try:
				if(lists[0][0] != 'sense'):
					continue
			except:
				continue

			for l in lists[0][1]['dt']:
				if l[0] == 'text':
					strprint(l[1])
				else:
					continue

	print('Short Defination: ')
	for sdef in res['shortdef']:
		strprint(sdef)

def get_meaning(word='welcome', flag = 0):
	url = 'https://dictionaryapi.com/api/v3/references/sd2/json/'+word+'?key=880ce8f2-178b-40a5-a675-6862884fd925'

	response = requests.get(url)
	result = response.json()
	if response.status_code != 200:
		print('Something went wrong: HTTP Error Code: %d' %(response.status_code))
		return
	if type(result[0]) == str:
		if (flag == 1 or len(result) == 0):
			print('Sorry, we did not find any meaning matching your word')
			return

		print('Did you mean following words? Enter the number of word that you want to search')
		for i, res in enumerate(result):
			print('%d. '%(i+1) + res)
		i = int(input().split()[0])

		try:
			word = result[i - 1]
			get_meaning(word, flag = 1)
			return
		except:
			print('Enter Valid Choice')
			return

	for res in result:
		print(' ')
		print(' ')
		print(' ')
		print_meaning(res)


word = input('Enter the word you want to search: ')
get_meaning(word)