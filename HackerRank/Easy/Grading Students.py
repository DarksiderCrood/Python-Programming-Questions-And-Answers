import math
import os
import random
import re
import sys

def gradingStudents(grades):
    # Write your code here
    l = []
    for x in grades:
        l.append( x-x%5+5 if x%5>2 and x>=38 else x)
    return l

if __name__ == '__main__':
    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    print(result)
