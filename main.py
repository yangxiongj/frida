# This is a sample Python script.
import sys

import frida
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.



def message(message, data):
    if message["type"] == 'send':
        print("[*] {0}".format(message['payload']))
    else:
        print(message)

process = frida.get_remote_device().attach('小红书')

with open('Jshook-frida.js', 'r', encoding='utf-8') as f:
    jscode = f.read()

script = process.create_script(jscode)
script.on("message", message)
script.load()
sys.stdin.read()