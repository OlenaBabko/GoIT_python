out = ''
value = 'f' 
try:
    value = float(value)
except ValueError:
  out = f"value {value} can't be converted to float"
  
if out:
    print(out)