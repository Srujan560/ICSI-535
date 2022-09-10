g1= [[0,1,1,0,0,0,0,0,0,0,0,0],
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
[0,0,0,1,1,0,0,0,1,0,0,0]]
maps ={0:'A',1:'B',2:'C',3:'D',4:'E',5:'F',6:'G',7:'H',8:'P',9:'Q',10:'R',11:'S'}
visited =[0]*12
ans=[]
stack_bfs=[]
stack_bfs.append(11)# let add our staring index (node)
temp_num=0
"""
let have while loop that run till stack is not empty and current pop is not 6
Check if current node is not been visited and loop through and get adjacent neighbors 
then put in stack where left most at top of stack so when pop it goes through level of adjacent matrix 
"""
while stack_bfs and temp_num!=6:
    print(stack_bfs)
    temp_num=stack_bfs.pop()
    if visited[temp_num]==0:#let check and update our visited nodes
        visited[temp_num]=1
        ans.append(temp_num)
        temp_stack=[]# this stack make sure that we have left most stack at top of our stack
        for index,val in reversed(list(enumerate(g1[temp_num]))):# going reversed b/c we get right most neighbor to be bottom of our stack and left most at top our stack
            if val==1 and visited[index]==0 and index not in stack_bfs:# make sure it is a neighbor and not been visited not it is the stack
                temp_stack.append(index)
        for x in stack_bfs:#loop add current stack and right to left at top of the sack
            temp_stack.append(x)
        stack_bfs=temp_stack# give the update stack
#for printing purpose
temp_str="BFS "
for x in ans:
    temp_str =temp_str+maps[x]+" "
print(temp_str)
