# from engine.features import chatBot
# response = chatBot("Tell me about yourself")
# print(response)


import subprocess
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

from engine.command import speak

def whatsApp(mobile_no, message, flag, name):
    driver = webdriver.Chrome()  # Ensure you have chromedriver installed and in PATH
    driver.get("whatsapp://")  # Open WhatsApp Desktop app
    
    time.sleep(5)  # Wait for the app to load
    
    search_box = driver.find_element(By.XPATH, "//div[@contenteditable='true'][@title='Search input textbox']")
    search_box.send_keys(name)
    search_box.send_keys(Keys.ENTER)
    
    if flag == 'message':
        message_box = driver.find_element(By.XPATH, "//div[@contenteditable='true'][@title='Type a message']")
        message_box.send_keys(message)
        message_box.send_keys(Keys.ENTER)
        jarvis_message = "Message sent successfully to " + name
    
    elif flag == 'call':
        call_button = driver.find_element(By.XPATH, "//span[@data-icon='audio-call']")
        call_button.click()
        jarvis_message = "Calling " + name
    
    else:
        video_call_button = driver.find_element(By.XPATH, "//span[@data-icon='video-call']")
        video_call_button.click()
        jarvis_message = "Starting video call with " + name
    
    time.sleep(5)  # Give time for the action to complete
    
    print(jarvis_message)
    driver.quit()

# Example usage
# whatsApp("+1234567890", "Hello! This is an automated message.", "message", "John")


# Create Whatsapp Function in features.py
def whatsApp(mobile_no, message, flag, name):
    

    if flag == 'message':
        target_tab = 22
        jarvis_message = "message send successfully to "+name

    elif flag == 'call':
        target_tab = 7
        message = ''
        jarvis_message = "calling to "+name

    else:
        target_tab = 6
        message = ''
        jarvis_message = "staring video call with "+name


    # Encode the message for URL
    encoded_message = quote(message)
    print(encoded_message)
    # Construct the URL
    whatsapp_url = f"whatsapp://send?phone={mobile_no}&text={encoded_message}"

    # Construct the full command
    full_command = f'start "" "{whatsapp_url}"'

    # Open WhatsApp with the constructed URL using cmd.exe
    subprocess.run(full_command, shell=True)
    time.sleep(10)
    subprocess.run(full_command, shell=True)
    
    pyautogui.hotkey('ctrl', 'f')

    for i in range(1, target_tab):
        pyautogui.hotkey('tab')

    pyautogui.hotkey('enter')
    speak(jarvis_message)

