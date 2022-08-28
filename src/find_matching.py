#!/usr/bin/env python3

def find_matching(L, pattern):
    temp = []
    for i, x in enumerate(L):
        if pattern in x:
            temp.append(i)
    
    return temp

def main():
     list = ["sensitive", "engine", "rubbish", "comment"]
     print(find_matching(list,'en'))

if __name__ == "__main__":
    main()
