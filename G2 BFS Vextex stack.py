g2 = {'S' :['D','E','P'],
'A': [],
'C': ['A'],
'D': ['B', 'C', 'E'], 
'B': ['A'], 
'G': [], 
'E': ['H', 'R'], 
'F': ['C', 'G'], 
'H': ['P', 'Q'], 
'P': [ 'Q'],
'Q': [], 
'R': ['F']
}
visited ={'A':0,'B':0,'C':0,'D':0,'E':0,'F':0,'G':0,'H':0,'P':0,'Q':0,'R':0,'S':0}
ans=[]
stack_bfs=[]
stack_bfs.append(list(g2.keys())[0])
temp_str=""
current_stack=""
while stack_bfs and temp_str!='G':#Let make sure our stack is not empty or our Node to ='G'
    print("Stack_BFS",stack_bfs)
    current_stack=stack_bfs.pop()
    temp_str=current_stack[-1]
    if visited[temp_str]==0: # Let check if visited or not
        visited[temp_str]=1
        ans.append(temp_str)
        temp_stack=[]# we create a temp stack to put current stack at top, so when we pop we pop at level not depth 
        for x in reversed(g2[temp_str]):#We loop in revers so we put most right at bottom of stack 
            if visited[x]==0: #and x  not in stack_bfs: # make sure it has not been visited yet, and not in stack already 
                new_stack = list(current_stack)
                new_stack.append(x)
                # print(new_stack)
                
                temp_stack.append(new_stack)
        
        # print("temp_stack",temp_stack)
        if temp_stack:# If we Nodes to add to current stack
            for x in (stack_bfs):# puts the currrent node stacks at top
                temp_stack.append(x)
            stack_bfs=temp_stack # return newst nodes at which order to go
    # print("End Loop")
print("BFS expanded",ans) 
print("BFS PATH",current_stack)
   
            

