def print_array(arr, n):
    i = 0
    while (i < n):
    print(arr[i], end = " ")
    i += 1
arr = list()
n = int(input("Enter number of elements: "))
print("Enter elements:")
i = 0
while (i < n):
    tmp = int(input(""))
    arr.append(tmp)
    i += 1
print("Array:")
print_array(arr, n)
print("")
