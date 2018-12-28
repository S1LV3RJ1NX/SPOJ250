# https://www.spoj.com/problems/ACPC10A/

while True:
	x,y,z = map(int, input().split(' '))
	
	if x==y==z== 0:
		break
	else:
		if y-x == z-y:
			print("AP",z+(z-y))
		else:
			print("GP",z*(z//y))
