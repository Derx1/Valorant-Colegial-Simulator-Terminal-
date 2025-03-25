import random 
import os
from game import *
from dados import *
from international import *
def gerar_times(num_times):
    times = []
    for nome in random.sample(NOMES_TIMES, num_times):
        jogadores = []
        for i in range(5):  # Garantir que as funções são atribuídas em ordem
            funcao = Time.FUNCOES[i]
            jogador = Time.gerar_jogador()
            jogador.funcao = funcao
            jogadores.append(jogador)
        time = Time(nome, jogadores)
        times.append(time)
    return times

def mostrar_times_e_confrontos(times):
    print("\n--- Times Participantes ---")
    for i, time in enumerate(times, start=1):
        print(f"{i}. {time.nome}")


def mostrar_times_detalhados():
    print("\n=== Times e Jogadores ===")
    
    # Criar dicionário para contar vitórias por temporada
    vitorias_por_time = {}
    for time in times:
        vitorias_por_time[time.nome] = {'inverno': 0, 'verao': 0}
    
    # Contar vitórias de cada time
    for ano, numero, time_nome, _ in campeoes_gerais:
        if numero == 1:  # Inverno
            if time_nome in vitorias_por_time:
                vitorias_por_time[time_nome]['inverno'] += 1
        else:  # Verão
            if time_nome in vitorias_por_time:
                vitorias_por_time[time_nome]['verao'] += 1
    
    for i, time in enumerate(times, 1):
        # Criar indicadores de campeonatos
        indicadores = []
        
        # Adicionar indicador de inverno (x)
        if vitorias_por_time[time.nome]['inverno'] > 1:
            indicadores.append(f"x ({vitorias_por_time[time.nome]['inverno']})")
        elif vitorias_por_time[time.nome]['inverno'] == 1:
            indicadores.append("x")
            
        # Adicionar indicador de verão (+)
        if vitorias_por_time[time.nome]['verao'] > 1:
            indicadores.append(f"+ ({vitorias_por_time[time.nome]['verao']})")
        elif vitorias_por_time[time.nome]['verao'] == 1:
            indicadores.append("+")
        
        # Juntar indicadores com espaços
        indicador_str = " ".join(indicadores)
        
        # Nome do time com indicadores
        nome_display = f"{time.nome} {indicador_str}".strip()
        
        print(f"\n{i}. {nome_display}")
        print("-" * 90)  # Aumentado para acomodar o novo formato
        print(f"{'Nome':<20}{'Idade':<8}{'Habilidade':<12}{'Função':<15}{'K/D':<15}")
        print("-" * 90)
        
        for jogador in time.jogadores:
            lider = "*" if jogador == time.lider else ""
            kd = jogador.get_kd_display()
            print(f"{jogador.nome + lider:<20}{jogador.idade:<8}{jogador.habilidade:<12}"
                  f"{jogador.funcao:<15}{kd:<15}")
    
    input("\nPressione Enter para continuar...")

def mostrar_campeoes_detalhados():
    if not campeoes_gerais:
        print("\nAinda não há campeões registrados.")
        return
    
    print("\n=== Histórico de Campeões ===")
    for ano, numero, time_nome, jogadores in campeoes_gerais:
        temporada = "Inverno" if numero == 1 else "Verão"
        print(f"\nCampeonato {ano}.{numero} ({temporada})")
        print(f"Campeão: {time_nome}")
        print("\nJogadores do time campeão:")
        print(f"{'Nome':<20}{'Idade':<8}{'Habilidade':<12}{'K/D':<15}")
        print("-" * 60)
        
        for jogador in jogadores:
            abates = jogador['total_abates']
            mortes = jogador['total_mortes']
            ratio = round(abates / mortes if mortes > 0 else abates, 2)
            kd = f"{abates}/{mortes} ({ratio})"
            print(f"{jogador['nome']:<20}{jogador['idade']:<8}"
                  f"{jogador['habilidade']:<12}{kd:<15}")
    
    input("\nPressione Enter para continuar...")

def mostrar_resultados_torneios():
    ano, numero = resultados_manager.mostrar_campeonatos_disponiveis()
    if ano is not None and numero is not None:
        resultados_manager.mostrar_resultados_campeonato(ano, numero)
    
    input("\nPressione Enter para continuar...")

def menu_navegacao():
    while True:
        print("\n=== Menu de Navegação ===")
        print("1. Ver Times e Jogadores")
        print("2. Ver Campeões")
        print("3. Ver Resultados dos Torneios")
        print("4. Ver Campeonatos Internacionais")
        print("5. Iniciar Novo Torneio")
        print("6. Sair")
        
        opcao = input("\nEscolha uma opção: ").strip()
        
        if opcao == "1":
            mostrar_times_detalhados()
        elif opcao == "2":
            mostrar_campeoes_detalhados()
        elif opcao == "3":
            mostrar_resultados_torneios()
        elif opcao == "4":
            menu_internacional()
        elif opcao == "5":
            return True  # Inicia novo torneio
        elif opcao == "6":
            return False  # Sai do programa
        else:
            print("Opção inválida!")

