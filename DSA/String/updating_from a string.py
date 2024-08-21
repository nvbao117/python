string1 = "Hello,I'm Bao"
print("initial string : ")
print(string1)

list1 = list(string1)
list1[2] = 'p'
string2 = "".join(list1)
print(string2)
string3 = string1[0:2] +'p' + string1[3:]
print(string3)


print("Delete_a_character")
string1 = "Hello,I'm Bao"
print("initial string:")
print(string1)
print("deleting character at 2nd index:")
string2 = string1[0:2]+string1[3:]
print(string2)