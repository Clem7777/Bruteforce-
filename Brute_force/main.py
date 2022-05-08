import random
import pyautogui
import string

chats = "abcdefghijklmnopqrstuvwxyz0123456789"

chars = string.printable
chars_list = list(chars)

print(chars_list)

mdp = pyautogui.password("Enter your password : ")
find_pass = ""

while(find_pass != mdp):
    find_pass = random.choices(chars_list, k=len(mdp))
    print(str(find_pass))
    
    if(find_pass == list(mdp)):
        print("Your password is : " + "".join(find_pass))
        break
