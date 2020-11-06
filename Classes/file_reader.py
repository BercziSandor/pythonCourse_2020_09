class FileReader:
    def __init__(self, path = None):
        self._path = path
        self._f_obj = None

    def setPath(self, path):
        self.close()
        self._path = path

    def close(self):
        if self._f_obj is not None:
            self._f_obj.close()

        self._f_obj = None

    def open(self):
        self.close()
        try:
            self._f_obj = open(self._path)
        except Exception as e:
            return { 'status': False, 'details': str(e) }
        else:
            return { 'status': True, 'details': '' }

    def readLine(self):
        if self._f_obj is None:
            return { 'status': -1, 'data': None, 'details': 'no file' }

        try:
            data = self._f_obj.readline()
        except Exception as e:
            return { 'status': -1, 'data': None, 'details': str(e) }
        else:
            status = 1 if len(data) > 0 else 0
            return { 'status': status, 'data': data, 'details': '' }

if __name__ == '__main__':
    path = 'nincs_ilyen.txt'

    fr = FileReader(path)
    ret_dic = fr.open()
    print(ret_dic)

    path = 'van_ilyen.txt'
    fr.setPath(path)
    ret_dic = fr.open()
    print(ret_dic)

    while True:
        ret_dic = fr.readLine()
        if ret_dic['status'] < 0:
            print('hiba!!!!', ret_dic)
            break

        if ret_dic['status'] == 0:
            break

        print(ret_dic['data'], end='')
