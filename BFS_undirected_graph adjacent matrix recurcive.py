from collections import deque
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
q=deque()
q.append(11)# add our staring node
"""
Let check our deque and pop left b/c we want go through levels 
if current pop node is 6 than we found our goal than loop through our answer than print the results
Let loop through each adjacent neighbor add to our deque
after the loop is done than call bfs() with update q, visited nodes

"""
def bfs(visited,ans=[],q=deque()):
    print(q)
    if not q:
        print("Nothing in the queue")
        return ans
    temp_num = q.popleft()
    if visited[temp_num]==0:# check if has not been visited than update if has not been visited
        visited[temp_num]=1
        ans.append(temp_num)# keep record which node we visited in order
        if temp_num==6:# our goal 
            # for printing answer 
            temp_str="BFS: "
            for x in ans:
                temp_str=temp_str+maps[x]+" "
            print(temp_str)
            return ans # 
        for index,val in enumerate(g1[temp_num]):
            if val == 1 and visited[index]==0 and index not in q:# let make sure it neighbor and not been visited and not in queue
                q.append(index)
        return bfs(visited,ans,q)# after adding all the adjacent neighbors call it again till we find target is 6 or queue is empty
ans= bfs(visited,ans,q)
# print(ans)