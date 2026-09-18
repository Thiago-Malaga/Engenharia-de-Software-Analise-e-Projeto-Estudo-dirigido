import datetime
import os
import csv

# Nome do ficheiro onde o estado do estacionamento será guardado
ARQUIVO_DADOS = "estado_estacionamento.csv"

class Vaga:
    def __init__(self, linha, coluna, reservada=False):
        self.localizacao = f"{linha}{coluna}"
        
        # REQUISITO 1: Visualização de vagas em tempo real[cite: 2]
        # Atributo que guarda o momento exato da atualização para manter o tempo real.
        self.tempo_ultima_atualizacao = datetime.datetime.now()
        self.ocupado = False 
        
        # REQUISITO 2: Prevenção de estacionamento em vagas reservadas[cite: 2]
        # Atributo que define se a vaga é exclusiva para funcionários.
        self.reservada = reservada

    def ocupar_vaga(self):
        # REQUISITO 1 (Critério de Aceitação 2): Ao ocupar uma vaga livre (reportagem manual), 
        # o sistema altera o status e atualiza o tempo[cite: 2].
        self.ocupado = True
        self.tempo_ultima_atualizacao = datetime.datetime.now()

    def desocupar_vaga(self):
        # REQUISITO 1: Atualização em tempo real da liberação da vaga[cite: 2].
        self.ocupado = False
        self.tempo_ultima_atualizacao = datetime.datetime.now()

    def __repr__(self):
        # REQUISITO 1 (Critério de Aceitação 1) e REQUISITO 2 (Critério de Aceitação 1):
        # Mostra de maneira simples se a vaga está livre/ocupada (Req 1) 
        # e sinaliza claramente se ela é reservada ou pública (Req 2)[cite: 2].
        status = "Ocupada" if self.ocupado else "Livre"
        tipo = "Reservada" if self.reservada else "Pública"
        tempo_formatado = self.tempo_ultima_atualizacao.strftime("%H:%M:%S")
        return f"[{self.localizacao} | {tipo} | {status} | {tempo_formatado}]"


def criar_estacionamento(num_linhas, num_colunas, linha_reservada):
    letras = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    matriz = []
    
    linha_reservada = str(linha_reservada).upper()
    
    for i in range(num_linhas):
        linha_vagas = []
        letra_linha = letras[i]
        
        for j in range(1, num_colunas + 1):
            # REQUISITO 2 (Critério de Aceitação 1): Sinalização de vagas reservadas[cite: 2].
            # Define que as vagas pertencentes à linha recebida como parâmetro serão marcadas como exclusivas.
            is_reservada = True if letra_linha == linha_reservada else False
            linha_vagas.append(Vaga(letra_linha, j, is_reservada))
            
        matriz.append(linha_vagas)
        
    return matriz


def imprimir_estacionamento(matriz):
    # REQUISITO 1 (Critério de Aceitação 1): Mostrar de maneira simples as vagas[cite: 2].
    for linha in matriz:
        for vaga in linha:
            print(vaga, end="  ")
        print("\n")


def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


def buscar_vaga(matriz, coordenada):
    try:
        letra = coordenada[0].upper()
        coluna = int(coordenada[1:]) - 1 
        linha = ord(letra) - ord('A')
        
        if 0 <= linha < len(matriz) and 0 <= coluna < len(matriz[0]):
            return matriz[linha][coluna]
    except (IndexError, ValueError):
        pass
    
    return None


def salvar_estado(matriz):
    with open(ARQUIVO_DADOS, mode='w', newline='', encoding='utf-8') as arquivo:
        writer = csv.writer(arquivo)
        writer.writerow(["linha", "coluna", "ocupado", "reservada", "tempo"])
        
        for linha in matriz:
            for vaga in linha:
                linha_str = vaga.localizacao[0]
                coluna_str = vaga.localizacao[1:]
                tempo_str = vaga.tempo_ultima_atualizacao.isoformat()
                writer.writerow([linha_str, coluna_str, vaga.ocupado, vaga.reservada, tempo_str])


