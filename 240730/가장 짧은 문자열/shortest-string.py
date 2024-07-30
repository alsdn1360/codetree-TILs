str1 = input()
str2 = input()
str3 = input()

sub = max(len(str1), len(str2), len(str3)) - min(len(str1), len(str2), len(str3))

print(sub)