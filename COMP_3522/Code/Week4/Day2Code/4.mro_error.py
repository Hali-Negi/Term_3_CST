class F: 
    remember2buy = 'Milk' 

class E(F): 
    remember2buy = 'Eggs' 

class G(F,E): 
    pass 


print(G.__mro__)

