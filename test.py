def str_to_tuple(str):
    nums = []
    for char in str:
        if char.isnumeric():
            nums.append(int(char))
    return tuple(nums)

print(str_to_tuple(str((0,0))))

print(str((0,0)))