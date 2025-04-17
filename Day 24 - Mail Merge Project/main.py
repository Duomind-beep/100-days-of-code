with open('Input/Names/invited_names.txt') as invited_names:
    for name in invited_names.readlines():
        stripped_name = name.strip()
        with open('Input/Letters/starting_letter.txt') as letter:
            draft = letter.read()
            new_letter = draft.replace('[name]', stripped_name)
            with open(f'Output/ReadyToSend/letter_for_{stripped_name}.txt', mode='w') as final_draft:
                final_draft.write(new_letter)
