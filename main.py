#Importações de bibliotecas necessarias
from TelaMenu import Ui_Dialog
from PyQt5 import QtCore, QtGui, QtWidgets
from impostos import ValorInss,ValorIrrf,ValorFgts,ValorValeA,ValorValeT,ValorLiquido,lista_,lista,ref,ValorInss2,listaref
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
from os import startfile
from excell import EnviarPlanilha
import random

# Funções dos botões e para o acionamento de outras funcionalidades
def pegaMes_Ano_Hora():
    from datetime import datetime
    data_e_horaAtual = datetime.now()
    ano = data_e_horaAtual.strftime('%Y')
    mes = data_e_horaAtual.strftime('%m')
    dia = data_e_horaAtual.strftime('%d')
    data = data_e_horaAtual.strftime('%d/%m/%Y')
    hora = data_e_horaAtual.strftime('%H:%M')
    lst_hora = []
    lst_hora.append(data)
    lst_hora.append(hora)
    return lst_hora

def calculoTotal():
    if ui.txtValorBruto.text() != '' and ui.txtNome.text() != '' and ui.txtCargo.text() != '':
        valor = ui.txtValorBruto.text()
        listaValores = lista_(valor)
        print(listaValores)
        referencia = ref()
        print(referencia)

        inss = lista[0]
        irrf = lista[1]
        fgts = lista[2]
        valeT = lista[3]
        valeA = lista[4]
        totalVenci = int(valor)+valeA+valeT
        totalDes = sum(lista)
        valorLiquido = totalVenci - totalDes
        total = valorLiquido
        #clear da lista

        ui.txtINSS.setText(f'{inss:,.2f}')
        ui.txtIRFF.setText(f'{irrf:,.2f}')
        ui.txtFGTS.setText(f'{fgts:,.2f}')
        ui.txtValeT.setText(f'{valeT:,.2f}')
        ui.txtValeA.setText(f'{valeA:,.2f}')
        ui.lineEdit_8.setText(f'{total:,.2f}')
        pdf(totalDes,totalVenci,valorLiquido)
        data = pegaMes_Ano_Hora()
        print(data)
        #EnviarPlanilha(ui.txtNome.text(),ui.txtCargo.text(),ui.txtValorBruto.text(),inss,irrf,fgts,valeT,valeA,data)
        ui.btnNovo.setEnabled(True)
        ui.btnPdf.setEnabled(True)
        ui.btnExcell.setEnabled(True)
        ui.btnCalcular.setEnabled(False)
        ui.txtNome.setEnabled(False)
        ui.txtCargo.setEnabled(False)
        ui.txtValorBruto.setEnabled(False)
    else:
        print('Preencha os dados necessarios')        
        
