print('''
        A Mansão Sombria
      
    Você é um viajante que, durante uma tempestade 
intensa, se vê forçado a procurar abrigo em uma mansão
antiga, localizada em uma colina distante. Ao se aproximar,
você sente uma estranha sensação de desconforto, 
mas o frio e a chuva o convencem a entrar.
      ''')

print('''
    Assim que você entra na mansão, 
a porta se fecha atrás de você com 
um estrondo. O silêncio toma conta do lugar, 
quebrado apenas pelo som da chuva batendo nas 
janelas sujas. O ar é denso e cheira a mofo. 
Diante de você, há duas opções:
      ''')
def inicio():
    print("Você está diante de uma mansão sombria.")
    escolha = input("Deseja (1) Subir a escada ou (2) Entrar na sala à esquerda? ")
    if escolha == '1':
        subir_escada()
    elif escolha == '2':
        entrar_sala()

def subir_escada():
    print('''Você sobe a escada de madeira velha que range a cada passo.
          Chegando ao topo, você vê um longo corredor com três portas:
          ''')
    escolha = input("Deseja (1) Abrir a porta à direita, (2) Entrar na porta à esquerda, ou (3) Seguir em frente? ")
    if escolha == '1':
        abrir_direita()
    elif escolha == '2':
        entrar_esquerda()
    elif escolha == '3':
        seguir_frente()

def entrar_sala():
    print('''Você entra na sala à esquerda. Ao abrir a porta, percebe
          que está em uma biblioteca antiga, cheia de livros empoeirados
          e móveis velhos. No centro da sala, há uma mesa com um livro aberto,
          brilhando com uma luz estranha.''')
    escolha = input("Deseja (1) Ler o livro ou (2) Ignorar o livro? ")
    if escolha == '1':
        ler_livro()
    elif escolha == '2':
        ignorar_livro()

def abrir_direita():
    print('''Ao abrir a porta, você se depara com uma pequena sala vazia,
          exceto por uma cadeira de balanço que se move sozinha. Um frio
          intenso invade o ambiente, e você sente uma presença maligna.
          ''')
    escolha = input("Deseja (1) Sair correndo ou (2) Sentar-se na cadeira? ")
    if escolha == '1':
        sair_correndo()
    elif escolha == '2':
        sentar_cadeira()

def entrar_esquerda():
    print('''Você entra na sala e se depara com um quarto antigo. 
          No chão, há uma boneca de porcelana com os olhos vidrados 
          olhando diretamente para você. De repente, a porta se fecha 
          e o quarto fica frio.
          ''')
    escolha = input("Deseja (1) Pegar a boneca ou (2) Ignorar a boneca? ")
    if escolha == '1':
        pegar_boneca()
    elif escolha == '2':
        ignorar_boneca()

def seguir_frente():
    print('''Você continua a caminhar pelo corredor até o fim, 
          onde a sombra que parecia se mover desaparece. 
          Há uma porta antiga, com uma fechadura enferrujada.''')
    escolha = input("Deseja (1) Tentar abrir a porta ou (2) Voltar pelo corredor? ")
    if escolha == '1':
        abrir_porta()
    elif escolha == '2':
        volta_corredor()

def ler_livro():
    print("Você começou a ler o livro...")

def ignorar_livro():
    print("Você ignorou o livro, mas algo está errado...")

# Início da história
inicio()
