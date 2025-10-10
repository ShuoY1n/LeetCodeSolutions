"""
Meeting Scheduler
Problem: Find available time slots for two people to meet

Given two people's existing meetings and their available time windows, 
find all possible time slots when both people are free for a meeting.

This question was found on the web.
"""

import math

def timeToString(times):
    """Convert time in minutes to HH:MM format"""
    output = []

    for time in times:
        hours1 = math.floor(time[0] / 60)
        mins1 = time[0] - hours1 * 60
        

        hours2 = math.floor(time[1] / 60)
        mins2 = time[1] - hours2 * 60

        output.append([f"{hours1:02d}:{mins1:02d}", f"{hours2:02d}:{mins2:02d}"])

    return output

def findAvailableTimes(times, window1, window2):
    """Find gaps between meetings"""
    startingTimeIndex = 0
    endingTimeIndex = 1
    startingTime = 0
    endingTime = 0
    output = []

    while endingTimeIndex < len(times):
        endingTime = times[endingTimeIndex][0]
        startingTime = times[startingTimeIndex][1]
        
        if endingTime <= startingTime:
            startingTimeIndex+=1
            endingTimeIndex+=1
            continue
        
        output.append([startingTime, endingTime])
        startingTimeIndex+=1
        endingTimeIndex+=1


    startWindow = 0
    endWindow = 0

    if (window1[0][0] > window2[0][0]):
        startWindow = window1[0][0]
    else:
        startWindow = window2[0][0]

    if (window1[0][1] < window2[0][1]):
        endWindow = window1[0][1]
    else:
        endWindow = window2[0][1]

    

    while output[0][1] < startWindow:
        output.pop(0)
    
    if output[0][0] < startWindow:
        output[0][0] = startWindow
    
    while output[len(output) - 1][0] > endWindow:
        output.pop(len(output) - 1)
    
    if output[len(output) - 1][1] > endWindow:
        output[len(output) - 1][1] = endWindow
    

    if times[len(times) - 1][0] > endWindow:
        times.pop(len(times) - 1)
    
    if times[len(times) - 1][1] < endWindow:
        output.append([times[len(times) - 1][1], endWindow])

    if times[0][0] > startWindow:
        output.append([startWindow, times[0][0]])

    return output

def getTimes(str):
    """Convert time strings to minutes"""
    output = []
    for substr in str:
        min1 = 0
        min2 = 0
        time1 = []
        time2 = []

        time1 = substr[0].split(':')
        min1 = int(time1[0]) * 60 + int(time1[1])
        
        time2 = substr[1].split(':')
        min2 = int(time2[0]) * 60 + int(time2[1])

        output.append([min1, min2])

    return output

def combineTimes(times1, times2):
    """Merge two sorted lists of meetings"""
    output = []
    p1 = 0
    p2 = 0
    i = 0

    while p1 < len(times1) and p2 < len(times2):
        if (times1[p1][0] < times2[p2][0]):
            output.append(times1[p1])
            p1+=1
        else:
            if times1[p1][0] == times2[p2][0] and times1[p1][1] == times2[p2][1]:
                p1+=1

            output.append(times2[p2])
            p2+=1
        i+=1

    while p1 < len(times1):
        output.append(times1[p1])
        p1+=1

    while p2 < len(times2):
        output.append(times2[p2])
        p2+=1
    
    return output

# Test case
if __name__ == "__main__":
    meetings1 = [['9:00', '10:30'], ['12:00', '13:00'], ['16:00', '18:00']]
    timeWindow1 = ['9:00', '20:00']

    meetings2 = [['10:00', '11:30'], ['12:30', '14:30'], ['14:30', '15:00'], ['16:00', '17:00']]
    timeWindow2 = ['10:00', '18:30']

    sampleOut = [['11:30', '12:00'], ['15:00', '16:00'], ['18:00', '18:30']]

    timesInNumFormat = findAvailableTimes(combineTimes(getTimes(meetings1), getTimes(meetings2)), getTimes([timeWindow1]), getTimes([timeWindow2]))
    result = timeToString(timesInNumFormat)
    
    print("Available meeting times:")
    print(result)
    print("\nExpected output:")
    print(sampleOut)
