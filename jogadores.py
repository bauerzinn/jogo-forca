
import json

class Jogadores:
    def __init__(self, nickname, pontos, vitorias, derrotas):
        self.nickname = nickname
        self.pontos = pontos
        self.vitorias = vitorias
        self.derrotas = derrotas

    def salva_nickname(self):
        with open("jogadores.json", "r+") as arquivo:
            jogadores = json.load(arquivo)
        novo_jogador = {"nickname": self.nickname,
                            "historico": {
                                "pontuacao": self.pontos,
                                "vitorias": self.vitorias,
                                "derrotas": self.derrotas
                                }
                            }
        jogadores.append(novo_jogador)
        with open("jogadores.json", 'w') as arquivo:
            json.dump(jogadores, arquivo, indent=4)
    
    def atualiza(self, pontos, vitorias, derrotas):
        with open("jogadores.json", "r+") as arquivo:
            jogadores = json.load(arquivo)
            for jogador in jogadores:
                if self.nickname == jogador['nickname']:
                    jogador["historico"]["pontuacao"] += pontos
                    jogador["historico"]["vitorias"] += vitorias
                    jogador["historico"]["derrotas"] += derrotas
                arquivo.seek(0)
                json.dump(jogadores, arquivo, indent=4)
                arquivo.truncate()

    def cheka_nickname(self):
        with open("jogadores.json", "r") as arquivo:
            jogadores = json.load(arquivo)

        for jogador in jogadores:
            if jogador["nickname"] == self.nickname:
                print("Bem vindo de volta jogador:", self.nickname)
                print('HISTÓRICO_DE_PONTUAÇÃO')
                print("Pontuação -> ", jogador["historico"]["pontuacao"])
                print("Vitórias -> ", jogador["historico"]["vitorias"])
                print("Derrotas -> ", jogador["historico"]["derrotas"])
                return True
        else:
            return False
        
    def mostrar_info(self):
        print('_Tutorial_')
        print(f'Olá {self.nickname}, o jogo da forca se baseia em uma palavra')
        print('secreta e aleatória. Você deve descobrir a palavra')
        print('secreta chutando uma letra ou fazendo um palpite de qual')
        print('é a palavra secreta.')
        print()
        print('A cada letra ou palpite errado, um membro do jogador é')
        print('exposto na forca (cabeça, torso, pernas e braços). Quando')
        print('todos os membros estiverem na forca, você perde.')

class Ranking(Jogadores):
    def _init_(self, nickname, pontos, vitorias, derrotas):
        super()._init_(nickname, pontos, vitorias, derrotas)
    
    def ranking(self):
        with open("jogadores.json", "r+") as arquivo:
            jogadores = json.load(arquivo)
        ranking = sorted(jogadores, key=lambda x: x["historico"]["pontuacao"], reverse=True)
        print('RANKING_DOS_JOGADORES')
        for i, jogador in enumerate(ranking, start=1):
            print(f"{i}. {jogador['nickname']} - Pontuação: {jogador['historico']['pontuacao']} - Vitórias: {jogador['historico']['vitorias']}")
     
    #método pra criar posição no hanking a cada ultima jogada
    #método para mostrar o hanking