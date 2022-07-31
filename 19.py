rates = [600, 800, 1800, 2500]
stat = {"mean": None, "min": None, "max": None, "item_number": 0, "total": 0}


stat["mean"] = sum(rates)/len(rates)    
stat["min"] = min(rates)
stat["max"] = max(rates)
stat["item_number"] = len(rates)
stat["total"] = sum(rates)