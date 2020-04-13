import os
from os import listdir
from datetime import datetime

directory = "C:\\"
files = [[]]
folder_layer = 0
folders_found = 0
files_found = 0

def checkForFolders(folder, folder_name):
    global folder_layer, files, folders_found
    for file in folder:
        if os.path.isdir(folder_name + "\\"+ file):
            files[folder_layer].append(folder_name + "\\" + file)
            folders_found += 1
    

def getNewFiles(dir):
    global folder_layer, files
    try:
        new_files = listdir(dir)
    except Exception as e:
        pass
        new_files = []
    return new_files


def getExistingFolders(layer_num):
    return files[layer_num]


def getFolders(dir):
    global folder_layer, files, files_found
    new_files = getNewFiles(dir)
    for file in new_files:
        if os.path.isdir(dir + file):
            files[folder_layer].append(dir + file)
    i = 1
    while True:
        folders = getExistingFolders(folder_layer)
        folder_layer = i
        files.append([])
        if folders == []:
            return
        for folder in folders:
            new_files = getNewFiles(folder)
            if new_files != []:
                checkForFolders(new_files, folder)
        i += 1

start = datetime.now().strftime("%H:%M:%S")
getFolders(directory)
for group in files:
    for folder in group:
        try:
            files_found += len(listdir(folder))
        except WindowsError:
            pass
finish = datetime.now().strftime("%H:%M:%S")
print("Start: {} | Finish: {}".format(start, finish))
print("Found {} folders and {} files.".format(folders_found, files_found))