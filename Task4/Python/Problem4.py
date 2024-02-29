'''
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

'''

#Given code has used type conversion for solution come up with a code that not uses type conversion.
#You need to correct complete function body.
#Do not change class name and method name.

class Solution {
public:
    string addBinary(string a, string b) {
        string result;
        int carry = 0;
        int i1 = a.length() - 1;
        int i2 = b.length() - 1;
        while (i1 >= 0 || i2 >= 0 || carry > 0) {
            int v1 = i1 >= 0 ? a[i1] - '0' : 0;
            int v2 = i2 >= 0 ? b[i2] - '0' : 0;
            int sum = v1 + v2 + carry;
            result.push_back((sum & 1) + '0');
            carry = (sum >> 1) & 1;
            i1--;
            i2--;
        }
        
        reverse(begin(result), end(result));
        return result;
    }
}