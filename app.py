#!/usr/bin/env/python3

###################################################
# Createby: wh04m1su
# Gmail: wh04m1su@gmail.com
# Telegram: https://t.me/wh04m1su



###
#Librerias

import tkinter as tk 
import os 
import sys
import urllib.request
import socket


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(5)


###
# App Config

app = tk.Tk()
app.title("wifNet")
app.resizable(False, False)
app.geometry("300x230")
app.config(bg = "#211E1E")


###
# Funciones

def exit():
	pass


def publicIP():
	lista = "0123456789."
	
	ip=""
	
	dato=urllib.request.urlopen("http://checkip.dyndns.org").read()
	
	for x in str(dato):
	
		if x in lista:
	
			ip += x
	
	return ip


def status():
    try:
        s.connect(("www.google.com", 80))
    except (socket.gaierror, socket.timeout):
        labeltext.set("Status: Ofline") 
        #labeltexto.config(textvariable=labeltext)   


    else:
        labeltext.set("Status: Online")
        s.close()
        puIP.set("publicIP: " + publicIP())




###
# App Widgets


label=tk.Label(app, text='Status | Internet Connection', font = (10), fg = '#00ff00', bg = "#211E1E").place(x = 35, y = 5)

botonS=tk.Button(app, text='Start', bg = "#211E1E", fg = '#00ff00', command=status).place(x = 80, y = 50)

botonE=tk.Button(app, text='Exit', bg = "#211E1E", fg = 'red', command=exit).place(x = 150, y = 50)

labeltext = tk.StringVar()

puIP = tk.StringVar()

labeltexto=tk.Label(app, textvariable=labeltext, bg = '#211E1E', fg = 'blue', font=(15), width = 25, height = 3).place(x = 9, y = 100)

puIPL=tk.Label(app, textvariable=puIP, bg = '#211E1E', fg = 'yellow', font=(15), width = 25, height = 3).place(x = 9, y = 150)

app.mainloop()