
class Writer():
    @staticmethod
    def read(name):
        f = open(name, 'r')
        try:
            max_score = int(f.readline())
            f.close()
            return max_score
        except:
            f.close()


    @staticmethod
    def nameRead(name):
        f = open(name, 'r')
        try:
            nik = f.readlines()
            f.close()
            return nik
        except:
            f.close()


    @staticmethod
    def write(name,score,nik,mode):
        try:
            f = open(name, mode)
            f.writelines(str(score) + "\n" + nik + "\n")
            f.close()
        except:
            f.close()

