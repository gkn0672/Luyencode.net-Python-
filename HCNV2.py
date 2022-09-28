hcn1 = [int(i) for i in input().split()]
hcn2 = [int(i) for i in input().split()]
hcn = []

width = abs(hcn1[0] - hcn1[2]) + abs(hcn2[0] - hcn2[2]) - (max(hcn1[0], hcn1[2], hcn2[0], hcn2[2]) - min(hcn1[0], hcn1[2], hcn2[0], hcn2[2])) 
height = abs(hcn1[1] - hcn1[3]) + abs(hcn2[1] - hcn2[3]) - (max(hcn1[1], hcn1[3], hcn2[1], hcn2[3]) - min(hcn1[1], hcn1[3], hcn2[1], hcn2[3])) 
if((width <= 0) or (height <=0)):
    print(0)
else:
    print(width * height)

