def input():
  print ("PRE" + payload)
  return "Hola"

def output():
  print ("POST" + payload)
  return "Adios"


result = locals()[channel]()
