from tkinter.messagebox import NO
from xml.dom import WrongDocumentErr
from openpyxl import Workbook


def cria_xls() -> Workbook:
    pasta = Workbook()
    return pasta

def cria_planilha(nome_planilha: str, pasta: Workbook) -> None:
    pasta.active
    pasta.create_sheet(nome_planilha)
