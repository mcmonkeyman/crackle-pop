#!/usr/bin/env python3

def crackle_pop():
    c_pop_list = []
    for i in list(range(1, 100)):
        chosen = i 
        if (i%3 == 0 or i%5 == 0):
            chosen = ''
        if (i%3 == 0):
            chosen += 'Crackle'
        if (i%5 == 0):
            chosen += 'Pop'
        c_pop_list.append(chosen)
    return c_pop_list



if __name__ == '__main__':
    print('Running crackle_pop...')
    print(crackle_pop())
