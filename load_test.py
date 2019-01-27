import numpy as np

with open("pickles/hero_id", "rb") as f:
	d = np.load(f)

print(sum(d[0]))