import json
import time
import gspread

from oauth2client.service_account import ServiceAccountCredentials


from pprint import pprint

class ApiSheets:
    def loadJson(self):

        data = self.sheet.get_all_records()
        self.data_json=json.dumps(data)
        return data

    def updateQuantity(self,id, quantity):
        self.sheet.update_cell(id+1,4,quantity)
    def __init__(self):
        self.scope = ["https://spreadsheets.google.com/feeds",
                 'https://www.googleapis.com/auth/spreadsheets',
                 "https://www.googleapis.com/auth/drive.file",
                 "https://www.googleapis.com/auth/drive"]
        self.creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", self.scope)
        self.client = gspread.authorize(self.creds)
        self.sheet = self.client.open("CC-sheet").sheet1
        self.data_json={"id":0}


def main(readProdus):
    prodString = ""
    sheets=ApiSheets()
    for i in range(1, 6):
        a = int(str(readProdus[f'{i}'])[2:-2])
        id=i
        quantityNedeed=a
        for row in sheets.loadJson():
            if row['id']==id:
                stock=row['Cantitate(tone)']
                denumire=row['Denumire']
                if quantityNedeed==0:
                    prodString+=""
                else:
                    if quantityNedeed>stock:
                        print(f'LOG_SHEETSAPI {denumire} nu mai este in stoc')
                        prodString+= f'\n{denumire} nu mai este in stoc';
                    else:
                        sheets.updateQuantity(id=id, quantity=stock-quantityNedeed)
                        print(f'LOG_SHEETSAPI {denumire} : {quantityNedeed} tone confirmat')
                        prodString+= f'\n{denumire} : {quantityNedeed} tone confirmat'
    return prodString

if __name__ == '__main__':
    main(1,50)
