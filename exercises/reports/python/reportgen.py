import re
import datetime
# Exercises
# For each event except for End events, add the end time, e.g. the first line in the example above should read 09:20-10:00 Breakfast Presidio.
with open('/Users/svenkata/Projects/Parsing-Workshop/exercises/reports/example.txt', 'r') as file:
    times = []
    events = []
    rooms = []
    lines = file.readlines()
    for line in lines:
        logline = line.split()
        time, event = logline[0], logline[1]
        if len(logline) > 2:
            room = " ".join(logline[2:])
        times.append(time)
        events.append(event)
        if room:
            rooms.append(room)

with open('/Users/svenkata/Projects/Parsing-Workshop/exercises/reports/output.txt', 'w+') as output:
    for i in range(len(times)-1):
        output.write("{}-{} {} {}\n".format(times[i], times[i+1], events[i], rooms[i]))
    output.write("{} {}\n".format(times[-1], events[-1]))



# Compute the total number of minutes each event type occupies over all days, e.g. your output should have one line for each event type: Exercises 20 minutes.
with open('/Users/svenkata/Projects/Parsing-Workshop/exercises/reports/output.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        if 'End' not in line:
            logline = line.split()
            time, event = logline[0], logline[1]
            start, end = time.split("-")
            end = datetime.datetime.strptime(end, "%H:%M")
            start = datetime.datetime.strptime(start, "%H:%M")
            duration = (end - start).seconds // 60
            print("Event {} runs for {} minutes".format(event, duration))

# Repeat exercise 2 with respect to each room.
with open('/Users/svenkata/Projects/Parsing-Workshop/exercises/reports/output.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        if 'End' not in line:
            logline = line.split()
            time, event = logline[0], logline[1]
            room = ''
            if len(logline) > 2:
                room = ' '.join(logline[2:])
            start, end = time.split("-")
            end = datetime.datetime.strptime(end, "%H:%M")
            start = datetime.datetime.strptime(start, "%H:%M")
            duration = (end - start).seconds // 60
            if room != '':
                print("Event runs for {} minutes in room {}".format(duration, room))

# In addition to the total number of minutes, output the percentage of time for each event type, e.g. Exercises 20 minutes 12%.
# Repeat exercise 4 with respect to reach room.