def pdf(totalVenc,totalDescontos,valorLiquido):
    data = pegaMes_Ano_Hora()
    referencia = ref()
    print(referencia)
    if ui.txtValorBruto.text() == '':
        ui.lineEdit_8.setText('Não foi possível gerar o pdf solicitado')
    else:
        relatorioPDF = canvas.Canvas("Holerite.pdf", pagesize=letter)
        relatorioPDF.setFillColor('blue')
        relatorioPDF.setFont('Times-Roman', 18)
        relatorioPDF.drawString(10, 750, "Folha De Pagamento")

        relatorioPDF.setStrokeColor('blue')
        relatorioPDF.setLineWidth(1)
        # linha Horizontal Superior
        relatorioPDF.line(10, 740, 590, 740)
        relatorioPDF.line(10, 700, 590, 700)
        relatorioPDF.line(10, 680, 590, 680)
        relatorioPDF.line(10, 320, 590, 320)
        relatorioPDF.line(350, 270, 590, 270)
        # linha Vertical Esquerda
        relatorioPDF.line(10, 240, 10, 740)
        relatorioPDF.line(70, 700, 70, 320)
        relatorioPDF.line(300, 700, 300, 320)
        relatorioPDF.line(350, 240, 350, 700)
        relatorioPDF.line(480, 240, 480, 700)
        # linha horizontal Inferior
        relatorioPDF.line(10, 240, 590, 240)
        # linha Vertical Direita
        relatorioPDF.line(590, 740, 590, 240)
        # Dados Escritos
        relatorioPDF.setFillColor('black')
        relatorioPDF.setFont('Times-Roman', 12)
        relatorioPDF.drawString(75, 720, f"{ui.txtNome.text()}")
        relatorioPDF.drawString(75, 706, f"{ui.txtCargo.text()}")
        relatorioPDF.drawString(25, 720, f"{random.randint(0,1000)}")
        relatorioPDF.drawString(25, 685, "Cód")
        relatorioPDF.drawString(150, 685, "Descrição")
        relatorioPDF.drawString(80, 650, "Valor Bruto")
        relatorioPDF.drawString(80, 630, "FGTS")
        relatorioPDF.drawString(80, 610, "INSS")
        relatorioPDF.drawString(80, 590, "IRRF")
        relatorioPDF.drawString(80, 570, "Vale Transporte")
        relatorioPDF.drawString(80, 550, "Vale Alimentação")
        relatorioPDF.drawString(310, 685, "Ref")
        relatorioPDF.drawString(310, 630, f"{listaref[2]}")
        relatorioPDF.drawString(310, 610, f"{listaref[0]}")
        relatorioPDF.drawString(310, 590, f"{listaref[1]}")
        relatorioPDF.drawString(310, 570, f"{listaref[3]}")
        relatorioPDF.drawString(310, 550, f"{listaref[4]}")
        relatorioPDF.drawString(380, 685, "Vencimentos")
        relatorioPDF.drawString(320, 720, f"Documento gerado as {data[1]} da data de {data[0]}")
        # Valor Bruto
        relatorioPDF.drawString(360, 650, f"{ui.txtValorBruto.text()}")
        # Valor INSS
        relatorioPDF.drawString(483, 630, f"{ui.txtFGTS.text()}")
        # Valor FGTS
        relatorioPDF.drawString(483, 610, f"{ui.txtINSS.text()}")
        # valor IRFF
        relatorioPDF.drawString(483, 590, f"{ui.txtIRFF.text()}")
        # Valor ValeT
        relatorioPDF.drawString(360, 570, f"{ui.txtValeT.text()}")
        # Valor ValeA
        relatorioPDF.drawString(360, 550, f"{ui.txtValeA.text()}")
        relatorioPDF.drawString(490, 685, "Descontos")
        relatorioPDF.drawString(360, 300, "Total de Vencimentos")
        relatorioPDF.drawString(487, 280, f"{totalVenc}")
        relatorioPDF.drawString(360, 280, f"{totalDescontos}")
        relatorioPDF.drawString(487, 300, "Total de Descontos")
        relatorioPDF.drawString(360, 250, "Valor Líquido")
        # Valor Liq
        relatorioPDF.drawString(487, 250, f"{valorLiquido}")

        relatorioPDF.save()
        print('Gerando pdf ...')

def startPdf():
    startfile("Holerite.pdf")

def calculo():
        if (ui.txtINSS2.text() != ''):
            valor = int(ui.txtINSS2.text())
            #Definindo os valores
            if valor > 5839.45:
                inss = 642.34
            elif valor >=2219.73 and valor <=5839.45:
                inss = (valor * 0.11)
            elif valor < 1751.82:
                inss = (valor * 0.08)
            elif valor <= 2219.72 and valor >= 1751.82:
                inss = (valor * 0.09)
            ui.lblRespostaINSS.setText(str(inss))
        else:
            ui.lblRespostaINSS.clear()

def calculoinssSolo():
    if ui.txtINSS2.text() !='':
        inss = ValorInss2(ui.txtINSS2.text())
        final = inss.pop()
        ui.lblRespostaINSS.setText(f'{final:,.2f}')
    else:
        ui.lblRespostaINSS.setText('Digite um valor !')

def calculoirrfSolo():
    if ui.txtIRRF2.text() != '':
        irrf = ValorIrrf(ui.txtIRRF2.text())
        final = irrf.pop()
        ui.lblRespostaIRRF.setText(f'{final:,.2f}')
    else:
        ui.lblRespostaIRRF.setText('Digite um valor !')

