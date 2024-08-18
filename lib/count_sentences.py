#!/usr/bin/env python3

class MyString:
    def __init__(self, value=''):
        self.value = value if isinstance(value, str) else ''

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if isinstance(new_value, str):
            self._value = new_value
        else:
            print("The value must be a string.")
            self._value = ''

    def is_sentence(self):
        return self.value.endswith('.')

    def is_question(self):
        return self.value.endswith('?')

    def is_exclamation(self):
        return self.value.endswith('!')

    def count_sentences(self):
        sentences = [s.strip() for s in self.value.replace('!', '.').replace('?', '.').split('.') if s.strip()]
        return len(sentences)

# Example usage
string = MyString(123)  # This should print: "The value must be a string."
print(string.value)  # Output: '' (empty string)



# year_of_birth = input("\nEnter your year of birth:  ")
# age = 2024 - int(year_of_birth)
# print(f"\nYou are  {age} years old")  # f-string formatting

# fruits = ["banana", "mango", "orange", "pineapple"]

# for fruit in fruits:
#     print(fruit)
#     if fruit == "mango":
#         break
#     else:
#         print("I love " + fruit)
        