def carregar_estado():
    if not os.path.exists(ARQUIVO_DADOS):
        return None

    linhas_dict = {}
    
    with open(ARQUIVO_DADOS, mode='r', encoding='utf-8') as arquivo:
        reader = csv.DictReader(arquivo)
        for row in reader:
            linha_str = row["linha"]
            coluna_int = int(row["coluna"])
            ocupado = row["ocupado"] == "True"
            reservada = row["reservada"] == "True"
            tempo = datetime.datetime.fromisoformat(row["tempo"])
            
            vaga = Vaga(linha_str, coluna_int, reservada)
            vaga.ocupado = ocupado
            vaga.tempo_ultima_atualizacao = tempo
            
            if linha_str not in linhas_dict:
                linhas_dict[linha_str] = []
            linhas_dict[linha_str].append(vaga)
            
    matriz = []
    for letra in sorted(linhas_dict.keys()):
        linha_ordenada = sorted(linhas_dict[letra], key=lambda v: int(v.localizacao[1:]))
        matriz.append(linha_ordenada)
        
    return matriz if matriz else None


def menu_interativo():
    limpar_tela()
    print("=== TELA DE LOGIN ===")
    tipo_usuario = ""
    while tipo_usuario not in ['aluno', 'servidor']:
        tipo_usuario = input("Você é 'aluno' ou 'servidor'? ").strip().lower()
        if tipo_usuario not in ['aluno', 'servidor']:
            print("Entrada inválida. Por favor, digite 'aluno' ou 'servidor'.")

    estacionamento = carregar_estado()
    
    if estacionamento is None:
        estacionamento = criar_estacionamento(3, 3, 'c')
        mensagem_alerta = "Sistema iniciado com um novo estacionamento."
    else:
        mensagem_alerta = "Dados recuperados do ficheiro CSV com sucesso!"

    while True:
        limpar_tela()
        print("=== APLICATIVO DE ESTACIONAMENTO EM TEMPO REAL ===")
        print(f"Usuário Logado: {tipo_usuario.capitalize()}")
        print("As vagas reservadas estarão assinaladas na matriz abaixo.\n")
        
        # Chamada para exibir a matriz (Requisito 1 visual)
        imprimir_estacionamento(estacionamento)
        
        if mensagem_alerta:
            print(f"-> {mensagem_alerta}\n")
            mensagem_alerta = ""
            
        print("Comandos: <coordenada> <acao> (Exemplo: 'A1 ocupar' ou 'A1 desocupar')")
        entrada = input("Digite o comando ou 'sair' para encerrar e guardar: ").strip().lower()
        
        if entrada == 'sair':
            salvar_estado(estacionamento)
            limpar_tela()
            print("Situação guardada no ficheiro CSV. Sistema encerrado com segurança.")
            break
            
        partes = entrada.split()
        if len(partes) != 2:
            mensagem_alerta = "ERRO: Formato inválido! Use '<coordenada> <ação>'."
            continue
            
        coordenada, acao = partes[0], partes[1]
        vaga = buscar_vaga(estacionamento, coordenada)
        
        if not vaga:
            mensagem_alerta = f"ERRO: Vaga '{coordenada.upper()}' não existe."
            continue
            
        if acao == 'ocupar':
            # REQUISITO 2 (Critérios de Aceitação 2 e 3)[cite: 2]: 
            # Se a vaga for reservada e o aluno tentar ocupar (reportar),
            # o sistema exibe mensagem de alerta informando a proibição e rejeita a ação.
            if vaga.reservada and tipo_usuario == 'aluno':
                mensagem_alerta = f"ALERTA: A vaga {vaga.localizacao} é reservada. Estacionamento de alunos é proibido neste local."
            elif vaga.ocupado:
                mensagem_alerta = f"AVISO: A vaga {vaga.localizacao} já está ocupada."
            else:
                # REQUISITO 1: Permite o aluno (ou servidor) ocupar a vaga se estiver livre e não houver restrições[cite: 2].
                vaga.ocupar_vaga()
                mensagem_alerta = f"SUCESSO: Vaga {vaga.localizacao} ocupada com sucesso."
                
        elif acao == 'desocupar':
            if not vaga.ocupado:
                mensagem_alerta = f"AVISO: A vaga {vaga.localizacao} já está livre."
            else:
                # REQUISITO 1: Liberação de vaga[cite: 2].
                vaga.desocupar_vaga()
                mensagem_alerta = f"SUCESSO: Vaga {vaga.localizacao} desocupada com sucesso."
                
        else:
            mensagem_alerta = "ERRO: Ação não reconhecida! Digite 'ocupar' ou 'desocupar'."


if __name__ == "__main__":
    menu_interativo()