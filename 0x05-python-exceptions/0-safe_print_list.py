#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        squad=0
        for i in my_list:
            if squad<0:
                print(i,end=' ')
                squad+=1
            else:
                break
        print()
        return squad
    except:
        return squad

