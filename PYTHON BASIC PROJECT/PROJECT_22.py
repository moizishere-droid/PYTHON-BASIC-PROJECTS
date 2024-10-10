def Table():
    number = int(input("Enter the number of which you want to geneartaed table: "))
    for a in range(1,11):
        print(f"{number} x {a} = {number*a}")

Table()