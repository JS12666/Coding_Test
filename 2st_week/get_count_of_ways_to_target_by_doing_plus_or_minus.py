numbers = [1, 1, 1, 1, 1]
target_number = 3

result = []
def get_count_of_ways_to_target_by_doing_plus_or_minus(array, target):
    all_ways = []

    def get_all_ways_by_doing_plus_or_minus(array, current_index, current_sum):
        if current_index == len(array):
            all_ways.append(current_sum)
            return

        get_all_ways_by_doing_plus_or_minus(array, current_index+1, current_sum + array[current_index])
        get_all_ways_by_doing_plus_or_minus(array, current_index+1, current_sum - array[current_index])

    get_all_ways_by_doing_plus_or_minus(array, 0, 0)
    print(all_ways)

    count = 0
    for way in all_ways:
        if target == way:
            count += 1

    return count

print(result)
print(get_count_of_ways_to_target_by_doing_plus_or_minus(numbers, target_number))  # 5를 반환해야 합니다!