# hashing.py
# It distribute hash values unformly accrosss hash table
# collosion =: same hash value for more then one key/input
# Direct Chaning: Implimenting the bucket as the linked lis. Colliding elements are stored in this lists
# Open Addressing: Colliding elements are stored in other vacent buckets. During storage and llokups 
# these are ound through so called Probing
# Linear probing:
# Quadratic Probing: 
# Double hasing: use two hash function and add the hash values for elements to get the key value.
#  
def mod(numbers, cell_number):
    return numbers % cell_number
mod(400, 24)

## ASCII function
def mod_ascii(string, cell_number):
    total = 0
    for i in string:
        total += ord(i)
    return total % cell_number

mod_ascii('abc', 24)