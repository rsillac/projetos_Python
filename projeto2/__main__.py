import random
from openpyxl import workbook
import manipula_xls

def main():
    lista_planilhas = ['receitas', 'despesas', 'resultado']
    pasta = manipula_xls.cria_xls()
    pasta.active
    for planilha in lista_planilhas:
        manipula_xls.cria_planilha(planilha, pasta)
    pasta.save("orcamento.xls")

if __name__ == "__main__":
    main()