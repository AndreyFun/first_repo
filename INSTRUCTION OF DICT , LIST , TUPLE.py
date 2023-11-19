#def my_sum(*elements):
    #for i in elements:
        #print(f"elements : {i}")
   # print(f"A : {a}; B : {b}")  
#args = {"a" :3 , "b" : 4}
#args = [2, 3 ]
#my_sum(*args)          

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>      (TUPLE INSTRUCTIONS) <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

##print(f"dimension amound : {len(point)}")
##point = (1 , "iu" , 3 ,4 ,5 , 6 , "p")

##print(point[:4+3])

##x, y, z ,_ ,_ ,o,p = point

##print(type(y))
##coordinate = "Coordinates : "
##print(f"X: {x} ; Y: {y}; Z: {z} ; K : {o}")
    
##for num in point: 
 #       coordinate += f"{num};"
 #   print(coordinate)    

##break
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>   LIST INSTRUCTIONS : <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

#point = [1 , "iu" , 3 ,4 ,5 , 6 , "p"]
#point.append(83)
#print(f"dimension amound : {len(point)}")

#print(point[:4+3])

#x, y, z ,_ ,_ ,o,p,_ = point

#print(type(y))
#print(f"X: {x} ; Y: {y}; Z: {z} ; K : {o}")

#print(point)
#coordinate = "Coordinates : "
#for num in point: 
    
#    coordinate += f"{num};"
#print(coordinate)    
#point.pop()

#print(point)  
 
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>      DICT INSTRUCTIONS :      <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<   
        
    
EASY = {"first" : 321 , "second" : 123, "third" : 333,"4" : 4 }

_ , y , z ,_= EASY.values()
print(f"Y : {y}; X : {z}")

coordinate = "coordinate : "
for var , value in EASY.items():
    coordinate += f" {var} : {value};"
print(coordinate)    

print(EASY)

a = {}
a['name'] = "Dima"
a['surname'] = "Ivanov"
print(a)
del a ['name']
print(a)

  
