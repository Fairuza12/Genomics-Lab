import os
def build_suffix_tree(string):
    suff_tree = {}
    for i in range(len(string)+1):
        suffix = string[i:]+"$"
        insert(suffix,suff_tree)
    return suff_tree

def common_prefix(string,word):
    return os.path.commonprefix([string,word])

def insert(sequence,tree):
    if len(tree):
        tree[sequence] = []
        return tree
    pattern_match = False
    for word in list(tree):
        prefix = common_prefix(sequence,word)
        x = len(prefix)
        if len(prefix)>0:
            pattern_match = True
            tree[prefix] = [word[x:],sequence[x:]]
    if not pattern_match:
        tree[sequence] = []
    return tree


print(build_suffix_tree("ATCATGTCATG"))