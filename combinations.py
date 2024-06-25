#generate all combinations of a set of elements

def combination(x):
    if len(x)==0:
        return [[]]  
    first=x[0]
    others=x[1:]
    remaining=combination(others)
    tot=[] 
    tot.extend(remaining)
    for y in remaining:
        new=[first]+y
        tot.append(new)
    return tot

elements=['a', 'b', 'c', 4]
res=combination(elements)
print(res)