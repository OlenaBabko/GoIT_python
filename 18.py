rates = [600, 800, 1800, 2500]

rates_min = min(rates) 
rates_max = max(rates)   

item_number = len(rates)
total = sum(rates)
mean =total / item_number

print(item_number)
print(total)
print(mean)