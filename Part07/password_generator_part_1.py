# Write your solution here
from string import ascii_lowercase
from random import sample

def generate_password(len: int) -> str:
    return "".join(sample(ascii_lowercase,len))
    
