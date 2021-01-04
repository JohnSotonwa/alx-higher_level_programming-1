#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    cmpt = 0
    for index in range(x):
        try:
            print('{:d}'.format(my_list[index]), end='')
        except IndexError:
            break
        except Exception:
            pass
        else:
            cmpt += 1

    print('')
    return cmpt
