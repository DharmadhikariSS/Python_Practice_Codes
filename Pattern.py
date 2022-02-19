print('''Star Pattern (Sample 1)

*
**
***
****
*****

This Pattern Will be Printed''')

n = int(input("Enter Value for no. of rows: "))
for i in range(0, n):
    for k in range(0, i+1):
        print("* ", end="")
    print("\n")

print("____________________________________________")
print("____________________________________________")

print(''' Star Pattern (sample 2)

*
**
***
****
*****

This Pattern Will be Printed''')

n = int(input("Enter Value for no. of rows: "))

List = []
for i in range(0, n+1):
    List.append("*"*i)
print("\n".join(List))

print("____________________________________________")
print("____________________________________________")

print(''' Star Pattern With Prior Space 

    *
   **
  ***
 ****
*****

This Pattern Will be Printed''')

n = int(input("Enter Value for no. of rows: "))
a = 2 * n - 2
for i in range(0, n):
    for k in range(0, a):
        print(end=" ")
    a = a - 2

    for k in range(0, i+1):
        print("* ", end="")

    print("\r")


