
def find_non_repeating_int(nums: list[int]) -> int:
    nums2 = set(nums)

    unique_nums = []
    for element in nums2:
        count = nums.count(element)
        if count == 1:
            unique_nums.append(element)

    return unique_nums


def find_non_repeating_char(string: str) -> str:

    string_list = [w for w in string]
    string_set = set(string_list)
    unique_char = []

    for element in string_set:
        count = string_list.count(element)
        if count == 1:
            unique_char.append(element)

    return unique_char


if __name__ == '__main__':

    A = [1, 2, 3, 4, 5, 4, 3, 2, 1, 0]
    print(find_non_repeating_int(A))

    Name = 'nimishvaibhav'
    print(find_non_repeating_char(Name))

