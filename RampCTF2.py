import hashlib

def md5_hash(text):
    return hashlib.md5(text.encode()).hexdigest()

def find_password(md5_hash_value, salt, wordlist_path):
    with open(wordlist_path, 'r') as f:
        for line in f:
            word = line.strip()
            candidate = word + salt
            if md5_hash(candidate) == md5_hash_value:
                return word
    return None

# Given salt, MD5 hash, and wordlist path
given_md5_hash = '8f3c7709d96e04d878ef3644105dadf2'
given_salt = 'dc2084ae10d1'
wordlist_path = '/Users/jjoh/Downloads/word-list-7-letters.txt'

# Find the password
password = find_password(given_md5_hash, given_salt, wordlist_path)
if password:
    print("Found password:", password)
else:
    print("Password not found in the dictionary.")
