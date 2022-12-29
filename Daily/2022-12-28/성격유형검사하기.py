from collections import defaultdict

def solution1(survey, choices):
    
    score = defaultdict(int)
    for s, c in zip(survey, choices):
        if c < 4:
            score[s[0]] += 4-c
        elif c > 4 : 
            score[s[1]] += c-4
    
    # 결론
    answer = ''
    if score['T'] >= score['R']:
        answer += 'T'
    else:
        answer += 'R'
        
    if score['C'] >= score['F']:
        answer += 'C'
    else:
        answer += 'F'
        
    if score['J'] >= score['M']:
        answer += 'J'
    else:
        answer += 'M'
        
    if score['A'] >= score['N']:
        answer += 'A'
    else:
        answer += 'N'
        
        
    return answer

def solution2(survey, choices):
    answer = ''
    dicts = {'T' : 0, 'R' : 0, 'C' : 0, 'F' : 0, 'J' : 0, 'M' : 0, 'A' : 0, 'N' : 0}
    for i in range(len(survey)) : 
        if choices[i] - 4 < 0: # choices 값이 4 미만일 시, survey의 앞의 값 출력
            dicts[survey[i][0]] += 4 - choices[i]

        elif choices[i] - 4 > 0: # choices 값이 4 초과 시, survey의 앞의 값 출력
            dicts[survey[i][1]] += choices[i] - 4

    answer += 'R' if dicts['R'] >= dicts['T'] else 'T'
    answer += 'C' if dicts['C'] >= dicts['F'] else 'F'
    answer += 'J' if dicts['J'] >= dicts['M'] else 'M'
    answer += 'A' if dicts['A'] >= dicts['N'] else 'N'

    return answer

if __name__ == "__main__":
    import random

    for _ in range(100):
        survey = []
        choices = []
        for i in range(10):
            survey.append(random.choice(['TR','RT','CF','FC','JM','MJ','AN','NA']))
            choices.append(random.randint(1, 7))
        assert solution1(survey, choices) == solution2(survey, choices), f"{survey}, {choices}, {solution1(survey, choices)}, {solution2(survey, choices)}"