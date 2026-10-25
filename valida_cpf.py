#validar
def validar_cpf(cpf): #comando do botao
    cpf_texto = cpf.replace(".","").replace("-","").strip()
        
    if len(cpf_texto) != 11 or cpf_texto[0]*11 == cpf_texto:
        return False, "Digite um CPF válido!"
    try:
        num = int(cpf_texto)     
    except:
        return False, "Digite apenas números!"
       
    #calcula digitos ver
    def calcular_digito(digitos): 
      soma = 0
      peso = len(digitos)+1
      for digito in digitos:
        soma += int(digito)*peso
        peso-=1
      resto = soma%11
      return "0" if resto <= 1 else str(11-resto)
    
    digitos = list(cpf_texto[:9])
    div1 = calcular_digito(digitos)
    digitos.append(div1)
    div2 = calcular_digito(digitos)
    digitos.append(div2)

    if "".join(digitos[-2:]) == cpf_texto[-2:]:
        return True, "CPF válido!"
    else:
        return False, "CPF inválido!"