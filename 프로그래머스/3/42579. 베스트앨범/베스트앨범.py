def solution(genres, plays):
    answer = []
    
    # 장르별 재생 횟수 
    genre_play_cnt = {}
    for genre, play in zip(genres, plays):
        if genre in genre_play_cnt:
            genre_play_cnt[genre] += play
        else:
            genre_play_cnt[genre] = play
    
    # 장르별 곡 정보
    genre_songs = {}
    
    for i, (genre, play) in enumerate(zip(genres, plays)):
        if genre in genre_songs:
            genre_songs[genre].append((play, i))
        else:
            genre_songs[genre] = [(play, i)]
    
    # 장르별 총 재생횟수 기준으로 장르 정렬
    sorted_genres = sorted(genre_play_cnt.keys(), key=lambda x: genre_play_cnt[x], reverse=True)
    
    # 각 장르마다 노래를 선택
    for genre in sorted_genres:
        # 해당 장르의 노래들을 재생 횟수로 정렬 
        songs = sorted(genre_songs[genre], key=lambda x: (-x[0], x[1]))
        
        # 장르별로 최대 2곡까지 선택
        for i in range(min(2, len(songs))):
            answer.append(songs[i][1])  
    
    return answer