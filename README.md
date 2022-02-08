# Infosys-certification-problem

## Problem Statement

Concider a non-empty array of position integers inarr. Identify and print outarr based onn the below logic:
  * For each element in inarr, starting from the left-most element. Generate a sequence of numbers such that:
    * Starting number in the sequence is element
    * Next number in the sequence is generated based on the current number such that:
      * If the current number is even, divide it by 2 to get the next number in the sequence 
      * If the current number is odd, multiply it by 3 and add 1 get the next number in the sequence
    * Repeat the above steps and keep generating the numbers until the number 1 is generated
  * Identify the count of numbers for each of the sequence generated
  * In the order of occurence of elements in inarr, add the corresponding identified counts to outarr
  
  **Note**: Each sequence will always reach 1 in finite number of steps <br/>
  
  **Input format**: <br />
  
    First line contains the elements of inarr separated by " "(space).
    Read the input from standard input stream.
  **Output format**:
  
    Print outarr with the elements separated by ',' to the standard output stream.
    
| Sample Input  | Sample Output | 
| ------------- | ------------- | 
| 10 100        | 7,26          | 

## Explanation
The elements of the given inarr are 10,100. <br />
The sequence generated for each element starting from the left most element of inarr and their corresponding count are: <br/>
 * For 10: Starting number of the sequence is 10. Since 10 is even the 2nd number of the sequence is 10/2=5. Since 5,the 2nd number of the sequence, is odd the 3rd number in the sequence is ((5*3)+1)=16. Similarly by repeating the steps the sequence generated for element 10 is: <br />
 10, 5, 16, 8, 4, 2, 1  <br />
 The count of the numbers in the sequence is 7
 
 * For 100: Using Similar rules , The count of the numbers is 26.
