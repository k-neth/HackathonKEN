
def entryPrompt():
    enternum = input("Enter a list of integers separated by spaces: ")
    return enternum
    
def myFunction(enternum):
    try:
        num_list = list(map(int, enternum.split()))
    
        uniquenums = list(set(num_list))

        uniquenums.sort(reverse=True)

        print(uniquenums)

    except ValueError:
        print( "invalid input")
        

def myOutput():
    while True:
        enternum=entryPrompt()
        myFunction(enternum)
    
myOutput()


   
   

