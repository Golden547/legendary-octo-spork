# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 20:43:08 2022

@author: shn99
"""

from tkinter import*

root=Tk()

root.title("Fibonacci")
root.geometry("400x400")        

sum2=0

def Fibonacci():
    num = 10
    first_no = 0
    second_no = 1
    sum=0
    counter=1

while (counter <= num):
     label_series["text"] += str(sum) + " "
     counter = counter+1
     first_no=second_no
     second_no=sum
     sum=first_no + second_no

label["text"] = "Fibonacci Sum : " + str(sum2)
    
root.mainloop()