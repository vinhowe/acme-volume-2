# python_intro.py
"""Python Essentials: Introduction to Python.
Vin Howe
<Class>
<Date>
"""


# Problem 1 (write code below)
if __name__ == "__main__":
    print("Hello, world!")

# Problem 2
def sphere_volume(r):
    """ Return the volume of the sphere of radius 'r'.
    Use 3.14159 for pi in your computation.
    """
    PI = 3.14159
    return (4/3)* PI * (r ** 3)


# Problem 3
def isolate(a, b, c, d, e):
    """ Print the arguments separated by spaces, but print 5 spaces on either
    side of b.
    """
    print(a, b, c, end=" ", sep=" "*5)
    print(d, e)


# Problem 4
def first_half(my_string):
    """ Return the first half of the string 'my_string'. Exclude the
    middle character if there are an odd number of characters.

    Examples:
        >>> first_half("python")
        'pyt'
        >>> first_half("ipython")
        'ipy'
    """
    return my_string[:len(my_string)//2]

def backward(my_string):
    """ Return the reverse of the string 'my_string'.

    Examples:
        >>> backward("python")
        'nohtyp'
        >>> backward("ipython")
        'nohtypi'
    """
    return my_string[::-1]


# Problem 5
def list_ops():
    """ Define a list with the entries "bear", "ant", "cat", and "dog".
    Perform the following operations on the list:
        - Append "eagle".
        - Replace the entry at index 2 with "fox".
        - Remove (or pop) the entry at index 1.
        - Sort the list in reverse alphabetical order.
        - Replace "eagle" with "hawk".
        - Add the string "hunter" to the last entry in the list.
    Return the resulting list.

    Examples:
        >>> list_ops()
        ['fox', 'hawk', 'dog', 'bearhunter']
    """
    items = ["bear", "ant", "cat", "dog"]
    print(items)
    items.append("eagle")
    print(items)
    items[2] = "fox"
    print(items)
    items.pop(1)
    print(items)
    items.sort(reverse=True)
    print(items)
    items[items.index("eagle")] = "hawk"
    print(items)
    items[-1] += "hunter"
    print(items)


# Problem 6
def pig_latin(word):
    """ Translate the string 'word' into Pig Latin, and return the new word.

    Examples:
        >>> pig_latin("apple")
        'applehay'
        >>> pig_latin("banana")
        'ananabay'
    """
    if word[0] in "aeiou":
        print(f"{word}hay")
    else:
        print(f"{word[1:]}{word[0]}ay")


# Problem 7
def palindrome():
    """ Find and return the largest panindromic number made from the product
    of two 3-digit numbers.
    """
    def is_palindromic(n):
        str_n = str(n)
        return str_n == str_n[::-1]

    largest = -1
    largest_operands = None
    for i in range(100, 1000):
        for j in range(100, 1000):
            product = i*j
            if is_palindromic(product):
                largest = product
                largest_operands = (i, j)
    return largest_operands, largest


# Problem 8
def alt_harmonic(n):
    """ Return the partial sum of the first n terms of the alternating
    harmonic series, which approximates ln(2).
    """
    return sum(((-1)**(i + 1)) / i for i in range(1, n))


if __name__ == "__main__":
    # print(sphere_volume(2))
    # isolate(1, 2, 3, 4, 5)
    # print(first_half("python"))
    # print(first_half("ipython"))
    # print(backward("python"))
    # print(backward("ipython"))
    # list_ops()
    # pig_latin("apple")
    # pig_latin("banana")
    # print(palindrome())
    # print(alt_harmonic(500000))
