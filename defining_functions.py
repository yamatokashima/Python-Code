# finding largest palindrome from the product of 2 2-digit numbers:

def pal(n):
    return str(n) == str(n)[::-1]


def largest_pal():
    start = 0
    for num1 in range(10, 100):
        for num2 in range(10, 100):
            large_pal = num1 * num2
            if pal(large_pal) and large_pal > start:
                start = large_pal
    return start


print(largest_pal())

# list of all even numbers between 18 and 47

even_numbers = [x for x in range(18, 48) if x % 2 == 0]
print(even_numbers)

# list of qsquares of even numbers between 1 and 20:

even_squares = []
for i in range(2, 21, 2):
    even_squares.append(i**2)

print(even_squares)

# sum of cubes between 7 and 37

sum_cube = 0
for i in range(7, 38):
    sum_cube += i**3

print(sum_cube)

# list of all numbers divisible by 3, 5, or both between 1 and 30:

numb = [i for i in range(1, 30) if (i % 3 == 0 and i %
                                    5 == 0) or i % 3 == 0 or i % 5 == 0]

print(numb)

# make below list uppercase:

friends = ['Alice', 'Bob', 'Charlie', 'Derek']

upfriends = []
for name in friends:
    upfriends.append(name.upper())
print(upfriends)

# remove names that don't end in vowel:


def condense(friends):
    vowels = 'aeiou'
    return [friend for friend in friends if friend[-1] in vowels]


print(condense(friends))

# converting Euro to Dollar (Euro * 1.1):

euros = [4.50, 6.70, 3.25, 9.99, 12.75, 0.35]

dollars = [round(euro * 1.1, 2) for euro in euros]
print(dollars)

# showing people > 60 inches tall:

heights = [71, 48, 55, 65, 68, 60, 58, 53]

tall_enough = [height for height in heights if height > 60]
print(tall_enough)

# "tall enough" or "too short" for heights:

all_heights = [height if height > 60 else "None" for height in heights]
print(all_heights)

# creating pairs from seperate lists:

letters_a = ['A', 'B', 'C', 'D', 'E']
letters_z = ['Z', 'Y', 'X', 'W', 'V']

# long-hand to better understand step-by-step
biglist = list(zip(letters_a, letters_z))

fl = []
for index in biglist:
    tl = ''
    for char in index:
        tl += char
    fl.append(tl)
print(fl)

biglist = [''.join([x, y]) for x, y in zip(
    letters_a, letters_z)]  # list comprehension version
print(biglist)

# using enumerate

i = 2
for i, letter in enumerate(letters_a):
    print(f"{letter} is letter {i+1} of the alphabet")

# grade based on scores


def letter_grade(grade):
    if grade >= 90:
        return "A"
    elif grade >= 80:
        return "B"
    elif grade >= 70:
        return "C"
    elif grade >= 60:
        return "D"
    else:
        return "F"


print(letter_grade(89))

# grade based on list of scores


def letter_grades(grades):
    return [letter_grade(grade) for grade in grades]


print(letter_grades([42, 92, 82]))

# vowel count in word

# phrase = 'General Assembly'
# vowels = 'aeiouAEIOU'
# for letter in phrase:
#     vowel_count = 0
#     for count in letter:
#         if count in vowels:
#             vowel_count += 1
#         else:

#     print(phrase,str(vowel_count))


def vowel_count(phrase):
    vowels = 'aeiouAEIOU'
    count = 0
    for letter in phrase:
        if letter in vowels:
            count += 1
    return count

# every one letter uppercase:


def toggle_case(sentence):
    result = ''
    for letter in sentence:
        if letter in 'aeiouAEIOU':
            result += letter.lower()
        else:
            result += letter.upper()
    return result

# remove vowels in all words except words <= 1 letter


def smart_disemvowel(sentence):
    words = sentence.split()
    result = []
    for word in words:
        if len(word) > 1:
            result.append(disemvowel(word))
        else:
            result.append(word)
    return ' '.join(result)

# word reverser


def word_reverser(sentence):
    words = sentence.split()
    words = words[::-1]
    reversed_sentence = ' '.join(words)
    return reversed_sentence

# letter in word reverser


def letter_reverser(sentence):
    reversed_words = []
    for word in sentence.split():
        reversed_word = word[::-1]
        reversed_words.append(reversed_word)
    return " ".join(reversed_words)
