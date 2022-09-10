from collections import deque
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
visited ={'A':0,'B':0,'C':0,'D':0,'E':0,'F':0,'G':0,'H':0,'P':0,'Q':0,'R':0}
# print(list(g2.keys())[0])
# for k,v in visted.items():
#     visted[k]=1
# print(visted)
q= deque()
ans=[]
q.append(list(g2.keys())[0])# First Let add our Start node 'S' in our deque
#we will solve dfs using recursion 
"""
First We check if q is empty
than we will pop the leftmost or FIFO
Than We sill if it is 'G' our target to find Goal
than go through each Node that is neighbors
than add the first neighbor we visit
than recursively call our function if not found it will come back to the for loop else it will return path it took 
"""
def dfs(visted,q=deque(),ans=[]):
    print(q)
    if not q:
        return ans# return an list
    temp = q.popleft()
    ans.append(temp)
    if(temp=='G'):
        str_ans_path =""
        for x in ans:
            str_ans_path=str_ans_path+x+" "
        print("DFS",str_ans_path)
        ans =str_ans_path #This is break our for loop
        return ans # we return string
        # exit()
    visted[temp]=1
    # print(visted)
    for x in g2[temp]:
        if visted[x]==0 and temp not in (list(q)):#Only visit a unvisited node and make sure is not in the list already
            q.append(x)# add to the deque
            ans = dfs(visted,q,ans)# here we store answer
            if isinstance(ans,str): # check if it is an answer
                break#than exit the for loop
    return ans#Just return the same string till nothing left
t =dfs(visited,q,ans)   
# print(t, "if this list than we where not able find our Goal")