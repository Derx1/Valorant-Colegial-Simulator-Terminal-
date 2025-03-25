import random
from game import *
from dados import *

class JogadorInternacional(Jogador):
    def __init__(self, nome, idade, habilidade, funcao, nacionalidade):
        super().__init__(nome, idade, habilidade, funcao)
        self.nacionalidade = nacionalidade
        
    def get_kd_ratio(self):
        if self.total_mortes == 0:
            return 0.0 if self.total_abates == 0 else float('inf')
        return round(self.total_abates / self.total_mortes, 2)
        
    def get_kd_display(self):
        kd_frac = f"{self.total_abates}/{self.total_mortes}"
        kd_dec = self.get_kd_ratio()
        if kd_dec == float('inf'):
            return f"{kd_frac} (∞)"
        return f"{kd_frac} ({kd_dec:.2f})"
        
    def __str__(self):
        return (f"{self.nome} ({self.nacionalidade}) - Idade: {self.idade}, Habilidade: {self.habilidade}, "
                f"Função: {self.funcao}, Abates: {self.abates}, Total Abates: {self.total_abates}, "
                f"Mortes: {self.mortes}, Total Mortes: {self.total_mortes}, K/D: {self.get_kd_display()}")

class TimeInternacional(Time):
    def __init__(self, nome, jogadores, nacionalidade):
        super().__init__(nome, jogadores)
        self.nacionalidade = nacionalidade
        self.moral = 3
        
    def atualizar_jogadores(self):
        novos_jogadores = []
        for jogador in self.jogadores:
            jogador.envelhecer()
            if jogador.idade > 17:
                novos_jogadores.append(self.gerar_jogador_internacional(jogador.funcao, self.nacionalidade))
            else:
                novos_jogadores.append(jogador)
        self.jogadores = novos_jogadores
        if self.lider not in self.jogadores:
            self.atualizar_lider()

    @staticmethod
    def gerar_jogador_internacional(funcao, nacionalidade):
        nome = (f"{random.choice(NOMES_JOGADORES_INTERNACIONAIS[nacionalidade])} "
               f"{random.choice(SOBRENOMES_INTERNACIONAIS[nacionalidade])}")
        habilidade = round(random.gauss(85, 4))
        habilidade = max(85, min(90, habilidade))
        idade = random.choices([15, 16, 17], weights=[25, 35, 40], k=1)[0]
        return JogadorInternacional(nome, idade, habilidade, funcao, nacionalidade)

