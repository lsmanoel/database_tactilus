import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Python program to convert a list 
# of character 
  
def list2string(s): 
  
    # initialization of string to "" 
    new = "" 
  
    # traverse in the string  
    for x in s: 
        new += x  
  
    # return string  
    return new 

def string_list2np(string_list):   
    string_buffer = ""
    char_list = []
    matrix_np = np.ones(32*32)
    matrix_np_index = 0

    for i, line in enumerate(string_list):
        for j, cell in enumerate(line):
            if cell == '\\':
                string_buffer = list2string(char_list)
                if string_buffer != "":
                    matrix_np[matrix_np_index] = float(string_buffer)
                    matrix_np_index = matrix_np_index + 1
            elif cell =='t' or cell =='r' or cell =='n':
                string_buffer = ""
                char_list = [] 
            else:
                char_list.append(cell) 
    return matrix_np

# ==============================================================================  
file_path = sys.argv[1]
# file_path = "./../Session.7.9.2019B.txt"

# ==============================================================================  
frame_signature = b'FRAME'
frame_signature_size = 5

# ==============================================================================  
# auto = sys.argv[1]

# ==============================================================================  
frame = []
frame_size = 43
frame_counter = 0
frame_list = []
matrix_string_list = []
matrix_np = []

with open(file_path, 'rb') as file:
    for i, line in enumerate(file.readlines()):
        
        if line[:frame_signature_size] == frame_signature[:frame_signature_size]:
            frame_counter = frame_size
                     
        if frame_counter == 0:
            # print("---", frame_counter)
            pass
        else:
            frame_counter = frame_counter - 1
            # print(frame_counter)

        if frame_counter == 42:
            frame_instant = line
        elif frame_counter < 41 and frame_counter > 8:
            matrix_string_list.append(str(line)[2:-1])
        elif frame_counter == 8:
            maximum_pressure = line
        elif frame_counter == 7:
            minimum_pressure = line
        elif frame_counter == 5:
            average_pressure = line
        elif frame_counter == 4:
            center_of_pressure_x = line
        elif frame_counter == 3:
            center_of_pressure_y = line
        elif frame_counter == 2:
            contact_area = line
        elif frame_counter == 1:
            matrix_np = string_list2np(matrix_string_list)
            frame_dict = {
                'matrix_string_list':matrix_string_list,
                'matrix_np':matrix_np,
                'maximum_pressure':maximum_pressure,
                'minimum_pressure':minimum_pressure,
                'average_pressure':average_pressure,
                'center_of_pressure_x':center_of_pressure_x,
                'center_of_pressure_y':center_of_pressure_y,
                'contact_area':contact_area     
            }
            frame_list.append(frame_dict)
            matrix_string_list = []

          
for i, frame in enumerate(frame_list):
    print(i, np.mean(frame['matrix_np']), frame['contact_area'])

# for i, frame in enumerate(frame_list):
#     print(i, frame['matrix_np'])

print(len(frame_list))

database_np = np.ones((len(frame_list), 1024))

print(database_np.shape)
for i, frame in enumerate(frame_list):
    database_np[i, :] = frame['matrix_np']

np.savetxt("outest.csv", database_np, delimiter=",")

# # ==============================================================================  
# string_buffer = ""
# string_list = []
# matrix_np = np.ones(32*32)
# matrix_np_index = 0

# for i, line in enumerate(frame_dict['matrix_string_list']):
#     for j, cell in enumerate(line):
#         if cell == '\\':
#             string_buffer = list2string(string_list)
#             if string_buffer != "":
#                 matrix_np[matrix_np_index] = float(string_buffer)
#                 matrix_np_index = matrix_np_index + 1
#         elif cell =='t' or cell =='r' or cell =='n':
#             string_buffer = ""
#             string_list = [] 
#         else:
#             string_list.append(cell) 
