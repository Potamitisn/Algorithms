from typing import List


def insertion_sort(A: List[float], n: int) -> List[float]:
    # Complexity : n * n
    for j in range(1,n):
        key = A[j]
        i = j-1
        while i>=0 and A[i] > key:
            A[i+1] = A[i]
            i = i -1
        A[i+1] = key
    return A

def merge_sort(A: List[float], p: int, r: int, verbose=False):
   # Complexity : n * log(n) 
    def merge(A: List[float], p: int, q: int, r: int, verbose: bool):

        L1 = A[p:q] + [float("inf")]
        L2 = A[q:r] + [float("inf")]

        for i in range(p, r):
            if L1[0] < L2[0]:
                A[i] = L1.pop(0)
            else:
                A[i] = L2.pop(0)
            
        
        if verbose:
            print("---")
            for i in range(p, r):
                print(f"A[{i}] = {A[i]}")
            print("---")
    
    if p < r - 1:
        q = (p + r + 1) // 2
        merge_sort(A, p, q, verbose)
        merge_sort(A, q, r, verbose)
        merge(A, p, q, r, verbose)
    
    return A

