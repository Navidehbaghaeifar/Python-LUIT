import os #Import os Module

dict_list = [] #Empty list to store dictionaries

for file in os.listdir(): ##Iterate over files in the working directory
    file_dict = {}
    file_dict['path'] = os.path.realpath(file) #get path name of file
    file_dict['size'] = os.path.getsize(file) #get size of file
    dict_list.append(file_dict) #add dictionary to list

print(*dict_list, sep="\n") #print dictionary of file information in new line