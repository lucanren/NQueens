#python3 NQueensBTGreen.py

import sys
import random
import time

def goal_test(s,l):
    return len(s)==l

def get_next_unassigned_var(s):
    return len(s)

def get_sorted_values(s,v,l): #v = var = row number
    out = []
    for i in range(0,l):
        switch = True
        for j in range(0,v):
            if abs(s[j]-i) == abs(j-v) or i in s:
                switch = False
        if switch: out.append(i)
    random.shuffle(out)
    return out

def nq_backtrack(state,length):
    if goal_test(state,length): return state
    var = get_next_unassigned_var(state)
    for val in get_sorted_values(state,var,length):
        new_state = state+ [val]
        result = nq_backtrack(new_state,length)
        if result is not None:
            return result
    return None

def test_solution(state):
    for var in range(len(state)):
        left = state[var]
        middle = state[var]
        right = state[var]
        for compare in range(var + 1, len(state)):
            left -= 1
            right += 1
            if state[compare] == middle:
                print(var, "middle", compare)
                return False
            if left >= 0 and state[compare] == left:
                print(var, "left", compare)
                return False
            if right < len(state) and state[compare] == right:
                print(var, "right", compare)
                return False
    return True

s = time.perf_counter()
x = nq_backtrack([],30)
print(x)
print(test_solution(x))
y = nq_backtrack([],31)
print(y)
print(test_solution(y))
e = time.perf_counter()
print("Total time: " + str(e-s) + " seconds!")


