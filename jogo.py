# Personagem: classe mae
# Herói (herdeiro): controlado pelo usuário
# Inimigo (herdeiro): adversario do usuário
import random
class Personagem:
    def __init__(self, nome, vida, nivel):
        # Atributos privados e protegidos
        self.__nome = nome
        self.__vida = vida
        self.__nivel = nivel

    # Encapsulamento para recuperar atributos
    def get_nome(self):
        return self.__nome
    
    def get_vida(self):
        return self.__vida
    
    def get_nivel(self):
        return self.__nivel
    # Métodos da classe MÃE
    def exibir_detalhes(self):
        return f"Nome: {self.get_nome()}\nVida: {self.get_vida()}\nNivel: {self.get_nivel()}"

    def receber_ataque(self, dano):
        self.__vida -= dano
        if self.__vida < 0:
            self.__vida = 0

    def atacar(self, alvo):
        dano = random.randint(self.get_nivel() * 2, self.get_nivel() * 4)
        alvo.receber_ataque(dano)
        print(f"{self.get_nome()} atacou {alvo.get_nome()} e causou {dano} de dano")

    def ataque_especial(self, alvo):
        dano = random.randint(self.get_nivel() * 5, self.get_nivel() * 8)
        alvo.receber_ataque(dano)
        print(f"{self.get_nome()} usou habilidade especial {self.get_habilidade()} em {alvo.get_nome()} e causou {dano} de dano")
# classes HEREDITARIAS 
class Heroi(Personagem): 
    # ATRIBUTOS HERDADOS e protegendo seus valores + POLIMORFISMO para acrescentar novo atributo
    def __init__(self, nome, vida, nivel, habilidade):
        super().__init__(nome, vida, nivel)
        self.__habilidade = habilidade 
    # ENCAPSULAMENTO: retornar novo atributo protegido
    def get_habilidade(self): # 
        return self.__habilidade
    # POLIMORFISMOS: reemplementando método da classe mâe e retornando novo comando
    def exibir_detalhes(self):
        return f"{super().exibir_detalhes()}\nHabilidade: {self.get_habilidade()}\n"
  
class Inimigo(Personagem):
    def __init__(self, nome, vida, nivel, tipo):
        super().__init__(nome, vida, nivel)
        self.__tipo = tipo

    def get_tipo(self):
        return self.__tipo
    
    def exibir_detalhes(self): 
        return f"{super().exibir_detalhes()}\nTipo: {self.get_tipo()}\n"

class Jogo:
    """ Classe Orquestradora do Jogo"""
    def __init__(self):
        self.heroi = Heroi(nome="Herói", vida = 100, nivel= 5, habilidade="Super Força")
        self.inimigo = Inimigo(nome="Morcego", vida=85, nivel=5, tipo="Voador")

    def iniciar_batalha(self):
        """ FAzer a gestão da batalha em turnos """
        rodada = 1 
        print("Iniciando batalha!")
        while self.heroi.get_vida() > 0 and self.inimigo.get_vida() > 0:               
            print("\nDetalhe dos Personagens")
            print(self.heroi.exibir_detalhes())
            print(self.inimigo.exibir_detalhes())

            if rodada > 1:
                print(f"ROUND {rodada}")
            else:
                print("ROUND 1")

            input("Pressione Enter para atacar... ")
            escolha = input("Escolha (1 - Ataque Normal, 2 - Ataque Especial): ") 
            
            if escolha == "1":
                self.heroi.atacar(self.inimigo)
            elif escolha == "2":
                self.heroi.ataque_especial(self.inimigo)
            else:
                print("Escolha invalida. Escolha novamente...")
            
            if self.inimigo.get_vida() > 0 :
                self.inimigo.atacar(self.heroi)
            rodada += 1

        if self.heroi.get_vida() > 0:
            print("\nParabéns, você venceu a batalha!")
        else:
            print("\nInfelizmente você foi derrotado!")

# Criar instancia do Jogo e iniciar batalha
jogo =  Jogo()
jogo.iniciar_batalha()

