n = 5
arr = [2, 3, 6, 6, 5]
x = max(arr)
count = 0
arr = sorted(arr, reverse=True)
for i in arr:
    if i != x:
        count += 1
runnerUp = arr[len(arr)-count]
print(runnerUp)
