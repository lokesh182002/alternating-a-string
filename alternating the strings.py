str1=input("enter string1:")
str2=input("enter string2:")
str3=""
len1=len(str1)
len2=len(str2)
if len1==len2:
    for i in range(len1):
        str3=str3+str2[i]
        str3=str3+str1[i]
    print("resultant string after alternating characters:",str3)
else:
    print("both strings are not same length")
