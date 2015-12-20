def break_words(stuff):
    '''This function will break up words'''
    words = stuff.split(' ')
    return words

def sort_words(words):
    '''Sorting the words'''
    return sorted(words)

def print_first(words):
    '''print after popping it off'''
    word = words.pop(0)
    print word

def print_last(words):
    '''print last after poppint'''
    word = words.pop(-1)
    print word

def sort_sentence(sentence):
    '''sort sentene by breaking the sentence and than sorting'''
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    '''last and firs words by breaking sentense and using our functions'''
    words = break_words(sentence)
    print_first(words)
    print_last(words)

def print_first_and_last_sorted(sentence):
    '''same as previous, but before printing we are sorting the words'''
    words = sort_sentence(sentence)
    print_first(words)
    print_last(words)
