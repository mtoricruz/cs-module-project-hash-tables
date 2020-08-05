def word_count(s):
    d = {}
    s = s.lower()
    ignore = '" : ; , . - + = / \ | [ ] { } ( ) * ^ &'.split(' ')
    for character in ignore:
        s = s.replace(character, '')
        
    for word in s.split():
        if word.isspace():
            continue

        if word not in d:
            d[word] = 1
        else:
            d[word] += 1
        
    return d



if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))