import json

import requests
import plugins.getDate as d
import plugins.default as default
class ApiAnaf:

    def searchCompany(cui_firma):

        print("LOG ANAFAPI: Incep cautarea firmei")

        returnJson=default.defaultResponseAnafApi.getDefaultJson()

        url = 'https://webservicesp.anaf.ro/PlatitorTvaRest/api/v6/ws/tva'
        body=[
            {
                "cui": cui_firma,
                "data": str(d.get_date())
            }
        ]
        try:
            response = requests.post(url, json = body)
            responseJson = json.loads(response.text)

            if(responseJson["cod"]!=200):
                print("Log Api Anaf Eroare la conectarea la server")
                print(returnJson)
                return returnJson

            returnJson["cod"] = responseJson["cod"]
            for company in responseJson["found"]:
                is_platitor_tva=company["scpTVA"]
                if(is_platitor_tva==False):
                    returnJson["cod"] = 0
                    print("Log Api Anaf Compania nu este platitoare de tva")
                    return returnJson

                try:
                    returnJson["cui"]                = str(company["cui"])
                except:
                    returnJson["cui"]="error"
                try:
                    returnJson["denumire"         ]  = company["denumire"]
                except:
                    returnJson["denumire"]="error"
                try:
                    returnJson["adresa"           ]  = company["adresa"]
                except:
                    returnJson["adresa"]="error"
                try:
                    returnJson["nrRegCom"         ]  = company["nrRegCom"]
                except:
                    returnJson["nrRegCom"]="error"
                try:
                    returnJson["stare_inregistrare"] = company["stare_inregistrare"]
                except:
                    returnJson["stare_inregistrare"]="error"
                try:
                    returnJson["scpTVA"           ]  = company["scpTVA"]
                except:
                    returnJson["scpTVA"]="error"
                try:
                    returnJson["telefon"] = company["telefon"]
                except:
                    returnJson["telefon"] = "error"

                print("Log Api Anaf OK")
                print(returnJson)
                return returnJson
        except:
            print("Log Api Anaf Eroare request")
            print(returnJson)
            return returnJson


if __name__ == '__main__':
    print(ApiAnaf.searchCompany(7495004))

#print(x.text)




# import requests
#
# url = 'https://webservicesp.anaf.ro/PlatitorTvaRest/api/v6/ws/tva'
# myobj = [
#     {
#         "cui": 7491004,
#         "data": "2022-02-27"
#     },
#     {
#         "cui": 43794096,
#         "data": "2022-02-27"
#     }
# ]
#
# x = requests.post(url, json = myobj)
#
# print(x.text)