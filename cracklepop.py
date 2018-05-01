#!/usr/bin/env python3

def crackle_pop():
    c_pop_list = []
    for i in list(range(1, 100)):
        toPrint = i 
        if (i%3 == 0 or i%5 == 0):
            toPrint = ''
        if (i%3 == 0):
            toPrint += 'Crackle'
        if (i%5 == 0):
            toPrint += 'Pop'
        c_pop_list.append(toPrint)
    return c_pop_list



if __name__ == '__main__':
    print('Running crackle_pop...')
    print(crackle_pop())
