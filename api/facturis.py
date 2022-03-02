import json
import sys
import plugins.default as default
import requests
import plugins.getDate as d
class ApiFacturis:
    def getClienti():
        url = "https://api.facturis-online.ro/api/"
        jsonGetClienti={
            "APIkey": "9d766ddf5ee42d146c477222c0ff17a5",
            "u": "admin",
            "p": "",
            "c": "38935296",
            "met": "Produse",
            "act": "Get"
        }
        response = requests.request("POST", url, params=jsonGetClienti)

        responseJson = json.loads(response.text)

        print(response)

        print(response.text)

    def AdaugareClient(jsonAnaf):
        jsonAdaugareClient=default.defaultResponseFacturis.getDefaultJsonAdaugareClient()
        jsonAdaugareClient["clienti_key"] = jsonAnaf["cui"]
        jsonAdaugareClient["clienti_nume"] =jsonAnaf["denumire"]
        jsonAdaugareClient["clienti_cod"] = jsonAnaf["cui"]
        jsonAdaugareClient["clienti_reg"] = jsonAnaf["nrRegCom"]
        jsonAdaugareClient["clienti_tel"] = jsonAnaf["telefon"]
        jsonAdaugareClient["clienti_email"]=jsonAnaf["email"]
        jsonAdaugareClient["clienti_sediu"]=jsonAnaf["adresa"]
        jsonAdaugareClient["clienti_card"] = jsonAnaf["cui"]

        url = "https://api.facturis-online.ro/api/"
        response = requests.request("POST", url, params=jsonAdaugareClient)

        responseJson = json.loads(response.text)

        print(response)

        print(response.text)
        try:
            if responseJson["success"]==2000:
                return 1
        except:
            try:
                if responseJson["error"]==1112:
                    return 0
            except:
                return -1
        return -1
    def AdaugareFactura(jsonAnaf):
        checkClient = ApiFacturis.AdaugareClient(jsonAnaf)
        #checkClient=1
        if checkClient == -1:
            print("eroare Verificare Client")
            return -1
        print("Incepere adaugare Factura")
        jsonAdaugareFactura = default.defaultResponseFacturis.getDefaultJsonAdaugareFactura()
        jsonAdaugareFactura["dataFact"]["facturi_codf_client"] = int(jsonAnaf["cui"])
        jsonAdaugareFactura["dataFact"]["facturi_key"] =            str(jsonAnaf["cui"]        )
        jsonAdaugareFactura["dataFact"]["facturi_nume_client"] =    str(jsonAnaf["denumire"])
        jsonAdaugareFactura["dataFact"]["facturi_nrreg_client"] =   str(jsonAnaf["nrRegCom"])
        jsonAdaugareFactura["dataFact"]["facturi_sediu_client"] =   str(jsonAnaf["adresa"])
        jsonAdaugareFactura["dataFact"]["facturi_judet_client"] =   str(jsonAnaf["adresa"])
        jsonAdaugareFactura["dataFact"]["facturi_sediu_client"] =   str(jsonAnaf["adresa"])
        jsonAdaugareFactura["dataFact"]["facturi_clienti_tel"] =    str(jsonAnaf["telefon"])
        jsonJson=json.dumps(jsonAdaugareFactura)
        print(jsonJson)
        url = "https://api.facturis-online.ro/api/"
        response = requests.request("GET", url, params=jsonAdaugareFactura)
        print(response)
        print(response.text)
    # def AdaugareFactura(jsonAnaf):
    #
    #     response=ApiFacturis.AdaugareClient(jsonAnaf)
    #     if response==-1:
    #         return 0
    #     jsonAdaugareFactura=default.defaultResponseFacturis.getDefaultJsonAdaugareFactura()
    #     print(jsonAdaugareFactura["dataFact"]["facturi_moneda"])
    #     temp=d.get_date_now()
    #     jsonAdaugareFactura["dataFact"]["facturi_data"] = temp["data"]
    #     jsonAdaugareFactura["dataFact"]["facturi_data_scadenta"] = temp["data"]
    #     jsonAdaugareFactura["dataFact"]["facturi_nume_client"] = jsonAnaf["denumire"]
    #     jsonAdaugareFactura["dataFact"]["facturi_codf_client"] =jsonAnaf["cui"]
    #     jsonAdaugareFactura["dataFact"]["facturi_nrreg_client"] =jsonAnaf["nrRegCom"]
    #     jsonAdaugareFactura["dataFact"]["facturi_sediu_client"] =jsonAnaf["adresa"]
    #     jsonAdaugareFactura["dataFact"]["facturi_clienti_tel"] = jsonAnaf["telefon"]
    #     jsonAdaugareFactura["dataFact"]["facturi_key"] = jsonAnaf["cui"]
    #
    #     url = "https://api.facturis-online.ro/api/"
    #     print(jsonAdaugareFactura)
    #     response = requests.request("POST", url, params=jsonAdaugareFactura)
    #     responseJson = json.loads(response.text)
    #     print("LOG:ADAUGARE CLIENT")
    #     print(response)
    #     print(response.text)
    #
    #
    # def AdaugareFacturaTest(cui):
    #
    #     response_default = {
    #         "APIkey": "9d766ddf5ee42d146c477222c0ff17a5",
    #         "u": "admin",
    #         "p": "",
    #         "c": "38935296",
    #         "met": "Facturi",
    #         "act": "Ins",
    #         "dataFact": {
    #             "facturi_key": "7495004",
    #             "facturi_punct_de_lucru": "",
    #             "facturi_gestiune": "",
    #             "facturi_data": "2019-01-09 15:30:52",
    #             "facturi_data_scadenta": "2019-01-31",
    #             "facturi_serie": "AG",
    #             "facturi_numar": "1",
    #             "facturi_cota_tva": "19%",
    #             "facturi_moneda": "RON",
    #             "facturi_nume_client": "GHERGHICEANU S.R.L.",
    #             "facturi_tip_persoana": "juridica",
    #             "facturi_codf_client": "7495004",
    #             "facturi_nrreg_client": "J22/869/1995",
    #             "facturi_sediu_client": "Bacau",
    #             "facturi_judet_client": "Bacau",
    #             "facturi_cont_client": "Cont",
    #             "facturi_banca_client": "banca",
    #             "facturi_clienti_adresa_livrare": "adresa de livrare",
    #             "facturi_clienti_judet_livrare": "judetul de livrare",
    #             "facturi_clienti_oras_livrare": "orasul de livrare",
    #             "facturi_clienti_tel": "telefon client",
    #             "facturi_obs_client": "obs_client",
    #             "facturi_nume_delegat": "nume delegat",
    #             "facturi_act_delegat": "act delegat",
    #             "facturi_obs_delegat": "obs delegat",
    #             "facturi_obs_up": "alte observatii",
    #             "facturi_status": "Emisa",
    #             "fk_agent_name": "Nume Agent"
    #
    #         },
    #         "dataProd": [{
    #             "facturi_prod_nume": "produs test1",
    #             "facturi_prod_moneda": "RON",
    #             "facturi_prod_pretftva": "50",
    #             "facturi_prod_pretctva": "59.5",
    #             "facturi_prod_cant": "1.000",
    #             "facturi_prod_val": "50",
    #             "facturi_prod_val_tva": "9.5",
    #             "facturi_prod_val_tot": "59.5",
    #             "prod_cod": "-",
    #             "prod_sku": "-",
    #             "prod_cod1": "-",
    #             "prod_cod_cautare": "prod_cod",
    #             "facturi_prod_tva": "19%"
    #
    #         },
    #             {
    #                 "facturi_prod_nume": "produs test2",
    #                 "facturi_prod_moneda": "RON",
    #                 "facturi_prod_pretftva": "456",
    #                 "facturi_prod_pretctva": "542.64",
    #                 "facturi_prod_cant": "1.000",
    #                 "facturi_prod_val": "456",
    #                 "facturi_prod_val_tva": "86.64",
    #                 "facturi_prod_val_tot": "542.64",
    #                 "prod_cod": "-",
    #                 "prod_sku": "-",
    #                 "prod_cod1": "-",
    #                 "prod_cod_cautare": "prod_cod",
    #                 "facturi_prod_tva": "19%"
    #             }]
    #     }
    #     url = "https://api.facturis-online.ro/api/"
    #
    #     response = requests.request("GET", url, params=response_default)
    #     responseJson = json.loads(response.text)
    #     print("LOG:ADAUGARE CLIENT")
    #     print(response)
    #     print(response.text)



#
# json_file = {
#     "APIkey": "9d766ddf5ee42d146c477222c0ff17a5",
#     "u": "admin",
#     "p": "",
#     "c": "38935296",
#     "met": "Clienti",
#     "act": "Ins",
#     "clienti_key": "",
#     "clienti_nume": "Client Test",
#     "clienti_cod": "RO7495004",
#     "clienti_reg": "J22\/869\/1995",
#     "clienti_tel": "0987654321",
#     "clienti_tip": "juridica",
#     "clienti_card": "0o9i8u7y",
#     "clienti_email": "email@domeniu.ro",
#     "clienti_sediu": "Str. Pacii nr. 20",
#     "clienti_oras": "Bucuresti",
#     "clienti_banca": "Banca",
#     "clienti_judet": "",
#     "clienti_cont": "",
#     "clienti_obs": "Observatii",
#     "clienti_obs1": "Obs. Client",
#     "clienti_adresa_livrare": "Adresa",
#     "clienti_nr_zile": "15",
#     "clienti_disc": "0%"
# }
# url = "https://api.facturis-online.ro/api/"
#
# response = requests.request("POST", url, params=json_file)
# print(response.text)
