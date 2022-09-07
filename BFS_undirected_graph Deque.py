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

g1 = [[0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
[1,0,1,1,0,0,0,0,0,0,0,0],
[0,1,0,1,0,0,0,0,0,0,0,0],
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
count =0

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
    else:
        nodes_letters =["S","P","Q","H","E","R","F","G","C","A","B","D"]
        ans_str=""
        for x in ans:
            ans_str = ans_str+nodes_letters[x]+" "
            print(ans_str)
        # return ans
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
bfs_recurison(q,visted,ans)
# Let Prints the nodes in order that we Visted 



    