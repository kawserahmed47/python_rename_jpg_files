import os
os.chdir('papaya')
i=1
for file in os.listdir():
    src=file
    dst="papaya_"+str(i)+".jpg"
    os.rename(src,dst)
    i+=1