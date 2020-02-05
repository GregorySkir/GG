def remove_duplicates(dups_list):
    # return list(set(text.split()))
    new_list = []
    for l in dups_list:
        if l not in new_list:
            new_list.append(l)
    return new_list

num = 100
print('tic')
print(remove_duplicates(list(range(num)) + list(range(num))))
print('toc')

print('tic')
print(list(set(list(range(num)) + list(range(num)))))
print('toc')

