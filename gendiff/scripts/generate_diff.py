import json


def generate_diff(path_file1, path_file2):
    a = json.load(open(path_file1))
    b = json.load(open(path_file2))

    diff_list = []
    keys_file1 = sorted(a.keys())
    keys_file2 = sorted(b.keys())
    for item in keys_file1:
        if item not in keys_file2:
            print(f'- {item}: {a[item]}')
            diff_list.append(f'\n- {item}: {a[item]}')
        if item in keys_file2 and a[item] == b[item]:
            print(f'  {item}: {a[item]}')
            diff_list.append(f'\n  {item}: {a[item]}')
        if item in keys_file2 and a[item] != b[item]:
            print(f'- {item}: {a[item]} \n+ {item}: {b[item]}')
            diff_list.append(f'\n- {item}: {a[item]} \n+ {item}: {b[item]}')
    for item in keys_file2:
        if item not in keys_file1:
            print(f'+ {item}: {b[item]}')
            diff_list.append(f'\n+ {item}: {b[item]}')
    print(*diff_list)

# gendiff/scripts/file1.json
# gendiff/scripts/file2.json
generate_diff('gendiff/scripts/file1.json', 'gendiff/scripts/file2.json')