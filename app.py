# Author - Douglas Snow
# Date 1/31/2023

import pyautogui
import time
import argparse
import os
import tempfile
import img2pdf


print("Open the book on the left side of the screen and the terminal on the right.")
print("-------------")

input("Move mouse to top left of page and click enter")
top_leftX, top_leftY = pyautogui.position()

input("Move mouse to bottom right of page and click enter")
bottom_rightX, bottom_rightY = pyautogui.position()

input("Move mouse to the next page button and click enter")
next_x, next_y = pyautogui.position()

pages = input("Enter number of pages")

input("Click enter to continue")
images = []

for i in range(int(pages)):
    time.sleep(1.1)
    my_screenshot = pyautogui.screenshot(region=(top_leftX,top_leftY, bottom_rightX-top_leftX, bottom_rightY-top_leftY))
    pyautogui.click(next_x, next_y)
    address = "C:\\Users\\dsnow\\Desktop\\screenshot/"
    temp_dir = tempfile.mkdtemp()
    file = address + str(i) + ".png"
    my_screenshot.save(file)
    images.append(file)
    
def image2pdf(images):
    with open("book.pdf", "wb") as f:
        f.write(img2pdf.convert(images))

image2pdf(images)
print("Book saved to book.pdf")

