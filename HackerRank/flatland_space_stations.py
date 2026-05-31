#Flatland is a country with a number of cities, some of which have space stations. Cities are numbered consecutively and each has a road of 1km length connecting it to the next city. It is not a circular route, so the first city doesn't connect with the last city. Determine the maximum distance from any city to its nearest space station.
# Example
# n = 3
# c = [1]
# There are n=3 cities and city 1 has a space station. They occur consecutively along a route. City 1 is  unit away and city  is  units away. City 0 is 1 - 0 = 1 units from its nearest space station as one is located there. The maximum distance is 1.
# Function Description
# Complete the flatlandSpaceStations function in the editor below.
# flatlandSpaceStations has the following parameter(s):
# int n: the number of cities
# int c[m]: the indices of cities with a space station
# Returns
# - int: the maximum distance any city is from a space station
# Input Format
# The first line consists of two space-separated integers,  and .
# The second line contains  space-separated integers, the indices of each city that has a space-station. These values are unordered and distinct.
# Constraints
# There will be at least  city with a space station.
# No city has more than one space station.
# Output Format
# Sample Input 0
# STDIN   Function
# -----   --------
# 5 2     n = 5, c[] size m = 2
# 0 4     c = [0, 4]
# Sample Output 0
# 2


def flatlandSpaceStations (n , c):
    c.sort()
    max_distance = c[0]
    
    for i in range(len(c) - 1):
        distance = (c[i+1] - c[i]) // 2
        max_distance = max(max_distance, distance)

    last_distance = (n-1) - c[-1]
    max_distance = max(max_distance, last_distance)

    return max_distance

def main():
    n, m = map(int, input().split())
    c = list(map(int, input().split()))

    result = flatlandSpaceStations(n, c)
    print(result)   

if __name__ == "__main__":
    main()