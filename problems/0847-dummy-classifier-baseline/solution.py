import numpy as np
from collections import Counter

def dummy_classifier(y_train, n_test, strategy, constant=None):
    """
    Produce baseline predictions of length n_test using the given strategy.
    Returns a Python list of predicted labels.
    """

    if strategy == "constant":
        return [constant]*n_test
    elif strategy == "most_frequent":
        count = Counter(y_train)
        value, _ = count.most_common(1)[0]
        return [value]*n_test

    elif strategy == "uniform":
        count = Counter(y_train)
        return [ i % len(count) for i in range(n_test) ]
    elif strategy == "stratified":
        count = Counter(y_train)
        classes = sorted(count)

        ideal = {c: n_test * count[c] / len(y_train) for c in classes}
        allocation = {c: int(ideal[c]) for c in classes}

        remaining = n_test - sum(allocation.values())

        for c in sorted(classes, key=lambda c: (-(ideal[c] % 1), c))[:remaining]:
            allocation[c] += 1

        return [c for c in classes for _ in range(allocation[c])]
                

    
