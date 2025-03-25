import random  
import os
from dados import*

class Jogador:
    def __init__(self, nome, idade, habilidade, funcao):
        self.nome = nome
        self.idade = idade
        self.habilidade = habilidade
        self.funcao = funcao
        self.agente = None  # Novo atributo para o agente
        self.abates = 0
        self.total_abates = 0
        self.mortes = 0
        self.total_mortes = 0
        self.abates_no_round = 0

    def sortear_agente(self, agentes_escolhidos=None):
        if agentes_escolhidos is None:
            agentes_escolhidos = []

        # Lista de agentes disponíveis para a função do jogador
        agentes_disponiveis = AGENTES_POR_FUNCAO[self.funcao]

        if self.funcao == "Flex":
            # Remove os agentes já escolhidos por outros jogadores
            agentes_disponiveis = [agente for agente in agentes_disponiveis if agente not in agentes_escolhidos]

        # Sorteia um agente dentre os disponíveis
        if agentes_disponiveis:
            self.agente = random.choice(agentes_disponiveis)
            agentes_escolhidos.append(self.agente)
        else:
            raise ValueError("Não há agentes disponíveis para a função 'Flex' sem duplicação.")


    def zerar_abates_no_round(self):
        self.abates_no_round = 0  # Reseta os abates no round

    def __str__(self):
        return (f"{self.nome} (Idade: {self.idade}, Habilidade: {self.habilidade}, "
                f"Função: {self.funcao}, Abates: {self.abates}, Total Abates: {self.total_abates}, Mortes: {self.mortes}, Total Mortes: {self.total_mortes})")

    def envelhecer(self):
        self.idade += 1
        if self.idade <= 17:
            self.habilidade += random.randint(-3, 4)
            self.habilidade = max(75, min(90, self.habilidade))
    def get_kd_ratio(self):
        """Retorna o K/D ratio em formato decimal"""
        if self.total_mortes == 0:
            return self.total_abates
        return round(self.total_abates / self.total_mortes, 2)

    def get_kd_display(self):
        """Retorna ambos os formatos de K/D"""
        ratio = self.get_kd_ratio()
        return f"{self.total_abates}/{self.total_mortes} ({ratio})"


class Time:
    FUNCOES = ["Duelista", "Flex", "Iniciador", "Controlador", "Sentinela"]

    def __init__(self, nome, jogadores):
        self.nome = nome
        self.jogadores = jogadores
        self.lider = self.definir_lider()  # Escolher o líder do time
        self.moral = 3 

    def definir_lider(self):
        return random.choice(self.jogadores)

    def atualizar_lider(self):
        self.lider = random.choice(self.jogadores)

    def obter_media_habilidade(self):
        return sum(j.habilidade for j in self.jogadores) / len(self.jogadores)

    def limpar_abates(self):
        for jogador in self.jogadores:
            jogador.abates = 0

    def limpar_mortes(self):
        for jogador in self.jogadores:
            jogador.mortes = 0

    def atualizar_jogadores(self):
        novos_jogadores = []
        for jogador in self.jogadores:
            jogador.envelhecer()
            if jogador.idade > 17:
                # Gera um novo jogador com a mesma função
                novos_jogadores.append(self.gerar_nvjogador(jogador.funcao))
            else:
                novos_jogadores.append(jogador)
        self.jogadores = novos_jogadores
        if self.lider not in self.jogadores:
            self.atualizar_lider()

    @staticmethod
    def gerar_jogador():
        nome = f"{random.choice(NOMES_JOGADORES)} {random.choice(SOBRENOMES)}"
        habilidade = round(random.gauss(82.5, 5))  # Média de 82.5 com desvio padrão de 5
        habilidade = max(75, min(90, habilidade))  # Garante que esteja entre 75 e 90
        idade = random.randint(15, 17)
        funcao = random.choice(Time.FUNCOES)
        return Jogador(nome, idade, habilidade, funcao)

    @staticmethod
    def gerar_nvjogador(funcao_antiga):
        nome = f"{random.choice(NOMES_JOGADORES)} {random.choice(SOBRENOMES)}"
        habilidade = round(random.gauss(82.5, 5))  # Média de 82.5 com desvio padrão de 5
        habilidade = max(75, min(90, habilidade))  # Garante que esteja entre 75 e 90
        idade = random.choices([15, 16, 17], weights=[60, 25, 15], k=1)[0]
        return Jogador(nome, idade, habilidade, funcao_antiga)


