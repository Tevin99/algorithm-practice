def solution(phone_book):
    # Sort the list so possible prefix pairs become adjacent
    phone_book.sort()
    
    # Compare each number with the next one
    for i in range(len(phone_book) - 1):
        # If the next number starts with the current one,
        # a prefix exists → return False
        if phone_book[i + 1].startswith(phone_book[i]):
            return False
    
    # No prefix found
    return True