from InsertionSort import InsertionSort

datax = [34, 8, 64, 51, 32, 21, 45, 73, 17, 3, 99, 45, 67, 28, 
         73, 58, 82, 10, 1, 87, 42, 16, 70, 25, 93, 12, 37, 48]

sorter = InsertionSort(datax)

print(f"Unsorted Original Array = {datax}")
inbuilt_sort = sorted(datax)
sorter.sort()
print(f"After Sorting ...")
sorter.print_array()

test = sorter.return_array() == inbuilt_sort

if test == True:
    print("Test Passed")
else:
    print("Test Failed")
