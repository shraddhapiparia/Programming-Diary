# 1360. Number of Days Between Two Dates 

# Example 1:

# Input: date1 = "2019-06-29", date2 = "2019-06-30"
# Output: 1
# Example 2:

# Input: date1 = "2020-01-15", date2 = "2019-12-31"
# Output: 15

class Solution:
    def isLeapYear(self, year):
        return year%4 == 0 and year%100 != 0 or year%400 == 0
    
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        diff = 0
        days = [31,28,31,30,31,30,31,31,30,31,30,31]
        if date1 >date2:
            date1, date2 = date2, date1
        y1,m1,d1 = map(int, date1.split("-"))
        y2,m2,d2 = map(int, date2.split("-"))
        for year in range(y1,y2):
            diff += 365+self.isLeapYear(year)
        days[1] = 29 if self.isLeapYear(y1) else 28
        diff -= sum(days[:m1-1])+ d1 
        days[1] = 29 if self.isLeapYear(y2) else 28
        diff += sum(days[:m2-1])+ d2
        return diff
