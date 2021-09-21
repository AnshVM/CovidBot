import requests
import json

async def covid(message):
  msg = message.content
  chn = message.channel
  x = requests.get('https://api.apify.com/v2/key-value-stores/toDWvRj1JpTXiM8FF/records/LATEST?disableRedirect=true')

  json_data = json.loads(x.text)

  if(msg == "oy covid active"):
    await message.channel.send("Total active covid cases in india: {0}".format(json_data['activeCases']))

  if(msg == "oy covid recovered"):
    await chn.send("Total recovered from covid in india are: {0}".format(json_data['recovered']))

  if(msg == 'oy covid deaths'):
    await chn.send("Total deaths in india due to covid: {0}".format(json_data['deaths']))

  if(msg == "oy covid total"):
    await chn.send("Total covid cases in india are: {0}".format(json_data['totalCases']))


  if(msg.startswith("oy covid region")):
    region = msg[16:]
    regionData = json_data['regionData']
    print(region)

    for data in regionData:
      print(data)
      if data['region'].lower() == region.lower():
        print('founr')
        await chn.send("Active cases in {0} are {1}".format(region,data['totalInfected']))
        await chn.send("Total recovered in {0} are {1}".format(region,data['recovered']))
        await chn.send("Total deaths due to covid in {0} are {1}".format(region,data['deceased']))

    
  if(msg == "oy covid"):
    await message.channel.send("Total active covid cases in india: {0}".format(json_data['activeCases']))


  