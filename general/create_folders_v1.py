import os

drives = ['C','D','E']
dl = int(input("where is master drive. \ncurrent drives 1, C 2, D 3,E \n"))
drive = drives[dl-1] + ":\" 
proj = input("project title ")
proj += "\" 
seq = input("sequnce name ")
seq += "\"
shot = input("shot number: ")
shot += "\"
task = input("task: 1, FX or 2, Comp")
subfs = []
list_fol = ['asset','geo','cache','preview','version','plate']
subf = input('subfolders to create. pick number with single space inbetween \n 1- asset 2- geo 3- cache 4- preview 5-version 6- plate \n')
ls = subf.split(' ')
for x in ls:
    num = int(x) - 1
    subfs.append(list_fol[num])

path = drive + proj + seq + shot
path_preview = path
path = r'path'

if not os.path.exists(path):
    for items in subfs:
        os.mkdir(path + "\" + items) 

print (f'folder structure created successfuly here {path_preview}')
print ('Happy VFX')
