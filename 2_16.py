def validate(value):
    try:
      out = float(value)
    except ValueError:
      out = None
        
    return out