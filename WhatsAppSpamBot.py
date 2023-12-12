import pyautogui, webbrowser
from time import sleep

# Include your country code and no spaces
phone = 'PHONE_NUMBER'

# Open whatsapp web
webbrowser.open(f'https://web.whatsapp.com/send?phone={phone}')
sleep(15)

# Open a simple file
with open('text.txt','r') as file:

    for line in file:
        # Write the lines on page opened
        pyautogui.typewrite(line)

        # Press enter (send message)
        pyautogui.press("enter")
