def all_capital(s):
    return s.upper()

def remove_spaces(s):
    return s.strip()

def find_it(s, a):
    return s.find(a)

def replace_it(s, old, new):
    return s.replace(old, new)

def punctuation(s):
    sentences = s.split('.')
    return '. '.join(sentence.capitalize() for sentence in sentences)

print('Correct your Text:')
s = input("Enter the text here: ")

print('1. Capitalize your text properly')
print('2. Replace an existing word')
print('3. Remove unnecessary spacing between words')
print('4. Find a specific word in the text')
while(1):
    choice = input("Enter your choice [1/2/3/4]: ")

    if choice in ('1', '2', '3', '4'):
        if choice == '1':
            p=punctuation(s)
            print(p)
        elif choice == '2':
            x = input("Word to be replaced: ").strip()
            y = input("Modified word: ").strip()
            r=replace_it(s, x.lower(), y.lower())
            print(r)
        elif choice == '3':
            remove=remove_spaces(s)
            print(remove)
        elif choice == '4':
            z = input('Word to find: ').strip()
            f=find_it(s, z())
            print(f)
    else:
        print("Make correct choice:")

        