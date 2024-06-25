#generate all permutations of a sequence of elements

def permutation(x):
    if len(x)==0:
        return [[]] 
    tot=[] 
    for i in range(len(x)):
        actual=x[i]
        remaining=x[:i]+x[i+1:]
        others=permutation(remaining)
        for y in others:
            tot.append([actual]+y)
    return tot

element=['a', 'b', 'c', 4]
res=permutation(element)
print(res)
