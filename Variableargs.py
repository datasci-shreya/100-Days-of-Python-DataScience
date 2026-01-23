#variable argument type
def Addition(*No):
    print(No)
    print(type(No)) #tuple #double are allowed 
    print(len(No))  

def main():
    Addition(11,21,51,101)

if __name__ == "__main__":
    main()