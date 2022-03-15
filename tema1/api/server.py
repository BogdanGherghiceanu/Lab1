import cgi
import api.mail as mail
import api.anaf as anaf
import api.facturis as facturis
import api.googlesheets as gsheet
import api.googlesheets as gsheetAPI


from http.server import HTTPServer, BaseHTTPRequestHandler

class requestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        pathString=self.path
        pathString=pathString.split("/")
        print(pathString)
        error=1
        try:
            if pathString[1]=='email':
                print("get email")
            if(pathString[1]=='cui'):
                cui=pathString[2]
                print(cui)
                self.send_response(200)
                self.send_header('content-type', 'text/html')
                self.end_headers()
                readHtml = open("../html/produse.html", "r")
                htmlString = readHtml.read()
                self.wfile.write(htmlString.encode())
                error=0
            if self.path.endswith('/home')== True:
                error=0
                self.send_response(200)
                self.send_header('content-type', 'text/html')
                self.end_headers()
                readHtml = open("../html/cui.html", "r")
                htmlString = readHtml.read()
                self.wfile.write(htmlString.encode())

        except:
            print("Redirect to homepage")
            error=1
        if error==1:
            self.send_response(301)
            self.send_header('Location', '/home')
            self.send_header('content-type', 'text/html')
            self.end_headers()




    def do_POST(self):

        pathString = self.path
        pathString = pathString.split("/")
        print(pathString)
        try:
            ctype, pdict = cgi.parse_header(self.headers.get('content-type'))
            pdict['boundary'] = bytes(pdict['boundary'], "utf-8")
            content_len = int(self.headers.get('Content-length'))
            pdict['CONTENT-LENGTH'] = content_len
            if ctype == 'multipart/form-data':
                fields = cgi.parse_multipart(self.rfile,pdict)
                if pathString[1] == "home":
                    readCui1 = str( fields.get('cui'))
                    readCui=readCui1[2:-2]
                    self.send_response(301)
                    self.send_header('content-type','text/html')
                    self.send_header('Location',f'/cui/{readCui}/produs/')
                    self.end_headers()
                if pathString[3]=="produs" :
                    readProdus={}
                    for i in range(1,6):
                        readProdus[f'{i}']=fields.get(f'{i}')
                        print(readProdus[f'{i}'])
                    readEmail=fields.get('email')
                    cui=int(pathString[2])

                    returnJson = anaf.ApiAnaf.searchCompany(cui)
                    returnJson['email'] = f'"{readEmail[0]}"'
                    if returnJson['denumire']=="":
                        mail.sendMailLipsaFirma(readEmail[0],cui)
                    if returnJson['scpTVA']==False:
                        mail.sendMailTVAFalse(readEmail[0], returnJson)
                    else:

                        prodString=gsheetAPI.main(readProdus)
                        mail.sendMail(readEmail[0], returnJson,prodString)





                    self.send_response(301)
                    self.send_header('content-type', 'text/html')
                    self.send_header('Location', f'/email')
                    self.end_headers()

        except:
            self.send_response(301)
            self.send_header('content-type', 'text/html')
            self.send_header('Location', '/home')
            self.end_headers()






        #self.path.encode()
def main():
    PORT=800
    server = HTTPServer(('',PORT), requestHandler)
    print('Serverul ruleaza PORT:%s'%PORT)
    server.serve_forever()


if __name__ == '__main__':
   main()
