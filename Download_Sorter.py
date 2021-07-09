import os
import time

time.sleep(3)
paths = ['Photos','Videos','Executables','Compressed','Documents','Presentations','Code','Audio','Other','Spreadsheets']
exeptions =['Download_Sorter.py']
for path in paths:
    exeptions.append(path)

for path in paths:
    if os.path.isdir(path)==False:
        os.mkdir(path)

vExtensions = ['.mp4','.MOV','.mpx','.mpeg','.flv','MP4','webm','mov']
pExtensions = ['.jpeg','.jpg','.png','.PNG','.gif','.JPG','HEIC']
cExtensions = ['.zip','.rar','.7z','.tgz','.gz','bz2']
coExtensions = ['.cs','.py']
eExtensions = ['.exe','.msi']
dExtensions = ['.pdf','.docx','.doc','.rtf','.txt','RTF']
prExtensions = ['.pptx','.ppsx','.ppt']
aExtensions = ['.mp3','.flv','ogg']
sExtensions = ['xlsx','xlsm','xlsb','xltx','xls']
everything = [x for x in os.listdir() if x not in exeptions]
print(everything)

for file in everything:
    if any(c in file for c in vExtensions):
        fType = 'Videos'
    elif any(c in file for c in pExtensions):
        fType = 'Photos'
    elif any(c in file for c in eExtensions):
        fType = 'Executables'
    elif any(c in file for c in cExtensions):
        fType = 'Compressed'
    elif any(c in file for c in dExtensions):
        fType = 'Documents'
    elif any(c in file for c in prExtensions):
        fType = 'Presentations'
    elif any(c in file for c in aExtensions):
        fType = 'Audio'
    elif any(c in file for c in coExtensions):
        fType = 'Code'
    elif any(c in file for c in sExtensions):
        fType = 'Spreadsheets'
    else:
        fType = 'Other'
    print('moving - '+file+' - into '+fType)
    os.rename(file,fType+'/'+file)
time.sleep(15)
