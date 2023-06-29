'''
import math
import random

result_1=math.pow(2,4)
print("result_1 is", result_1)

result_2 = math.sqrt(16)
print("result_2 is", result_2)

result_3 = random.randint(0,100)
print("result_3 is", result_3)

names = ["Amaryllis", "Godson", "Emily", "Reina", "Derin", "Elena", "Inacio"]
print("Original names: ",names)

random.shuffle(names)
print("Names after shuffling: ",names)

result_4 = random.choice(names)
print("Chosen name is: ",result_4)
'''
'''
from math import pow,sqrt
from random import randint,shuffle,choice
result_1=pow(2,4)
print("result_1 is", result_1)

result_2 = sqrt(16)
print("result_2 is", result_2)

result_3 = randint(0,100)
print("result_3 is", result_3)

names = ["Amaryllis", "Godson", "Emily", "Reina", "Derin", "Elena", "Inacio"]
print("Original names: ",names)

shuffle(names)
print("Names after shuffling: ",names)

choice(names)
print("Chosen name is: ",result_4)
'''
'''
import math as mathematics
import random as misc

result_1=mathematics.pow(2,4)
print("result_1 is", result_1)

result_2 = mathematics.sqrt(16)
print("result_2 is", result_2)

result_3 = misc.randint(0,100)
print("result_3 is", result_3)

names = ["Amaryllis", "Godson", "Emily", "Reina", "Derin", "Elena", "Inacio"]
print("Original names: ",names)

misc.shuffle(names)
print("Names after shuffling: ",names)

result_4 = misc.choice(names)
print("Chosen name is: ",result_4)
'''
'''
from math import pow as power
from math import sqrt as square_root
from random import randint as randnum
from random import shuffle as shuf
from random import choice as choose

result_1=power(2,4)
print("result_1 is", result_1)

result_2 = square_root(16)
print("result_2 is", result_2)

result_3 = randnum(0,100)
print("result_3 is", result_3)

names = ["Amaryllis", "Godson", "Emily", "Reina", "Derin", "Elena", "Inacio"]
print("Original names: ",names)

shuf(names)
print("Names after shuffling: ",names)

result_4 = choose(names)
print("Chosen name is: ",result_4)
'''