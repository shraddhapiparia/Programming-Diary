# 252. Meeting Rooms
# Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all meetings.

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if not intervals:
            return True
        intervals.sort()
        prev = intervals[0][1]
        for pair in intervals[1:]:
            if pair[0] < prev:
                return False
            prev = pair[1]
        return True
       
       
# O(nlogn)
