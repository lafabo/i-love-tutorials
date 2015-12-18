tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non the line."
backslash_cat = "I'm \\ a \\ cat."

flat_cat = """
I'll do a list:
\t* Cat food
\t* Fishes
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat 
print flat_cat

print 'heh\b'
print 'cat\f'
print 'dog\N{2}'
print 'hello\v'

while True:
    for i in ['/', '-', '|', '\\', '|']:
        print "%s\r" % i
