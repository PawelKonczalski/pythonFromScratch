'''
whether:   el. unique  |  order | change of specific item | new items
lists           NO         YES             YES                 YES
krotki          NO         YES             NO                  NO
dictionaries    YES        NO              YES                 YES
sets            YES        NO              NO                  YES

         COLLECTIONS: BONUS in the form of   &   -   ^
'''

A = {1, 4, 20, -4, 20}
B = {2, 1, 25, 40, 20}
C = {20, -4}

A.discard(4)

print(A)
print(A&B)
print(A|B)
print(A-B)
print(A^B)

print(C.issubset(A))
