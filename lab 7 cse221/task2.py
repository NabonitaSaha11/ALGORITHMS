# -*- coding: utf-8 -*-
"""task 2 .ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1h_exwAHy-Kc4y_O-d3bADy5xBnZEqHjQ
"""

class union:
    def __init__(self, n):
        self.parent = list(range(n+1))
        self.rank = [0] * (n+1)

    def find(self, u):
        if u != self.parent[u]:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        root1 = self.find(u)
        root2 = self.find(v)

        if root1 == root2:
            return

        if self.rank[root1] > self.rank[root2]:
            self.parent[root2] = root1
        elif self.rank[root1] < self.rank[root2]:
            self.parent[root1] = root2
        else:
            self.parent[root2] = root1
            self.rank[root1] += 1


def min_cost(n, m, edges):
    found = union(n)
    edges.sort(key=lambda x: x[2])

    mst_c = 0
    mst_e = 0

    for u, v, w in edges:
        if found.find(u) != found.find(v):
            found.union(u, v)
            mst_e += 1
            mst_c += w
            if mst_e == n - 1:
                break

    return mst_c

input = open('input2_1.txt' , 'r')
output = open('output2_1.txt' , 'w')
val = input.readline().split(' ')

n=int(val[0])
m=int(val[1])

connect = []

for val in range(m):
    u, v, w = map(int, input.readline().strip().split(" "))
    connect.append((u,v,w))

result = min_cost(n, m, connect)
output.write(str(result))

input.close()
output.close()