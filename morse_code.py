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

morse_to_alphabet={
    

    
    
    '.': 'A',
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
def word_to_morse(word):
    word = word.upper()
    morse_code = ""
    for char in word:
        morse_code += morse_code_dict[char]
        if char != ' ':
            morse_code += ' '
    return morse_code
word="mohamed"
print(word_to_morse(word))

def morse_to_word(morse_code):
    english_word = ""
    current_letter = ""

    for char in morse_code:
        if char == '.':
            current_letter += '.'
        elif char == '-':
            current_letter += '-'
        elif char == ' ':
            if current_letter in morse_to_alphabet:
                 english_word+= morse_to_alphabet[current_letter]
            current_letter = ""
        else:
            # Handle unknown characters
            pass

    if current_letter in morse_to_alphabet:
        english_word+= morse_to_alphabet[current_letter]

    return english_word
morse_code="-- --- .... .- -- . -.."
print(morse_to_word(morse_code))
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
test=test_word_morse_conversion()
print(test)
