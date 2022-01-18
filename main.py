class Diff():

    def __init__(self, ratio = 1):

        self.ratio = ratio

        if self.ratio == None:

            raise ExamException('il valore ratio non è accettabile')

        if self.ratio <= 0:
                
                raise ExamException('il valore ratio non è accettabile')

        if ratio == None:

            self.ratio = 0
                

        if type(self.ratio) != int:
            raise ExamException("il valore ratio inserito non è corretto")


    def compute(self, lista):

        try:

            lista_diff = []

            lenght1 = len(lista)

            for i in range(0, lenght1 - 1):

                lista_diff.append(lista[i + 1] - lista[i])

            lenght2 = len(lista_diff)

            for i in range(0, lenght2):

                lista_diff[i] = lista_diff[i] / self.ratio

            return lista_diff

        except Exception: 
            raise ExamException('qualcosa è andato storto, non sò cosa, cazzo')

class ExamException(Exception):
    pass



diff = Diff()

result = diff.compute([2,2,3,4,5,6])

print(result)