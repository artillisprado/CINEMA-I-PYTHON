def saberRepetidos(lista):
    l = []
    for i in lista:
        if i not in l:
            l.append(i)
        else:
          print('\033[1;31mA cadeira {} Ã© InvÃ¡lida, Tente novamente !\033[m'.format(i))
          return True  
    return False  

def saberdevolver(lista):
    l = []
    for i in lista:
        if i not in l:
            l.append(i)
        else:
          print('\033[1;31mA cadeira {} Ã© InvÃ¡lida, Tente novamente !\033[m'.format(i))
          return True  
    return False  

contador = 0 #contador da matriz, ele vai contando e adicionando na matriz.
matriz = [] #matriz onde os valores do for em baixo vai guardar
linhas = input('Informe o nÃºmero de linhas: ')#digite a linha
while True: #se for letra
    try:
        linhas = int(linhas)
        break
    except:
        linhas = input('Valor invÃ¡lido, Informe o nÃºmero de linhas novamente: ')
colunas = input('Informe o nÃºmero de colunas: ')#digite a coluna
while True:#se coluna for letra
    try:
        colunas = int(colunas)
        break
    except:
        colunas = input('Valor invÃ¡lido, Informe o nÃºmero de colunas novamente: ')
for e in range(linhas): 
    linha = []
    for i in range(colunas):
        valor = str(contador)        
        v = int((linhas*colunas)-1)
        valor = valor.zfill(len(str(v)))
        linha.append(valor)
        contador += 1
    matriz.append(linha) 
print('')
for e in matriz:#mostra a matriz:
    print(" ".join(e))
awc = 0
pop = []
while True:#Para fazer com que as perguntas  se repitam repentidamente atÃ© o comprador sair.
  print('')
  print('-=-' * 2, '\033[1;32mBem vindo ao sistema de venda de ingressos.\033[m', '-=-' * 2)
  print('''Escolha a operaÃ§Ã£o:
  01- Comprar ingressos (Valor: R$ 10,00)
  02- Devolver ingressos (taxa de 10% sobre o valor.)
  03- Resumo das vendas
  04- Sair''')
  print('')
  pergunta = input('Digite sua escolha:')
  while True:#ConversÃ£o de pergunta em inteiro, caso seja letra
    try:
      pergunta = int(pergunta)
      break
    except:
      pergunta = input('Por favor, digite novamente sua escolha:')
  while True:#caso seja diferente de 1,2,3,4
      if pergunta != 1 and pergunta != 2 and pergunta != 3 and pergunta != 4:
          pergunta = int(input('Valor invÃ¡lido, dÃ­gite novamente:'))
      else:
        print('')
        break
  done = False 
  cadvolver = 0
  if pergunta == 1:#pergunta 1
    fil = []
    while done == False:
      print('\033[1;36mO valor de venda o ingresso Ã© de R$ 10,00.\033[m')
      print('')
      for e in matriz:#mostra a matriz
            print(" ".join(e))
      print('')
      cadeiraquero = input('Quais acentos deseja comprar ? [dÃ­gite o nÃºmero do assento]: ').replace(" ","").split(",")#pergunta da cadeira,replace troca o espaÃ§o por nada,e o split separa a vÃ­rgula
      errou = False     
      for el in cadeiraquero:
        try:
            el = int(el)
            errou = False
        except:
            errou = True
      if errou == True:
        print("{} Ã© invÃ¡lido".format(el))
        break
      Ganhou = False
      for el in cadeiraquero:
        if 0 <= int(el) <= (linhas*colunas)-1:
          Ganhou = False
        else:
          Ganhou = True
      if Ganhou == True:
        print("{} Ã© invÃ¡lido".format(el))
        break 
      temRepetidos = saberRepetidos(cadeiraquero)
      if(temRepetidos):
        done = True
        break  
      else:
        for p in cadeiraquero:
          if p not in pop:
            if Ganhou == False and errou == False:
              for el in cadeiraquero:
                el = int(el)
                linha = el//colunas
                coluna = el%colunas
                matriz[linha][coluna] = 'xx'
                done = True
          else:
            print('\033[1;31mCompra invÃ¡lida \033[m')
            done = True
            break  
      for t in cadeiraquero:     
        fil.append(t)
    for o  in fil:
      pop.append(o)
    for e in matriz:
        print(" ".join(e))
  elif pergunta == 2: #devoluÃ§Ã£o da grana do cinema
    cont = 0
    while done == False:
      print('\033[1;34mSobre o valor da devoluÃ§Ã£o, vocÃª terÃ¡ o retorno de 90%, enquanto 10% fica com o cinema !\033[m')
      print('')
      for e in matriz:#mostra a matriz
        print(" ".join(e))
      print('')
      cadeiradevolver = input('Quais acentos deseja devolver ? [dÃ­gite o nÃºmero do assento]: ').replace(" ","").split(",")#pergunta da cadeira,replace troca o espaÃ§o por nada,e o split separa a vÃ­rgula
      temdevolver = saberdevolver(cadeiradevolver)
      errou = False
      if(temdevolver):
        done = True
        break
      else:        
        for el in cadeiradevolver:
          try:
              el = int(el)
              errou = False
          except:
              errou = True
        if errou == True:
          print("{} Ã© invÃ¡lido".format(el))
          break
        Ganhou = False
        for el in cadeiradevolver:
          if 0 <= int(el) <= (linhas*colunas)-1:
            Ganhou = False
          else:
            Ganhou = True
        if Ganhou == True:
          print("{} Ã© invÃ¡lido".format(el))
          break
        if Ganhou == False and errou == False:
          for el in cadeiradevolver:
            el = int(el)
            linha = el//colunas
            coluna = el%colunas
            matriz[linha][coluna] = "0" + str(el)
            done = True
          for i in cadeiradevolver:
            cont += 1
    cadvolver+=cont
    for e in matriz:
        print(" ".join(e))
  elif pergunta ==3:
    for e in matriz:#mostra a matriz
        print(" ".join(e))
    print('')
    pessoasnasala = 0
    for y in matriz:
      for x in y:  
        if x == 'xx':
          pessoasnasala +=1
        else:
          continue  
    yop = 10*pessoasnasala
    yop2 = (10*awc)*10/100
    print('OcupaÃ§Ã£o na sala no momento: {}'.format(pessoasnasala))
    print('Quantidade de ingressos devolvidos: {}'.format(awc))
    print('Valor total apurado: R$ {}'.format(yop + yop2))
  elif pergunta == 4:
    break
  else:
    print('')
  awc += cadvolver
print(pop)
print('Fim')
