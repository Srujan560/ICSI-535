import queue


g4= {
    'S':{'D':3,'E':9,'P':1},
    'D':{'B':1,'C':8,'E':2},
    'E':{'H':8,'R':2},
    'P':{'Q':15},
    'B':{'A':2},
    'C':{'A':2},
    'H':{'P':4,'Q':4},
    'R':{'F':2},
    'Q':{},
    'A':{},
    'F':{'G':2},
    'G':{}

}
visited ={'A':0,'B':0,'C':0,'D':0,'E':0,'F':0,'G':0,'H':0,'P':0,'Q':0,'R':0,'S':0}

p_queue = queue.PriorityQueue() #
p_queue.put((0,'S',['S']))# In here We put current cost Current Node , and empty list
ans =[]
while not p_queue.empty():
    print(p_queue.queue)
    temp= p_queue.get()# let get lowest cost 
    visited[temp[1]]=1# update Graph 
    if temp[1]=='G':# stop once we find cheap 
        # temp[3].append(temp[1])
        ans=temp[2]# return the list
        ans.append(temp[0])# add the cost
        p_queue.task_done()# empty the stack
    for x  in g4[temp[1]]:
        if visited[x]==0:# make sure it is not visited 
            t3=list(temp[2])
            t3.append(x)
            # here we add all the adjacent neighbor and the cost ... only lost cost will run  
            p_queue.put((temp[0]+g4[temp[1]][x],x,t3))
# print(ans)
cost = ans.pop()
temp_str="UCS G4 Cost "+str(cost)+" "
for x in ans:
    temp_str = temp_str +x+" "
print(temp_str)


# # test = ((4,['A','B','C']),(11,['a','c','f']))
# # temp = list(test)
# # temp.append((6,['a','x','z']))
# # test=tuple(temp)
# # print(test)
# # for x in test:
# #     for i in x:
# #         print(i)
# # print(test)
# # test=sorted(test, reverse=True)
# # print(test)
# p_queue = queue.PriorityQueue()
# p_queue.put((0,'S'))#let add stating node
# ans = ["S"]*len(g4['S'])
# possible1=[0,'S']
# possible2=[0,'S']
# possible3=[0,'S']

# # ans[2] = ['G']
# # ans[1]=['S']*10
# # if 'G' in ans[2]:
# #     print("LOLOLO")
# # print(ans)
# test =[]
# while not p_queue.empty():
#     print(p_queue.queue)
#     temp = p_queue.get()
#     if temp[0]==0:
#         for x,val in enumerate(g4[temp[1]]):
#             if x==0:
#                 # possible1[0]=g4[temp[1]][val]
#                 # possible1.append(val)
#                 p_queue.put((g4[temp[1]][val],val,val))
#             if x==1:
#                 # possible2[0]=g4[temp[1]][val]
#                 # possible2.append(val)
#                 p_queue.put((g4[temp[1]][val],val,val))
#             if x==2:
#                 # possible3[0]=g4[temp[1]][val]
#                 # possible3.append(val)
#                 p_queue.put((g4[temp[1]][val],val,val))
#     else:
#         check= 0
#         # print(possible1[-1],"****",list(g4[temp[1]].keys()))
#         # print(temp[1],"^^^^",list(g4[possible1[-1]].keys()))
#         # break
#         if not g4[temp[1]]:
#             g_checker=0
#             if temp[1]=='G':
#                 g_checker=1
#             if temp[2]=='D':
#                 possible1.append(temp[1])
#                 possible1[0]= possible1[0]+temp[0]
#                 if g_checker !=1:
#                     possible1.append('STOP')
#             if temp[2]=='E':
#                 possible2.append(temp[1])
#                 possible2[0]= possible2[0]+temp[0]
#                 if g_checker !=1:
#                     possible2.append('STOP')
#             if temp[2]=='P':
#                 possible3.append(temp[1])
#                 possible3[0]= possible3[0]+temp[0]
#                 if g_checker !=1:
#                     possible3.append('STOP')
#         else:
#             for x in g4[temp[1]]:
#                 # print(list(g4[possible1[-1]].keys()),x ,"*******")
                
#                 if temp[2]=='D' and 'STOP' not in possible1:# if D
#                     many_paths = len(g4[temp[1]])
#                     ok_to_put_queue=[]
#                     if( many_paths>1):
#                         cheap_path=[[0] for i in range(many_paths)]
#                         print(cheap_path)
#                         for ind,val in enumerate(g4[temp[1]]):
#                             cheap_path[ind].append(val)
#                             cheap_path[ind][0] = g4[temp[1]][val]
#                         print(cheap_path)
#                         for ind,someVal in enumerate(cheap_path):
#                             print(g4[someVal[1]].keys())
#                             if len(g4[someVal[1]])==1 and list(g4[someVal[1]].keys())[0] != 'G':
#                                 cheap_path[ind][0]=100#put cost high so it not be added
#                                 # cheap_path.append(list(g4[someVal[1]].keys())[0])
#                         print(cheap_path)
#                         for ss in cheap_path:
#                             if ss[0]!=100:
#                                 ok_to_put_queue.append(ss[1])

