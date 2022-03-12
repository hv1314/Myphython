import os

print("Enter the number os seconds")

sec= int(input())

strOne = "shutdown /s /t "
strTwo = str(sec)

str= strOne+strTwo

os.system(str)
