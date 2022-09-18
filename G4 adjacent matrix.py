import queue
g4 =[
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 8, 0, 2, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 8, 0, 0, 2, 0],
    [0, 0, 3, 0, 0, 0, 2, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 4, 4, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 3, 9, 0, 0, 0, 1, 0, 0, 0]

]
maps ={0:'A',1:'B',2:'C',3:'D',4:'E',5:'F',6:'G',7:'H',8:'P',9:'Q',10:'R',11:'S'}

visited = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0}
# we know 3 possible paths from the starting node

priority_q = queue.PriorityQueue()
priority_q.put((0,11,[11]))#Let put our starting Node
ans= []
exp=[]
while not priority_q.empty():
    print(priority_q.queue)
    temp = priority_q.get()
    visited[temp[1]]=1
    if temp[1] not in exp:
        exp.append(temp[1])
    if temp[1]==6:
        ans=temp[2]
        # ans.append(temp[1])
        ans.append(temp[0])
        priority_q.task_done()
        break
    # print(g4[temp[1]])
    for index,val in enumerate(g4[temp[1]]):
        # print(index,"**",val)
        if val !=0 and visited[index]==0:# make sure it an adjacent neighbor and not been Visisted[index]
            temp_list = list(temp[2])
            temp_list.append(index)
            priority_q.put((temp[0]+val,index,temp_list))

print(ans)
temp_str= "UCS expanded: "
for x in exp:
    temp_str =temp_str+maps[x]+" "
print(temp_str)
temp_str = "UCS cost "+str(ans[-1])+" and path "
ans.pop()# remove our cost 
for x in ans:
    if x <12:
        temp_str = temp_str+maps[x]+" "
print(temp_str)
# # we know 3 possible paths from the starting node
# paths = [
#     [],
#     [],
#     []
# ]
# priority_q = queue.PriorityQueue()
# priority_q.put((0,11))#Let put our starting Node
# ans= []
"""
first if starting node let add the first 3 paths in each one speared paths (paths[0], paths[1], paths[2])
Each list in paths will remember the total cost and order they picked the edge
we will priority queue and pass in tuple and tuple follows (cost, index, which paths index) so we can have access all path has taken 
priority queue will pick lowest cost when we call priority queue get() it will remove that the
than we check if is node is adjacent than we check that same node is not added twice (back tracking)
Once we find our first 6 (Goal) and cost than we check if other paths have more cost or less if more we stop the other paths or
we update our new ans to be the lowest cost
"""
# history_queue=[]
# while  not priority_q.empty():
#     print(priority_q.queue, "Priority queue")
#     temp = priority_q.get()
#     if temp[0]==0:# if staring node
#         for index,val in enumerate(g4[temp[1]]):
#             # print(index,"***",val)
#             if val!=0:
#                 for x,path in enumerate(paths):# loop through it add first index and take paths.. we 3 paths are so each node take a paths index
#                     # print(len(path))
#                     if len(path)==0:
#                         paths[x].append(val)# add the cost to our paths[0]array
#                         paths[x].append(temp[1])# than stating node 
#                         paths[x].append(index)# than node that about in the queue
#                         priority_q.put((val,index,x))
#                         break
            
#                 # print(x,"****",path,"\n")
#     else:
#         #and g4[paths[temp[2][-1]]][temp[1]]!=0
#         num = g4[paths[temp[2]][-1]][temp[1]]# this so make sure it is node that is adjacent
#         # print(num)
#         if -1  not in paths[temp[2]] and temp[1] not in paths[temp[2]] and 6!= paths[temp[2]][-1] and num !=0:#checks matrix if does have -1 and no copies
#             paths[temp[2]].append(temp[1])#add our index
#             paths[temp[2]][0] = paths[temp[2]][0]+temp[0]#update the cost
#             if temp[1] == 6 and not ans:# make sure it first to reach goal 
#                 ans = paths[temp[2]]
#         for index,val in enumerate(g4[temp[1]]):# loop to find and queue next nodes
#             if temp[2]==0:
#                 if index not in paths[0] and val!=0 and paths[0][-1]!=6 and -1 not in paths[0]:# we do not want queue if cost more than current answer and not go after index 6
#                     # paths[0][0]= paths[0][0]+val
#                     # paths[0].append(index)
#                     # if index ==6:
#                     #     paths[0].append('GOAL')
#                     # if index ==6 and  not ans:
#                     #     ans=paths[0]
#                     #     priority_q.put((val,index,0))
#                     #     # paths[1].append('GOAL')
#                     # else:
#                     # print(index,"***",g4[paths[temp[2]][-1]])
#                     if (val,index,0) not in list(priority_q.queue) and  g4[paths[temp[2]][-1]][index ]!=0:
#                         priority_q.put((val,index,0))# cost, index , which path it belongs to
#                         # history_queue.append((val,index,0))

#             if temp[2]==1:
#                 if index not in paths[1] and val!=0 and paths[1][-1]!=6 and -1  not in paths[1]:
#                     # paths[1][0]= paths[1][0]+val
#                     # paths[1].append(index)
#                     # if index ==6 and  not ans:
#                     #     ans=paths[1]
#                     #     # paths[1].append('GOAL')
#                     # else:
#                     if (val,index,1) not in list(priority_q.queue) and g4[paths[temp[2]][-1]][index ]!=0:
#                         priority_q.put((val,index,1))
#             if temp[2]==2:
#                 if index not in paths[2] and val!=0 and paths[2][-1]!=6  and -1 not in  paths[2]:
#                     # paths[2][0]= paths[2][0]+val
#                     # paths[2].append(index)
#                     # if index ==6:
#                     #     paths[2].append('GOAL')
#                     # if index ==6 and  not ans:
#                     #     ans=paths[2]
#                     #     # paths[1].append('GOAL')
#                     # else:
#                     if (val,index,2) not in list(priority_q.queue) and g4[paths[temp[2]][-1]][index ]!=0:
#                         priority_q.put((val,index,2))
                       
#                     # priority_q.put((val,index,2))
#     print(paths[0],"path 1")
#     print(paths[1],"path 2")
#     print(paths[2],"path 3\n")

#                     # break
#     # if paths[0][-1]==6 or paths[1][-1]==6 or paths[2][-1]==6:
#     #     pass
#     if ans:# to make sure we stop asking if paths cost more than current
#         if ans[2]!=paths[0][2] and ans[0]<paths[0][0] and -1 not in paths[0]:
#             paths[0].append(-1)
#         if ans[2]!=paths[1][2] and ans[0]<paths[1][0] and -1 not in paths[1]:
#             paths[1].append(-1)
#         if ans[2]!=paths[2][2] and ans[0]<paths[2][0] and -1 not in paths[2]:
#             paths[2].append(-1)
#         # stop code if we have two -1s and 6 than stop the code
#         if paths[0][-1]==6 and paths[1][-1]==-1 and paths[2][-1]==-1:
#             break
#         if paths[1][-1]==6 and paths[0][-1]==-1 and paths[2][-1]==-1:
#             break
#         if paths[2][-1]==6 and paths[1][-1]==-1 and paths[0][-1]==-1:
#             break
# print(priority_q.queue, "Priority queue")
# print(paths[0],"path 1")
# print(paths[1],"path 2")
# print(paths[2],"path 3\n")
# # for printing 
# temp_str = "UCS cost "+str(ans[0])+" and path "
# for x in ans:
#     if x <12:
#         temp_str = temp_str+maps[x]+" "
# print(temp_str)