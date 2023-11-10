# In one city, bus tickets use numbers from 100000 to 999999. Your task is to find the number of lucky tickets between two input tickets' values.
# The ticket is considered to be lucky if the sum of first 3 digits equals to the sum of last 3 digits:
# 123321 is lucky, i.e. 1+2+3 equals to 3+2+1
# 123444 is not lucky, i.e. 1+2+3 doesn't equal to 4+4+4


def lucky_number(ticket):
    status='lucky'

    ticket_str=str(ticket)
    digit_list=[int(digit) for digit in ticket_str]

    if sum(digit_list[:3])!=sum(digit_list[3:]):
        status=' not lucky'

    return status

print(lucky_number(123123))