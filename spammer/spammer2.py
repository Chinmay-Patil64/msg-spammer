import webbrowser
import pyautogui
import random
import time
from urllib.parse import quote

# Check if pyperclip is installed
try:
    import pyperclip
except ImportError:
    print("Please install pyperclip:  pip install pyperclip")
    exit()
# You should have WhatsApp Web open and logged in before running this script.

phone = "999999999999"   # Replace with the recipient's phone number and country code (e.g., 15551234567 for +1 555-123-4567) 

messages = [
    "HEY 👀",
    "Are you alive?",
    "BROOOO 😂",
    "Reply kar 😭",
    "HELLOOOOO",
    "Hey bro 😂 This message was prepared using Python! #{}",
]

# 1. Open the chat only once
url = f"https://web.whatsapp.com/send?phone={phone}"
webbrowser.open(url)

print("Waiting for WhatsApp Web to load...")
time.sleep(12)          # increase if your internet is slow

# 2. Send messages in the same tab
for i in range(1, 3):   # start with only 3 messages for testing
    message = random.choice(messages)
    
    if "{}" in message:
        message = message.format(i)
    
    print(f"[{i}] Sending: {message}")
    
    # Copy message to clipboard and paste it
    pyperclip.copy(message)
    time.sleep(0.1)  # wait for clipboard to update
    
    pyautogui.hotkey('ctrl', 'v')   # paste
    time.sleep(0.1)  # wait for paste to complete
    pyautogui.press('enter')        # send
    
    time.sleep(0.1)                 # wait before next message