def display(data):
    print(f"the average is {data}")
def get_input():
    received_a=int(input("a="))
    received_b=int(input("b="))
    received_c=int(input("c="))
    received_d=int(input("d="))
    return (received_a,received_b,received_c,received_d,)
def compute(a,b,c,d):
    average=(a+b+c+d)/4
    return average
def main():
    (a,b,c,d)=get_input()
    average=compute(a,b,c,d)
    display(average)
main()
    