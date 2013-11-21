from random import randint
system_num=randint(1, 100)
print "Guess What!!"
type_num=input()
while system_num != type_num:
    if system_num > type_num:
        print "%d is too small" %type_num
        type_num=input()
    else :
        print "%d is too large" %type_num
        type_num=input()
print "Bingo!!! %d is right!!" %type_num
