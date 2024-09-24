
numbers = [3, 6, 2, 5, 10, 25, 20]

def bubble_sort(arr):
    
    n = len(arr)
    for i in range(n):

        for j in range(0, n - i - 1):

            print(arr[j], arr[j + 1])

            if arr[j] > arr[j + 1]:

                arr[j], arr[j + 1] = arr[j + 1], arr[j]

                print('Yes!!')
                print(arr)

    return arr

sorted_list = bubble_sort(numbers)
print(sorted_list)
