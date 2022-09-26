from PIL import Image, ImageGrab
from io import BytesIO
import win32clipboard
import keyboard
import time

def send_to_clipboard(clip_type, data):
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(clip_type, data)
    win32clipboard.CloseClipboard()

def create_screen():
    image = ImageGrab.grab()
    output = BytesIO()
    image.convert("RGB").save(output, "BMP")
    data = output.getvalue()[14:]
    output.close()
    send_to_clipboard(win32clipboard.CF_DIB, data)    

def main():
    keyboard.add_hotkey('Alt + [', create_screen)
    while True:
        time.sleep(0.01)
        
if __name__ == '__main__':
    main()