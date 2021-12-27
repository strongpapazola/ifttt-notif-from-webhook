from pycoingecko import CoinGeckoAPI
import requests
import json
from time import sleep
cg = CoinGeckoAPI()

def rupiah(value):
 str_value = str(value)
 separate_decimal = str_value.split(".")
 after_decimal = separate_decimal[0]
 before_decimal = separate_decimal[1]
 reverse = after_decimal[::-1]
 temp_reverse_value = ""
 for index, val in enumerate(reverse):
  if (index + 1) % 3 == 0 and index + 1 != len(reverse):
   temp_reverse_value = temp_reverse_value + val + "."
  else:
   temp_reverse_value = temp_reverse_value + val
 temp_result = temp_reverse_value[::-1]
 return "Rp " + temp_result + "," + before_decimal

while True:
 p = cg.get_price(ids='binancecoin', vs_currencies='idr')
 #{'binancecoin': {'idr': 7748341}}
 if p['binancecoin']['idr'] >= 9000000:
  url = "https://maker.ifttt.com/trigger/moment/with/key/mn-PJ3lpBg7-kX7W5ci3PgfVgublPxk_p4bB5piDmh5"
  payload = json.dumps({
    "value1": rupiah(float(p['binancecoin']['idr']))
  })
  headers = {
    'Content-Type': 'application/json'
  }
  response = requests.request("POST", url, headers=headers, data=payload)
  print(response.text)
  exit()
 sleep(5)

