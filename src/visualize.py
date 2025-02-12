#!/usr/bin/env python3

# command line args
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--input_path',required=True)
parser.add_argument('--key',required=True)
parser.add_argument('--percent',action='store_true')
parser.add_argument('--output_path',required=True)
args = parser.parse_args()

# imports
import os
import json
import matplotlib.pyplot as plt
from collections import Counter,defaultdict

# open the input path
with open(args.input_path) as f:
    counts = json.load(f)

# normalize the counts by the total values
if args.percent:
    for k in counts[args.key]:
        counts[args.key][k] /= counts['_all'][k]

# print the count values
items = sorted(counts[args.key].items(), key=lambda item: (item[1],item[0]), reverse=True)
top_10 = items[:10]
# plotting
plot_keys, plot_vals = [], []
for k, v in top_10:
    print(k,':',v)
    plot_keys.append(k)
    plot_vals.append(v)

plt.figure(figsize=(12,6))
bars = plt.bar(range(len(plot_keys)), plot_vals)
plt.title(f'Top 10 Values for {args.key}')
plt.xlabel('Key')
plt.ylabel('Count' if not args.percent else 'Percentage')
plt.xticks(range(len(plot_keys)), plot_keys)

plt.savefig(args.output_path)

