morse_code_dict = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    ' ': ' '  # Space between words
}

morse_to_alphabet = {
    '.-': 'A',
    '-...': 'B',
    '-.-.': 'C',
    '-..': 'D',
    '.': 'E',
    '..-.': 'F',
    '--.': 'G',
    '....': 'H',
    '..': 'I',
    '.---': 'J',
    '-.-': 'K',
    '.-..': 'L',
    '--': 'M',
    '-.': 'N',
    '---': 'O',
    '.--.': 'P',
    '--.-': 'Q',
    '.-.': 'R',
    '...': 'S',
    '-': 'T',
    '..-': 'U',
    '...-': 'V',
    '.--': 'W',
    '-..-.': 'X',
    '-.--': 'Y',
    '--..': 'Z',
    ' ': ' '  # Space between words
}


def word_to_morse(word):
    word = word.upper()
    morse_code = ""
    invalid_char_count = 0  # Counter for invalid characters

    for char in word:
        if char in morse_code_dict:
            morse_code += morse_code_dict[char] + ' '
        elif char == ' ':
            morse_code += ' '
        else:
            invalid_char_count += 1

    if invalid_char_count > 0:
        print(f"Your input includes {invalid_char_count} invalid character(s) that were neglected during the conversion")

    return morse_code


def morse_to_word(morse_code):
    english_word = ""
    current_morse = ""
    invalid_char_count = 0  # Counter for invalid characters

    for char in morse_code:
        if char in ('.', '-'):
            current_morse += char
        elif char == ' ':
            if current_morse in morse_to_alphabet:
                english_word += morse_to_alphabet[current_morse]
            else:
                invalid_char_count += 1
            current_morse = ""
        else:
            invalid_char_count += 1

    if current_morse in morse_to_alphabet:
        english_word += morse_to_alphabet[current_morse]

    if invalid_char_count > 0:
        print(f"Your input includes {invalid_char_count} invalid character(s) that were neglected during the conversion")

    return english_word


def test_word_morse_conversion():
    method = input("Choose a method (word to morse or morse to word): ")

    if method.lower() == "word to morse":
        word = input("Enter the word to convert to Morse code: ")
        morse_code = word_to_morse(word)
        print("Morse code:", morse_code)
    elif method.lower() == "morse to word":
        morse_code = input("Enter the Morse code to decode: ")
        word = morse_to_word(morse_code)
        print("Decoded word:", word)
    else:
        print("Invalid method. Please choose either word to Morse or Morse to word.")

test_word_morse_conversion()

