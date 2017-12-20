import sys
from functions import *
from node import *


if __name__ == '__main__':
    print "Program Started:\t"
    loop=True

    while(loop):
        write = raw_input("Enter Input Please !\t")
        query = get_input(write)

        if len(query['class']) > 0 and len(query['attr']) > 0 and query['attr'] != 'none':
            f_n = 'classes/' + query['class'] + '.txt'
            input = query['attr']

        elif len(query['class']) > 0 and len(query['attr']) == 0:
            f_n = 'classes/' + query['class'] + '.txt'
            input = ''

        elif len(query['class']) > 0 and query['attr'] == 'none':
            f_n = 'ide.txt'
            input = query['class']

        elif len(query['class']) == 0:
            f_n = 'ide.txt'
            input = ''

        try : root = fileparse(f_n)
        except:
            print 'Not found!'
            continue

        if write=="end":
            loop=False
            print "system closed!"

        else:
            root.search(input)

