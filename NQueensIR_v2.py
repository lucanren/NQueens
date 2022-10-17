#python3 NQueensIRGreen.py

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
                #print(var, "middle", compare)
                return False
            if left >= 0 and state[compare] == left:
                #print(var, "left", compare)
                return False
            if right < len(state) and state[compare] == right:
                #print(var, "right", compare)
                return False
    return True

# s = time.perf_counter()
# x = nq_backtrack([],30)
# print(x)
# print(test_solution(x))
# y = nq_backtrack([],31)
# print(y)
# print(test_solution(y))
# e = time.perf_counter()
# print("Total time: " + str(e-s) + " seconds!")

#-----------------------------------------------------------

def genState(s):
    nums = [x for x in range(0,s)]
    random.shuffle(nums)
    state = []
    for i in range(0,s):
        state.append(nums.pop())
    return state

def mostAtk(s): #returns which row getting most attacked (since 1 row = 1 queen)
    # atk = [] #index = row
    # for q1 in s: #row
    #     ind = s.index(q1)
    #     count = 0
    #     for q2 in s:
    #         if ind!=s.index(q2):
    #             if q2 == q1: count+=1
    #             if abs(s.index(q2)-s.index(q1)) == abs(q2-q1): count+=1
    #     atk.append(count)
    # maxAtk = [x for x in range(0,len(atk)) if atk[x]==max(atk)]
    # random.shuffle(maxAtk)
    # print(atk)
    # print(maxAtk)
    # return maxAtk[0]
    atk = [] #index = row
    for i in range(0,len(s)): #row
        count = 0
        for j in range(0,len(s)):
            if i!=j:
                if s[i] == s[j]: count+=1
                if abs(s[j]-s[i]) == abs(j-i): count+=1
        atk.append(count)
    maxAtk = [x for x in range(0,len(atk)) if atk[x]==max(atk)]
    #print(maxAtk)
    random.shuffle(maxAtk)
    #print(atk)
    return maxAtk[0]

def minAtk(s,r): #s,r because know which row to focus on
    atk=[] #index = queen pos within row
    for q in range(0,len(s)): #square
        count = 0
        for p in range(0,len(s)):
                if(p!=r):  #CANT SKIP THE CURRENT POS FIX
                    if q == s[p]: count+=1
                    if abs(p-r) == abs(s[p]-q): count+=1
        atk.append(count)
    minAtk = [x for x in range(0,len(atk)) if atk[x]==min(atk)]
    random.shuffle(minAtk)
    return minAtk[0]

def totalConf(s):
    atk = [] #index = row
    for i in range(0,len(s)): #row
        count = 0
        for j in range(0,len(s)):
            if i!=j:
                if s[i] == s[j]: count+=1
                if abs(s[j]-s[i]) == abs(j-i): count+=1
        atk.append(count)
    return sum(atk)

def incRepair(s):
    if(test_solution(s)==True):
        global solution
        solution = s
        return s
    r = mostAtk(s)
    p = minAtk(s,r)
    n = [x for x in s]
    n[r] = p
    print(n)
    c = totalConf(n)
    print("Conflicts: " + str(c))
    #print()
    incRepair(n)
    return None

s1 = time.perf_counter()
for i in range(31,33):
    x = genState(i)
    print("Conflicts: " + str(totalConf(x)))
    print("Initial State: " + str(x))
    print()
    incRepair(x)
    print("Verification: " + str(test_solution(solution))) 
    print()
e1 = time.perf_counter()
print()
print("Total time: " + str(e1-s1))

# x = [0,2,4,1,5,5,6,3]
# #x=[0, 2, 4, 1, 7, 5, 6, 3]
# print(x)
# print(mostAtk(x))
