#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
import random
import sys

ASSIGN_TASK = True
ASSIGN_TURN = True
if len(sys.argv) == 3:
    if sys.argv[2].lower() == 'task':
        ASSIGN_TASK = True
        ASSIGN_TURN = False
    if sys.argv[2].lower() == 'turn':
        ASSIGN_TASK = False
        ASSIGN_TURN = True
if len(sys.argv) == 4:
    if sys.argv[3].lower() == 'task':
        ASSIGN_TASK = True
    if sys.argv[3].lower() == 'turn':
        ASSIGN_TURN = True


TOTAL_TASKS = 4
STUDENTS_PER_TURN_RATIO = 4

MP5_STUDENTS = ['Diana', 'Sara B', 'Anabel', 'Víctor', 'Sara D',
                'Estefanía', 'Lidia', 'Carlos', 'Fátima', 'Aqsa',
                'Carmen', 'Ángela', 'Nayely', 'Dani', 'Mehdi',
                'Natalia', 'Mireia', 'Marc', 'Jan', 'Rosi']

MP10_STUDENTS = ['Diana', 'Sara B', 'Anabel', 'Víctor', 'Sara D',
                 'Estefanía', 'Lidia', 'Carlos', 'Fátima', 'Aqsa',
                 'Carmen', 'Ángela', 'Nayely', 'Dani', 'Mehdi',
                 'Mireia', 'Marc', 'Jan', 'Rosi']


"""
Get total of turns needed to distribute every student
according to the student per turn ratio
"""
def get_num_of_turns(students_list):
    total_stundets = len(students_list)
    
    return math.ceil(total_stundets / STUDENTS_PER_TURN_RATIO)


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
Create list of tasks
"""
def create_tasks_list():
    tasks_list = []
    i = 0
    while i < TOTAL_TASKS:
        tasks_list.append('Tasca ' + str(i+1))
        i += 1

    return tasks_list


"""
Create dict of students with a randomly assigned task
"""
def distribute_tasks_between_students(task_list, original_students_list):
    students_list = original_students_list.copy()
    students_dict = {}

    while students_list:
        for task in task_list:
            if not students_list:
                break
            else:
                selected_student = random.choice(students_list)
                students_dict[selected_student] = task
                students_list.remove(selected_student)

    return students_dict


"""
Print result depending on options
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
        task_list = create_tasks_list()
        students_dict = distribute_tasks_between_students(task_list, students_list)

    print_result(turns_dict, students_dict, students_list)
