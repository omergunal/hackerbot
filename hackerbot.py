# coding=utf-8
import aiml
import os
import sys
sys.path.append("modules/")
import helper
import command

#Author : Omer Gunal (https://github.com/omergunal, https://twitter.com/ogunal00)



# Create the kernel and learn AIML files
kernel = aiml.Kernel()
kernel.learn("aiml/std-startup.xml")

kernel.respond("load aiml b")

os.system('cls' if os.name == 'nt' else 'clear') # clear terminal

# Press CTRL-C to break this loop
while True:
    message = raw_input(">> ")
    if message == "quit" or message == "exit": # exit from chat
        print("bye...")
        exit()
    elif message == "save":
        kernel.saveBrain("bot_brain.brn")
    elif message[:1] == "!": # If the message specifies a command
        split_message = message.split() # split message 
        command.Commands(split_message) # send to command module
    else:
        bot_response = kernel.respond(message)
        # Do something with bot_response
        print(bot_response)
