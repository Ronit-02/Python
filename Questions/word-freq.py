
def word_frequency(phrase):
    result = {}
    words = phrase.split()
    
    for word in words:
        if word not in result:
            result[word] = 1
        else:
            result[word] += 1
    
    return result


print(word_frequency(input('enter your phrase: ')))