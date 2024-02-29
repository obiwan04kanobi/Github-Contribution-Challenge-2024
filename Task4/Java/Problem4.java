/**

Given two binary strings a and b, return their sum as a binary string.

Example 1:
Input: a = "11", b = "1"
Output: "100"

Example 2:
Input: a = "1010", b = "1011"
Output: "10101"
 

Constraints:

1 <= a.length, b.length <= 104
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.

**/

//Given code has used type conversion for solution come up with a code that not uses type conversion
//You need to correct complete function body.
//Do not change class name and method name.

import java.math.BigInteger; 
 
class Solution { 
    public String addBinary(String a, String b) { 
        BigInteger aInt = new BigInteger(a, 2); 
        BigInteger bInt = new BigInteger(b, 2); 
         
        BigInteger additionNoCarry = aInt.xor(bInt); 
        BigInteger carry = aInt.and(bInt).shiftLeft(1); 
         
        while (carry.signum() != 0) { 
            BigInteger newAdditionNoCarry = additionNoCarry.xor(carry); 
 
            carry = additionNoCarry.and(carry).shiftLeft(1);             
            additionNoCarry = newAdditionNoCarry; 
        } 
         
        return additionNoCarry.toString(2); 
    } 
} 