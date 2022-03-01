import sys

import requests




json_file = {
    "APIkey": "9d766ddf5ee42d146c477222c0ff17a5",
    "u": "admin",
    "p": "eusuntjohn",
    "c": "38935296",
    "met": "Clienti",
    "act": "Ins",
    "clienti_key": "",
    "clienti_nume": "Client Test",
    "clienti_cod": "RO7495004",
    "clienti_reg": "J22\/869\/1995",
    "clienti_tel": "0987654321",
    "clienti_tip": "juridica",
    "clienti_card": "0o9i8u7y",
    "clienti_email": "email@domeniu.ro",
    "clienti_sediu": "Str. Pacii nr. 20",
    "clienti_oras": "Bucuresti",
    "clienti_banca": "Banca",
    "clienti_judet": "",
    "clienti_cont": "",
    "clienti_obs": "Observatii",
    "clienti_obs1": "Obs. Client",
    "clienti_adresa_livrare": "Adresa",
    "clienti_nr_zile": "15",
    "clienti_disc": "0%"
}
url = "https://api.facturis-online.ro/api/"

response = requests.request("POST", url, params=json_file)
print(response.text)
