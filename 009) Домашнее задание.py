n = int(input())
nums_list = list(map(int, input().split()))

min_index = nums_list.index(min(nums_list))
max_index = nums_list.index(max(nums_list))
left_index = min(min_index, max_index)
right_index = max(min_index, max_index)

amount = sum(number for number in nums_list if number > 0)

product = 1
for number in nums_list[left_index + 1 : right_index]:
    product *= number

print(amount, product)