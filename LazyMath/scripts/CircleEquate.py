from math import *
import time
from resources import Banner
import os
import sys

def equation_origin(r):
	# Formula Is r^2 = x^2 + y^2
	radius = pow(int(r), 2)
	print(f"[!] Equation Is : {int(radius)} = x^2 + y^2 ")

def equation_standard(h, k, r):
	# Formula Is ( x - h )^2 + ( y - k )^2 = r^2
	radius = pow(int(r), 2)
	print(f"[!] Equation Is : ( x - ({int(h)}) )^2 + (y - ({int(k)}) )^2 = {int(radius)} ")
	h = int(h) * int(-1)
	k = int(k) * int(-1)
	print(f"[!] Where: h = {int(h)}, k = {int(k)} and r = {int(r)}^2 or r = {int(radius)} ")
		

def equation_general(h, k, r,):
	# Formula Is x^2 + y^2 + Dx + Ey + F = 0 Note: This Equation Can Only Be Obtain By Expanding Standard Equation
	x_1 = int(h) + int(h)
	x_2 = pow(int(h), 2)
	y_1 = int(k) + int(k)
	y_2 = pow(int(k), 2)
	radius = pow(int(r), 2)
	xy = int(x_2) + int(y_2)
	xy = xy - radius
	radius = radius - radius
	print(f"[!] Equation Is: x^2 + y^2 + ({int(x_1)})x + ({int(y_1)})y + ({int(xy)}) = {int(radius)} ")
	print(f"[!] Where: D = {int(x_1)}, E = {int(y_1)} and F = {int(xy)} ")

def equation_conversion(d, e, f):
	# No Formula Here But The Idea Goes Like This
	# x^2 + y^2 + Dx + Ey + F = 0
	# x^2 + y^2 + Dx + Ey + F - F = 0 - F
	# (x^2 + Dx) + (y^2 + Ey) = F
	# (x^2 + Dx + ?) + (y^2 + Ey + ?) = F
	# Formula To Get Constant Of (xN) and (yN): C = ( b/2 )^2 | where b is D in Dx
	# (sqrt{x^2} + Dx + sqrt{xN}) + (sqrt{y^2} + Ey + sqrt{yN}) = F
	# To Get The Operation To Use Copy The Operation Used In Dx
	# (x + xN)^2 + (y + yN)^2 = sqrt{F}
	# (x + xN)^2 + (y + yN)^2 = F^2
	d = int(d) / 2
	e = int(e) / 2
	xn = pow(int(d), 2)
	yn = pow(int(e), 2)
	f = int(f) * int(-1)
	r = int(f) + int(xn) + int(yn)
	r = sqrt(int(r))
	print(f"[!] Equation Is: ( x + ({int(d)}) )^2 + ( y + ({int(e)}) )^2 = {int(r)}^2 ")
	d = int(d) * int(-1)
	e = int(e) * int(-1)
	print(f"[!] Where Final Is: ({int(d)}, {int(e)}) r = {int(r)} ")

def main():
	os.system("cls")
	Banner.logo()
	print("SERIES: CIRCLE EQUATIONS")
	print("Available Equations: ")
	print(" 1 - Origin Equation ")
	print(" 2 - Standard Equation ")
	print(" 3 - General Equation ")
	print(" 4 - Conversion Equation (From General Equation To Standard Equation) ")
	function_use = input("[+] Input The Equation To Be Used( 1 - 4 ): ")
	if function_use == "1":
		os.system("cls")
		r = input("[+] What Is The Radius (r): ")
		print("[*] Computing...")
		time.sleep(2.0)
		os.system("cls")
		equation_origin(r) 
	if function_use == "2":
		os.system("cls")
		r = input("[+] What Is The Radius (r): ")
		h = input("[+] What Is The Horizontal (h): ")
		k = input("[+] What Is The Vertical (k): ")
		print("[*] Computing...")
		time.sleep(2.0)
		os.system("cls")
		equation_standard(h, k, r,)
	if function_use == "3":
		os.system("cls")
		print("[!] Please Do Make Sure You Had First Do The Standard Equation Or Else You Will Get An Error Or Wrong Answer.")
		print("[!] Note: Before You Type On Radius Make Sure It Is On Square Root Form Like (5^2) And When Typing It Please Don't Include The Exponent Like (type 5 only no need to include ^2) ")
		r = input("[+] What Is The Radius (r): ")
		h = input("[+] What Is The Horizontal (h): ")
		k = input("[+] What Is The Vertical (k): ")
		print("[*] Computing...")
		time.sleep(2.0)
		os.system("cls")
		equation_general(h, k, r)
	
	if function_use == "4":
		os.system("cls")
		d = input("[+] What Is The Constant Of x (D): ")
		e = input("[+] What Is The Constant Of y (E): ")
		f = input("[+] What Is The Constant (F): ")
		print("[*] Computing...")
		time.sleep(2.0)
		os.system("cls")
		equation_conversion(d, e, f)
	
	else:
		pass
	

if __name__ == "__main__":
	main()