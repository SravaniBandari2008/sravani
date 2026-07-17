#from array import *
#a = array("i",[1,2,3,4,5])
#print (a)
#print(a.typecode)
#print(a.insert(2,10))
#from array import *
#a = array("i",[])
#n= int (input("enter the number:"))
#for i in range(0,n):
#   a.append(int(input("enter the next number")))
#for x in a:
#    print(x, end=" ")

#str = "engineer."
#print(str.endswith("er."))
#print(str.replace("g","e"))
#print(str.find("i"))
#print(str.count("e"))
#print(str.capitalize())
#print(str[0:8])
  

#contacts = ["rahul", "riya", "remo", "sagar", "harshith"]


#if "remo" in contacts:
 #   index = contacts.index("remo")
  #  contacts[index] = "saketh"


#print("Updated Contact List:")
#for contact in contacts:
#    print(contact)

#input:[1,2,3,4,5]
#def find_max(arr):
#   max_val= arr[0]
#  for num in arr:
#     if num > max_val:
#       max_val = num
#return max_val

#print (find_max([3,7,2,9,1]))
#sum of array elements
#def sum_array(arr):
#    total=0
#    for num in arr:
 #       total = total + num
#    return total
#print(sum_array([1,2,3,4,5]))
#reverse in array
#def reverse_array(arr):
#    reversed_arr = []
  #  for i in range(len(arr)-1, -1, -1):
  #      reversed_arr.append(arr[i])
#   return reversed_arr

#print(reverse_array([1,2,3,4,5]))

# Remove duplicates in an array

#rotate array
#t(rotate_array([1, 2, 3, 4, 5,6], 2))





    # Strings
#def count_characters(text):
    #counts = {}
    #for char in text:
   #     if char in counts:
  #          counts[char] += 1
 #       else:
#            counts[char] = 1
#return counts


#print(count_characters("college"))

#check is string is anagram
#def is_anagram(str1, str2):
   # if len(str1) != len(str2):
        #return False
  #  return sorted(str1) == sorted(str2)

#print(is_anagram("listen", "silent"))  
#print(is_anagram("tide", "diet"))

# check the longest word in a string
#def longest_word(text):
  #  words = text.split()
   # longest = ""
    #for word in words:
     #   if len(word) > len(longest):
      #      longest = word
    #return longest

#print(longest_word("I am a nonchalant person"))

#find missing number
#n = 5
#numbers = [1, 2, 4, 5]
#expected_sum = n * (n + 1) // 2
#actual_sum = sum(numbers)
#missing_number = expected_sum - actual_sum
#print(missing_number)

#two sum problem
#def two_sum(numbers, target):
  #  num_dict = {}
   # for i, num in enumerate(numbers):
    #    complement = target - num
     #   if complement in num_dict:
      #      return [num_dict[complement], i]
       # num_dict[num] = i
    #return []
#num=[2, 7, 11, 15]
#target=9
#print(two_sum(num, target))

#move zeros to the end of an array

#def move_zeros(arr):
  #  non_zero_index = 0 #non zero index stores the index of the next non-zero element
   # for i in range(len(arr)): #loops through every index
    #    if arr[i] != 0: #check if the current element is non-zero
     #      arr[non_zero_index] = arr[i]
      #      non_zero_index += 1
    #while non_zero_index < len(arr):
     #   arr[non_zero_index] = 0
      #  non_zero_index += 1
    #return arr

#print(move_zeros([0, 1, 0, 3, 12]))

#count vowels and consonants in a string
#def count_vowels_consonants(text):
  #  vowels = "aeiouAEIOU"
   # vowel_count = 0
    #consonant_count = 0
    #for char in text:
     #   if char.isalpha():
      #      if char in vowels:
       #
       #    else:
        #        consonant_count += 1
    #return vowel_count, consonant_count

#text = "Hello, World!"
#vowels, consonants = count_vowels_consonants(text)
#print("Vowels:", vowels)
#print("Consonants:", consonants)

#first non-repeating character in a string
#def first_non_repeating_character(text):
  #  char_count = {}
   # for char in text:
    #    if char.isalpha():
     #       char_count[char] = char_count.get(char, 0) + 1
    #for char in text:
     #   if char.isalpha() and char_count[char] == 1:
      #      return char
    #return None
#text = "guess"
#result = first_non_repeating_character(text)
#if result:
#    print("First non-repeating character:", result)
#else:
#    print("No non-repeating character found.")

#check panagram
#def is_pangram(text):
  # alphabet = set("abcdefghijklmnopqrstuvwxyz")
   #text_set = set(text.lower())
   #return alphabet.issubset(text_set)

#text = "pack my box with five dozen liquor jugs"
#if is_pangram(text):
#    print("The text is a pangram.")
#else:
#    print("The text is not a pangram.")

#string compression
#def string_compression(text):
   # compressed = ""
    #count = 1

    #for i in range(len(text)):
     #   if i < len(text) - 1 and text[i] == text[i + 1]:
      #      count += 1
       # else:
        #    compressed += text[i] + str(count)
         #   count = 1

    #return compressed
#text = "aaabbccccd"
#result = string_compression(text)
#print("Compressed String:", result)

#find all substring
# Input string
s = input("Enter a string: ")

# Print all substrings
n = len(s)

for i in range(n):
    for j in range(i + 1, n + 1):
        print(s[i:j])
