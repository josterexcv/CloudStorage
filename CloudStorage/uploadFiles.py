  
import os
import dropbox
from dropbox.files import WriteMode

class TransferData:
    def __init__(self,access_token):
        self.access_token =  access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        for root, dirs, files in os.walk(files_from):

            for filename in files:
                local_path = os.path.join(root, filename)

                relative_path = os.path.repath(local_path, file_from)
                dropbox_path = os.path.join(file_to, relative_path)

                with open(local_path, 'rb') as f:
                    dbx.files_upload(f.read(), dropbox_path, mode=('overWrite'))

def main():
    access_token = ''
    TransferData = TransferData(access_token)

    file_from = str(input("Enter the folder path to transfer : -"))
    file_to = input("enter the full path to upload to Dropbox:- ")
    
    transferData.upload_file(file_from, file_to)
    print("file had been moved !!!")

main()    