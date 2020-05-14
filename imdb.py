import json

cheat = {}

def input():
  print ("PRE: " + payload)
  print ("Type: ")
  print (type(payload))
  print (payload[0])
  cheat = payload
  
  for i in payload:
    print (i)
  
  return {'url':'https://imdb8.p.rapidapi.com/title/get-details?tconst=tt0944947'}

def output():
  print ("POST: " + payload)
  print ("Cheat: ")
  print (type(payload))
  print (cheat)
  print ("-------")
  
  return json.loads(payload)


result = locals()[channel]()
