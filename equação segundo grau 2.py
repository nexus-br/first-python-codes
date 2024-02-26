#--*-- coding utf-8 --*--
#feito por rogerio nexus dezembro de 2023
import matplotlib.pyplot as plt
import numpy as np
opt = 0
while opt == 0:
    print("""   Programa para equações de primeiro grau. 
            Versão 0.1.1
            lagoa santa - brazil
            dezembro de 2023
            Feito por roger nexus            
            ©Direitos reservados
            """)
    try:
        a = float(input("digite o valor do ponto a: "))
        b = float(input("digite o valor do ponto b: "))
        c = float(input("digite o valor do ponto c: "))
    except:
        print("erro, valores incorretos, tente novamente")
    print("-_-/\\"*32)
    print ("gerando grafico")
    print(a)
    print(b)
    print(c)
    #array com valores de x
    #config gráfico em x
    x = np.linspace(a,b,50)
    y = x**2 
    #exibição
    plt.plot(x,y,"-r")
    plt.show()
    #continue
    opt = int(input("digite 1 para sair ou 0 para continuar"))
    if opt == 1:
        break
print("""                    
            fim do aplicativo
            para nova consulta abra o programa novamente
--------------------------------------------------------------------------
""")