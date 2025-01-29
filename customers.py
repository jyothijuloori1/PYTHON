class Customer:
    def __init__(self):
        self.customer_id='213'
        self.first_name='Juluru'
        self.last_name="jyothi"
        self.phone='9381893704'
        self.email='jyothi@gmail.com'
        self.street='krmnght'
        self.city='hyd'
        self.state='Telangana'
        self.zip_code='500079'
    def display(self):
        print(f"{self.customer_id},{self.first_name},{self.last_name},{self.phone},{self.email},{self.street},{self.city}{self.state},{self.zip_code}")
class order(Customer):
    def __init__(self):
        self.order_id='123'
        self.customer_id='213'
        self.order_status='order_placed'
        self.order_date='1/29/25'
        self.req_date='2/2/25'
        self.shipped_date='1/2/25'
        self.store_id='1234'
        self.staff_id='987'
    def display(self):
        print(f"name={self.order_id},{self.customer_id},{self.order_status},{self.order_date},{self.req_date},{self.shipped_date},{self.store_id},{self.staff_id}")

obj1=Customer()
obj1.display()
obj2=order()
obj2.display()
print(obj1.__dict__)
