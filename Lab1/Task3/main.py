from list_func import get_evens

while True:
    try:
        entered_list = list(map(int, input("Enter space-separated integer numbers: ").split()))
        break
    except:
        print("Incorrect input")
        
print(get_evens(entered_list))