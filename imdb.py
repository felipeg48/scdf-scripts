import json

def input():
  print ("PRE: " + payload)
  print ("Type: ")
  print (type(payload))
  
  return {'url':'https://imdb8.p.rapidapi.com/title/get-details?tconst=tt0944947'}

def output():
  print ("POST" + payload)
  return json.loads(payload)


result = locals()[channel]()