class CampeonatoInternacional:
    def __init__(self, ano, times_nacionais, resultados_manager):
        self.ano = ano
        self.times = self.gerar_times_internacionais() + [self.criar_selecao_brasileira(times_nacionais)]
        self.campeoes = []
        self.resultados_manager = resultados_manager
        self.rounds_para_vitoria = 13

    def criar_selecao_brasileira(self, times_nacionais):
        print("\n=== Seleção de Jogadores para a Seleção Brasileira ===")
        jogadores_selecionados = []
        todos_jogadores = []
        
        for time in times_nacionais:
            for jogador in time.jogadores:
                jogador_int = JogadorInternacional(
                    jogador.nome, 
                    jogador.idade,
                    jogador.habilidade,
                    jogador.funcao,
                    "Brasil"
                )
                jogador_int.total_abates = jogador.total_abates
                jogador_int.total_mortes = jogador.total_mortes
                jogador_int.time_atual = time.nome
                todos_jogadores.append(jogador_int)
        
        for funcao in Time.FUNCOES:
            print(f"\nEscolhendo {funcao}:")
            jogadores_disponiveis = [j for j in todos_jogadores if j.funcao == funcao]
            print("\nJogadores disponíveis:")
            for i, jogador in enumerate(jogadores_disponiveis, 1):
                print(f"{i}. {jogador.nome} (Time: {jogador.time_atual}, Habilidade: {jogador.habilidade}, K/D: {jogador.get_kd_display()})")
            
            while True:
                try:
                    escolha = int(input(f"\nEscolha o número do jogador para a função {funcao}: ")) - 1
                    if 0 <= escolha < len(jogadores_disponiveis):
                        jogador_escolhido = jogadores_disponiveis[escolha]
                        jogadores_selecionados.append(jogador_escolhido)
                        todos_jogadores.remove(jogador_escolhido)
                        break
                    print("Escolha inválida!")
                except ValueError:
                    print("Por favor, digite um número válido.")

        print("\nEscolha o líder da seleção:")
        for i, jogador in enumerate(jogadores_selecionados, 1):
            print(f"{i}. {jogador.nome} (Time: {jogador.time_atual}, Função: {jogador.funcao})")
        
        while True:
            try:
                lider_escolha = int(input("\nEscolha o número do jogador que será o líder: ")) - 1
                if 0 <= lider_escolha < len(jogadores_selecionados):
                    time_brasil = TimeInternacional("Brasil", jogadores_selecionados, "Brasil")
                    time_brasil.lider = jogadores_selecionados[lider_escolha]
                    break
                print("Escolha inválida!")
            except ValueError:
                print("Por favor, digite um número válido.")

        return time_brasil

    def gerar_times_internacionais(self):
        times = []
        paises_disponiveis = list(NOMES_JOGADORES_INTERNACIONAIS.keys())
        paises_disponiveis.remove("Brasil")
        paises_selecionados = random.sample(paises_disponiveis, 15)
        
        for pais in paises_selecionados:
            jogadores = []
            for funcao in Time.FUNCOES:
                nome = (f"{random.choice(NOMES_JOGADORES_INTERNACIONAIS[pais])} "
                       f"{random.choice(SOBRENOMES_INTERNACIONAIS[pais])}")
                habilidade = round(random.gauss(85, 4))
                habilidade = max(80, min(90, habilidade))
                idade = random.randint(15, 17)
                jogador = JogadorInternacional(nome, idade, habilidade, funcao, pais)
                jogadores.append(jogador)
            
            time = TimeInternacional(pais, jogadores, pais)
            times.append(time)
        
        return times

    def simular(self):
        map_pool = MapPool()
        map_pool.rotacionar_mapas(self.ano)
    
        campeonato = Campeonato(self.ano, 0, self.times)
        campeonato.MAPAS_DISPONIVEIS = map_pool.get_mapas_ativos()
        campeonato.resultados_manager = self.resultados_manager
            
        original_adicionar_resultado = campeonato.resultados_manager.adicionar_resultado
        def novo_adicionar_resultado(*args, **kwargs):
            if 'fase' in kwargs:
                kwargs['fase'] = f"Internacional - {kwargs['fase']}"
            elif len(args) > 3:
                args = list(args)
                args[3] = f"Internacional - {args[3]}"
                args = tuple(args)
            original_adicionar_resultado(*args, **kwargs)
        
        campeonato.resultados_manager.adicionar_resultado = novo_adicionar_resultado
        
        campeonato.simular()
        self.campeoes = [(self.ano, 0, time) for _, _, time in campeonato.campeoes]

def mostrar_historico_internacional(campeoes_internacionais):
    if not campeoes_internacionais:
        print("\nAinda não houve campeonatos internacionais.")
        return
    
    print("\n=== Histórico de Campeonatos Internacionais ===")
    for ano, _, time_vencedor in campeoes_internacionais:
        print(f"\nCampeonato Internacional {ano}")
        print(f"Campeão: {time_vencedor.nome} ({time_vencedor.nacionalidade})")
        print("\nJogadores do time campeão:")
        print(f"{'Nome':<25}{'Idade':<8}{'Habilidade':<12}{'Função':<15}{'K/D':<20}{'Nacionalidade':<15}")
        print("-" * 95)
        
        for jogador in time_vencedor.jogadores:
            lider = "*" if jogador == time_vencedor.lider else ""
            print(f"{jogador.nome + lider:<25}{jogador.idade:<8}{jogador.habilidade:<12}"
                  f"{jogador.funcao:<15}{jogador.get_kd_display():<20}{jogador.nacionalidade:<15}")