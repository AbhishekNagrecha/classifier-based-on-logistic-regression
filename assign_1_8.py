import csv
import random
import math
import operator
import os
import numpy as np

basepath = 'C:/Users/Abhishek Nagrecha/Desktop/SEM1/PATTERN_RECOGNITION/Assign_2/dataset1/training_validation'
get_training = []
classes = {'0':[0,188],'1':[189,386],'2':[387,581],'3':[582,780],'4':[781,966],'5':[967,1153],'6':[1154,1348],
'7':[1349,1549],'8':[1550,1729],'9':[1730,1933]}

def get_values():

    for entry in os.listdir(basepath):
        ff = os.path.join(basepath, entry)
        if os.path.isfile(ff):
            with open(ff, 'r') as f:
                for line in f:
                    whole_array = []
                    for line_char in line:
                        whole_array.append(line_char)
                    whole_array.remove('\n')
                temporary = []
                temporary.append(whole_array)
                temporary.append(entry)

                find_training.append(temporary)







