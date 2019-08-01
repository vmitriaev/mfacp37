import requests, json


def error(message):
    '''Вывод сообщения об ошибке'''
    errMsg = ('ERROR: ' + message)
    lines = '-' * len(errMsg)
    return '\n' + lines + '\n' + errMsg + '\n' + lines + '\n'


def res(data):
    '''Вывод ответа'''
    j = json.dumps(data.json(), sort_keys=True, indent=2)
    c = data.status_code
    m = ('\nCode: ' + str(c) + '\n' + 'Response:' + '\n' + j + '\n')
    if c == 200:
        return '\nStatus: OK' + m

    elif c == 201:
        return '\nStatus: CREATED' + m

    elif c == 400:
        return '\nStatus: BAD REQUEST' + m

    elif c == 404:
        return '\nStatus: NOT FOUND' + m

    else:
        return error('unknown status code ' + str(c))


class Req():
    '''Экземпляром класса является объект, имеющий атрибуты для отправки запроса: method, url, json'''

    def __init__(self, meth, url, body):
        '''Инициализация объекта класса Req'''
        self.meth = meth
        self.url = url
        self.body = body
        self.d_url = 'https://reqres.in/api/'

    def send(self):
        '''Отправка запроса'''
        s_meth = str(self.meth).lower()
        s_url = str(self.url).lower()
        f_url = str(self.d_url + s_url).lower()
        s_body = str(self.body).lower()

        if s_meth == 'get':
            i = requests.get(url=f_url)
            return res(i)

        elif s_meth == 'post':
            i = requests.post(url=f_url, data=s_body)
            return res(i)

        elif s_meth == 'put':
            i = requests.put(url=f_url, data=s_body)
            return res(i)

        elif s_meth == 'patch':
            i = requests.patch(url=f_url, data=s_body)
            return res(i)

        elif s_meth == 'delete':
            i = requests.delete(url=f_url)
            c = i.status_code
            if c == 204:
                return '\nStatus: NO CONTENT' + '\nCode: ' + str(c) + '\n'

            else:
                return error('unknown status code ' + str(c))

        else:
            return error('unknown method ' + s_meth.upper())


while True:
    m = input('Type method GET, POST, PUT, PATCH, DELETE, or STOP for exit: ')
    if m.lower() in ('get', 'delete'):
        u = input('Endpoint: https://reqres.in/api/')
        b = '{}'
        r = Req(m, u, b)
        print(r.send())

    elif m.lower() in ('post', 'put', 'patch'):
        u = input('Endpoint: https://reqres.in/api/')
        b = input('Body (JSON):\n')
        r = Req(m, u, b)
        print(r.send())

    elif m.lower() in ('exit', 'stop', '0'):
        break

    else:
        print(error('unknown method ' + m.upper()))
