def merge(a, b):
    if not a: return b
    if not b: return a
    if a.data < b.data:
        a.bottom = merge(a.bottom, b); return a
    else:
        b.bottom = merge(a, b.bottom); return b

def flatten(root):
    if not root or not root.next: return root
    root.next = flatten(root.next)
    return merge(root, root.next)
