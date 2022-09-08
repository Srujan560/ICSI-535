from inspect import stack


g1 = {'S' :['D','E','P'],
'A': ['B', 'C'],
'C': ['A', 'D', 'F'],
'D': ['B', 'C', 'E', 'S'], 
'B': ['A', 'D'], 
'G': ['F'], 
'E': ['D', 'H', 'R', 'S'], 
'F': ['C', 'G', 'R'], 
'H': ['E', 'P', 'Q'], 
'P': ['H', 'Q', 'S'],
'Q': ['H', 'P'], 
'R': ['E', 'F']
}
visited ={'A':0,'B':0,'C':0,'D':0,'E':0,'F':0,'G':0,'H':0,'P':0,'Q':0,'R':0,'S':0}
ans=[]
stack_dfs =[]
stack_dfs.append(list(g1.keys())[0])# Let get first element for our graph 1
temp_str =""
while stack_dfs and temp_str!='G':# we make sure our stack is not empty and not 'G' our target find Goal 
    print(stack_dfs)
    temp_str=stack_dfs.pop()#Let pop element from top of the stack
    if(visited[temp_str]==0):# make that element is not visited yet
        ans.append(temp_str)# add it to our node we visited
        visited[temp_str]=1# change it 1 to mark visited
        # if(temp_str=='G'):
        #     break
        for x in reversed(g1[temp_str]):# Let access adjacent node from back of the list meaning from farthest right (Deepest )  
            stack_dfs.append(x) # let push that Node at bottom of our stack, So we can pop the Left most node first 
    
# print(ans)
# For Printing Purpose 
ans_str ="DFS stacks: "
for x in ans:
    ans_str=ans_str+x+" "
print(ans_str)