def search_id(ids, target, index=0):
    if index >= len(ids):
        return -1
    if ids[index] == target:
        return index
    return search_id(ids, target, index + 1)
print(search_id([101, 205, 330, 412, 550, 678],330))
print(search_id([101, 205, 330, 412, 550, 678],990))


