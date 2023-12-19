# 자료형의 참/거짓
# "python"  참
# ""        거짓
# [1,2,3]   참
# []        거짓
# ()        거짓
# {}        거짓
# 1         참
# 0         거짓
# None      거짓

a = [1,2,3,4]
while a:
    a.pop()
    print(a)

# 변수
from copy import copy
# 메모리가 실제로 값을 저장하는 곳
a = [1,2,3]
b = a
# a를 처음부터 끝까지 슬라이싱해서 새로운값 넣어줌
c = a[:]
# copy 사용해서 주소공유 X 값 복사
d = copy(a)
a[1] = 4
# 두개가 같은 주소를 바로보는지 확인
# print(a is b)
print(a)
print(b)
print(c)
print(d)