class Campeonato:
    def __init__(self, ano, numero, times, rounds_para_vitoria=13):
        self.ano = ano
        self.numero = numero
        self.times = random.sample(times, len(times))  # Sorteia a ordem dos confrontos
        self.campeoes = []
        self.rounds_para_vitoria = rounds_para_vitoria
        self.resultados_manager = None  # Novo atributo
        self.modo_simulacao_rapida = False  # Novo atributo para controlar o modo de simulação
        self.MAPAS_DISPONIVEIS = []  # Será definido pelo MapPool

    def sortear_agentes(self, time1, time2):
        """Sorteia agentes para os jogadores dos dois times, com o flex sendo o último a ser sorteado."""
        agentes_escolhidos = []  # Lista para rastrear agentes já atribuídos

        # Primeiro sorteamos os jogadores que não são flex
        for jogador in time1.jogadores + time2.jogadores:
            if jogador.funcao != "Flex":  # Se o jogador não for "Flex"
                jogador.sortear_agente(agentes_escolhidos)

        # Agora sorteamos o agente para os jogadores flex
        for jogador in time1.jogadores + time2.jogadores:
            if jogador.funcao == "Flex":  # Apenas os jogadores com função "Flex"
                jogador.sortear_agente(agentes_escolhidos)
                
    def simular_partida(self, time1, time2, melhor_de=None):
        # Determine melhor_de based on the phase
        if melhor_de is None:
            if len(self.times) == 2:  # Final
                melhor_de = 5
            elif len(self.times) in [4, 8, 16]:  # Oitavas, Quartas, Semifinal
                melhor_de = 3
            else:  # Fase de grupos
                melhor_de = 1

        mapas = random.sample(self.MAPAS_DISPONIVEIS, melhor_de)
        mapas_vencidos = {time1.nome: 0, time2.nome: 0}
        rounds_totais = {time1.nome: 0, time2.nome: 0}
        modo_rapido = True if self.modo_simulacao_rapida else False

        for mapa in mapas:
            print(f"\n--- Mapa Atual: {mapa} ---")
            self.sortear_agentes(time1, time2)
            
            placar = [0, 0]
            time1.limpar_abates()
            time1.limpar_mortes()
            time2.limpar_abates()
            time2.limpar_mortes()

            if not self.modo_simulacao_rapida:
                self.mostrar_agentes(time1, time2)
                
                if not modo_rapido:
                    resposta = input("\nPressione Enter para continuar, 'r' para modo rápido, ou 'n' para sair: ").strip().lower()
                    if resposta == 'n':
                        print("Encerrando simulação...")
                        exit()
                    elif resposta == 'r':
                        modo_rapido = True

            while not (max(placar) >= self.rounds_para_vitoria and abs(placar[0] - placar[1]) >= 2):
                x = random.randint(0, 4)

                vencedor, abates, mortes = self.simular_round(time1, time2)

                if vencedor == time1:
                    placar[0] += 1
                    self.distribuir_abates(time1, abates, vencedor=True)
                    self.distribuir_abates(time2, abates, vencedor=False, x=x)
                    self.distribuir_mortes(time2, vencedor=False)
                    self.distribuir_mortes(time1, vencedor=True, mortes=x)
                else:
                    placar[1] += 1
                    self.distribuir_abates(time2, abates, vencedor=True)
                    self.distribuir_abates(time1, abates, vencedor=False, x=x)
                    self.distribuir_mortes(time1, vencedor=False)
                    self.distribuir_mortes(time2, vencedor=True, mortes=x)

                self.limpar_console()
                print(f"Mapa: {mapa} | Placar: {time1.nome} {placar[0]} x {placar[1]} {time2.nome} | Mapas: {mapas_vencidos[time1.nome]} x {mapas_vencidos[time2.nome]}")
                self.mostrar_abates_round(time1, time2)

                # Se não estiver no modo rápido e não for o round final, pedir input
                round_final = max(placar) >= self.rounds_para_vitoria and abs(placar[0] - placar[1]) >= 2
                if not modo_rapido and not round_final:
                    resposta = input("\nPressione Enter para continuar, 'r' para modo rápido, ou 'n' para sair: ").strip().lower()
                    if resposta == 'n':
                        print("Encerrando simulação...")
                        exit()
                    elif resposta == 'r':
                        modo_rapido = True

            # Atualizar rounds totais
            rounds_totais[time1.nome] += placar[0]
            rounds_totais[time2.nome] += placar[1]

            # Atualizar mapas vencidos
            if placar[0] > placar[1]:
                mapas_vencidos[time1.nome] += 1
            else:
                mapas_vencidos[time2.nome] += 1

            print(f"\nMapa: {mapa} | Placar Final: {time1.nome} {placar[0]} x {placar[1]} {time2.nome}")
            print(f"Mapas Vencidos: {time1.nome} {mapas_vencidos[time1.nome]} x {mapas_vencidos[time2.nome]} {time2.nome}")

            # Verificar se algum time já venceu a série
            if mapas_vencidos[time1.nome] > melhor_de // 2 or mapas_vencidos[time2.nome] > melhor_de // 2:
                vencedor = time1 if mapas_vencidos[time1.nome] > mapas_vencidos[time2.nome] else time2
                fase_atual = "Final" if len(self.times) == 2 else (
                    "Semifinal" if len(self.times) == 4 else (
                    "Quartas de Final" if len(self.times) == 8 else 
                    "Oitavas de Final"
                ))
                self.resultados_manager.adicionar_resultado(
                    self.ano,
                    self.numero,
                    fase_atual,
                    'eliminatorias',
                    time1,
                    time2,
                    mapas_vencidos[time1.nome],
                    mapas_vencidos[time2.nome]
                )
                if melhor_de == 1:
                    return vencedor, placar[0], placar[1]
                return vencedor

        if melhor_de == 1:
            return time1 if mapas_vencidos[time1.nome] > mapas_vencidos[time2.nome] else time2, rounds_totais[time1.nome], rounds_totais[time2.nome]

        return time1 if mapas_vencidos[time1.nome] > mapas_vencidos[time2.nome] else time2

    def simular_round(self, time1, time2):
        # Zera os abates no round para cada jogador antes de começar o round
        for jogador in time1.jogadores:
            jogador.zerar_abates_no_round()
        for jogador in time2.jogadores:
            jogador.zerar_abates_no_round()
        habilidades_originais_time1 = {j: j.habilidade for j in time1.jogadores}
        habilidades_originais_time2 = {j: j.habilidade for j in time2.jogadores}

        # Ajuste aleatório de habilidade para simular variação por round
        for jogador in time1.jogadores:
            jogador.habilidade += random.uniform(-2, 2)
        for jogador in time2.jogadores:
            jogador.habilidade += random.uniform(-2, 2)

        # Peso das funções no desempenho do time
        pesos_funcoes = {
            "Duelista": 1.5,
            "Flex": 1.48,
            "Iniciador": 1.46,
            "Controlador": 1.46,
            "Sentinela": 1.47,
        }
        chance_time1 = sum(j.habilidade * pesos_funcoes[j.funcao] for j in time1.jogadores)
        chance_time2 = sum(j.habilidade * pesos_funcoes[j.funcao] for j in time2.jogadores)

        # Impacto do líder
        chance_time1 += time1.lider.habilidade * 1.1
        chance_time2 += time2.lider.habilidade * 1.1

        # Moral do time (simples, pode ser aprimorada)
        chance_time1 += time1.moral * 2
        chance_time2 += time2.moral * 2

        # Eventos aleatórios
        evento = random.choice(["clutch", "erro_tatico", "neutro"])
        if evento == "clutch":
            if random.random() > 0.5:
                chance_time1 *= 1.01
            else:
                chance_time2 *= 1.01
        elif evento == "erro_tatico":
            if random.random() > 0.5:
                chance_time1 *= 0.9
            else:
                chance_time2 *= 0.99
        chance_time1*=random.randint(-5, 10)
        chance_time2*=random.randint(-5, 10)
        vencedor = time1 if chance_time1 > chance_time2 else time2
        abates = 5
        mortes = 5

        # Atualiza a moral
        if vencedor == time1:
            time1.moral = min(time1.moral + 1, 5)
            time2.moral = max(time2.moral - 1, 0)
        else:
            time2.moral = min(time2.moral + 1, 5)
            time1.moral = max(time1.moral - 1, 0)

        # Restaurar as habilidades originais
        for jogador in time1.jogadores:
            jogador.habilidade = habilidades_originais_time1[jogador]
        for jogador in time2.jogadores:
            jogador.habilidade = habilidades_originais_time2[jogador]

        return vencedor, abates, mortes

    def distribuir_mortes(self, time, vencedor=False, mortes=0):
        jogadores_disponiveis = time.jogadores[:]  # Cópia da lista de jogadores para controle

        if vencedor:
            # O número de mortes no time vencedor será igual ao número de abates distribuídos no time perdedor.
            mortes_distribuidas = 0
            while mortes_distribuidas < mortes and jogadores_disponiveis:
                jogador = random.choice(jogadores_disponiveis)
                jogador.mortes += 1
                jogador.total_mortes += 1
                mortes_distribuidas += 1

                # Remove o jogador para garantir que ele morra apenas uma vez no round
                jogadores_disponiveis.remove(jogador)
        else:
            # Todos os jogadores do time perdedor sofrem uma morte, mas apenas uma vez por round
            for jogador in time.jogadores:
                jogador.mortes += 1
                jogador.total_mortes += 1

    @staticmethod
    def distribuir_abates(time, abates, vencedor, x=0):
        # Definir pesos por função (Duelistas têm maior chance)
        pesos_funcoes = {
            "Duelista": 1.3,
            "Flex": 1.2,
            "Iniciador": 1.1,
            "Controlador": 1.1,
            "Sentinela": 1.1,
        }
        
        # Calcular pontos totais para cada jogador baseado em habilidade e função
        jogadores_pontos = []
        for jogador in time.jogadores:
            # Normalizar habilidade para um multiplicador (75-90 -> 1.0-1.5)
            multiplicador_habilidade = 1 + ((jogador.habilidade - 75) / 20)
            # Calcular pontos totais considerando função e habilidade
            pontos = multiplicador_habilidade * pesos_funcoes[jogador.funcao]
            jogadores_pontos.append((jogador, pontos))
        
        # Calcular soma total dos pontos para normalização
        total_pontos = sum(pontos for _, pontos in jogadores_pontos)
        
        # Converter pontos em probabilidades
        jogadores_prob = [(jogador, pontos/total_pontos) for jogador, pontos in jogadores_pontos]
        
        # Determinar quantos abates distribuir
        pontos_distribuidos = abates if vencedor else x
        
        # Distribuir os abates com base nas probabilidades
        while pontos_distribuidos > 0:
            # Usar random.choices para selecionar jogador baseado nas probabilidades
            jogador = random.choices(
                population=[j for j, _ in jogadores_prob],
                weights=[p for _, p in jogadores_prob],
                k=1
            )[0]
            
            jogador.abates += 1
            jogador.total_abates += 1
            jogador.abates_no_round += 1
            pontos_distribuidos -= 1
    
    @staticmethod
    def mostrar_abates_round(time1, time2):
        largura_nome = 25  # Largura da coluna para o nome
        largura_kd = 15    # Largura para o K/D
        largura_funcao = 15  # Largura para a função
        largura_agentes = 15

        # Cabeçalho
        print(f"{'Time ' + time1.nome:<{largura_nome + largura_kd + largura_funcao + largura_agentes}}"
            f"{'':<5}"
            f"{'Time ' + time2.nome:<{largura_nome + largura_kd + largura_funcao + largura_agentes}}")
        print(f"{'Nome':<{largura_nome}}{'K/D (Δ)':<{largura_kd}}{'Função':<{largura_funcao}}{'Agentes':<{largura_agentes}}"
            f"{'':<5}"
            f"{'Nome':<{largura_nome}}{'K/D (Δ)':<{largura_kd}}{'Função':<{largura_funcao}}{'Agentes':<{largura_agentes}}")
        print("-" * (2 * (largura_nome + largura_kd + largura_funcao + largura_agentes) + 5))

        # Exibição dos jogadores de ambos os times
        for jogador1, jogador2 in zip(time1.jogadores, time2.jogadores):
            lider1 = "*" if jogador1 == time1.lider else ""
            lider2 = "*" if jogador2 == time2.lider else ""

            # Cálculo da diferença de abates para exibição
            delta_abates1 = f"+{jogador1.abates_no_round}" if jogador1.abates_no_round > 0 else ""
            delta_abates2 = f"+{jogador2.abates_no_round}" if jogador2.abates_no_round > 0 else ""

            linha_time1 = (f"{jogador1.nome + lider1:<{largura_nome}}"
                        f"{f'{jogador1.abates}/{jogador1.mortes} {delta_abates1}':<{largura_kd}}"
                        f"{jogador1.funcao:<{largura_funcao}}{jogador1.agente:<{largura_agentes}}")
            linha_time2 = (f"{jogador2.nome + lider2:<{largura_nome}}"
                        f"{f'{jogador2.abates}/{jogador2.mortes} {delta_abates2}':<{largura_kd}}"
                        f"{jogador2.funcao:<{largura_funcao}}{jogador2.agente:<{largura_agentes}}")
            print(f"{linha_time1}{'':<5}{linha_time2}")

    @staticmethod
    def mostrar_agentes(time1, time2):
        largura_nome = 25
        largura_funcao = 15
        largura_agente = 20

        print("\n--- Agentes Sorteados ---")
        print(f"{'Time ' + time1.nome:<{largura_nome + largura_funcao + largura_agente}}"
            f"{'':<5}"
            f"{'Time ' + time2.nome:<{largura_nome + largura_funcao + largura_agente}}")
        print(f"{'Nome':<{largura_nome}}{'Função':<{largura_funcao}}{'Agente':<{largura_agente}}"
            f"{'':<5}"
            f"{'Nome':<{largura_nome}}{'Função':<{largura_funcao}}{'Agente':<{largura_agente}}")
        print("-" * (2 * (largura_nome + largura_funcao + largura_agente) + 5))

        for jogador1, jogador2 in zip(time1.jogadores, time2.jogadores):
            linha_time1 = (f"{jogador1.nome:<{largura_nome}}{jogador1.funcao:<{largura_funcao}}{jogador1.agente:<{largura_agente}}")
            linha_time2 = (f"{jogador2.nome:<{largura_nome}}{jogador2.funcao:<{largura_funcao}}{jogador2.agente:<{largura_agente}}")
            print(f"{linha_time1}{'':<5}{linha_time2}")
    @staticmethod
    def limpar_console():
        os.system('cls' if os.name == 'nt' else 'clear')

    def simular(self):
        print(f"\nCampeonato {self.ano}.{self.numero}")
        
        # Adicionar opção de simulação rápida no início
        print("\nEscolha o modo de simulação:")
        print("1. Simulação normal (confirmar cada partida)")
        print("2. Simulação rápida (simular campeonato inteiro automaticamente)")
        
        while True:
            try:
                escolha = input("\nEscolha uma opção (1/2): ").strip()
                if escolha in ['1', '2']:
                    self.modo_simulacao_rapida = (escolha == '2')
                    break
                print("Opção inválida! Digite 1 ou 2.")
            except ValueError:
                print("Entrada inválida!")

        # Realizar a fase de grupos para 32 times
        if len(self.times) == 32:
            print("\n--- Fase de Grupos ---")
            self.realizar_fase_de_grupos()
            print("\n--- Oitavas de Final ---")
            self.times = random.sample(self.times, len(self.times))
            oitavas = [(self.times[i], self.times[i + 1]) for i in range(0, len(self.times), 2)]
        else:
            print(f"\n--- {'Oitavas de Final' if len(self.times) == 16 else 'Fase Inicial'} ---")
            self.times = random.sample(self.times, len(self.times))
            oitavas = [(self.times[i], self.times[i + 1]) for i in range(0, len(self.times), 2)]

        times_ativos = []
        for time1, time2 in oitavas:
            print(f"\nPróxima Partida: {time1.nome} vs {time2.nome}")
            if not self.modo_simulacao_rapida:
                self.exibir_infos_jogadores(time1, time2)
                if input("\nDeseja simular essa partida? (s/n): ").strip().lower() == 'n':
                    print("Encerrando simulação...")
                    exit()

            vencedor = self.simular_partida(time1, time2, melhor_de=(5 if len(self.times) == 2 else 3))
            times_ativos.append(vencedor)

        # Fases Eliminatórias subsequentes
        while len(times_ativos) > 1:
            fase = {
                8: "Quartas de Final",
                4: "Semifinais",
                2: "Final"
            }.get(len(times_ativos), "Fase Eliminatória")
            
            print(f"\n--- {fase} ---")
            novos_times = []
            
            for i in range(0, len(times_ativos), 2):
                print(f"\nPróxima Partida: {times_ativos[i].nome} vs {times_ativos[i + 1].nome}")
                if not self.modo_simulacao_rapida:
                    self.exibir_infos_jogadores(times_ativos[i], times_ativos[i + 1])
                    if input("\nDeseja simular esse jogo? (s/n): ").strip().lower() == 'n':
                        print("Encerrando simulação...")
                        exit()

                melhor_de = 5 if len(times_ativos) == 2 else 3
                vencedor = self.simular_partida(times_ativos[i], times_ativos[i + 1], melhor_de=melhor_de)
                novos_times.append(vencedor)
                
            times_ativos = novos_times

        # Exibir o vencedor final
        vencedor_final = times_ativos[0]
        self.campeoes.append((self.ano, self.numero, vencedor_final))
        print(f"\nVencedor do Campeonato {self.ano}.{self.numero}: {vencedor_final.nome}\n")

    @staticmethod
    def exibir_infos_jogadores(time1, time2):
        print("\n--- Informações dos Jogadores ---")
        # Cabeçalho dos times
        print(f"{'Time ' + time1.nome:<77}{'Time ' + time2.nome}")

        # Subcabeçalho das colunas
        print(f"{'Nome':<20}{'Idade':<10}{'Habilidade':<12}{'Função':<15}{'Abates/Mortes':<13}"
            f"{'':<7}"
            f"{'Nome':<20}{'Idade':<10}{'Habilidade':<12}{'Função':<15}{'Abates/Mortes':<13}")

        print("-" * 150)

        # Garantir que ambas as listas tenham o mesmo número de jogadores
        jogadores_time1 = time1.jogadores
        jogadores_time2 = time2.jogadores
        max_jogadores = max(len(jogadores_time1), len(jogadores_time2))

        # Preencher os times para alinhar as linhas
        if len(jogadores_time1) < max_jogadores:
            jogadores_time1 += [None] * (max_jogadores - len(jogadores_time1))
        if len(jogadores_time2) < max_jogadores:
            jogadores_time2 += [None] * (max_jogadores - len(jogadores_time2))

        # Exibir as informações alinhadas
        for j1, j2 in zip(jogadores_time1, jogadores_time2):
            # Jogador 1 (time 1)
            if j1:
                lider1 = "*" if j1 == time1.lider else ""
                linha1 = f"{j1.nome + lider1:<20}{j1.idade:<10}{j1.habilidade:<12}{j1.funcao:<15}" \
                        f"{f'{j1.total_abates}/{j1.total_mortes}':<15}"
            else:
                linha1 = " " * 72  # Espaço vazio se não houver jogador

            # Jogador 2 (time 2)
            if j2:
                lider2 = "*" if j2 == time2.lider else ""
                linha2 = f"{j2.nome + lider2:<20}{j2.idade:<10}{j2.habilidade:<12}{j2.funcao:<15}" \
                        f"{f'{j2.total_abates}/{j2.total_mortes}':<15}"
            else:
                linha2 = " " * 72  # Espaço vazio se não houver jogador

            # Exibir as linhas dos dois jogadores lado a lado
            print(f"{linha1}{'':<5}{linha2}")
    def realizar_fase_de_grupos(self):
        self.fase_de_grupos_realizada = True
        print("\n--- Fase de Grupos ---")
        
        grupos = []
        times_temp = self.times.copy()
        random.shuffle(times_temp)
        
        # Criar os grupos
        for i in range(0, 32, 4):
            grupo = times_temp[i:i+4]
            grupos.append(grupo)
        
        resultados_grupos = {}
        confrontos_diretos = {}
        
        # Inicializar resultados e confrontos
        for i, grupo in enumerate(grupos):
            nome_grupo = f'Grupo {chr(65+i)}'
            resultados_grupos[nome_grupo] = {
                time.nome: {
                    'pontos': 0,
                    'vitorias': 0,
                    'derrotas': 0,
                    'rounds_vencidos': 0,
                    'rounds_perdidos': 0,
                    'saldo_rounds': 0,
                    'maior_diferenca': 0,
                    'time_obj': time
                } for time in grupo
            }
            confrontos_diretos[nome_grupo] = {
                time1.nome: {time2.nome: None for time2 in grupo} for time1 in grupo
            }
        
        # Simular os jogos de cada grupo
        for i, grupo in enumerate(grupos):
            nome_grupo = f'Grupo {chr(65+i)}'
            print(f"\n=== {nome_grupo} ===")
            
            for j, time1 in enumerate(grupo):
                for time2 in grupo[j+1:]:
                    print(f"\nPróxima Partida: {time1.nome} vs {time2.nome}")
                    
                    # Só exibe as informações e pede confirmação se não estiver no modo rápido
                    if not self.modo_simulacao_rapida:
                        self.exibir_infos_jogadores(time1, time2)
                        if input("\nDeseja simular essa partida? (s/n): ").strip().lower() == 'n':
                            print("Encerrando simulação...")
                            exit()
                    
                    vencedor, rounds_time1, rounds_time2 = self.simular_partida(time1, time2, melhor_de=1)
                    diferenca = abs(rounds_time1 - rounds_time2)

                    # Registrar o resultado no gerenciador de resultados
                    self.resultados_manager.adicionar_resultado(
                        self.ano,
                        self.numero,
                        'Fase de Grupos',
                        'grupos',
                        time1,
                        time2,
                        rounds_time1,
                        rounds_time2,
                        grupo=nome_grupo
                    )
                    
                    # Atualizar resultados
                    if vencedor == time1:
                        resultados_grupos[nome_grupo][time1.nome]['pontos'] += 3
                        resultados_grupos[nome_grupo][time1.nome]['vitorias'] += 1
                        resultados_grupos[nome_grupo][time2.nome]['derrotas'] += 1
                        confrontos_diretos[nome_grupo][time1.nome][time2.nome] = True
                        confrontos_diretos[nome_grupo][time2.nome][time1.nome] = False
                    else:
                        resultados_grupos[nome_grupo][time2.nome]['pontos'] += 3
                        resultados_grupos[nome_grupo][time2.nome]['vitorias'] += 1
                        resultados_grupos[nome_grupo][time1.nome]['derrotas'] += 1
                        confrontos_diretos[nome_grupo][time2.nome][time1.nome] = True
                        confrontos_diretos[nome_grupo][time1.nome][time2.nome] = False
                    
                    # Atualizar estatísticas
                    for time_nome, rounds_favor, rounds_contra in [(time1.nome, rounds_time1, rounds_time2), 
                                                                (time2.nome, rounds_time2, rounds_time1)]:
                        stats = resultados_grupos[nome_grupo][time_nome]
                        stats['rounds_vencidos'] += rounds_favor
                        stats['rounds_perdidos'] += rounds_contra
                        stats['saldo_rounds'] = stats['rounds_vencidos'] - stats['rounds_perdidos']
                        if time_nome == vencedor.nome:
                            stats['maior_diferenca'] = max(stats['maior_diferenca'], diferenca)

        # Mostrar classificação final dos grupos
        print("\n=== Classificação Final dos Grupos ===")
        times_classificados = []
        
        for nome_grupo, resultados in resultados_grupos.items():
            print(f"\n{nome_grupo}")
            
            header = (
                f"{'Time':<25} {'P':^4} {'V':^4} {'D':^4} "
                f"{'RV':^4} {'RP':^4} {'SR':^4} {'MD':^4}"
            )
            print(header)
            print("-" * len(header))
            
            times_ordenados = sorted(
                resultados.items(),
                key=lambda x: (
                    x[1]['pontos'],
                    x[1]['saldo_rounds'],
                    x[1]['rounds_vencidos'],
                    x[1]['maior_diferenca']
                ),
                reverse=True
            )
            
            for i, (nome_time, stats) in enumerate(times_ordenados):
                linha = (
                    f"{nome_time:<25} "
                    f"{stats['pontos']:^4} "
                    f"{stats['vitorias']:^4} "
                    f"{stats['derrotas']:^4} "
                    f"{stats['rounds_vencidos']:^4} "
                    f"{stats['rounds_perdidos']:^4} "
                    f"{stats['saldo_rounds']:^4} "
                    f"{stats['maior_diferenca']:^4}"
                )
                print(linha)
                
                if i < 2:  # Os dois primeiros de cada grupo se classificam
                    times_classificados.append(stats['time_obj'])
        
        self.times = times_classificados
