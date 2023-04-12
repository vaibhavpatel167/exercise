""Suppose you are buying something online on amazon.com 

On the website, you get
a 15% discount if you are a prime member. Additionally, you are also getting a discount of 8% on the item because it's black Friday sales.

Write a function that takes as input the amount of the asset that you are buying and a logical variable indicating whether you are a prime member applies the discount offered appropriately and returns the result.""
def calculate_price(amount, is_prime_member):
    discount_rate = 0.0
    
    if is_prime_member:
        discount_rate += 0.15
    discount_rate += 0.08
    final_price = amount * (1 - discount_rate)
    
    return final_price

price_without_discount = 5000 
is_prime_member = False

final_price = calculate_price(price_without_discount, is_prime_member)
print(final_price) 



"""Problem 2:

Chit Chat Application - Function:

(a) In few chit-chat programs, there is a limitation on the number of letters that you can send to your family and friends.

Write a function that takes as input the,

message and checks whether the number of letters is less than 200 or above. If the length of the information is less than 200, the chat should be returned.


If the length of the chat is greater than 200, data consisting of only the first 200 characters should be returned.


(b) How one can check if the restriction is on a number of words rather than letters?
Write a function that allows a message with only 30 words."""
def check_message_length(message):
    if len(message) <= 200:
        return message
    else:
        return message[:200]
def check_message_length(message):
    words = message.split()
    if len(words) <= 30:
        return message
    else:
        return ' '.join(words[:30])