import pandas as pd
data = pd.read_csv('data.txt', names=['value'])

# Part 1
previous_value = data['value'][0]
AmoutOfIncreases = 0
for current_value in data['value']:    
    if current_value > previous_value:
        AmoutOfIncreases = AmoutOfIncreases + 1    
    previous_value = current_value
print(AmoutOfIncreases)

# Part 2
data['index'] = data['value'].rolling(window=3).mean()
previous_value = increases = 0
for mean in data['index']:
    current_value = mean
    if current_value > previous_value:
        increases = increases+1
    previous_value = current_value
print(increases)