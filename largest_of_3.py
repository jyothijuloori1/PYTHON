def display(data):
    print(f"the largest is {data}")
def get_input():
    received_a=int(input("a="))
    received_b=int(input("b="))
    received_c=int(input("c="))
   
    return (received_a,received_b,received_c,)
def compute(a,b,c):
    if (a>b & a>c):
        largest=a
    if (b>a & b>c):
        largest=b
    else:
       largest=c
       return largest
def main():
    (a,b,c)=get_input()
    largest=compute(a,b,c)
    display(largest)
main()

   