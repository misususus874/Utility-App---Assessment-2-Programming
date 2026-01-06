#Part 5
mini_list = [4, 'chicken', 5, 6, 'Italy', 10, 'banana', 'orange', 2, 'plant']
print(f'Original list: {mini_list}')
sublst = mini_list[2:6]
print(f'Sliced List: {sublst}')

if 'Italy' in sublst:
    print('Is Italy in list? True')
else:
    print('Is Italy in list? False')

sublst.append('Paris')
sublst.remove('Italy')
sublst.insert(1, 'beef')
print(f'List after modifications: {sublst}')
print(f'Length of list: {len(sublst)}')
print(f'Converted to tuple: {tuple(sublst)}')
