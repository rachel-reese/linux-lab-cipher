import sys

shift = int(sys.argv[1])
line = sys.stdin.readline()

def encrypt(shift, line):
  alphabet = ['empty','A','B','C','D',
            'E','F','G','H',
            'I','J','K','L',
            'M','N','O','P',
            'Q','R','S','T',
            'U','V','W','X',
            'Y','Z']
  encrypted_string = ""
  block_size = 0
  line_size = 0

  line = line.upper()
  for char in line:
    if char not in alphabet:
      continue
    else:
      curr_char_idx = alphabet.index(char)
      new_char_idx = curr_char_idx + shift
      if new_char_idx > 26:
        new_char_idx -= 26;
      encrypted_string += alphabet[new_char_idx]
      block_size += 1
      if block_size == 5:
        if line_size == 10:
          encrypted_string += '\n'
          line_size = 0
        else:
          encrypted_string += ' '
        block_size = 0
      
print(encrypted_string)

encrypt(shift, line)