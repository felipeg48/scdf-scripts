import json

def input():
  print ("PRE" + payload)
  return json.loads(payload)

def output():
  print ("POST" + payload)
  return json.loads(payload)


result = locals()[channel]()
