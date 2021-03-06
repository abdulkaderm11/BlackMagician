"""
折纸问题
请把纸条竖着放在桌⼦上，然后从纸条的下边向上⽅对折，压出折痕后再展 开。此时有1条折痕，突起的⽅向指向纸条的背⾯，
这条折痕叫做“下”折痕 ；突起的⽅向指向纸条正⾯的折痕叫做“上”折痕。如果每次都从下边向上⽅ 对折，对折N次。
请从上到下计算出所有折痕的⽅向。
给定折的次数n,请返回从上到下的折痕的数组，若为下折痕则对应元素为"down",若为上折痕则为"up".
FULL BINARY TREE
n=1							down
n=2					down			up
n=3				down	up		down	up
"""

def fold(n, result, s):
	if n != 0:
		fold(n-1, result, "down")
		result.append(s)
		fold(n-1, result, "up")

if __name__ == "__main__":
	result = []
	num = 3
	fold(3, result, "down")
	print(result)