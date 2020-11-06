# kompozícióval oldjuk meg:

from file_reader import FileReader

class SpecReader_2(FileReader):
    def __init__(self, path = None):
        self._reader = FileReader(path)

    def setPath(self, path):
        self._reader.setPath(path)

    def close(self):
        self._reader.close()

    def open(self):
        return self._reader.open()

    def readLine(self):
        while True:
            ret_dic = self._reader.readLine()
            if ret_dic['status'] <= 0:
                return ret_dic

            data = ret_dic['data'].strip()
            if len(data) == 0: continue

            if data[0] == '#': continue

            return ret_dic

if __name__ == '__main__':
    sr_1 = SpecReader_2()
    path = 'nincs_ilyen.txt'

    path = 'van_ilyen.txt'
    sr_1.setPath(path)
    ret_dic = sr_1.open()
    print(ret_dic)
