from file_reader import FileReader

# örököltetéssel oldjuk meg

class SpecReader_1(FileReader):
    def __init__(self, path = None):
        super().__init__(path)

    def readLine(self):
        while True:
            ret_dic = super().readLine()
            if ret_dic['status'] <= 0:
                return ret_dic

            data = ret_dic['data'].strip()
            if len(data) == 0: continue

            if data[0] == '#': continue

            return ret_dic

if __name__ == '__main__':
    sr_1 = SpecReader_1()
    path = 'nincs_ilyen.txt'

    path = 'van_ilyen.txt'
    sr_1.setPath(path)
    ret_dic = sr_1.open()
    print(ret_dic)

    while True:
        ret_dic = sr_1.readLine()
        if ret_dic['status'] < 0:
            print('hiba!!!!', ret_dic)
            break

        if ret_dic['status'] == 0:
            break

        print(ret_dic['data'], end='')
