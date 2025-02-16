# testTypes.p
# This program tests 5 types of variables
# author: Niamh Hogan

# int
i = 3

# float
fl = 3.5

# boolean
isa = True

# str 
memo = 'how now Brown Cow'

# list
lots = []

print(type(i))
print(type(fl))
print(type(isa))
print(type(memo))
print(type(lots))

print('Variable {} is of type:{} and value:{}'.format('i', type(i), i))
print('Variable {} is of type:{} and value:{}'.format('fl', type(fl), fl))
print('Variable {} is of type:{} and value:{}'.format('is', type(isa), isa))
print('Variable {} is of type:{} and value:{}'.format('memo', type(memo), memo))
print('Variable {} is of type:{} and value:{}'.format('lots', type(lots), lots))