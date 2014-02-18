from collections import defaultdict
clist =  [8,1,3,9]

def pivot(clist):
    if len(clist)==1:
        return 0
    elif len(clist)==0:
        return -1
    else:
        visited=defaultdict(int)
        p=len(clist)/2
        visited[p]+=1
        front=clist[:p]
        end=clist[p+1:]
        while len(front)>=1 and len(end)>=1 and visited[p]<=1:
            if sum(front)<sum(end):
                p+=len(end)/2
            elif sum(front)>sum(end):
                p-=len(front)/2
            else:
                return p
            visited[p]+=1
            front=clist[:p]
            end=clist[p+1:]
        return -1

print pivot(clist)