def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    if not nums:
        raise ValueError('Empty array')
    else:
        return min(nums), max(nums)

print(min_max([3, -1, 5, 5, 0]))  # Должно быть (-1, 5)
print(min_max([42]))              # Должно быть (42, 42)
print(min_max([-5, -2, -9]))      # Должно быть (-9, -2)
print(min_max([1.5, 2, 2.0, -3.1])) # Должно быть (-3.1, 2)
print(min_max([]))                  # Должно быть ValueError

