# def values():
#     l=[1,2,3,4,5]
#     for x in l:
#         yield x
#
# # print((values()))
#
# for i in values():
#     print(i)
#
# l=[1,2,3,4]
# a=(x for x in l)

def fib(max):
    a,b=0,1
    while True:
        c=a+b
        if c<max:
            yield c
            a=b
            b=c
        else:
            break

f=fib(10)
print(f)
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
