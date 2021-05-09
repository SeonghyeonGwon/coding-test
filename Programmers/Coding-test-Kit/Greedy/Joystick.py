def solution(name):
    answer = 0
    
    # 전체 String에서 A가 연속으로 제일 많은 범위를 찾는다
    # 그 범위를 피해가는 것과 지나칠 때의 이동 코스트를 비교해서 적은 쪽을 택한다
    count = 0
    max_count = 0
    max_index = 0
    result = 0
    
    for i in range(len(name)):
        if ord(name[i]) - ord('A') < ord('Z') - ord(name[i]) + 1:
            result += ord(name[i]) - ord('A')
        else:
            result += ord('Z') - ord(name[i]) + 1
        
        
        # A의 길이를 센다
        if name[i] == 'A':
            count += 1
        elif count > 0:
            count = 0
        
        # 가장 긴 A의 길이와 위치를 알아낸다
        if count > max_count:
            max_count = count
            max_index = i - max_count + 1
            
    # 첫 시작이 A이면서 제일 길 때는 뒤에서부터 길이를 세는 것이 제일 최적이다
    if max_index == 0 and name[0] == 'A':
        result += len(name) - max_count
        
    # 앞에서부터 A를 건너뛰어 가는 것이 좋거나 A가 아예 없는 경우 전체 길이를 세는 것이 최적이다
    elif (max_index - 1) * 2 > max_count or max_count == 0:
        result += len(name) - 1
        
        if max_count != 0:
            # 맨 끝에 A가 있는 경우 제외
            for i in range(len(name)):
                if name[len(name) - 1 - i] == 'A':
                    result -= 1
                else:
                    break
        
    # 건너뛰어 가는 것이 더 걸릴 경우에는 A에 도달하기 직전까지 왔다가 다시 되돌아가는 길이를 센다
    else:
        result += len(name) - 1 - max_count + max_index - 1
        
    return result