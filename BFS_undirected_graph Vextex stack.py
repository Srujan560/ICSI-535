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
stack_bfs=[]
stack_bfs.append(list(g1.keys())[0])
temp_str=""
while stack_bfs and temp_str!='G':#Let make sure our stack is not empty or our Node to ='G'
    print("Stack_BFS",stack_bfs)
    temp_str=stack_bfs.pop()
    if visited[temp_str]==0: # Let check if visited or not
        visited[temp_str]=1
        ans.append(temp_str)
        temp_stack=[]# we create a temp stack to put current stack at top, so when we pop we pop at level not depth 
        for x in reversed(g1[temp_str]):#We loop in revers so we put most right at bottom of stack 
            if visited[x]==0 and x  not in stack_bfs: # make sure it has not been visited yet, and not in stack already 
                temp_stack.append(x)
        # print("temp_stack",temp_stack)
        if temp_stack:# If we Nodes to add to current stack
            for x in (stack_bfs):# puts the currrent node stacks at top
                temp_stack.append(x)
            stack_bfs=temp_stack # return newst nodes at which order to go
    # print("End Loop")
print("ans BFS",ans) 
   
            

