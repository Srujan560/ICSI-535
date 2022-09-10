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
visited ={'A':0,'B':0,'C':0,'D':0,'E':0,'F':0,'G':0,'H':0,'P':0,'Q':0,'R':0,'S':0}
ans=[]
q=deque()
q.append(list(g2.keys())[0])
"""
First We need go Levels So We will add all the adjacent nodes to deque
Than keep adding all the current node adjacent nodes
If we found 'G' than stop our recursive method
If not found we return order of node we visited

"""
def bfs(visited,q=deque(),answer=[]):
    print(q)
    if not q:# if deque is empty that return path
        print("Exiting no more node to go")
        return answer
    temp_str= q.popleft()# remove First item we added 
    if visited[temp_str]==0:#check if we visited this node 
        visited[temp_str]=1#update node to visited 
        answer.append(temp_str)# add to which node we have visited
        if temp_str=='G':#If we found our 'G' than stop bfs
            print("BFS",answer)
            return answer
        for x in g2[temp_str]:#looping the adjacent nodes
            if visited[x]==0:#make sure that node not visited yet
                if x not in list(q):#also make sure not already in queue 
                    q.append(x)
        # if q:
        return bfs(visited,q,answer)# Once added queue than call bfs do same for the rest of link
        # else:
        #     print("Exiting No more node to go")

ans = bfs(visited,q,ans)
# print(ans)