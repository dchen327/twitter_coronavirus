#!/usr/bin/env python3
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--input_paths', nargs='+', required=True)
parser.add_argument('--hashtags', nargs='+', required=True)
parser.add_argument('--output_path', required=True)
args = parser.parse_args()

# imports
import os
import json
import matplotlib.pyplot as plt
from collections import Counter,defaultdict
from matplotlib import rc

rc('font', family='UnBatang')

hashtag_to_daily_usage = defaultdict(list)
for path in args.input_paths:
    # each path is 1 day
    with open(path) as f:
        tmp = json.load(f)
        print(path)
        for k in tmp:
            print(k, sum(tmp[k].values()))
        for hashtag in args.hashtags:
            print(hashtag)
            daily_usage = 0
            if hashtag in tmp:
                daily_usage += sum(tmp[hashtag].values())
            hashtag_to_daily_usage[hashtag].append(daily_usage)
            
print(hashtag_to_daily_usage)
plt.figure(figsize=(12,6))
num_days = len(hashtag_to_daily_usage[args.hashtags[0]])

for hashtag in args.hashtags:
    plt.plot(range(num_days), hashtag_to_daily_usage[hashtag], label=hashtag)

plt.xlabel('Days')
plt.ylabel('Tweets Per Day')
plt.title('Tweets Per Day of Hashtags Over the Year')

plt.legend()

plt.savefig(args.output_path)

