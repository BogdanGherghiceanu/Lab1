import requests

url = 'https://webservicesp.anaf.ro/PlatitorTvaRest/api/v6/ws/tva'
myobj = [
    {
        "cui": 7491004,
        "data": "2022-02-27"
    },
    {
        "cui": 43794096,
        "data": "2022-02-27"
    }
]

x = requests.post(url, json = myobj)

print(x.text)