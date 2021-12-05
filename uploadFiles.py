import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self,folder):
        dbx = dropbox.Dropbox(self.access_token)


        f = open(folder, 'rb')
        dbx.files_upload(f.read(), folder)

def main():
    access_token = 'sl.A8vmWK1G4yZeKca3J0OTj0ABKgckrco_-HYIZd9JfWA9WXjFPz7F7PK1pjheVrg8xA7RE20MteB40u24Ob6zlFP42GM24pfvV2n1pxbPNgg1_e1MxrGf316Mtde23Q-minrv_6ZlU7CI'
    transferData = TransferData(access_token)

    folder = input("Enter the file path to transfer it to dropBox : -")
   

    # API v2
    transferData.upload_file(folder)
    print("file has been moved !!!")


main()