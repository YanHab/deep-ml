import math

def softmax(scores: list[float]) -> list[float]:
    # Your code here
    prob = []
    sum_exp = 0

    maximum = max(scores)
    for item in scores:  
        sum_exp += math.exp(item - maximum)
    
    for item in scores:
        prob.append(math.exp(item - maximum)/sum_exp)

    return prob