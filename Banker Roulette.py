# this code has two optional ways of randomly choosing a name from list

import random


friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

# 1st option
# print(random.choice(friends))

# 2nd option
business_cards = random.randint(0,4)
print(friends[business_cards])