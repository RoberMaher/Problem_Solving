/*
 Problem

Given an array of integers, find the sum of its elements.

 Function Description

Complete the function:

simpleArraySum(ar)
Parameters:
ar: an array of integers
Returns:
An integer representing the sum of the array elements.
 Input Format
The first line contains an integer n (the size of the array).
The second line contains n space-separated integers.
 Output Format
Print a single integer: the sum of the array elements.
 Constraints
1≤n≤10
5
0≤ar[i]≤10
9
 Sample Input
6
1 2 3 4 10 11
 Sample Output
31
 Explanation

Sum the elements:

1 + 2 + 3 + 4 + 10 + 11 = 31
 */

#include <stdio.h>

int simpleArraySum(int ar[] , int n) {
  int sum = 0;
  for (int i = 0 ; i < n ; i++) {
    sum += ar[i];
  }
  return sum;  
}

int main() {
  int n;
  scanf("%d", &n);

  int ar[n];
  for (int i = 0 ; i < n ; i++) {
    scanf("%d", &ar[i]);
  }

  int result = simpleArraySum(ar, n);
  printf("%d\n", result);

}
