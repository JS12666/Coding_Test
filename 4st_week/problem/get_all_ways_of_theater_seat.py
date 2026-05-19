seat_count = 9
vip_seat_array = [4, 7]

#123 4 56 7 89
#123 56 89

# n 번째 티켓을 가진 사람이 앉을 수 있는 방법
# 1. n 번째 좌석에 앉기
# -> 좌석은 n - 1개가 남아있고, 사람도 n -1 번째 티켓까지 가진 사람이 있는 상황
# 2. n - 1번째 좌석에 앉기
# -> n-1번째 티켓을 가진 사람은 n번째 좌석에 앉아야함
# 좌석은 N -2 개가 남아있고, 사람도 n-2 번째 티켓까지 가진 사람이 있는 상황
# => F(N) : N 명의 사람들을 좌석에 배치하는 방법
# F(N) = F(N-1) + F(N-2)

memo = {
    1: 1,
    2: 2
}

def get_all_ways_of_theater_seat(total_count, fixed_seat_array):
    all_ways =  1
    current_index = 0

    for fixed_seat in fixed_seat_array:
        fixed_seat_index = fixed_seat - 1
        count_of_ways = fibo_dynamic_programming(fixed_seat_index - current_index, memo)
        all_ways *= count_of_ways
        current_index = fixed_seat_index + 1

    fibo_dynamic_programming(total_count - current_index, memo)
    all_ways *= count_of_ways

    return all_ways


def fibo_dynamic_programming(n, fibo_memo):
    if n in fibo_memo:
        return  fibo_memo[n]

    nth_fibo = fibo_dynamic_programming(n - 1, fibo_memo) + fibo_dynamic_programming(n - 2, fibo_memo)
    fibo_memo[n] = nth_fibo

    return nth_fibo

# 12가 출력되어야 합니다!
print(get_all_ways_of_theater_seat(seat_count, vip_seat_array))