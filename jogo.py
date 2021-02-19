from time import sleep
import random as rd


class Boneco:
    def __init__(self):
        self.forca = """
                +---+
                |   |
                    |
                    |
                    |
                    |
            ============
        """
        self.cabeca = """
                +---+
                |   |
                0   |
                    |
                    |
                    |
            ============
        """
        self.tronco = """
                +---+
                |   |
                0   |
                |   |
                    |
                    |
            ============
        """
        self.braco_dir = """
                +---+
                |   |
                0   |
                |\  |
                    |
                    |
            ============
        """
        self.braco_esq = """
                +---+
                |   |
                0   |
               /|\  |
                    |
                    |
            ============
        """
        self.perna_dir = """
                +---+
                |   |
                0   |
               /|\  |
                 \  |
                    |
            ============
        """
        self.perna_esq = """
                +---+
                |   |
                0   |
               /|\  |
               / \  |
                    |
            ============
        """


class Forca(Boneco):
    conjunto = ('linha', 'poder', 'laje', 'operar', 'galho', 'ultimato', 'casa', 'elefante', 'abacaxi', 'geladeira',
                'hidratante', 'panela', 'cozinha', 'galinha', 'cachorro', 'gato', 'zelador', 'rio de janeiro',
                'minas gerais', 'sao paulo', 'rio grande do sul')

    def __init__(self):
        super().__init__()
        self.palavra: str = rd.choice(Forca.conjunto)
        self.letras_erradas = []
        self.letras_certas = []
        self.certo = False

    def jogar(self):
        print('<<<<<<<<<< JOGO DA FORCA >>>>>>>>>>')

        linhas = list('_' * len(self.palavra))
        erro = 0

        while True:
            try:
                if erro == 0:
                    print(self.forca)
                elif erro == 1:
                    print(self.cabeca)
                elif erro == 2:
                    print(self.tronco)
                elif erro == 3:
                    print(self.braco_dir)
                elif erro == 4:
                    print(self.braco_esq)
                elif erro == 5:
                    print(self.perna_dir)
                elif erro == 6:
                    print(self.perna_esq)
                    print()
                    print(f'A palavra é {self.palavra}')
                    print('\033[31mAH NÃO!!')
                    print('Você foi enforcado!\033[m')
                    break

                print('Palavra:', ''.join(linhas))

                if ''.join(linhas) == self.palavra:
                    sleep(1)
                    print()
                    print('\033[34mVOCÊ ACERTOU!!')
                    print('PARABÉNS!!!!!!\033[m')
                    break

                chute = str(input('Digite uma letra: ')).strip()[0]
                if chute.isalpha():
                    if chute in self.palavra and chute.isalpha() not in self.letras_certas:
                        self.letras_certas.append(chute)
                        self.certo = True
                    elif chute not in self.palavra and chute not in self.letras_erradas:
                        self.letras_erradas.append(chute)
                        self.certo = False
                    else:
                        print('\033[33mEsta letra já foi!')
                        print('Tente outra.\033[m')
                        sleep(2)
                else:
                    print('\033[31mVocê deve digitar apenas letras!\033[m')

                print()
                print('Letras corretas: ', end='')
                for letra in self.letras_certas:
                    print(letra, end=' ')
                print()
                print('Letras erradas: ', end='')
                for letra in self.letras_erradas:
                    print(letra, end=' ')
                print()

                for i, letra in enumerate(self.palavra):
                    if letra == chute:
                        linhas[i] = letra

                if not self.certo:
                    erro += 1
            except IndexError:
                print('\033[31mPor favor, digite uma letra.\033[m')


forca = Forca()
forca.jogar()
