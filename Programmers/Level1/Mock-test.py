def solution(answers):
    answer = []
    counts = [0,0,0]
    
    stu1 = [1,2,3,4,5]
    stu2 = [2,1,2,3,2,4,2,5]
    stu3 = [3,3,1,1,2,2,4,4,5,5]

    for i in range(len(answers)):
        if answers[i] == stu1[i % len(stu1)]:
            counts[0] += 1
        if answers[i] == stu2[i % len(stu2)]:
            counts[1] += 1
        if answers[i] == stu3[i % len(stu3)]:
            counts[2] += 1
            
    maxValue = max(counts)
    for i in range(len(counts)):
        if counts[i] == maxValue:
            answer.append(i+1)
    
    return answer