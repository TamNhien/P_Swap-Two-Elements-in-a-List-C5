def swapPositions(lst, pos1, pos2):
    for i, x in enumerate(lst):
        if i == pos1:
            elem1 = x
        if i == pos2:
            elem2 = x
    lst[pos1] = elem2
    lst[pos2] = elem1
    return lst

lst = [23, 65, 19, 90]
pos1, pos2 = 1, 3
print(swapPositions(lst, pos1-1, pos2-1))
    
    
                
