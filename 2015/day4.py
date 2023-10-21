import hashlib


def getHash(new_message):
    return hashlib.md5(new_message.encode()).hexdigest()


def findNumber(message, n_zeros):
    key = "0" * n_zeros
    number = 0

    while True:
        new_message = message + str(number)
        hash_md5 = getHash(new_message)
        if hash_md5.startswith(key):
            return (number, hash_md5)
        number += 1


message = input("Introduce your message: ")
n_zeros = int(input("Introduce the number of zeros: "))

print(findNumber(message, n_zeros))
