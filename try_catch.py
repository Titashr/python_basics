try:
  print(x)
except NameError:
  print("Invalid Data")
except:
  print("Something else went wrong")
else:
  print("Nothing went wrong") 