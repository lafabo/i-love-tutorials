def reverse(text):
    return text[::-1]

def is_palindrome(text):
    return text == reverse(text)

something = input('Input some text: ')
if (is_palindrome(something)):
    print('Yeah it\'s palyndrom')
else:
    print('Not a palyndrom')
