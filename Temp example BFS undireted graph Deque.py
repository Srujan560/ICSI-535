from collections import deque
#   S P Q H E R F G C A B D
# S 0 1 0 0 1 0 0 0 0 0 0 1
# P 1 0 1 1 0 0 0 0 0 0 0 0
# Q 0 1 0 1 0 0 0 0 0 0 0 0
# H 0 1 1 0 1 0 0 0 0 0 0 0
# E 1 0 0 1 0 1 0 0 0 0 0 1
# R 0 0 0 0 1 0 1 0 0 0 0 0
# F 0 0 0 0 0 0 0 1 1 0 0 0
# G 0 0 0 0 0 0 1 0 0 0 0 0
# C 0 0 0 0 0 0 1 0 0 1 0 1
# A 0 0 0 0 0 0 0 0 1 0 1 0
# B 0 0 0 0 0 0 0 0 0 1 0 1
# D 1 0 0 0 0 0 0 0 1 0 1 0
#   S P Q H E R F G C A B D


g1 = [
[0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
[1,0,0,1,0,0,0,0,0,0,0,0],
[1,0,0,1,0,1,0,0,0,0,0,0],
[0,1,1,0,1,0,0,0,0,0,0,0],
[1,0,0,1,0,1,0,0,0,0,0,1],
[0,0,0,0,1,0,1,0,0,0,0,0],
[0,0,0,0,0,0,0,1,1,0,0,0],
[0,0,0,0,0,0,1,0,0,0,0,0],
[0,0,0,0,0,0,1,0,0,1,0,1],
[0,0,0,0,0,0,0,0,1,0,1,0],
[0,0,0,0,0,0,0,0,0,1,0,1],
[1,0,0,0,0,0,0,0,1,0,1,0]
]
g2 = [
[0,1,1,0,0,0,0,0,0,0,0,0],
[1,0,0,1,0,0,0,0,0,0,0,0],
[1,0,0,1,0,1,0,0,0,0,0,0],
[0,1,1,0,1,0,0,0,0,0,0,1],
[0,0,0,1,0,0,0,1,0,0,1,1],
[0,0,1,0,0,0,1,0,0,0,1,0],
[0,0,0,0,0,1,0,0,0,0,0,0],
[0,0,0,0,1,0,0,0,1,1,0,0],
[0,0,0,0,0,0,0,1,0,1,0,1],
[0,0,0,0,0,0,0,1,1,0,0,0],
[0,0,0,0,0,1,1,0,0,0,0,0],
[0,0,0,0,1,1,0,0,0,1,0,0]]
maps ={0:'A',1:'B',2:'C',3:'D',4:'E',5:'F',6:'G',7:'H',8:'P',9:'Q',10:'R',11:'S'}



for x in g1:
    my_str = ""
    for y in x:
        my_str= my_str+str(y)+" "
    print(my_str)

def bfs_recurison(q, visited,ans):
    print(q)
    temp_index = q.popleft()
    if visted[temp_index]!=1:# Let make sure We do not vist node that we alredy visted
        visted[temp_index]=1 # Let mark it and say we Visted
        ans.append(temp_index) # let add Node that visted ... so we can keep track of which node we on before we find adjacent nodes
        for index,val in enumerate(g1[temp_index]): # Let loop through our Adj Matrxi 
            if val==1 and visted[index]==0: # We check if node is adjacent meaing connted by the edge and 
                #second one is there to check if that node was already visted saves but not adding the deque
                q.append(index)#add to the quee
    if len(q)!=0:
        ans = bfs_recurison(q, visited,ans)
        # print(ans,"Test")
        return ans
    else:
        return ans
"""
Start = Quee, 
Make Visted[] =size of (Nodes)
Visted[]=flase
get adj matrix from the start  and get all edges from start node to
than add to the quee
"""
q = deque()
# print("Hello")
# print(len(g1))
visted = [0]*len(g1)
# print(visted)
# print(g1[0])
visted[0]=1
for x,val in enumerate(g1[0]):
    # print(val,"Hi",x)
    if val==1:
        q.append(x)
ans =[]
ans.append(0)
# Let Prints the nodes in order that we Visted 
ans= bfs_recurison(q,visted,ans)
# print(ans)
nodes_letters =["S","P","Q","H","E","R","F","G","C","A","B","D"]
ans_str=""
for x in ans:
    ans_str = ans_str+nodes_letters[x]+" "

print("BFS recurison",ans_str)





# while q:
#     print(q)
#     temp_index = q.popleft()
#     if visted[temp_index]!=1:# Let make sure We do not vist node that we alredy visted
#         visted[temp_index]=1 # Let mark it and say we Visted
#         ans.append(temp_index) # let add Node that visted ... so we can keep track of which node we on before we find adjacent nodes
#         for index,val in enumerate(g1[temp_index]): # Let loop through our Adj Matrxi 
#             if val==1 and visted[index]==0: # We check if node is adjacent meaing connted by the edge and 
#                 #second one is there to check if that node was already visted saves but not adding the deque
#                 q.append(index)#add to the quee
#   1 2 3 4 5 6 7 8 9 10 11 12
# 1 0 1 1 1 0 0 0 0 0 0 0 0 1
# 2 1 0 0 0 1 1 0 0 0 0 0 0  2
# 3 1 0 0 0 0 0 0 0 0 0 0 0  3
# 4 0 0 0 0 0 0 1 1 0 0 0 0  4
# 5 0 0 0 0 0 0 0 0 1 1 0 0  5
# 6 0 1 0 0 0 0 0 0 0 0 0 0  6
# 7 0 0 0 0 0 0 0 0 0 0 0 1 1 7
# 8 0 0 0 1 0 0 0 0 0 0 0 0 0 8
# 9 0 0 0 0 1 0 0 0 0 0 0 0 0 9
#10 0 0 0 0 1 0 0 0 0 0 0 0 0 10
#11 0 0 0 0 0 0 1 0 0 0 0 0 0 11
#12 0 0 0 0 0 0 1 0 0 0 0 0 0 12

# gTestAns=[[0,1,1,1,0,0,0,0,0,0,0,0],
# [1,0,0,0,1,1,0,0,0,0,0,0],
# [1,0,0,0,0,0,0,0,0,0,0,0],
# [0,0,0,0,0,0,1,1,0,0,0,0],
# [0,0,0,0,0,0,0,0,1,1,0,0],
# [0,1,0,0,0,0,0,0,0,0,0,0],
# [0,0,0,0,0,0,0,0,0,0,1,1],
# [0,0,0,1,0,0,0,0,0,0,0,0],
# [0,0,0,0,1,0,0,0,0,0,0,0],
# [0,0,0,0,1,0,0,0,0,0,0,0],
# [0,0,0,0,0,0,1,0,0,0,0,0],
# [0,0,0,0,0,0,1,0,0,0,0,0],
# ]