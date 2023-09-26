import os


for (dirpath,dirnames,filenames) in os.walk('.\Postman'):
    print(f'I am at {dirpath}')

    for filename in filenames:
        pathfile = dirpath+"/"+filename
        print(f'  File: {dirpath}\\{filename} - size: {os.path.getsize(dirpath+"/"+filename)}B')

        f = open(pathfile)
        lines = f.readlines()
        f.close()

        i = 0
        s = ""
        for line in lines:
            i+=1
            s+=str(i) + ": " + line

        f = open(pathfile,'w')
        f.write(s)
        f.close()
