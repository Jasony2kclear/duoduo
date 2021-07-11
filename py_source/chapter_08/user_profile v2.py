def address1(first, last, **other):
    outfile = {}
    outfile['firstname'] = first
    outfile['lastname'] = last
    for key, value in other.items():
        outfile[key] = value
    return outfile

abc = address1('Lian ', 'Jun ', street='shangye', prov='macau')
print(abc)