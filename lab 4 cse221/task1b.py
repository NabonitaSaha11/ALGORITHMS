# -*- coding: utf-8 -*-
"""task1B

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1UXgfKRn4gcqg5GnBqvyBqigpEgaMisvy
"""

# using the adjacency matrix of task 1a for task 1b :
input=open("input1a_1.txt","r")
output=open("output1a_1.txt","w")
n=input.readline()
vertices=n[0]

import numpy as np
arr=np.zeros((int(vertices)+1,int(vertices)+1),dtype=int)


for i in range(int(n[2])):
  new=input.readline().split()
  row=new[0]
  col=new[1]
  val=new[2]
  arr[int(row)][int(col)]=val
for i in range ((int(vertices)+1)):
  for j in range((int(vertices)+1)):
    output.write(str(arr[i][j])+" ")

  output.write("\n")

#task 1b
input=open("input1b_1.txt","r")
output=open("output1b_1.txt","w")
n=input.readline()
vertices=n[0]
new=[0]*(int(vertices)+1)
for i in range(int(vertices)+1):
  for j in range(int(vertices)+1):
    if arr[i][j]!=0:
      if new[i]==0:
       new[i]=[(j,arr[i][j])]
      else:
        new[i].append((j,arr[i][j]))

for val in range(len(new)):
  if new[val]==0:
    output.write(str(val)+" "+":")
    output.write("\n")
  else:
    output.write(str(val)+" "+":")
    for i in new[val]:
      output.write(" "+str(i)+" ")
    output.write("\n")
input.close()
output.close()