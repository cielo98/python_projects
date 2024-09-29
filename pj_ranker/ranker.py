#내 코드
scores = {"John": 85, "Jane": 92, "Dav": 78}
def answer_rank() :
    name = input("순위를 알고 싶은 학생의 이름을 입력하세요. : ")
    rank = dict(sorted(scores.items(), key=lambda x: x[1], reverse=True))
    if name in rank :
        name_score = rank[f"{name}"]
        name_rank = list(rank.keys()).index(f"{name}")
        print(f"{name}의 점수는 {name_score}이고 순위는 {name_rank + 1}입니다.")
        return
    else :
        print("올바른 이름을 입력해주세요.")
        return answer_rank()
answer_rank()

# 개선 코드
scores = {"John": 85, "Jane": 92, "Dav": 78}

def answer_rank():
    while True:
        name = input("순위를 알고 싶은 학생의 이름을 입력하세요. : ").strip().capitalize()
        rank = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        if any(name == student[0] for student in rank):
            for i, (student_name, student_score) in enumerate(rank):
                if student_name == name:
                    print(f"{name}의 점수는 {student_score}이고 순위는 {i + 1}입니다.")
                    return  
        else:
            print("올바른 이름을 입력해주세요.")  
answer_rank()

# break: 현재 실행 중인 루프(예: for, while)만 종료합니다. 루프를 빠져나온 후, 함수가 더 실행할 코드가 있으면 그 코드가 계속 실행됩니다.
# return: 함수 전체를 종료합니다. return을 만나면 함수가 즉시 끝나고, 함수 아래의 코드는 실행되지 않습니다.

