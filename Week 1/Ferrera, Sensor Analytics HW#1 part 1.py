# -*- coding: utf-8 -*-
"""Untitled

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1huj1qTl4jErEnwve7Rbo3aZDWWNQegjT
"""

n=int(input())#size of list

lis=[]#list to which elements are going to be stored

for i in range(n):

    print("Enter a number:")

    lis.append(int(input()))#obtains a value from user and add it to the list

mean=sum(lis)//n#to find the mean

slis=sorted(lis)

if(n%2==0):

    median=(slis[(n-1)//2]+slis[(n-1)//2+1])/2 #finds median if total numbers are even

else:

    median=slis[(n-1)//2] #finds median if total numbers are odd

def most_frequent(lis): #function to find most repeated element in list

    return max(set(lis), key = lis.count)

mode=most_frequent(lis)#to find mode

print("Mean= "+str(mean))#print statements

print("Median= "+str(median))

print("Mode= "+str(mode))

