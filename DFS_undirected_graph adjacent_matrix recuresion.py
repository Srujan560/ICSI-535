from collections import  deque
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
q=deque()
q.append(11)# Add our stating node
ans=[]
# print(visited)

"""
First thing let make sure our queue is not empty
than pop left most and check if has already visited 
If not not visited let add check and its adjacent nodes is
loop through node that are adjacent node than add to queue than call dfs 
"""
def dfs(visited,q=deque(),ans=[]):
    print(q)
    if not q:
        print("No more items in queue")
        return ans
    
    temp_num = q.popleft()
    if visited[temp_num]==0:
        
        visited[temp_num]=1#upade our visited 
        ans.append(temp_num)# add to our answer
        if(temp_num==6):# our target  goal 
            temp_str="DFS "
            for x in ans:
                temp_str=temp_str+maps[x]+" "
            print(temp_str)
            return temp_str# return string so we know found our Goal 
        test_str=str(temp_num)+ ": "
        for x,val in enumerate(g1[temp_num]):# Loop through index and val 
            # test_str=test_str+str(x)+" "
            if val ==1 and visited[x]==0 and x not in list(q):# make sure it edge and not been visited and not in queue
                q.append(x)
                ans = dfs(visited,q,ans)# call right way b/c we are going Depth first  
                if isinstance(ans,str):# check if is string 
                    return ans
        # print(test_str)# this return 
        return dfs(visited,q,ans)
ans=dfs(visited,q,ans)
# print(ans)