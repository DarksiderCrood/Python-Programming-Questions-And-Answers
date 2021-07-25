import random
import numpy as np
res1 = random.randint(1, 100)
res2 = random.random() * 100
res3 = random.choice(range(0, 101))
print(res1, res2, res3)
# Create five random numbers
ran5 = np.random.randn(5)
print(ran5)