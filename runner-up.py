if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    unique_scores = sorted(list(set(arr)))
    
    if len(unique_scores) >= 2:
        print(unique_scores[-2])
    else:
        print(unique_scores[0])