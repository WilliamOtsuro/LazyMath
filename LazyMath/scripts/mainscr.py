import os

def goto_CircleEquate():
	os.system("cls")
	os.system("python CircleEquate.py")

def goto_DistanceMid():
	os.system("cls")
	os.system("python DistanceMid.py")

def main():
	print("[*] Equations Options: ")
	print(" ~ 1 - Equations On Distance And Midpoints ")
	print(" ~ 2 -  Equations On Circles ")
	goto_Destination = input("[+] Choose An Equation (1 - 2): ")
	if goto_Destination == "1":
		goto_DistanceMid()
	if goto_Destination == "2":
		goto_CircleEquate()

if __name__ == "__main__":
	main()