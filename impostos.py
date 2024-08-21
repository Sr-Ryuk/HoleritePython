#Funções para os valores de inss, fgts, irrf,
lista = []
listaref = []
listaref.clear()
lista.clear()

def ValorInss(valorN):

    if (valorN != ''):
        valor = int(float(valorN))
        if valor > 5839.45:
            percentualINSS = 0
            inss = 642.34
        elif valor >= 2219.73 and valor <= 5839.45:
            percentualINSS = 11
            inss = (valor * (percentualINSS/100))
        elif valor < 1751.82:
            percentualINSS = 8
            inss = (valor * (percentualINSS/100))
        elif valor <= 2219.72 and valor >= 1751.82:
            percentualINSS = 9
            inss = (valor * (percentualINSS/100))
        lista.append(inss)
        listaref.append(percentualINSS)

    else:
        inss = 0
    return lista

def ValorIrrf(valorN):

    if (valorN != ''):
        valor = int(float(valorN))
        if valor <= 1903.98:
            percentualIRRF = 0
            irrf = 0
        elif valor > 1903.98 and valor <= 2826.65:
            percentualIRRF = 7.5
            irrf = (0.075 * valor)
        elif valor > 2826.65 and valor <= 3751.05:
            percentualIRRF = 15.0
            irrf = (0.15 * valor)
        elif valor > 3751.05 and valor <= 4664.68:
            percentualIRRF = 25.5
            irrf = (0.255 * valor)
        elif valor>4664.68:
            percentualIRRF = 27.5
            irrf = (0.275*valor)
        lista.append(irrf)
        listaref.append(percentualIRRF)

    else:
        irrf = 0
    return lista

def ValorFgts(valorN):
    if valorN != '':
        valor = int(float(valorN))
        percentualFGTS = 8
        fgts = (valor * 0.08)
        lista.append(fgts)
        listaref.append(percentualFGTS)
    else:
        fgts = 0
    return lista

def ValorValeT(valorN):
    if valorN != '':
        valor = int(float(valorN))
        percentualValeT = 6
        valeT = (valor * 0.06)
        lista.append(valeT)
        listaref.append(percentualValeT)
    else:
        valeT = 0
    return lista

def ValorValeA(valorN):
    if valorN != '':
        valor = int(float(valorN))
        percentualValeT = 10
        valeA = (valor * 0.1)
        lista.append(valeA)
        listaref.append(percentualValeT)
    else:
        valeA = 0
    return lista

def ValorLiquido(valor, inss,irrf,fgts,valet,valea):
    if valor != '':
        valorN = int(float(valor))
        Total = valorN - sum(lista)
        lista.append(Total)
    else:
        Total = 0
    return lista

def lista_(valor):
    ValorInss(valor)
    ValorIrrf(valor)
    ValorFgts(valor)
    ValorValeA(valor)
    ValorValeT(valor)
    return lista

def ref():
    return listaref

def ValorInss2(valorN):

        if (valorN != ''):
            valor = int(float(valorN))
            if valor > 5839.45:
                inss = 642.34
            elif valor >= 2219.73 and valor <= 5839.45:
                inss = (valor * 0.11)
            elif valor < 1751.82:
                inss = (valor * 0.08)
            elif valor <= 2219.72 and valor >= 1751.82:
                inss = (valor * 0.09)
            lista.append(inss)
        else:
            inss = 0
        return lista