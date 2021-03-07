def solution(phone_book):
    phone_book.sort()
    temp = str(phone_book[0])
    
    for i in range(1,len(phone_book)):
        if str(phone_book[i])[:len(temp)] == temp:
            return False

        temp = str(phone_book[i])
        
    return True