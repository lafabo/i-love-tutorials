h=int(input())
m=int(input())
s=int(input())

h_d = 360/12*h
m_d = 360/12/60*m
s_d = 360/12/60/60*s

angle = h_d + m_d + s_d
print(angle)