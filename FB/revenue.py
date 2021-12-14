'''
Revenue Milestones
We keep track of the revenue Facebook makes every day, and we want to know on what days Facebook hits certain revenue milestones.
Given an array of the revenue on each day, and an array of milestones Facebook wants to reach, return an array containing the days on which Facebook reached every milestone.
Signature
int[] getMilestoneDays(int[] revenues, int[] milestones)
Input
revenues is a length-N array representing how much revenue FB made on each day (from day 1 to day N). milestones is a length-K array of total revenue milestones.
Output
Return a length-K array where K_i is the day on which FB first had milestones[i] total revenue. If the milestone is never met, return -1.
Example
revenues = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
milestones = [100, 200, 500]
output = [4, 6, 10]
Explanation
On days 4, 5, and 6, FB has total revenue of $100, $150, and $210 respectively. Day 6 is the first time that FB has >= $200 of total revenue.



revenues = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

10+20+30+40 -> 100 on day 4
100+50+60 -> 210 on day 6
210+70+80+90+100 -> 550 on day 10

return -> [4, 6, 10]

milestones = [100, 200, 500]

return -> [day1, day2, day3...]

'''

def milestone(revenues, milestones):
    s = 0
    rolling = []
    result = []
    for i in range(len(revenues)):
        s+=revenues[i]
        rolling.append(s)

    for milestone in milestones:
        for e, r in enumerate(rolling):
            if milestone<=r:
                result.append(e+1)
                break

    return result


if __name__=="__main__":
    revenues = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    milestones = [100, 200, 500]

    revenues_1 = [100, 200, 300, 400, 500]
    milestones_1 = [300, 800, 1000, 1400]
    expected_1 = [2, 4, 4, 5]

    revenues_2 = [700, 800, 600, 400, 600, 700]
    milestones_2 = [3100, 2200, 800, 2100, 1000]
    expected_2 = [5, 4, 2, 3, 2]

    print(milestone(revenues, milestones))
    print(milestone(revenues_1, milestones_1))
    print(milestone(revenues_2, milestones_2))