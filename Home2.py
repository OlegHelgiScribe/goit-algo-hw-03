import random

def get_numbers_ticket(min,max,quantity):
    if min<1 or max>50 or max<min or quantity not in range(min,max):
        return 'Error'
    gnlist=[]
    while(len(gnlist)<quantity):
        a = random.randint(min,max)
        if a not in gnlist:
            gnlist.append(a)
    gnlist.sort()
    return gnlist

lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)