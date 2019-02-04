# PasswordCracker#README

This was written in Python 3.6.
The wordlist used in /usr/share/dict/words is from MacOS Mojave Version Number 10.14.2. This path should be
changed if it is found in a different location in file system.

Libraries needed:
hashlib (imported as hl)



Rules to implement:
    done -- A seven char word from /usr/share/dict/words which gets the 1st letter capitalized and a 1-digit number appended
    done -- A 4 digit password with at least one of "*, ~, !, #" at the beginning (can be more than one)
    done -- A 5 char word from /usr/share/dict/words with the letter 'a' replaced with '@' and/or 'l' replaced with '1'
    done -- Any password up to 6 digit number (0 - 999999)
    done -- Any word from /usr/share/dict/words
