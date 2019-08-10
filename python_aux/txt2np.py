import matplotlib.pyplot as plt
import numpy as np

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

# ==============================================================================  
file_path = "./../Session.7.9.2019B.txt"

# ==============================================================================  
frame_id_signature = b'FRAME 1505'
frame_id_signature_size = 10
frame_signature_size = 5

print_trigger = False
frame = []
matrix_string_list = []
matrix_np = []

with open(file_path, 'rb') as file:
    for i, line in enumerate(file.readlines()):
        
        if line[:frame_signature_size] == frame_id_signature[:frame_signature_size]:
            print_trigger = False
            
        if line[:frame_id_signature_size] == frame_id_signature[:frame_id_signature_size]:    
            print_trigger = True
            
        if print_trigger is True:
            frame.append(line)

# ==============================================================================              
for i, line in enumerate(frame):
    if i>1 and i<34:
        matrix_string_list.append(str(line)[2:-1])

# ==============================================================================  
string_buffer = ""
string_list = []
matrix_np = np.ones(32*32)
matrix_np_index = 0

for i, line in enumerate(matrix_string_list):
    for j, cell in enumerate(line):
        if cell == '\\':
            string_buffer = list2string(string_list)
            if string_buffer != "":
                matrix_np[matrix_np_index] = float(string_buffer)
                matrix_np_index = matrix_np_index + 1
        elif cell =='t' or cell =='r' or cell =='n':
            string_buffer = ""
            string_list = [] 
        else:
            string_list.append(cell) 

matrix_np = matrix_np.reshape((32, 32))

# ==============================================================================  
fig = plt.figure(figsize=(10, 10))

# ------------------------------------------------------------------------------ax = fig.add_subplot(elc_plot_layout[0], elc_plot_layout[1], 1)
ax = fig.add_subplot(1, 1, 1)
ax.set_title(frame_id_signature)

img = ax.imshow(matrix_np, 
                interpolation ='gaussian', 
                cmap ='inferno')

#===============================================================================
plt.show()