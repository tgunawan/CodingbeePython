
def filter_bad_words(text, bad_words):
  words = text.lower().split()
  filtered_words = []
  for word in words:
    cleaned_word = ''.join(filter(str.isalnum, word))  
    if cleaned_word in [bw.lower() for bw in bad_words]:
      filtered_words.append("*" * len(word))
    else:
      filtered_words.append(word)
  return " ".join(filtered_words)

# contoh
bad_word_list = ["heck","damn", "hell", "idiot"]
user_input = input("Enter your text: ")
filtered_output = filter_bad_words(user_input, bad_word_list)
print(f"Original: {user_input}")
print(f"Filtered: {filtered_output}")

user_input_2 = "What the heck? Is that an i.dio.t?"
filtered_output_2 = filter_bad_words(user_input_2, bad_word_list)
print(f"Original: {user_input_2}")
print(f"Filtered: {filtered_output_2}")