class ResultadosManager: 
    def __init__(self):
        self.resultados = {}  # Estrutura: {ano: {numero: {'grupos': [], 'eliminatorias': []}}}
    
    def adicionar_resultado(self, ano, numero, fase, tipo, time1, time2, placar1, placar2, grupo=None):
        if ano not in self.resultados:
            self.resultados[ano] = {}
        
        if numero not in self.resultados[ano]:
            self.resultados[ano][numero] = {'grupos': [], 'eliminatorias': []}
        
        resultado = {
            'time1': time1.nome,
            'time2': time2.nome,
            'placar1': placar1,
            'placar2': placar2,
            'fase': fase
        }
        
        if tipo == 'grupos':
            resultado['grupo'] = grupo
            self.resultados[ano][numero]['grupos'].append(resultado)
        else:
            self.resultados[ano][numero]['eliminatorias'].append(resultado)
    
    def mostrar_campeonatos_disponiveis(self):
        if not self.resultados:
            print("\nNão há resultados registrados ainda.")
            return None, None
        
        print("\n=== Campeonatos Disponíveis ===")
        campeonatos = []
        for ano in sorted(self.resultados.keys()):
            for numero in sorted(self.resultados[ano].keys()):
                campeonatos.append((ano, numero))
                print(f"{len(campeonatos)}. Campeonato {ano}.{numero}")
        
        try:
            escolha = int(input("\nEscolha um campeonato (0 para voltar): "))
            if escolha == 0:
                return None, None
            if 1 <= escolha <= len(campeonatos):
                return campeonatos[escolha-1]
            print("Escolha inválida!")
            return None, None
        except ValueError:
            print("Entrada inválida!")
            return None, None
    
    def mostrar_resultados_campeonato(self, ano, numero):
        if not self.resultados[ano][numero]['grupos']:
            # Se não houver fase de grupos, mostrar direto as eliminatórias
            self.mostrar_eliminatorias(ano, numero)
            return
        
        while True:
            print("\n=== Tipo de Fase ===")
            print("1. Fase de Grupos")
            print("2. Fase Eliminatória")
            print("0. Voltar")
            
            try:
                escolha = int(input("\nEscolha uma opção: "))
                if escolha == 0:
                    return
                elif escolha == 1:
                    self.mostrar_grupos(ano, numero)
                elif escolha == 2:
                    self.mostrar_eliminatorias(ano, numero)
                else:
                    print("Opção inválida!")
            except ValueError:
                print("Entrada inválida!")
    
    def mostrar_grupos(self, ano, numero):
        print(f"\n=== Resultados da Fase de Grupos - Campeonato {ano}.{numero} ===")
        resultados_grupos = {}
        
        # Organizar resultados por grupo
        for resultado in self.resultados[ano][numero]['grupos']:
            grupo = resultado['grupo']
            if grupo not in resultados_grupos:
                resultados_grupos[grupo] = []
            resultados_grupos[grupo].append(resultado)

        # Calcular classificação por grupo
        standings = {}
        for grupo, resultados in resultados_grupos.items():
            standings[grupo] = {}
            for resultado in resultados:
                for time_nome in [resultado['time1'], resultado['time2']]:
                    if time_nome not in standings[grupo]:
                        standings[grupo][time_nome] = {
                            'pontos': 0,
                            'jogos': 0,
                            'vitorias': 0,
                            'derrotas': 0,
                            'rounds_pro': 0,
                            'rounds_contra': 0
                        }
                
                # Atualizar classificação
                time1, time2 = resultado['time1'], resultado['time2']
                if resultado['placar1'] > resultado['placar2']:
                    standings[grupo][time1]['pontos'] += 3
                    standings[grupo][time1]['vitorias'] += 1
                    standings[grupo][time2]['derrotas'] += 1
                else:
                    standings[grupo][time2]['pontos'] += 3
                    standings[grupo][time2]['vitorias'] += 1
                    standings[grupo][time1]['derrotas'] += 1
                
                standings[grupo][time1]['jogos'] += 1
                standings[grupo][time2]['jogos'] += 1
                standings[grupo][time1]['rounds_pro'] += resultado['placar1']
                standings[grupo][time1]['rounds_contra'] += resultado['placar2']
                standings[grupo][time2]['rounds_pro'] += resultado['placar2']
                standings[grupo][time2]['rounds_contra'] += resultado['placar1']
        
        # Mostrar resultados de cada grupo
        for grupo, resultados in sorted(resultados_grupos.items()):
            print(f"\nGrupo {grupo}")
            print("-" * 80)
            
            # Exibir tabela de classificação
            print("Classificação:")
            print(f"{'Time':<25} {'P':^4} {'J':^4} {'V':^4} {'D':^4} {'GP':^4} {'GC':^4} {'SG':^4}")
            print("-" * 80)
            
            # Ordenar times pela pontuação e saldo de gols
            sorted_teams = sorted(
                standings[grupo].items(),
                key=lambda x: (x[1]['pontos'], 
                            x[1]['rounds_pro'] - x[1]['rounds_contra'], 
                            x[1]['rounds_pro']),
                reverse=True
            )
            
            for time, stats in sorted_teams:
                saldo = stats['rounds_pro'] - stats['rounds_contra']
                print(f"{time:<25} {stats['pontos']:^4} {stats['jogos']:^4} "
                    f"{stats['vitorias']:^4} {stats['derrotas']:^4} "
                    f"{stats['rounds_pro']:^4} {stats['rounds_contra']:^4} "
                    f"{saldo:^4}")
            
            # Exibir partidas
            print("\nPartidas:")
            print("-" * 50)
            for r in resultados:
                print(f"{r['time1']} {r['placar1']} x {r['placar2']} {r['time2']}")
            print("\n")  # Espaço extra entre grupos
            
    def mostrar_eliminatorias(self, ano, numero): 
        print(f"\n=== Resultados das Eliminatórias - Campeonato {ano}.{numero} ===")
        
        # Obter apenas os resultados das eliminatórias
        resultados = self.resultados[ano][numero]['eliminatorias']
        
        if not resultados:
            print("Não há resultados registrados nas eliminatórias.")
            return

        # Determinar o número total de jogos e iniciar a lógica dinâmica
        total_jogos = len(resultados)
        fases = ["Final", "Semifinal", "Quartas de Final", "Oitavas de Final"]

        # Criar uma estrutura dinâmica para as fases
        fases_organizadas = {}
        fase_atual = 0
        while total_jogos > 0 and fase_atual < len(fases):
            jogos_na_fase = min(total_jogos, 2 ** fase_atual)
            fase_nome = fases[fase_atual] if fase_atual < len(fases) else f"Fase {fase_atual + 1}"
            fases_organizadas[fase_nome] = resultados[-jogos_na_fase:]  # Pegar os últimos jogos da lista
            resultados = resultados[:-jogos_na_fase]  # Remover os jogos já processados
            total_jogos -= jogos_na_fase
            fase_atual += 1

        # Exibir os resultados em ordem das oitavas até a final
        for fase in reversed(fases):  # Ordem inversa (Oitavas até Final)
            if fase in fases_organizadas:  # Garantir que a fase existe
                print(f"\n{fase}")  # Nome da fase
                print("-" * 50)  # Tracejado abaixo do nome da fase
                for jogo in fases_organizadas[fase]:
                    print(f"{jogo['time1']} {jogo['placar1']} x {jogo['placar2']} {jogo['time2']}")

        print("\n")  # Espaçamento final
class MapPool:
    def __init__(self):
        self.ano_atual = 2024
        self.mapas_ativos = MAPAS_INICIAIS.copy()
        
    def rotacionar_mapas(self, novo_ano):
        if novo_ano != self.ano_atual:
            # Se for o primeiro ano, mantém os mapas iniciais
            if self.ano_atual == 2024:
                self.mapas_ativos = MAPAS_INICIAIS.copy()
            else:
                # Remove 2 mapas aleatórios dos ativos
                mapas_removidos = random.sample(self.mapas_ativos, 2)
                for mapa in mapas_removidos:
                    self.mapas_ativos.remove(mapa)
                
                # Seleciona 2 mapas novos dos que não estão ativos
                mapas_disponiveis = [m for m in TODOS_MAPAS if m not in self.mapas_ativos]
                mapas_novos = random.sample(mapas_disponiveis, 2)
                self.mapas_ativos.extend(mapas_novos)
            
            self.ano_atual = novo_ano

    
    def get_mapas_ativos(self):
        return self.mapas_ativos.copy()

