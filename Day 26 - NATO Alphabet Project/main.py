import pandas

nato_data = pandas.read_csv('nato_phonetic_alphabet.csv')
nato_dict = {row.letter:row.code for (index,row) in nato_data.iterrows()}
chosen_word = input("Enter a word: ").upper()
phonetic_code = [nato_dict[letter] for letter in chosen_word]
print(phonetic_code)