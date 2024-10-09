import re

def validar_ean13(ean):
    """Função para validar um EAN-13"""
    if len(ean) != 13 or not ean.isdigit():
        return "EAN-13 deve conter 13 dígitos numéricos"
    
    soma_impares = sum(int(ean[i]) for i in range(0, 12, 2))
    soma_pares = sum(int(ean[i]) for i in range(1, 12, 2)) * 3
    total = soma_impares + soma_pares
    digito_verificador_calculado = (10 - (total % 10)) % 10
    
    if digito_verificador_calculado != int(ean[-1]):
        return "EAN-13 inválido"
    
    return None

def validar_cod_display(cod_display):
    """Função para validar um EAN-13"""
    if len(cod_display) != 13 or not cod_display.isdigit():
        return "CÓDIGO DO DISPLAY deve conter 13 dígitos numéricos"
    
    soma_impares = sum(int(cod_display[i]) for i in range(0, 12, 2))
    soma_pares = sum(int(cod_display[i]) for i in range(1, 12, 2)) * 3
    total = soma_impares + soma_pares
    digito_verificador_calculado = (10 - (total % 10)) % 10
    
    if digito_verificador_calculado != int(cod_display[-1]):
        return "CÓDIGO DO DISPLAY inválido"
    
    return None

def validar_quantidade_display(quantidade):
    """Função para validar se a quantidade_display é um número inteiro"""
    if isinstance(quantidade, int):
        return None  # Nenhum erro, é um número inteiro válido
    return "Quantidade (DISPLAY) deve ser um número inteiro"

def validar_quantidade_caixa(quantidade_caixa):
    """Função para validar se a quantidade_display é um número inteiro"""
    if isinstance(quantidade_caixa, int):
        return None  # Nenhum erro, é um número inteiro válido
    return "Quantidade da caixa deve ser um número inteiro"

def validar_ean14(ean_14):
    """Função para validar um EAN-14"""
    if len(ean_14) != 14 or not ean_14.isdigit():
        return "EAN-14 deve conter 14 dígitos numéricos"
    
    return None

def validar_altura(altura_cm):
    """Função para validar se a medida (cm) é um número positivo"""
    if altura_cm <= 0:
        return "O COMPRIMENTO CM deve ser um número positivo"
    return None

def validar_largura(largura_cm):
    """Função para validar se a medida (cm) é um número positivo"""
    if largura_cm <= 0:
        return "O COMPRIMENTO CM deve ser um número positivo"
    return None

def validar_comprimento(comprimento_cm):
    """Função para validar se a medida (cm) é um número positivo"""
    if comprimento_cm <= 0:
        return "O COMPRIMENTO CM deve ser um número positivo"
    return None

def validar_peso_bruto_kg(peso_bruto_kg):
    """Função para validar se a medida (cm) é um número positivo"""
    if peso_bruto_kg <= 0:
        return "O PESO BRUTO KG deve ser um número positivo"
    return None

def validar_preco_compra_un(preco_compra_un):
    """Função para validar se a medida (cm) é um número positivo"""
    if preco_compra_un <= 0:
        return "O PREÇOD E COMPRA UN deve ser um número positivo"
    return None

# Validação de CNPJ
def validar_cnpj(cnpj: str) -> bool:
    cnpj = re.sub(r'[^0-9]', '', cnpj)  # Remove qualquer caractere não numérico
    if len(cnpj) != 14 or cnpj == cnpj[0] * len(cnpj):  # Verifica tamanho e sequências repetidas
        return False

    # Cálculo do primeiro dígito verificador
    peso = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    soma = sum(int(cnpj[i]) * peso[i] for i in range(12))
    digito1 = (soma % 11)
    digito1 = 0 if digito1 < 2 else 11 - digito1

    # Cálculo do segundo dígito verificador
    peso = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    soma = sum(int(cnpj[i]) * peso[i] for i in range(13))
    digito2 = (soma % 11)
    digito2 = 0 if digito2 < 2 else 11 - digito2

    return cnpj[-2:] == f"{digito1}{digito2}"


def validar_formulario(ean_13, cod_display, quantidade_display, ean_14, quantidade_caixa, altura_cm, largura_cm, comprimento_cm, peso_bruto_kg, preco_compra_un):
    erros = []
    
    erro_ean = validar_ean13(ean_13)
    if erro_ean:
        erros.append(erro_ean)
    
    erro_cod_display = validar_cod_display(cod_display)
    if erro_cod_display:
        erros.append(erro_cod_display)

    erro_quantidade = validar_quantidade_display(quantidade_display)
    if erro_quantidade:
        erros.append(erro_quantidade)

    erro_ean14 = validar_ean14(ean_14)
    if erro_ean14:
        erros.append(erro_ean14)

    erro_quantidade = validar_quantidade_caixa(quantidade_caixa)
    if erro_quantidade:
        erros.append(erro_quantidade)
    
    erro_altura = validar_altura(altura_cm)
    if erro_altura:
        erros.append(erro_altura)

    erro_largura = validar_altura(largura_cm)
    if erro_largura:
        erros.append(erro_largura)

    erro_comprimento = validar_comprimento(comprimento_cm)
    if erro_comprimento:
        erros.append(erro_comprimento)

    erro_comprimento_peso_bruto_kg = validar_peso_bruto_kg(peso_bruto_kg)
    if erro_comprimento:
        erros.append(erro_comprimento_peso_bruto_kg)
    
    erro_validar_preco_compra_un = validar_preco_compra_un(preco_compra_un)
    if erro_comprimento:
        erros.append(erro_validar_preco_compra_un)

    return erros