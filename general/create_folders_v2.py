import os
# initial
drives = ['C','D','E']
subfs = []

#user inputs
dl = int(input("where is master drive. \ncurrent drives 1, C 2, D 3,E \n"))
drive = drives[dl-1]
proj = input("project title ")
seq = input("sequnce name ")
shot = input("shot number: ")

list_fol = ['asset','geo','cache','preview','version','plate']
subf = input('subfolders to create. pick number with single space inbetween \n 1- asset 2- geo 3- cache 4- preview 5-version 6- plate \n')
ls = subf.split(' ')
for x in ls:
    num = int(x) - 1
    subfs.append(list_fol[num])
print(subfs)
mainpath = [drive+':',proj,seq,shot]
mypath = os.sep.join(mainpath)

print(mypath)

if not os.path.exists(path):
    for items in subfs:
        mypath = os.sep.join(mainpath)
        os.mkdir(mypath + '\\' + tasks) 

print (f'folder structure created successfuly here {path_preview}')
print ('Happy VFX')
