from string import ascii_uppercase

f = open('enc.txt', 'r')
input_txt = f.read()
encrypted_txt = input_txt.upper()

num_chars = sum(char.isalpha() for char in list(encrypted_txt))
print(num_chars)

txt_frequencies = {}
for char in ascii_uppercase:
    count = encrypted_txt.count(char)
    txt_frequencies[char] = count / num_chars

wiki_frequency_data = {
    "A": 0.082,
    "B": 0.015,
    "C": 0.028,
    "D": 0.043,
    "E": 0.127,
    "F": 0.022,
    "G": 0.020,
    "H": 0.061,
    "I": 0.070,
    "J": 0.0015,
    "K": 0.0077,
    "L": 0.040,
    "M": 0.024,
    "N": 0.067,
    "O": 0.075,
    "P": 0.019,
    "Q": 0.00095,
    "R": 0.060,
    "S": 0.063,
    "T": 0.091,
    "U": 0.028,
    "V": 0.0098,
    "W": 0.024,
    "X": 0.0015,
    "Y": 0.020,
    "Z": 0.00074
}

wiki_letters_sorted = [k for k, v in sorted(wiki_frequency_data.items(), key = lambda item : item[1], reverse=True)]
txt_frequencies = [k for k, v in sorted(txt_frequencies.items(), key = lambda item : item[1], reverse=True)]
cipher_map = dict(zip(txt_frequencies, wiki_letters_sorted))

decrypted_str = ''
for c in input_txt:
    if c.isalpha():
        if (c.islower()):
           decrypted_str += cipher_map[c.upper()].lower()
        else:
            decrypted_str += cipher_map[c]
    else:
        decrypted_str += c

d1 = open("dec1.txt", "w")
d1.write(decrypted_str)
d1.close()

# Now, we construct the map with the side information from the encryption function
# We sort by frequencies after for the remainder of the letters
encryption_side_info = {'R':'O', 'H':'S', 'N':'X', 'W':'F', 'U':'B', 'G':'C', 'S':'D', 'F':'K'}
for key, val in encryption_side_info.items():
    wiki_letters_sorted.remove(key)
    txt_frequencies.remove(val)

cipher_map_fixed = {v:k for k, v in encryption_side_info.items()}

cipher_map_fixed.update(dict(zip(txt_frequencies, wiki_letters_sorted)))

decrypted_str_si = ''
for c in input_txt:
    if c.isalpha():
        if (c.islower()):
           decrypted_str_si += cipher_map_fixed[c.upper()].lower()
        else:
            decrypted_str_si += cipher_map_fixed[c]
    else:
        decrypted_str_si += c

d2 = open("dec2.txt", "w")
d2.write(decrypted_str_si)
d2.close()









