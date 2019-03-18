import os
os.chdir('enter your directory path here')
path = 'enter the same directory path as above'
dirs = os.listdir(path)
i = 0
for file in dirs:
    file_ext = file.rsplit('.')[-1]
    new_list = []
    for file_name in range(1):
        if(file_ext == 'png'):
            i += 1
            x = input('Name your .png file: ')
            new_list.append(x)
        elif(file_ext == 'py'):
            i += 1
            x = input('Name your .py file: ')
            new_list.append(x)
        elif (file_ext == 'jpg'):
            i += 1
            x = input('Name your .jpg file: ')
            new_list.append(x)
        elif (file_ext == 'xlsx'):
            i += 1
            x = input('Name your .xlsx file: ')
            new_list.append(x)
        elif (file_ext == 'pdf'):
            i += 1
            x = input('Name your .pdf file: ')
            new_list.append(x)
        elif (file_ext == 'docx'):
            i += 1
            x = input('Name your .docx file: ')
            new_list.append(x)
        elif (file_ext == 'docx'):
            i += 1
            x = input('Name your .docx file: ')
            new_list.append(x)
        elif (file_ext == 'zip'):
            i += 1
            x = input('Name your .zip file: ')
            new_list.append(x)
        elif (file_ext == 'mov'):
            i += 1
            x = input('Name your .mov file: ')
            new_list.append(x)
        elif (file_ext == 'csv'):
            i += 1
            x = input('Name your .csv file: ')
            new_list.append(x)
        else:
            print('There are either no files in your directory or there no files with the implemented extensions')
    #new_name = ''.join(new_list) + str(i) + '.' + file_ext <--- this will automatically increment 1 with as each file is added
    new_name = ''.join(new_list) + '.' + file_ext
    os.rename(file, new_name)
