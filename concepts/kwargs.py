def greet (name , nationality):
    print (f"Name is {name} from {nationality}")
greet ("Kenya","Roy")
# kwargs usage
greet (nationality="Kenya",name="Roy")
# kwargs in an array
def bizz(drinks, price):
    print (f"Available drinks are {drinks [0]} and there prices {price[0]}"  )
bizz(drinks= ["kahawa","Chai"], 
    price= [400,300])

def employee (**kwargs):
    print(kwargs)

employee (name= "Roy",age= 1, degree= "Software Dev")