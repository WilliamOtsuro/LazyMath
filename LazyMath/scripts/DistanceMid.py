import os
from math import *
import time
from resources import Banner

def distance_formula(x_one, x_two, y_one, y_two):
	# The Real Formula Is: PQ = sqrt{(x2-x1)^2 + (y2 - y1)^2}
	value_x = x_two - x_one
	value_y = y_two - y_one
	value_x = pow(value_x, 2)
	value_y = pow(value_y, 2)
	value_xy = value_x + value_y
	answer = sqrt(value_xy)
	print(f"[!] The Distance Would Be: {str(answer)}")

def midpoint_formula(x_one, x_two, y_one, y_two):
	# The Real Formula Is: M = ( x1 + x2 /2   y1 + y2 /2 )
	value_x = x_one + x_two
	value_y = y_one + y_two
	ans_x = value_x / 2
	ans_y = value_y / 2
	print(f"[!] The Midpoint Would Be: ({str(ans_x)}, {str(ans_y)})")

def main():
	Banner.logo()
	print("SERIES: DISTANCE AND MIDPOINT")
	x_one = input("[*] Input The Value Of x1 or x sub 1: ")
	x_two = input("[*] Input The Value Of x2 or x sub 2: ")
	y_one = input("[*] Input The Value Of y1 or y sub 1: ")
	y_two = input("[*] Input The Value Of y2 or y sub 2: ")
	print("[*] Computing... Please Wait.")
	time.sleep(2.0)
	os.system("cls")
	distance_formula(int(x_one), int(x_two), int(y_one), int(y_two))
	midpoint_formula(int(x_one), int(x_two), int(y_one), int(y_two))

if __name__ == "__main__":
	main()