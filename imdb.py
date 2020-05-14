def input():
  print ("PRE" + payload)
  return payload

def output():
  print ("POST" + payload)
  return payload

result = locals()[channel]()
