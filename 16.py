developer_rates = [600, 800, 1800, 2500, 3300]

total_juniors = 0

for rate in developer_rates:
    if rate < 1000:
      total_juniors += rate
        
print(total_juniors)