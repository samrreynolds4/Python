Letters = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
           'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' )
Numbers = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
           0, 0 ]

Message = input("Enter a sentence: ")

Low = 0
High = len(Letters)
Mid = int((High + Low)/2)
Found = 0
if 'a' > 'b':
    print("true")
else:
    print("false")
Message.replace(' ', "")
Message.lower()


for i in range(len(Message) - 1):

    Low = 0
    High = len(Letters)
    Mid = int((High + Low)/2)
    
    while(Found == 0):

        if Message[i] == Letters[Mid]:
            Numbers[Mid] = Numbers[Mid]+1
            print(Message[i], " Found: ", ++Numbers[Mid])
            break
        if Message[i] > Letters[Mid]:
            Low = Mid
            Mid = int((High + Low)/2)
        elif Message[i] < Letters[Mid]:
            High = Mid
            Mid = int((High + Low)/2)
        else:
            print("Not found")
            break
        
    
        
