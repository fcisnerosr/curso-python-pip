import os; import re
os.system('clear')

# # input
# country = input('Write a country: ')
pattern = (r',\d{1,}')


# Years from head and find the population in the input country
with open('./data.csv', 'r') as f:
    v_line = [line for line in f]


# Extract the head
head = iter(v_line)
head = next(head)

# Find the years trough regex
pattern = (r'\d{4,4}')
years   = re.findall(pattern, head)
print(years)


