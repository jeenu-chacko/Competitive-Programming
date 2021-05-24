from math import atan,degrees
degree_sign= u'\N{DEGREE SIGN}'
AB=int(input())
BC=int(input())
print(str(round(degrees(atan(AB/BC))))+degree_sign)