def calculovaleSolo():
    if ui.txtVales2.text() != '':
        valeT = ValorValeT(ui.txtVales2.text())
        final = valeT.pop()
        ui.lblRespostaValeT.setText(f'{final:,.2f}')
        valeA = ValorValeA(ui.txtVales2.text())
        final2 = valeA.pop()
        ui.lblRespostaValeA.setText(f'{final2:,.2f}')
    else:
        ui.lblRespostaValeT.setText(' ')
        ui.lblRespostaValeA.setText(' ')

def novo():
    lista.clear()
    ui.txtINSS.clear()
    ui.txtIRFF.clear()
    ui.txtFGTS.clear()
    ui.txtValeA.clear()
    ui.txtValeT.clear()
    ui.lineEdit_8.clear()
    ui.txtNome.clear()
    ui.txtCargo.clear()
    ui.txtValorBruto.clear()
    ui.btnPdf.setEnabled(False)
    ui.btnCalcular.setEnabled(True)
    ui.txtNome.setEnabled(True)
    ui.txtCargo.setEnabled(True)
    ui.txtValorBruto.setEnabled(True)
    ui.btnNovo.setEnabled(False)

def excel():
    if ui.txtValorBruto.text() != '' and ui.txtNome.text() != '' and ui.txtCargo.text() != '':
        inss = lista[0]
        irrf = lista[1]
        fgts = lista[2]
        valeT = lista[3]
        valeA = lista[4]
        data = pegaMes_Ano_Hora()
        print(data)
        EnviarPlanilha(ui.txtNome.text(),ui.txtCargo.text(),ui.txtValorBruto.text(),inss,irrf,fgts,valeT,valeA,data)
    else:
        pass
    startfile('Pasta1.xlsx')

# Abertura e denominação de sistemas e estruturas importantes
if __name__ == "__main__":

    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    ui.btnNovo.setEnabled(False)
    ui.txtINSS.setEnabled(False)
    ui.txtIRFF.setEnabled(False)
    ui.txtFGTS.setEnabled(False)
    ui.txtValeT.setEnabled(False)
    ui.txtValeA.setEnabled(False)
    ui.lineEdit_8.setEnabled(False)
    ui.btnPdf.setEnabled(False)

# Conecxão dos botões a suas respectivas funções
    ui.pushButton.clicked.connect(lambda: ui)
    ui.pushButton.clicked.connect(lambda: ui.stackedWidget.setCurrentWidget(ui.page))
    ui.pushButton_2.clicked.connect(lambda: ui.stackedWidget.setCurrentWidget(ui.page_2))
    ui.pushButton_3.clicked.connect(lambda: ui.stackedWidget.setCurrentWidget(ui.page_3))
    ui.pushButton_4.clicked.connect(lambda: ui.stackedWidget.setCurrentWidget(ui.page_4))
    ui.pushButton_5.clicked.connect(lambda: ui.stackedWidget.setCurrentWidget(ui.page_5))
    ui.pushButton_6.clicked.connect(lambda: ui.stackedWidget.setCurrentWidget(ui.page_6))
    ui.txtINSS2.textChanged.connect(lambda: calculoinssSolo())
    ui.txtIRRF2.textChanged.connect(lambda: calculoirrfSolo())
    ui.txtVales2.textChanged.connect(lambda: calculovaleSolo())
    ui.btnCalcular.clicked.connect(lambda: calculoTotal())
    ui.btnPdf.clicked.connect(lambda: startPdf())
    ui.btnExcell.clicked.connect(lambda: excel())
    ui.btnInstagram.clicked.connect(lambda: startfile('https://www.instagram.com/senacminas/'))
    ui.btnFacebook.clicked.connect(lambda: startfile('https://www.facebook.com/pages/Senac-Lavras/1649615995305605'))
    ui.BtnSite.clicked.connect(lambda: startfile('https://twitter.com/senacminas'))
    ui.btnNovo.clicked.connect(lambda: novo())
    ui.btnSenac.clicked.connect(lambda: startfile('https://www.mg.senac.br/Paginas/default.aspx'))
    
# Inicialização da aplicação
    Dialog.show()
    sys.exit(app.exec_())