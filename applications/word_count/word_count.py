characters_to_ignore = '" : , . - + = / \ | [ ] { } ( ) * ^ &'.split(' ')
def word_count(s):
    d = {}
    for character in characters_to_ignore:
        s = s.replace(character, '')
        
    sentence = s.split(' ')
    for word in sentence:
        word = word.lower()
        if word.isspace():
            continue

        if word == '':
            return {}

        if word not in d:
            d[word] = 0
        
        d[word] += 1

    return d



if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))