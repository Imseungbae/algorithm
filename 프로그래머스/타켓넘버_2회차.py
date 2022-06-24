result = 0
def solution(numbers, target):
    global result
    a = dfs(0,numbers[0], numbers, target)
    b = dfs(0,-numbers[0], numbers, target)
    return result

def dfs(idx, num, numbers, target):
    global result
    
    if idx == len(numbers):
        return 

    plus = num + numbers[idx]
    minus = num - numbers[idx]
    
    if target == plus:
        result = result + 1
        
    if target == minus:
        result = result + 1
    
    dfs(idx+1, plus, numbers, target)
    dfs(idx+1, minus, numbers, target)
    