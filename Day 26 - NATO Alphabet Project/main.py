import pandas

nato_data = pandas.read_csv('nato_phonetic_alphabet.csv')
nato_dict = {row.letter:row.code for (index,row) in nato_data.iterrows()}

def nato_coder():
    chosen_word = input("Enter a word: ").upper()

    try:
        phonetic_code = [nato_dict[letter] for letter in chosen_word]
    except KeyError:
        nato_coder()
    else:
        print(phonetic_code)

nato_coder()