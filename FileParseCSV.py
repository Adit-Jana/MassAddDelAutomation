import pandas as pd   #pandas version 1.0.3
import os  #
import glob #glob version 3.5

source = "F:\\Demo\\ctns\\" #source directory

dest = 'G:\\Destination\\'  #destination directory

os.chdir(source)

for file in glob.glob("*.xls"):
    out = file.split('.')[0]+'.csv'
    df = pd.read_excel(open(file,'rb'),sheet_name='CTN List')

    df.to_csv(os.path.join(dest,out), index=False)
    print("Done")
         

for file in glob.glob("*.xlsx"):
    out = file.split('.')[0]+'.csv'
    df = pd.read_excel(open(file,'rb'), sheet_name='CTN List')

    df.to_csv(os.path.join(dest,out), index=False)
    print("Done")

       
