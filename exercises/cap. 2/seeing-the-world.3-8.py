locations = ['united kingdom', 'japan', 'usa', 'canada', 'ireland']
print('Original order: ')
print(f'{locations}\n')

print('Sorted order: ')
print(f'{sorted(locations)}\n')

print('Original order: ')
print(f'{locations}\n')

print('Sorted order: (reverse)')
print(f'{sorted(locations, reverse=True)}\n')

print('Original order: ')
print(f'{locations}\n')

print('Reversed order: ')
locations.reverse()
print(f'{locations}\n')

print('Reversed order (again): ')
locations.reverse()
print(f'{locations}\n')

print('Sorted order: (perm.)')
locations.sort()
print(f'{locations}\n')


print('Sorted order: (perm./reverse)')
locations.sort(reverse=True)
print(f'{locations}\n')