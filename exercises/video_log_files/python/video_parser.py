import datetime
from collections import defaultdict

videos = defaultdict(int)
start_time = datetime.datetime.strptime("09/21/2018", "%m/%d/%Y")
end_time = datetime.datetime.strptime("09/23/2018", "%m/%d/%Y")

# PART1: Determine the top two most played videos during the days 9/21-9/22/2018.
with open('/Users/svenkata/Projects/Parsing-Workshop/exercises/video_log_files/logs.txt', 'r') as logfile:
    filtered_line = []
    lines = logfile.readlines()
    for line in lines:
        video, user, type, ctime = line.split()
        time = datetime.datetime.strptime(ctime, "%m/%d/%Y-%H:%M:%S")
        if time >= start_time and time < end_time:
            filtered_line.append(line)

print(*filtered_line)
videos = {}
for line in filtered_line:
    v, u, e, t = line.split()
    if e == "start":
        videos[(v, u)] = datetime.datetime.strptime(t, "%m/%d/%Y-%H:%M:%S")
    else:
        duration = datetime.datetime.strptime(t, "%m/%d/%Y-%H:%M:%S") - videos[(v, u)]
        videos[(v, u)] = duration.seconds
videos = sorted(videos.items(), key=lambda x:x[1], reverse=True)
for k, v in videos:
    print("Video {} was played by user {} for a duration of {} minutes".format(k[0], k[1], v//60))

most_played = set()
for k, v in videos:
    most_played.add(k[0])
    if len(most_played) == 2:
        break
        
print("Most played videos are : ", *most_played)

# PART2: Determine the duration that the fourth most played video was played.

all_videos = {}
with open('/Users/svenkata/Projects/Parsing-Workshop/exercises/video_log_files/logs.txt', 'r') as logfile:
    lines = logfile.readlines()
    print(*lines)
    for line in lines:
        v, u, e, t = line.split()
        if e == "start":
            all_videos[(v, u)] = datetime.datetime.strptime(t, "%m/%d/%Y-%H:%M:%S")
        else:
            duration = datetime.datetime.strptime(t, "%m/%d/%Y-%H:%M:%S") - all_videos[(v, u)]
            all_videos[(v, u)] = duration.seconds

all_videos = sorted(all_videos.items(), key=lambda x:x[1], reverse=True)
most_played = defaultdict(int)
for k, v in all_videos:
    print("Video {} was played by user {} for a duration of {} minutes".format(k[0], k[1], v//60))
    most_played[k[0]] += v//60

key_interest = list(most_played.keys())[3]
print("Duration of fourth most played video ({}) = {}".format(key_interest, most_played[key_interest]))


# PART3: Determine all users that have watched at least three videos simultaneously.
active_videos = defaultdict(set)
user_list = []
with open('/Users/svenkata/Projects/Parsing-Workshop/exercises/video_log_files/logs.txt', 'r') as logfile:
    lines = logfile.readlines()
    for line in lines:
        v, u, e, t = line.split()
        if e == "start":
            active_videos[u].add(v)
        elif e == "stop":
            active_videos[u].discard(v)

        for user, video in active_videos.items():
            if len(video) >= 3:
                user_list.append(user)

print("Users that have watched at least 3 videos simultaneously = {}".format(*user_list))
