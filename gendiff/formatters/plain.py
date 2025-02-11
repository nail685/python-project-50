def find_path(tree, target, path=[]):
    if not isinstance(tree, dict) or not tree:
        return None
    for key, subtree in tree.items():
        if key == target:
            return ".".join(path + [key])
        sub_path = find_path(subtree, target, path + [key])
        if sub_path:
            return sub_path
    return None 


def norm(data):
    return str(data).lower()


def plain(data_dict):
    for node in data_dict:
        path_node = find_path(data_dict, node)
        if data_dict[node][0] == 'nested' and isinstance(data_dict[node][1], dict):
            plain(data_dict[node][1])
        elif data_dict[node][0] == 'added':
            if isinstance(data_dict[node][1], dict):
                # path = find_path(data_dict, node)
                print(f"Property '{path_node}' was added with value: "
                      f"[complex value]")
            else:
                # path = find_path(data_dict, node)
                print(f"Property '{path_node}' was added with value: "
                      f"'{norm(data_dict[node][1])}'")
        elif data_dict[node][0] == 'removed':
            # path = find_path(data_dict, node)
            print(f"Property '{path_node}' was removed")
        elif data_dict[node][0] == 'changed' and len(data_dict[node]) == 3:
            if isinstance(data_dict[node][1], dict):
                # path = find_path(data_dict, node)
                print(f"Property '{path_node}' was updated. From "
                      f"'[complex value] to {norm(data_dict[node][2])}'")
            else:
                # path = find_path(data_dict, node)
                print(f"Property '{path_node}' was updated. From "
                      f"'{norm(data_dict[node][1])}' to "
                      f"'{norm(data_dict[node][2])}'")

