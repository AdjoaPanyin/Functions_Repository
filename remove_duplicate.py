def duplicate_remover(list):
    resolvedList = []
    for i in list:
        if i not in resolvedList:
            resolvedList.append(i)
            
    return resolvedList

myList = [1, 2, 3, 3, 4, 4, 5, 6, 7, 7, 8, 9]
print(duplicate_remover(myList))

list_mixture= [1, 2, 3, 3, "koo", "lisa", "koo",4, 4, 5, 6, 7, 7, 8, 9]
print(duplicate_remover(list_mixture))