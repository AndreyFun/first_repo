import sys
import importlib

def basel():
    if len(sys.argv) != 2:
        print(f"Usage : {sys.argv[0]} cuntry")
        sys.exit(1)
    country = sys.argv[1]
    country = country.lower()
    if country == "ukraine":
        print("SUN")
    elif country == "uermany":
        print("Raining")
    else : 
        print("I don't now")    
        sys.exit(1)
if __name__ == "__main__":   
    basel()     
        