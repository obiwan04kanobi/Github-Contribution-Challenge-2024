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

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        n=len(a)
        m=len(b)
        def add(a,b,n,m):
            c=""
            i=-1
            crr="0"
            while m!=0:
                if a[i]!=b[i]:
                    if crr=="0":
                        c="1"+c
                        crr="0"
                    else:
                        c="0"+c
                        crr="1"
                elif a[i]=="0":
                    if crr=="0":
                        c="0"+c
                        
                    else:
                        c="1"+c
                else:
                    if crr=="0":
                        c="0"+c
                        crr="1"
                    else:
                        c="1"+c
                i=i-1
                m=m-1
            if crr=="1":
                c="1"+c
            return c
        if n>=m:
            res=add(a,b,n,m)
        else:
            res=add(b,a,m,n)
        
                        







        return res
abc=Solution()
print(abc.addBinary("1010","1101"))