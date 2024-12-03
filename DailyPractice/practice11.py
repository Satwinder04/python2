# import array
# arr = array.array('i', [1, 2, 3])
# print(arr)
#
# # 1. Create an Array and Print It
# arr = [1, 2, 3, 4, 5]
# print("Array:", arr)
#
# # 2. Find the Sum of Elements in an Array
# print("Sum of Elements:", sum(arr))
#
# # 3. Find the Maximum and Minimum Elements
# print("Max:", max(arr), "Min:", min(arr))
#
# # 4. Reverse an Array
# print("Reversed Array:", arr[::-1])
#
# # 5. Find the Frequency of Each Element
# freq = {}
# for x in arr:
#     freq[x] = freq.get(x, 0) + 1
# print("Frequency of Elements:", freq)
#
# # 6. Search for an Element in an Array
# x = 3
# print(f"Is {x} in Array:", x in arr)
#
# # 7. Sort an Array
# print("Sorted Array:", sorted(arr))
#
# # 8. Remove Duplicates from an Array
# arr_with_duplicates = [1, 2, 2, 3, 4, 4, 5]
# print("Array without Duplicates:", list(set(arr_with_duplicates)))
#
# # 9. Merge Two Arrays
# arr1 = [1, 2, 3]
# arr2 = [4, 5, 6]
# print("Merged Arrays:", arr1 + arr2)
#
# # 10. Find the Second Largest Element in an Array
# print("Second Largest Element:", sorted(set(arr))[-2])
#
# # 11. Rotate an Array by N Positions
# n = 2
# print(f"Array Rotated by {n} Positions:", arr[n:] + arr[:n])
#
# # 12. Find the Intersection of Two Arrays
# arr1 = [1, 2, 3, 4]
# arr2 = [3, 4, 5, 6]
# print("Intersection of Arrays:", list(set(arr1) & set(arr2)))
