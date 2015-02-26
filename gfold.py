import os
from collections import defaultdict
from itertools import combinations
import re


sample_def = re.compile('(.*)-[0-9]{2,}-[0-9]{2,}-[0-9]{2,}')

conditions = defaultdict(list)

for root, dirs, files in os.walk('./data'):
    for file in files:
        if file.endswith('gfoldcounts.tsv'):
            sample = sample_def.match(file)
            if sample:

                print(sample.group(0))
                conditions[sample.group(1)].append(os.path.join(root, file))



for treatment, samples in conditions.items():
    pairwise_compare = combinations(samples,2)
    conditions[treatment] = [x for x in pairwise_compare] #seperate concern.



print(conditions)
