from selenium import webdriver
import random
import time
import re
import string

driver = webdriver.Chrome()  # Optional argument, if not specified will search path.
# or '/usr/lib/chromium-browser/chromedriver' if you use chromium-chromedriver

# NAME GENERATION
for i in range(10):
    driver.get('https://en.wikipedia.org/wiki/Special:Random')
    temp = driver.find_element_by_class_name("firstHeading").text
    for char in string.punctuation:
        temp = temp.replace(char, '') #REMOVES ALL PUNCTUATION
    for char in string.digits:
        temp = temp.replace(char, '') #REMOVES SPACES
    name = ''.join(temp.split())
    name = name[:random.randint(5,7)] #KEEPS 5 TO 7 LETTERS OF THE ORIGINAL STRING


    randomNumber = random.randint(10000,99999) #GENERATES RANDOM NUMBER
    text_file = open("names.txt", "a")
    text_file.write(name + str(randomNumber)) #OUTPUTS NAME AND NUMBER
    text_file.write("\n")

text_file.close()
time.sleep(1)
driver.close()
# NAME GENERATION FINISHED