def mostrar_resultados_internacionais():
    ano, numero = resultados_manager.mostrar_campeonatos_disponiveis()
    if ano is not None and numero is not None:
        resultados_manager.mostrar_resultados_campeonato(ano, numero)
    input("\nPressione Enter para continuar...")

def mostrar_selecoes_internacionais(times):
    print("\n=== Seleções Internacionais ===")
    for i, time in enumerate(times, 1):
        print(f"\n{i}. {time.nome} ({time.nacionalidade})")
        print("-" * 90)
        print(f"{'Nome':<20}{'Idade':<8}{'Habilidade':<12}{'Função':<15}{'K/D':<15}{'Nacionalidade':<15}")
        print("-" * 90)
        
        for jogador in time.jogadores:
            lider = "*" if jogador == time.lider else ""
            kd = jogador.get_kd_display()
            print(f"{jogador.nome + lider:<20}{jogador.idade:<8}{jogador.habilidade:<12}"
                  f"{jogador.funcao:<15}{kd:<15}{jogador.nacionalidade:<15}")
    
    input("\nPressione Enter para continuar...")

def menu_internacional():
    while True:
        print("\n=== Menu Internacional ===")
        print("1. Ver Histórico de Campeonatos Internacionais")
        print("2. Ver Resultados Detalhados")
        print("3. Ver Seleções Atuais")
        print("0. Voltar")
        
        opcao = input("\nEscolha uma opção: ").strip()
        
        if opcao == "1":
            mostrar_historico_internacional(campeoes_internacionais)
            input("\nPressione Enter para continuar...")
        elif opcao == "2":
            mostrar_resultados_internacionais()
        elif opcao == "3":
            if hasattr(campeonato_internacional_atual, 'times'):
                mostrar_selecoes_internacionais(campeonato_internacional_atual.times)
            else:
                print("\nNenhum campeonato internacional em andamento.")
                input("\nPressione Enter para continuar...")
        elif opcao == "0":
            break
        else:
            print("Opção inválida!")

def main():
    global times, campeoes_gerais, resultados_torneios, resultados_manager, campeoes_internacionais, campeonato_internacional_atual
    
    ano = 2024
    campeoes_gerais = []
    campeoes_internacionais = []
    resultados_torneios = []
    resultados_manager = ResultadosManager()
    campeonato_internacional_atual = None
    map_pool = MapPool()  # Criar instância do MapPool
    # Perguntar sobre campeonatos internacionais
    while True:
        try:
            print("\nDeseja incluir campeonatos internacionais?")
            resposta = input("Digite 'S' para sim ou 'N' para não: ").strip().upper()
            if resposta not in ['S', 'N']:
                raise ValueError("Resposta inválida. Digite 'S' para sim ou 'N' para não.")
            tem_internacional = resposta == 'S'
            break
        except ValueError as e:
            print(e)
    
    while True:
        # Perguntar o número de times
        while True:
            try:
                print("\nEscolha o número de times para o campeonato:")
                num_times = int(input("Digite 2, 4, 8, 16 ou 32: ").strip())
                if num_times not in [2, 4, 8, 16, 32]:
                    raise ValueError("Número inválido. Escolha entre 2, 4, 8, 16 ou 32.")
                break
            except ValueError as e:
                print(e)
        
        times = gerar_times(num_times)
        mostrar_times_e_confrontos(times)
        
        continuar = True
        while continuar:
            map_pool.rotacionar_mapas(ano)
            for numero in [1, 2]:
                campeonato = Campeonato(ano, numero, times)
                campeonato.resultados_manager = resultados_manager
                campeonato.MAPAS_DISPONIVEIS = map_pool.get_mapas_ativos()  # Definir mapas ativos
                campeonato.simular()
                
                vencedor_final = campeonato.campeoes[-1][2]
                jogadores_vencedores = [
                    {
                        "nome": j.nome,
                        "idade": j.idade,
                        "habilidade": j.habilidade,
                        "total_abates": j.total_abates,
                        "total_mortes": j.total_mortes,
                    }
                    for j in vencedor_final.jogadores
                ]
                campeoes_gerais.append((ano, numero, vencedor_final.nome, jogadores_vencedores))
                
                # Verificar se é ano de campeonato internacional (a cada 2 anos)
                if tem_internacional and numero == 2 and ano % 2 == 0:
                    print("\n=== Campeonato Internacional ===")
                    campeonato_internacional_atual = CampeonatoInternacional(ano, times, resultados_manager)
                    campeonato_internacional_atual.simular()
                    campeoes_internacionais.extend(campeonato_internacional_atual.campeoes)
            
            # Menu de navegação após cada ano
            continuar = menu_navegacao()
            
            if continuar:
                for time in times:
                    time.atualizar_jogadores()
                ano += 1
            else:
                break
        
        if not continuar:
            break
if __name__ == "__main__":
    main()