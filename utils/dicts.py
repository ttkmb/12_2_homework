def get_val(collection, key, default='git'):
    '''
    :param collection:
    :param key:
    :param default:
    :return:
    Функция возвращает значение из словаря по переданному ключу, если ключ существует.
    В ином случае возвращается значение default
    '''
    if key in collection:
        return collection[key]
    else:
        return default

