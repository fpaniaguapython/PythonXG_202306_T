class A:
    v = 2

class B(A):
    v = 1

class C(B):
    pass

o = C()
print(o.v)#1

print(A.v)#2
print(B.v)#1
print(C.v)#1