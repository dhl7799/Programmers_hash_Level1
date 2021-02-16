import collections

def solution(participant, completion):
    answer = collections.Counter(participant)-collections.Counter(completion)
    return list(answer.keys())[0]

p = ["mislav","stanko","mislav","ana"]
c = ["stanko","ana","mislav"]


print(solution(p,c))
