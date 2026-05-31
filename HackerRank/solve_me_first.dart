/*
Complete the function solveMeFirst to compute the sum of two integers.

Example

a = 7
b = 3

Return 10.

Function Description

Complete the  function with the following parameters:

int a: the first value
int b: the second value
Returns
-int: the sum of a and b

Constraints

1 <= a,b <= 100

Sample Input

a = 2
b = 3
Sample Output

5
Explanation

2+3=5
.
*/


import 'dart:io';

int solveMyFirst(int a, int b){
  return a+b;
}

void main (){
  int a = int.parse(stdin.readLineSync()!);
  int b = int.parse(stdin.readLineSync()!);
  print(solveMyFirst(a,b));
}

