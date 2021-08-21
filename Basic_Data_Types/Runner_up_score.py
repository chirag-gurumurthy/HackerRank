if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    my_list = []
    for x in arr:
        if x != max(arr):
            my_list.append(x)
    my_list.sort()
    print(my_list[-1])
