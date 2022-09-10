g2 =[
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0],
    [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0]
]
maps ={0:'A',1:'B',2:'C',3:'D',4:'E',5:'F',6:'G',7:'H',8:'P',9:'Q',10:'R',11:'S'}
visited =[0]*12
ans=[]
stack_dfs=[]
stack_dfs.append(11)#let add our starting node
temp_num=""
"""
Let make while loop that runs as long stack is not empty and current pop is not 6 (our target goal)
let check if current node that we pop form stack is not been visited yet
than add to our ans list 
than check all it adjacent neighbors b/c it DFS we need make sure we get far left to at top our stack
"""
while stack_dfs and temp_num!=6:
    print (stack_dfs)
    temp_num=stack_dfs.pop()
    if visited[temp_num]==0:# let check if visited if not than update
        visited[temp_num]=1
        ans.append(temp_num)# add our answer order we visited each node
        for index,val in reversed(list(enumerate(g2[temp_num]))):# we want go in reversed but also want to get index and val
            if val==1 and visited[index]==0 and index not in stack_dfs:#let make sure before adding to stack it not been visited and it is not in stack 
                stack_dfs.append(index)
#print the answer
temp_str= "DFS stack: "
for x in ans:
    temp_str= temp_str+maps[x]+" "
print(temp_str)