import os

# install kaggle package
os.system("pip3 install kaggle")

# create directory .kaggle in user folder
os.system("mkdir C:/Users/yadav/.kaggle")

# download kaggle.json file from kaggle and copy it to the .kaggle directory in user folder
os.system("copy C:/Users/yadav/Downloads/kaggle.json C:/Users/yadav/.kaggle/kaggle.json")

# Search for the datasets in the kaggle directory
os.system("kaggle datasets list -s 'python'")

# use ref of the requierd directory to download the dataset
# you can also simple copy the api from Kaggle
os.system("kaggle datasets download -d stackoverflow/pythonquestions")

# Unzip the zipped dataset using following
# from zipfile import ZipFile
# zf = ZipFile('path_to_file/file.zip', 'r')
# zf.extractall('path_to_extract_folder')
# zf.close()

from zipfile import ZipFile
zf = ZipFile('pythonquestions.zip', 'r')
zf.extractall()
zf.close()