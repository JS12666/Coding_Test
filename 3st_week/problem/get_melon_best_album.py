# 1. 속한 노래가 많이 재생된 장르를 먼저 수록한다.
# -> genre_array 에서 genre 별로 재생횟수를 모두 모아서 비교해준다. 그리고 가장 많이 재생된 장르 별로 노래를 2곡씩 넣어줄거다.
# -> class_count 장르 변수 사용?-> 어떤 장르가 올지 모르기 때문에 안됨
# 특정 키 값(장르) 에 대해서 value(재생횟수)를 모아서 합쳐주고 싶다. -> 딕셔너리
# dict = {"classic" : 650, "pop" : ... , ...}

# 2. 장르 내에서 많이 재생된 노래를 먼저 수록한다.
# -> 많이 재생된 장르 별로 2 곡을 넣어줄 때, 많이 재생된 노래보다 먼저 넣어줘야 한다.
# dict2 = {"classic" : [(0, 500), (2, 150), ... ], "pop" : [(...)] }

def get_melon_best_album(genre_array, play_array):
    # 구현해보세요!
    n = len(genre_array)
    genre_total_play_dict = {}
    genre_index_play_array_dict = {}
    for i in range(n):
        genre = genre_array[i]
        play = play_array[i]

        if genre in genre_total_play_dict:
            genre_total_play_dict[genre] += play
            genre_index_play_array_dict[genre].append([i, play])
        else :
            genre_total_play_dict[genre] = play
            genre_index_play_array_dict[genre] = [[i, play]]

    # 장르별로 가장 재생횟수가 많은 장르들 중, 곡 수가 많은 순서대로 2개씩 출력하기
    sorted_genre_play_array = sorted(genre_total_play_dict.items(), key=lambda item: item[1], reverse=True)
    result = []
    for genre, total_play in sorted_genre_play_array:
        sorted_genre_index_play_array = sorted(genre_index_play_array_dict[genre], key=lambda item: item[1], reverse=True)

        genre_song_count = 0
        for index, play in sorted_genre_index_play_array:
            if genre_song_count >= 2:
                break
            result.append(index)
            genre_song_count += 1

    return result


print("정답 = [4, 1, 3, 0] / 현재 풀이 값 = ", get_melon_best_album(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))
print("정답 = [0, 6, 5, 2, 4, 1] / 현재 풀이 값 = ", get_melon_best_album(["hiphop", "classic", "pop", "classic", "classic", "pop", "hiphop"], [2000, 500, 600, 150, 800, 2500, 2000]))