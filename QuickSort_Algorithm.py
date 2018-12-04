def swap(arr, i, j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp


def partition(arr, front, end):
    pivot = front
    left = front
    right = end
    flag = 0
    # ------------------------------------------------------
    while True:
        if left == right:
            break

        # pivot 在左邊
        if flag == 0:
            if (arr[pivot] < arr[right]) or (arr[pivot] == arr[right]):
                right -= 1
            elif arr[pivot] > arr[right]:
                swap(arr, pivot, right)
                pivot = right
                flag = 1
        # pivot 在右邊
        elif flag == 1:
            if arr[pivot] > arr[left]:
                left += 1
            elif (arr[pivot] < arr[left]) or (arr[pivot] == arr[left]):
                swap(arr, pivot, left)
                pivot = left
                flag = 0
    print(" ".join(str(result) for result in arr))
    return pivot


def quick_sort(raw_arr, front, end):
    if front < end:
        pivot = partition(raw_arr, front, end)
        quick_sort(raw_arr, front, pivot-1)
        quick_sort(raw_arr, pivot+1, end)
    else:
        pass


arr_num = input("欲排列數字個數：")
target_arr = input("輸入欲排列數字(以空白鍵分隔)：").split(' ')
target_arr = list(map(int, target_arr))
quick_sort(target_arr, 0, int(arr_num)-1)
