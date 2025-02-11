def build_diff(tree1, tree2):
    diff = {}
    union_nodes = tree1 | tree2
    for node in union_nodes:
        if node in tree2 and node not in tree1:
            diff[node] = ('added', tree2[node])
        elif node in tree1 and node not in tree2:
            diff[node] = ('removed', tree1[node])
        elif tree1[node] == tree2[node]:
            diff[node] = ('unchanged', tree1[node])
        elif isinstance(tree1[node], dict) and isinstance(tree2[node], dict):
            diff[node] = ('nested', build_diff(tree1[node], tree2[node]))
        else:
            diff[node] = ('changed', tree1[node], tree2[node])
    return dict(sorted(diff.items()))

