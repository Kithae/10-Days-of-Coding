def simple_multiplication_table(n):
    for a in range (1,11):
#the table shows products of numbers between 1 and 10
        for b in range (1,1+n):
 #n is a user defined number
            print (a * b, end= '\t')
        print ()
prod = int (input("enter the number: ")) #value of n
simple_multiplication_table(prod)
