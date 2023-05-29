# Entries in the log file have the following shape:

# 123.125.71.35 - - [17/May/2015:10:05:46 +0000] "GET /blog/tags/release HTTP/1.1" 200 40693 "-" "Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)"
# 110.136.166.128 - - [17/May/2015:10:05:08 +0000] "GET /images/web/2009/banner.png HTTP/1.1" 200 52315 "http://www.semicomplete.com/style2.css" "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:28.0) Gecko/20100101 Firefox/28.0"
# 50.150.204.184 - - [17/May/2015:10:05:46 +0000] "GET /images/googledotcom.png HTTP/1.1" 200 65748 "http://www.google.com/search?q=https//:google.com&source=lnms&tbm=isch&sa=X&ei=4-r8UvDrKZOgkQe7x4CICw&ved=0CAkQ_AUoAA&biw=320&bih=441" "Mozilla/5.0 (Linux; U; Android 4.0.4; en-us; LG-MS770 Build/IMM76I) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30"
# 207.241.237.225 - - [17/May/2015:10:05:58 +0000] "GET /blog/tags/examples HTTP/1.0" 200 9208 "http://www.semicomplete.com/blog/tags/C" "Mozilla/5.0 (compatible; archive.org_bot +http://www.archive.org/details/archive.org_bot)"
# 200.49.190.101 - - [17/May/2015:10:05:36 +0000] "GET /reset.css HTTP/1.1" 200 1015 "-" "-"
# Your goal is to extract various analytics from this log that could help when troubleshooting.

# Exercises
# Surface statistics of HTTP response codes: What percentage of requests return code 200, 400 etc?
import re
from collections import defaultdict

status_code=defaultdict(int)
with open('/Users/svenkata/Projects/Parsing-Workshop/exercises/analyzing_apache-logs/apache_logs.txt','r') as logfile:
    lines = logfile.readlines()
    for line in lines:
        m = re.search(r'GET\s\S+\s\S+\s(\d{3})', line)
        if m is not None:
            status_code[m.group(1)] += 1
    
    total_response_codes = sum(list(status_code.values()))
    for k, v in status_code.items():
        print("Percentage of response code {} is --> {:.2f}".format(k, v*100/total_response_codes))
    

    

# Similarly, surface statistics on what kind of browsers tried to access the website.
browsers = set()
pattern = r'"([^"]*)"'
with open('/Users/svenkata/Projects/Parsing-Workshop/exercises/analyzing_apache-logs/apache_logs.txt', 'r') as logfile: 
    lines = logfile.readlines()
    for line in lines:
        matches = re.findall(pattern, line)
        if matches:
            browsers.add(matches[-1])
    
    print("Broswers requested are : ", *browsers, sep="\n")

# What is the average number of requests per day?
requests_per_day = defaultdict(int)
pattern = r'-\s-\s\[(\d\d\/[A-Z][a-z]{2}\/\d{4}):'
with open('/Users/svenkata/Projects/Parsing-Workshop/exercises/analyzing_apache-logs/apache_logs.txt', 'r') as logfile: 
    lines = logfile.readlines()
    for line in lines:
        match = re.search(pattern, line)
        if match is not None:
            requests_per_day[match.group(1)] += 1

for k, v in requests_per_day.items():
    print("Requests on day {} = {}".format(k, v))

values = requests_per_day.values()
print("Avg requests per day = {}".format(sum(values)/len(values)))


# You implemented a rating feature on the website and users rate the website significantly worse between 6pm and 9pm. Your boss thinks this is because there are more users during those hours which slows down the response time. Evaluate whether

# This timeframe actually experiences most users.
# The response time is actually slower during this timeframe.
timestamp_counter = defaultdict(int)
response_counter = defaultdict(int)
pattern = r'\[\d\d\/[A-Z][a-z][a-z]\/\d{4}:(\d\d):\d\d:\d\d\s.*GET\s.*\d\d\d\s(\d+)'

with open('/Users/svenkata/Projects/Parsing-Workshop/exercises/analyzing_apache-logs/apache_logs.txt', 'r') as logfile: 
    lines = logfile.readlines()
    for line in lines:
        match = re.search(pattern, line)
        if match is not None:
            timestamp_counter[match.group(1)] += 1
            response_counter[match.group(1)] += int(match.group(2))

for k, v in timestamp_counter.items():
    print("Users in timeframe {}-{} = {}".format(k,str(int(k)+1),v))
timestamp_most_users = int(sorted(timestamp_counter.items(), key=lambda x:x[1], reverse=True)[0][0])

for k, v in response_counter.items():
    print("Response time in timeframe {}-{} = {}".format(k,str(int(k)+1),v))
timestamp_max_response_time = int(sorted(response_counter.items(), key = lambda x:x[1])[0][0])

print("Timeframe with most users = {}-{}".format(str(timestamp_most_users), str(timestamp_most_users+1)))
print("Timeframe with slowest response time = {}-{}".format(str(timestamp_max_response_time), str(timestamp_max_response_time+1)))