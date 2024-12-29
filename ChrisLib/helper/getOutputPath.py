import os

def getPath():
    folder_path = 'output'
    current_dir = os.path.dirname(os.path.realpath(__file__))
    folder_path = os.path.join(current_dir, "../..", folder_path)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    return folder_path