#                     # print('temp',temp[1]," *****",list(g4[possible1[-1]].keys()),"check ?",check)
#                     if check ==0 and temp[1] in list(g4[possible1[-1]].keys()) and temp[1] not in possible1:
#                         print('********')
#                         # ina =0
#                         # if len(list(g4[possible1[-1]].keys())) >1:
#                         #     check_cost = g4[possible1[-1]][temp[1]]
#                         #     for isthis in g4[possible1[-1]]:
#                         #         # print(g4[possible1[-1]][isthis])
#                         #         if check_cost >g4[possible1[-1]][isthis]:
#                         #             ina=1
#                         #     # exit()
#                         # if ina==0:
#                         check=1
#                         possible1[0]= possible1[0]+temp[0]
#                         possible1.append(temp[1])
                
#                     if x not in possible1 and 'G' not in possible1 and 'STOP' not in possible1 and (g4[temp[1]][x],x,'D') not in list(p_queue.queue):
#                         # possible1[0]= possible1[0]+g4[temp[1]][x]
#                         # possible1.append(x)
#                         # if x in list(g4[possible1[-1]].keys()):
#                         if len(ok_to_put_queue)!=0 and x in ok_to_put_queue or len(ok_to_put_queue)==0:
#                             p_queue.put((g4[temp[1]][x],x,'D'))
#                 if temp[2]=='E' and 'STOP' not in possible2:
#                     if check ==0 and temp[1] in list(g4[possible2[-1]].keys()) and temp[1] not in possible2:
#                         check=1
#                         possible2[0]= possible2[0]+temp[0]
#                         possible2.append(temp[1])
                
#                     if x not in possible2 and 'G' not in possible2 and 'STOP' not in possible2 and (g4[temp[1]][x],x,'E') not in list(p_queue.queue):
#                         # possible2[0]= possible2[0]+g4[temp[1]][x]
#                         # possible2.append(x)
#                         # if x in list(g4[possible2[-1]].keys()):
#                             p_queue.put((g4[temp[1]][x],x,'E'))
#                 if temp[2]=='P':
#                     if check ==0 and temp[1] in list(g4[possible3[-1]].keys()) and temp[1] not in possible3:
#                         check=1
#                         possible3[0]= possible3[0]+temp[0]
#                         possible3.append(temp[1])
#                     #let make sure it not the PQ already 
#                     if x not in possible3 and 'STOP' not in possible3 and 'G' not in possible3 and (g4[temp[1]][x],x,'P') not in list(p_queue.queue):
#                         # possible3[0]= possible3[0]+g4[temp[1]][x]
#                         # possible3.append(x)
#                         # if x in list(g4[possible3[-1]].keys()):# this checks that last index can access Node before we put in the p q
#                             p_queue.put((g4[temp[1]][x],x,'P'))
#     print(possible1,"p1")
#     print(possible2,"p2")
#     print(possible3,"p3",)
#     # time.sleep(1.5)
#     if 'G' in possible1 or 'G' in possible2 or 'G' in possible3:
#         # break
#         if not test:
#             # print("test ", test)
#             if 'G' in possible1:
#                 test=possible1
#                 # print("Test",test,"p1",possible1)
#                 # break
                
#             elif 'G' in possible2:
#                 test=possible2
#             else:
#                 test=possible3
#         else:
#             # print(temp[2]," **** ",test)
#             if temp[2]=='D' and 'D' != test[2]:
#                 # print(temp,"****",test)
#                 # break
#                 if test[0] < possible1[0] and 'STOP' not in possible1:
#                     possible1.append('STOP')
#                 else:
#                     if 'G' in possible1:
#                         test=possible1
#             elif temp[2]=='E' and 'E' != test[2]:
#                 # print(test[0],"****",possible2[0])
#                 # break
#                 if test[0] < possible2[0] and 'STOP' not in possible2:
#                     possible2.append('STOP')
#                 else:
#                     if 'G' in possible2:
#                         test=possible2
#             elif temp[2]=='P'and 'P' != test[2]:
#                 if test[0] < possible3[0] and 'STOP' not in possible3:
#                     possible3.append('STOP')
#                 else:
#                     if 'G' in possible3:
#                         test=possible3
#     if 'STOP' in possible2 and 'STOP' in possible3 and 'G' in possible1:
#         break
#     if 'STOP' in possible1 and 'STOP' in possible2 and 'G' in possible3:
#         break 
#     if 'STOP' in possible1 and 'STOP' in possible3 and 'G' in possible2:
#         break  
#     print(test,"Test\n")

#         # break
    
#     # print(temp[1],"Test")
#     # if visited[temp[1]]==0:
#     #     visited[temp[1]]=1
#     #     for index,val in enumerate(g4[temp[1]]):
#     #         print(index," val = ",val)
#     #         # if visited[val]==0:
#     #         # ans[index] = ans[index]+" "+val
#     #         num = temp[0]+g4[temp[1]][val]
#     #         # val=val
#     #         # print(val)
#     #         # temp[2]=list(temp[2]).append(temp[1])
#     #         # print(temp[2],"******")

#     #         p_queue.put((num,val))

        
#         # test =[x for x in ans if 'G' in x]
#         # if test:
#         #     temp_str= "UCS "+str(test)+" cost: "+str(temp[0])
#         #     print(temp_str)
#         # else:
#         # print(ans)
#     # print(temp)
# temp_str ="UCS cost "+str(test[0])+" "
# for index,val in enumerate(test):
#     if index !=0:
#         temp_str = temp_str+val+" "
# print(temp_str)

    