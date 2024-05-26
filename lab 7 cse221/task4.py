# -*- coding: utf-8 -*-
"""task4.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1-vN6frYmH7FG3B-7DOkbm2VLz8KhyM6D
"""

def mincoin(coin, value):
    dp = [float('inf')] * (value + 1)
    dp[0] = 0

    for a in range(1, value + 1):
        for b in range(len(coin)):
            if a>=coin[b] :
                dp[a] = min(dp[a], dp[a-coin[b]] + 1)
    if dp[value]!=float("inf"):
      return dp[value]
    else:
      return -1


input = open('input4_1.txt' , 'r')
output = open('output4_1.txt' , 'w')
n, x= map(int,input.readline().strip().split())
coin = list(map(int, input.readline().strip().split()))



minimum = mincoin(coin, x)
output.write(str(minimum))

input.close()
output.close()