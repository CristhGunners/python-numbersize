normal = [
    (1000 ** 5, 'P'),
    (1000 ** 4, 'T'), 
    (1000 ** 3, 'G'), 
    (1000 ** 2, 'M'), 
    (1000 ** 1, 'K'),
    (1000 ** 0, ''),
    ]

decimal = [
    (1024 ** 5, 'PB'),
    (1024 ** 4, 'TB'), 
    (1024 ** 3, 'GB'), 
    (1024 ** 2, 'MB'), 
    (1024 ** 1, 'KB'),
    (1024 ** 0, ('byte','bytes')),
    ]
    
def abbr(number,sys_type=normal):
    system=sys_type
    for factor, suffix in system:
        if number >= factor:
            break
    amount = int(number/factor)
    if isinstance(suffix, tuple):
        singular, multiple = suffix
        if amount == 1:
            suffix = singular
        else:
            suffix = multiple
    return str(amount) + suffix