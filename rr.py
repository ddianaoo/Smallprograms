status = 404
match status:
    case 400:
        print('bad')
    case 401 | 403 as error:
        print(f'{error} is authentication error')
    case 404:
        print('not found')
    case _:
        print('other')
