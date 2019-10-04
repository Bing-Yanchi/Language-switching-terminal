# By Bing_Yanchi
# import
import time,yaml
# language
language_choice = 'en'
def lang():
	global language
	if language_choice == 'cn':
		file = open('language_cn.yml', encoding='UTF-8')
		language = yaml.load(file, Loader = yaml.FullLoader)
	else:
		file = open('language_en.yml')
		language = yaml.load(file, Loader = yaml.FullLoader)
lang()
# welcome
print(language.get('msg#0'))
print()
# get version
version = 1.0
latest = 1.0
# check update
print(language.get('Info') + " » " + language.get('msg#1'))
if latest == version:
	print(language.get('Info') + " » " + language.get('msg#2'))
elif latest == "":
	print(language.get('Error') + " » " + language.get('msg#3'))
else:
	print(language.get('Warn') + " » " + language.get('msg#4')+ " " + str(latest))
	print(language.get('Warn') + " » " + language.get('msg#5'))
print()
# use
while True:
	# ask
	command = input(language.get('Input') + " » ")
	# main
	if command == 'help':
		# help
		help = language.get('help')[0]
		for a in help.keys():
			print(language.get('Help') + " » " + a + " -- " + help.get(a))
	elif command == 'exit':
		# exit
		print(language.get('msg#6'))
		break
	elif command == 'time':
		# time
		time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
		print(language.get('Time') + ' » '+ time)
	elif command == 'language' or command == 'lang':
		# language
		print(language.get('Info') + ' » '+ language.get('msg#7') + ':' + language.get('Language'))
		print(language.get('Info') + ' » '+ language.get('msg#8') + ' (en,cn):')
		language_choice = input(language.get('Input') + ' » ')
		if language_choice == 'en' or language_choice == 'cn':
			lang()
			print(language.get('msg#9') + ' » '+ language.get('Language'))
		else:
			print(language.get('Error') + " » " + language.get('Unknown') + ' ' + language.get('msg#7'))
	elif command == 'about':
		# about
		print(language.get('msg#10'))
	else:
		# unknown
		print(language.get('Error') + " » " + language.get('Unknown'))
	print()