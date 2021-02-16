def solution(participant,completion):
    answer=''
    temp = 0
    dic = {}
    for part in participant:
        dic[hash(part)] = part
        temp += int(hash(part))
        print(hash(part))
        print(temp)
    for com in completion:
        temp -= hash(com)
    answer = dic[temp]

    return answer

p = ["mislav","stanko","mislav","ana"]
c = ["stanko","ana","mislav"]


print(solution(p,c))
