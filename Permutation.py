#!/bin/env python3

# Find all possible permutations 
def p(elements, r):
    
    # Will be used a lot
    n = len(elements)
    
    # Errors
    if n < r:
        raise ValueError('n must be greater than or equal to r')
    
    # If r is done, return
    if r <= 0:
        return []
    
    # Make an empty set to use later
    setSet = []
    
    for i in range(0, n):
        # Make a copy of the elements list to avoid corruption of the original list
        set = elements.copy()
        
        # Get the current element
        e = set.pop(i)
        #print('e: ', e)
        #print('set: ', set)
        
        sets = p(set.copy(), r - 1)
        #print('sets: ', sets)
        
        if not sets:
            setSet = [[e]]
        else:
            for set1 in sets:
                setSet.append([e] + set1)
                #print(set1)
    
    # Return the final set of sets
    return setSet
