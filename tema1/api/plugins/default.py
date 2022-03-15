import json


class defaultResponseAnafApi:
    def getDefaultJson():
        response_default = {
            "cod": -1,
            "cui": 0,
            "denumire": "",
            "adresa": "",
            "nrRegCom": "",
            "telefon": "",
            "stare_inregistrare": "",
            "scpTVA": False,
            "email":"example@domain.ro"
        }
        return response_default


class defaultResponseFacturis:
    def getDefaultJsonAdaugareClient():
        response_default = {
            "APIkey": "9d766ddf5ee42d146c477222c0ff17a5",
            "u": "admin",
            "p": "eusuntjohn",
            "c": "38935296",
            "met": "Clienti",
            "act": "Ins",
            "clienti_key": "",
            "clienti_nume": "Client Test",
            "clienti_cod": "RO0",
            "clienti_reg": "J00/00/2000",
            "clienti_tel": "0000000",
            "clienti_tip": "juridica",
            "clienti_card": "0o9i8u7y",
            "clienti_email": "email@domeniu.ro",
            "clienti_sediu": "Str. Pacii nr. 20",
            "clienti_oras": "",
            "clienti_banca": "",
            "clienti_judet": "",
            "clienti_cont": "",
            "clienti_obs": "Observatii",
            "clienti_obs1": "Obs. Client",
            "clienti_adresa_livrare": "Adresa",
            "clienti_nr_zile": "15",
            "clienti_disc": "0%"
        }
        return response_default




    def getDefaultJsonAdaugareFactura():
        response_default = {
            "APIkey": "9d766ddf5ee42d146c477222c0ff17a5",
            "u": "admin",
            "p": "eusuntjohn",
            "c": "38935296",
            "met": "Facturi",
            "act": "Ins",
            "dataFact": {
                "facturi_key": "",
                "facturi_punct_de_lucru": "",
                "facturi_gestiune": "",
                "facturi_data": "01-03-2022 19:38:25",
                "facturi_data_scadenta": "16-03-2022",
                "facturi_serie": "AAA",
                "facturi_numar": "2",
                "facturi_cota_tva": "19%",
                "facturi_moneda": "RON",
                "facturi_nume_client": "Nume Client",
                "facturi_tip_persoana": "juridica",
                "facturi_codf_client": "18181818181",
                "facturi_nrreg_client": "cd23123213",
                "facturi_sediu_client": "Bacau",
                "facturi_judet_client": "Bacau",
                "facturi_cont_client": "Cont",
                "facturi_banca_client": "banca",
                "facturi_clienti_adresa_livrare": "adresa de livrare",
                "facturi_clienti_judet_livrare": "judetul de livrare",
                "facturi_clienti_oras_livrare": "orasul de livrare",
              "facturi_clienti_tel": "telefon client",
                "facturi_obs_client": "obs_client",
                "facturi_nume_delegat": "nume delegat",
                "facturi_act_delegat": "act delegat",
                "facturi_obs_delegat": "obs delegat",
                "facturi_obs_up": "alte observatii",
                "facturi_status": "Emisa",
                "fk_agent_name": "Nume Agent"

            },
            "dataProd": [{
                "facturi_prod_nume": "produs test1",
                "facturi_prod_moneda": "RON",
                "facturi_prod_pretftva": "50",
                "facturi_prod_pretctva": "59.5",
                "facturi_prod_cant": "1.000",
                "facturi_prod_val": "50",
                "facturi_prod_val_tva": "9.5",
                "facturi_prod_val_tot": "59.5",
                "prod_cod": "1",
                "prod_sku": "1",
                "prod_cod1": "1",
                "prod_cod_cautare": "1",
                "facturi_prod_tva": "19%"

            }]
        }

        aa={'APIkey': '9d766ddf5ee42d146c477222c0ff17a5',

            'u': 'admin',
            'p': 'eusuntjohn',
            'c': '38935296',
            'met': 'Facturi',
            'act': 'Ins',
            'dataFact': {
                'facturi_key': '7495004',
                'facturi_punct_de_lucru': '',
                'facturi_gestiune': '',
                'facturi_data': '2019-01-09 15:30:52',
                'facturi_data_scadenta': '2019-01-31',
                'facturi_serie': '',
                'facturi_numar': '',
                'facturi_cota_tva': '19%',
                'facturi_moneda': 'RON',
                'facturi_nume_client': 'Nume Client',
                'facturi_tip_persoana': 'juridica',
                'facturi_codf_client': '7495004',
                'facturi_nrreg_client': 'J22/869/1995', 'facturi_sediu_client': 'JUD. IAŞI, SAT IUGANI COM. MIRCEŞTI, NR.-', 'facturi_judet_client': 'JUD. IAŞI, SAT IUGANI COM. MIRCEŞTI, NR.-', 'facturi_cont_client': 'Cont', 'facturi_banca_client': 'banca', 'facturi_clienti_adresa_livrare': 'adresa de livrare', 'facturi_clienti_judet_livrare': 'judetul de livrare', 'facturi_clienti_oras_livrare': 'orasul de livrare', 'facturi_clienti_tel': '0788361756', 'facturi_obs_client': 'obs_client', 'facturi_nume_delegat': 'nume delegat', 'facturi_act_delegat': 'act delegat', 'facturi_obs_delegat': 'obs delegat', 'facturi_obs_up': 'alte observatii', 'facturi_status': 'Emisa', 'fk_agent_name': 'Nume Agent', 'clienti_nume': 'GHERGHICEANU S.R.L.'}, 'dataProd': [{'facturi_prod_nume': 'produs test1', 'facturi_prod_moneda': 'RON', 'facturi_prod_pretftva': '50', 'facturi_prod_pretctva': '59.5', 'facturi_prod_cant': '1.000', 'facturi_prod_val': '50', 'facturi_prod_val_tva': '9.5', 'facturi_prod_val_tot': '59.5', 'prod_cod': '-', 'prod_sku': '-', 'prod_cod1': '-', 'prod_cod_cautare': 'prod_cod', 'facturi_prod_tva': '19%'}, {'facturi_prod_nume': 'produs test2', 'facturi_prod_moneda': 'RON', 'facturi_prod_pretftva': '456', 'facturi_prod_pretctva': '542.64', 'facturi_prod_cant': '1.000', 'facturi_prod_val': '456', 'facturi_prod_val_tva': '86.64', 'facturi_prod_val_tot': '542.64', 'prod_cod': '-', 'prod_sku': '-', 'prod_cod1': '-', 'prod_cod_cautare': 'prod_cod', 'facturi_prod_tva': '19%'}]}



        return response_default
