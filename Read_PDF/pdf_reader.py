from PyPDF2 import PdfReader
import sys

file = sys.argv[1]
reader = PdfReader(file)
page = reader.pages[0]
text = page.extract_text(0)
text = text.replace("\n", " - ")
text = text.replace("          ", "")
text = text.strip()
text = text.lstrip()
text = text.rstrip()

position1 = text.find("00010")
fornecedor = text.find("Fornecedor")

file2 = file.replace ("PDF/", "")
numero_po = file2.replace(".PDF", "")

data_po_i = position1 + 43
data_po_f = data_po_i + 8
data_po = text[data_po_i:data_po_f].strip()

valor_total_i = data_po_f + 4
valor_total_f = valor_total_i + 11
valor_total = text[valor_total_i:valor_total_f].strip()

boq_i = text.find("BOQ")
if(boq_i < 0):
        boq = "N"
else:
    boq = text[boq_i + 4:boq_i + 10].strip()

contrato_i = text.find("Contrato")
if(contrato_i < 0):
    contrato = "N"
else:
    contrato_i = contrato_i + 8
    contrato_f = contrato_i + 12
    contrato = text[contrato_i:contrato_f].strip()


descricao_i = contrato_i + 22
descricao_f = fornecedor
descricao = text[descricao_i:descricao_f].strip()

print(numero_po+";"+boq+";"+contrato+";"+data_po+";"+valor_total+";"+descricao)

