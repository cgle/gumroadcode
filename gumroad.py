from collections import defaultdict
clist =  [0,0]

def pivot(clist):
    if len(clist)==1:
        return 0
    elif len(clist)==0:
        return -1
    else:
        visited=defaultdict(int)
        p=len(clist)/2
        front=clist[:p]
        end=clist[p+1:]
        while visited[p]<=1:
            add_var=0
            if len(front)==1 or len(end)==1:
                add_var=1
            if clist[p]>=0:
                if sum(front)<sum(end):
                    p+=len(end)/2+add_var
                elif sum(front)>sum(end):
                    p-=len(front)/2-add_var
                else:
                    return p
            else:
                if sum(front)<sum(end):
                    p-=len(front)/2-add_var
                elif sum(front)>sum(end):
                    p+=len(end)/2+add_var
                else:
                    return p
            visited[p]+=1
            front=clist[:p]
            end=clist[p+1:]
        return -1

print pivot(clist)
