def solution(n, lost, reserve):
    # 차집합을 이용하여 원래부터 한 벌 밖에 없는 경우는 생각하지 않음
    reserve_n = set(reserve) - set(lost)
    lost_n = set(lost) - set(reserve)
    
    for i in reserve_n:
        # reserve의 한 원소를 기준으로 앞, 뒤 위치를 설정
        front = i - 1
        back = i + 1
        
        if front in lost_n:
            lost_n.remove(front)
        elif back in lost_n:
            lost_n.remove(back)
            
    return n - len(lost_n)