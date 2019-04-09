import re

def Signaficance(number):
    '''significant figs of the input digit string'''
    integral, _, fractional = number.partition(".") # before decimal , decimal , after decimal

    if fractional: #if there is a decimal
        return len((integral + fractional).lstrip('0')) #return length of number without decimal and leading 0's
    else:
        return len(integral.strip('0')) #return number with no trailing 0's

if __name__ == '__MAIN__':
    print(Signaficance(50))
    print(Signaficance(.00341))
