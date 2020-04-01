#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
import random
import string
import sys

ALPHABET = list(string.ascii_uppercase)

MP5_STUDENTS = ['Diana', 'Sara B', 'Anabel', 'Víctor', 'Sara D',
                'Estefanía', 'Lidia', 'Carlos', 'Fátima', 'Aqsa',
                'Carmen', 'Ángela', 'Nayely', 'Dani', 'Mehdi',
                'Natalia', 'Mireia', 'Marc', 'Jan', 'Rosi']

MP10_STUDENTS = ['Diana', 'Sara B', 'Anabel', 'Víctor', 'Sara D',
                 'Estefanía', 'Lidia', 'Carlos', 'Fátima', 'Aqsa',
                 'Carmen', 'Ángela', 'Nayely', 'Dani', 'Mehdi',
                 'Mireia', 'Marc', 'Jan', 'Rosi']

ASSIGN_TASK = True
ASSIGN_TURN = True
if len(sys.argv) == 3:
    if sys.argv[2].lower() == 'task':
        ASSIGN_TASK = True
        ASSIGN_TURN = False
    elif sys.argv[2].lower() == 'turn':
        ASSIGN_TASK = False
        ASSIGN_TURN = True
if len(sys.argv) == 4:
    if sys.argv[3].lower() == 'task':
        ASSIGN_TASK = True
        ASSIGN_TURN = False

TOTAL_OPTIONS_PER_TASK = 4
STUDENTS_PER_TURN_RATIO = 4

TOTAL_TASKS = 4
args_list = list(sys.argv)
for arg in args_list:
    if arg.isdigit():
        TOTAL_TASKS = int(arg)


"""
Get total of turns needed to distribute every student
according to the student per turn ratio
"""
def get_num_of_turns(students_list):
    total_students = len(students_list)
    
    return math.ceil(total_students / STUDENTS_PER_TURN_RATIO)


"""
Create a dict with number of turns
"""
def create_turns_dict(turns_num):
    turns_dict = {}
    i = 0
    while i < turns_num:
        turns_dict['Torn ' + str(i+1)] = []
        i += 1
    
    return turns_dict


"""
Assign every student to a turn
"""
def assign_students_to_list(original_students_list, turns_dict):
    students_list = original_students_list.copy()

    for turn in turns_dict:
        while len(turns_dict.get(turn)) < STUDENTS_PER_TURN_RATIO:
            if not students_list:
                break
            else:
                selected_student = random.choice(students_list)
                turns_dict.get(turn).append(selected_student)
                students_list.remove(selected_student)

    return turns_dict


"""
Create list of options
"""
def create_options_list():
    options_list = []
    i = 0
    while i < TOTAL_OPTIONS_PER_TASK:
        options_list.append('Opció ' + ALPHABET[i])
        i += 1

    return options_list


"""
Create dict of students with a randomly assigned options per task
"""
def distribute_tasks_between_students(options_list, *original_students_list, **students_dict):
    students_list = list(original_students_list)

    while students_list:
        for task in options_list:
            if not students_list:
                break
            else:
                selected_student = random.choice(students_list)

                if selected_student not in students_dict.keys():
                    students_dict[selected_student] = task
                else:
                    students_dict[selected_student] = students_dict.get(selected_student) + ', ' +\
                                                      task[0].lower() + task[1:]

                students_list.remove(selected_student)

    return students_dict


"""
Print result depending on settings
"""
def print_result(turns_dict, students_dict, students_list):
    print('')
    if turns_dict and students_dict:
        for turn in turns_dict:
            print(turn + ':')
            for student in turns_dict.get(turn):
                print('\t' + student + ': ' + students_dict.get(student))

    elif turns_dict:
        for turn in turns_dict:
            print(turn + ':')
            for student in turns_dict.get(turn):
                print('\t' + student)

    elif students_dict:
        for student in students_list:
            print('\t' + student + ": " + students_dict.get(student))
    
    print('')


if __name__ == "__main__":
    if sys.argv[1].lower() == 'mp5':
        students_list = MP5_STUDENTS
    if sys.argv[1].lower() == 'mp10':
        students_list = MP10_STUDENTS

    turns_dict = {}
    students_dict = {}

    if ASSIGN_TURN is True:
        turns_num = get_num_of_turns(students_list)
        turns_dict = create_turns_dict(turns_num)
        turns_dict = assign_students_to_list(students_list, turns_dict)

    if ASSIGN_TASK is True:
        options_list = create_options_list()
        task = 1
        while task <= TOTAL_TASKS:
            students_dict = distribute_tasks_between_students(options_list,
                                                              *students_list,
                                                              **students_dict)
            task += 1

    print_result(turns_dict, students_dict, students_list)
