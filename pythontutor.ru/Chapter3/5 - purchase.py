a=int(input())
b=int(input())
n=int(input())

cost = (n*(a+b*0.01))

cost_r = int(cost)
cost_c = int(round((cost - cost_r), 2) * 100)

print(cost_r, cost_c)