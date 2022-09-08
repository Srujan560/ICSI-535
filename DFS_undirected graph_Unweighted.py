from collections import deque
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

# for k,v in g1.items():
#     print(k,"->",v)
#     temp = "\t"
#     for x in v:
#         temp=temp+x+", "
#     print(temp)
# print(g1['S'][0])

visted ={'A':0,'B':0,'C':0,'D':0,'E':0,'F':0,'G':0,'H':0,'P':0,'Q':0,'R':0}
# print(list(g1.keys())[0])
# for k,v in visted.items():
#     visted[k]=1
# print(visted)
q= deque()
ans=[]
q.append(list(g1.keys())[0])
def dfs(visted,q=deque(),ans=[]):
    if not q:
        return ans
    temp = q.popleft()
    ans.append(temp)
    if(temp=='G'):
        str_ans_path =""
        for x in ans:
            str_ans_path=str_ans_path+x+" "
        print("DFS",str_ans_path)
        ans =str_ans_path
        return ans
        # exit()
    visted[temp]=1
    print(visted)
    for x in g1[temp]:
        if visted[x]==0:
            q.append(x)
            ans = dfs(visted,q,ans)
            if isinstance(ans,str):
                break
    return ans
t =dfs(visted,q,ans)   
# print(t)



