a = [{"Name" : "Heewon", "Age" : 26, "Company" : "Fastcampus", "Skills" : ["Python", "Data Analysis"]}, {"Name" : "Heejin", "Age" : 24, "Company" : "Hyangachi", "Skills" : "Videography"}, {"Name" : "Chulsik", "Age" : 60, "Company" : "Kia Motors", "Skills" : "Sales"}]
b = a[1]
print(a[1]["Name"])
b.keys()
b.get('Name')
"Name" in b
b.items()

#dict의 키 값으로 값 수정 가능한 객체는 사용할 수 없음 (리스트, 딕셔너리 등) values로는 사용 가능
c = {'x': 10, 'y': 20}
c['z'] = 30 # c 딕셔너리의 'z' 값은 30이다. dict에서는 index 사용 안 하고 키 값으로 찾음.
len(c)

#-----------------------------------------------
my_dict = {'a': 1, 'b': 2, 'c': 3}
def find_key_by_value(my_dict, target_value):
    for key, value in my_dict.items():
        if value == target_value:
            return key
    return None
result = find_key_by_value(my_dict, 2)
print(result)
my_set = {3, 6, 9}
your_set = {2, 4, 8}
my_set.remove(9)
print(my_set & your_set)
len(my_dict)

my_dict['a']
my_dict.get('b')

# 세트에서 교집합은 &(intersection), 합집합은 |(union), 차집합은 - (difference) 
a = {1, 2, 3, 4}
a.remove(3)

b = {1, 2, 3}
c = {2, 3, 4}
b & c
b.intersection(c)

b = {10, 20, 30}
b.add(40)
b
b.update({70, 80, 90})
b = list(b)
b.sort()
b

# 리스트 [1, 2, 2, 3, 4, 4, 5]에서 중복된 요소를 제거하고 집합으로 변환한 후, 그 집합을 오름차순으로 정렬하여 출력하는 코드를 작성하시오.
a = [1, 2, 2, 3, 4, 4, 5]
a = set(a)
a = list(a)
a.sort()
print(a)

# 두 개의 리스트 [1, 2, 3, 4]와 [3, 4, 5, 6]을 각각 집합으로 변환한 후, 두 집합의 대칭 차집합을 계산하여 출력하는 코드를 작성하시오.
a = [1, 2, 3, 4]
a = set(a)
b = [3, 4, 5, 6]
b = set(b)
c = list(a - b) + list(b - a)
set(c)
c = list(a.difference(b)) + list(b.difference(a))
set(c)

# 주어진 딕셔너리 {'a': 10, 'b': 25, 'c': 7, 'd': 30}에서 값이 10 이상인 키만 추출하여 새로운 리스트를 생성하는 코드를 작성하시오.
# 키와 값 동시에 가져오려면 d.items()
my_dict = {'a': 10, 'b': 25, 'c': 7, 'd': 30}
result = [key for key, value in my_dict.items() if value >= 10] # 리스트 컴프리헨샨!!
print(result)

''' 리스트 컴프리헨션 :  [반복 실행문 for 변수 in 순회 가능 객체(list, set, range() 등) +if문, for 사용 가능]
    딕셔너리 컴프리헨션 : { 키 : 값 for 표현식 in 순회 가능 객체(list, set, range() 등) +if문, for 사용 가능}
    세트 컴프리헨션 : { 반복 실행문 for 표현식 in 순회 가능 객체(list, set, range() 등 +if문, for 사용 가능} '''

# 학생들의 성적을 딕셔너리로 저장하고, 평균 점수를 계산하여 출력하는 프로그램을 작성하시오. 예를 들어, {'John': 85, 'Jane': 92, 'Dave': 78}이라는 데이터가 주어지면, 이 학생 들의 평균 점수를 출력하시오.
scores = {'John': 85, 'Jane': 92, 'Dave': 78}
scores.values()
scores_values = list(scores.values())

def avg() :
    total = 0
    for i in scores_values :
        total = total + i
    return(total/len(scores_values))
print(avg())

# 사용자로부터 문자열을 입력받아, 각 단어의 빈도를 딕셔너리로 계산한 후, 빈도수가 높은 순서대로 단어를 출력하는 코드를 작성하시오.
string = input("문자열을 입력하세요. : ")
words = list(sorted(string.split())) # sorted로 별도의 리스트 생성
wordcount = {i : words.count(i) for i in words} # 리스트 컴프리헨션으로 dict 생성
print(sorted(wordcount.items(), key=lambda x: x[1], reverse=True))
# sorted 쓰면 바로 print 가능, 별도의 리스트 생성
# sorted()에서 딕셔너리일 경우 items()로 먼저 출력. dict 날 것으로는 순서 출력 불가능. 
# sorted(key=lambda x:x[(정렬 기준 자리)])


#문제24) 주어진 리스트 [('a', 1), ('b', 2), ('c', 3), ('a', 4)]를 딕셔너리로 변환하되, 키가 중복될 경우 값들을 리스트로 묶어서 저장하는 코드를 작성하시오. 예를 들어, 출력 결과는 {'a': [1, 4], 'b': 2, 'c': 3}과 같이 됩니다.
my_list = [('a', 1), ('b', 2), ('c', 3), ('a', 4)]
result = {}
for key, value in my_list :
    if key in result :
        if not isinstance(result[key], list):
            result[key] = [result[key]]
            result.append(result[key])
    else : 
        result[key] = value
print(result)