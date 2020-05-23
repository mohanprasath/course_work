#!/usr/bin/env python3

def square(num):
	return num ** 2

def triple(num):
	return num * 3

def main():
    for i in range(1, 11):
    	sq_val = square(i)
    	tp_val = triple(i)
    	if tp_val < sq_val:
    		break
    	else:
    		print("triple(" + str(i) + ")==" + str(tp_val) + " square("+ str(i) + ")==" + str(sq_val))

if __name__ == "__main__":
    main()
