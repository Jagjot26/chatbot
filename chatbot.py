from chatterbot import ChatBot #import the chatbot
from chatterbot.trainers import ChatterBotCorpusTrainer
import os
import time
import win32com.client
import playsound
from googlesearch import search
import colorama
from colorama import Fore, Back, Style
colorama.init()

bot= ChatBot('Bot')
trainer = ChatterBotCorpusTrainer(bot)
speaker = win32com.client.Dispatch("SAPI.SpVoice") 

corpus_path = 'C:/Users/jaysi\chatterbotcorpus/chatterbot-corpus-master/chatterbot_corpus/data/english/'

for file in os.listdir(corpus_path):
    trainer.train(corpus_path + file)

while True:
    print(Fore.CYAN)
    message = input('You: ')
    print(Style.RESET_ALL)  
    if 'search' in message.strip():
        s2='search'
        s1=message.strip()
        s3=s1[s1.index(s2) + len(s2):]
        print (Fore.GREEN + 'Chatbot: Give me a few seconds to look that up.')        
        speaker.Speak('Give me a few seconds to look that up.')
        for url in search(s3, stop=5):
         print(Fore.RED + '         ' + url)
         print(Style.RESET_ALL)
         continue
    if message.strip() == 'Bye':
        print(Fore.GREEN + 'Chatbot: Goodbye, and have a nice day!')
        print(Style.RESET_ALL)
        speaker.Speak('Goodbye, and have a nice day!')
        break
    if message.strip() == 'what time is it':
        print (Fore.GREEN + 'Chatbot: The exact time is - '+time.strftime("%H:%M:%S"))
        print(Style.RESET_ALL)
        speaker.Speak('The exact time is - '+time.strftime("%H:%M:%S"))
        continue
    if message.strip() == 'What time is it?':
        print (Fore.GREEN + 'Chatbot: The exact time is - '+time.strftime("%H:%M:%S"))
        print(Style.RESET_ALL)
        speaker.Speak('The exact time is - '+time.strftime("%H:%M:%S"))
        continue
    if message.strip() == 'what time is it?':
        print (Fore.GREEN + 'Chatbot: The exact time is - '+time.strftime("%H:%M:%S"))
        print(Style.RESET_ALL)
        speaker.Speak('The exact time is - '+time.strftime("%H:%M:%S"))
        continue
    if message.strip() == 'what is the time?':
        print (Fore.GREEN + 'Chatbot: The exact time is - '+time.strftime("%H:%M:%S"))
        print(Style.RESET_ALL)
        speaker.Speak('The exact time is - '+time.strftime("%H:%M:%S"))
        continue
    if message.strip() == 'what is the time':
        print (Fore.GREEN + 'Chatbot: The exact time is - '+time.strftime("%H:%M:%S"))
        print(Style.RESET_ALL)
        speaker.Speak('The exact time is - '+time.strftime("%H:%M:%S"))
        continue
    if message.strip() == 'what is the date today':
        print (Fore.GREEN + 'Chatbot: The date today is - '+time.strftime("%d/%m/%Y"))
        print(Style.RESET_ALL)
        speaker.Speak('The date today is - '+time.strftime("%d/%m/%Y"))
        continue
    if message.strip() == 'what is the date':
        print (Fore.GREEN + 'Chatbot: The date today is - '+time.strftime("%d/%m/%Y"))
        print(Style.RESET_ALL)
        speaker.Speak('The date today is - '+time.strftime("%d/%m/%Y"))
        continue
    if message.strip() == 'what is the date?':
        print (Fore.GREEN + 'Chatbot: The date today is - '+time.strftime("%d/%m/%Y"))
        print(Style.RESET_ALL)
        speaker.Speak('The date today is - '+time.strftime("%d/%m/%Y"))
        continue
    if message.strip() == 'what is the date today?':
        print (Fore.GREEN + 'Chatbot: The date today is - '+time.strftime("%d/%m/%Y"))
        print(Style.RESET_ALL)
        speaker.Speak('The date today is - '+time.strftime("%d/%m/%Y"))
        continue
    if message.strip() == 'bye':
        print(Fore.GREEN + 'Chatbot: Goodbye, and have a nice day!')
        print(Style.RESET_ALL)
        speaker.Speak('Goodbye, and have a nice day!')
        break
    if message.strip() == 'sing happy birthday':
        print(Fore.GREEN + 'Chatbot: Let me change my voice first.')
        print(Style.RESET_ALL)
        speaker.Speak('Let me change my voice first.')
        playsound.playsound('C:/Users/jaysi\Desktop/python files/song.mp3', True)
        continue
    if message.strip() == 'sing happy birthday for me':
        print(Fore.GREEN + 'Chatbot: Let me change my voice first.')
        print(Style.RESET_ALL)
        speaker.Speak('Let me change my voice first.')
        playsound.playsound('C:/Users/jaysi\Desktop/python files/song.mp3', True)
        continue
    if message.strip() == 'sing happy birthday to me':
        print(Fore.GREEN + 'Chatbot: Let me change my voice first.')
        print(Style.RESET_ALL)
        speaker.Speak('Let me change my voice first.')
        playsound.playsound('C:/Users/jaysi\Desktop/python files/song.mp3', True)
        continue
    else:
        reply = bot.get_response(message)
        print(Fore.GREEN + 'Chatbot:', reply)
        print(Style.RESET_ALL)
        speaker.Speak(reply)
