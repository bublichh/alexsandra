# def counter(s):
#     for i in s:
#         count = 0
#         for j in s:
#             if i == j:
#                 count+=1
#         print(i, count)


# def counter(s): #0(N*M)
#     for i in set(s):
#         count = 0
#         for g in s:
#             if i == g:
#                 count+=1
#         print(i,count)


def counter(s):
    syms = {}
    for i in s:
        syms[i] = syms.get(i,0) + 1
    for i, count in syms.items():
        print(i,count)

counter('avvbcd')