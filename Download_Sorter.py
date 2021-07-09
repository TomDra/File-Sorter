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

videoExtentions = ['.mp4','.MOV','.mpx','.mpeg','.flv','MP4','webm','mov']
photoExtentions = ['.jpeg','.jpg','.png','.PNG','.gif','.JPG','HEIC','.webp']
coppressedExtentions = ['.zip','.rar','.7z','.tgz','.gz','.bz2']
codexeExtentions = ['.cs','.py','.html','.css']
exeExtentions = ['.exe','.msi']
docsExtentions = ['.pdf','.docx','.doc','.rtf','.txt','RTF']
presentationExtentions = ['.pptx','.ppsx','.ppt']
audioExtentions = ['.mp3','.flv','ogg']
spreadsheetExtentions = ['xlsx','xlsm','xlsb','xltx','xls']
everything = [x for x in os.listdir() if x not in exeptions]
print(everything)

for file in everything:
    if any(c in file for c in videoExtentions):
        fType = 'Videos'
    elif any(c in file for c in photoExtentions):
        fType = 'Photos'
    elif any(c in file for c in exeExtentions):
        fType = 'Executables'
    elif any(c in file for c in coppressedExtentions):
        fType = 'Compressed'
    elif any(c in file for c in docsExtentions):
        fType = 'Documents'
    elif any(c in file for c in presentationExtentions):
        fType = 'Presentations'
    elif any(c in file for c in audioExtentions):
        fType = 'Audio'
    elif any(c in file for c in codexeExtentions):
        fType = 'Code'
    elif any(c in file for c in spreadsheetExtentions):
        fType = 'Spreadsheets'
    else:
        fType = 'Other'
    print('moving - '+file+' - into '+fType)
    os.rename(file,f'{fType}/{file}')
time.sleep(15)
