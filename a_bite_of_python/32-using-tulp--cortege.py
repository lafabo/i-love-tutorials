zoo = ('python', 'elephant', 'penguin')
print('Total: ', len(zoo))

new_zoo = 'monkey', 'camel', zoo

print('New total: ', len(new_zoo))
print('All animals: ', new_zoo)
print('Old animals: ', new_zoo[2])
print('Last animal from old animals: ', new_zoo[2][2])
print('Total (animals in new zoo): ', len(new_zoo)-1+len(new_zoo[2]))