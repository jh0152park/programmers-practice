def solution(phone_book):
    phone_book.sort()
    for i in range(1, len(phone_book)):
        prev_len = len(phone_book[i-1])
        if phone_book[i-1] == phone_book[i][:prev_len]:
            return False
    return True