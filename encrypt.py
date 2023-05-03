def encrypt_text(plaintext,n):
    ans = ""
    # iterate over the given text
    for i in range(len(plaintext)):
        ch = plaintext[i]
        
        # check if space is there then simply add space
        if ch==" " or ch == ',' or ch == '.' or ch == ';':
            ans+=" "
        # check if a character is uppercase then encrypt it accordingly 
        elif (ch.isupper()):
            ans += chr((ord(ch) + n-65) % 26 + 65)
        # check if a character is lowercase then encrypt it accordingly
        
        else:
            ans += chr((ord(ch) + n-97) % 26 + 97)

    return ans
def print_blocks(s):
    s = encrypt_text(plaintext, n)
    s = ''.join(filter(lambda c: c.isalpha(), s.upper()))  # remove non-alphabetical characters
    blocks = [s[i:i + 5] for i in range(0, len(s), 5)]
    for i in range(0, len(blocks), 10):
        for j in range(i, min(i + 10, len(blocks))):
            print(blocks[j], end=' ')


plaintext = "Congress shall make no law respecting an establishment of religion, or prohibiting the free exercise thereof; or abridging the freedom of speech, or of the press; or the right of the people peaceably to assemble, and to petition the government for a redress of grievances."
n = 1
s = encrypt_text(plaintext, n)
print("Plain Text is : " + plaintext)
print("Shift pattern is : " + str(n))
print("The Encrypted Text Is: ")
print(print_blocks(s))

