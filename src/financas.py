import pandas as pd
import os
import time
from datetime import datetime, timedelta

# --- Configuração de Caminhos ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, '..', 'data')
os.makedirs(DATA_DIR, exist_ok=True)

# --- Constantes de Arquivos ---
ARQUIVO_GANHOS = os.path.join(DATA_DIR, 'ganhos.csv')
ARQUIVO_DESPESAS_FIXAS = os.path.join(DATA_DIR, 'despesas_fixas.csv')
ARQUIVO_DESPESAS_VARIAVEIS = os.path.join(DATA_DIR, 'despesas_variaveis.csv')
ARQUIVO_DIVIDAS = os.path.join(DATA_DIR, 'dividas.csv')
ARQUIVO_INVESTIMENTOS = os.path.join(DATA_DIR, 'investimentos.csv')
ARQUIVO_CARTOES = os.path.join(DATA_DIR, 'cartoes.csv')
ARQUIVO_METAS = os.path.join(DATA_DIR, 'metas.csv')

# --- Helpers ---
def set_data_dir(path: str) -> None:
    """Atualiza ``DATA_DIR`` e todos os caminhos de arquivos.

    Parameters
    ----------
    path: str
        Novo diretório onde os arquivos CSV serão armazenados.
    """
    global DATA_DIR, ARQUIVO_GANHOS, ARQUIVO_DESPESAS_FIXAS, ARQUIVO_DESPESAS_VARIAVEIS
    global ARQUIVO_DIVIDAS, ARQUIVO_INVESTIMENTOS, ARQUIVO_CARTOES, ARQUIVO_METAS

    DATA_DIR = path
    os.makedirs(DATA_DIR, exist_ok=True)
    ARQUIVO_GANHOS = os.path.join(DATA_DIR, 'ganhos.csv')
    ARQUIVO_DESPESAS_FIXAS = os.path.join(DATA_DIR, 'despesas_fixas.csv')
    ARQUIVO_DESPESAS_VARIAVEIS = os.path.join(DATA_DIR, 'despesas_variaveis.csv')
    ARQUIVO_DIVIDAS = os.path.join(DATA_DIR, 'dividas.csv')
    ARQUIVO_INVESTIMENTOS = os.path.join(DATA_DIR, 'investimentos.csv')
    ARQUIVO_CARTOES = os.path.join(DATA_DIR, 'cartoes.csv')
    ARQUIVO_METAS = os.path.join(DATA_DIR, 'metas.csv')

# --- Constantes de Colunas ---
COLUNAS_GANHOS = ['Descricao', 'Data', 'Valor']
COLUNAS_DESPESAS_FIXAS = ['Descricao', 'Categoria', 'Data', 'Valor', 'Status', 'Forma_Pagamento']
COLUNAS_DESPESAS_VARIAVEIS = ['Descricao', 'Categoria', 'Data', 'Valor', 'Forma_Pagamento', 'Cartao_Utilizado', 'Numero_Parcelas']
COLUNAS_DIVIDAS = ['Descricao', 'Credor', 'Data_Pagamento', 'Valor_Parcela', 'Valor_Total', 'Status']
COLUNAS_INVESTIMENTOS = ['Produto', 'Corretora', 'Tipo', 'Valor_Aportado', 'Data_Aporte']
COLUNAS_CARTOES = ['Nome_Cartao', 'Limite', 'Dia_Vencimento']
COLUNAS_METAS = ['Objetivo', 'Valor_Alvo', 'Data_Alvo']

# --- Constantes de Configuração ---
CATEGORIAS_DESPESA = ("Casa", "Profissional", "Pessoal", "Mercado", "Farmácia e Saúde", "Lazer", "Shopping", "Festas", "Assinaturas", "Transporte", "Viagens", "Estudos", "Restaurante", "Uber/99Taxi", "Comida Delivery")
LIMITES_CATEGORIAS = {"Mercado": 800.00, "Lazer": 400.00, "Restaurante": 350.00, "Shopping": 500.00, "Uber/99Taxi": 150.00, "Comida Delivery": 200.00}


# --- Funções de Manipulação de Dados ---
def carregar_ou_criar_df(nome_arquivo, colunas):
    if os.path.exists(nome_arquivo):
        df = pd.read_csv(nome_arquivo)
        for col in colunas:
            if col not in df.columns:
                df[col] = None
        return df[colunas]
    else:
        return pd.DataFrame(columns=colunas)

def adicionar_ganho(descricao, data, valor):
    df = carregar_ou_criar_df(ARQUIVO_GANHOS, COLUNAS_GANHOS)
    novo_registro = pd.DataFrame([{'Descricao': descricao, 'Data': data, 'Valor': valor}])
    df_atualizado = pd.concat([df, novo_registro], ignore_index=True)
    df_atualizado.to_csv(ARQUIVO_GANHOS, index=False)

def adicionar_despesa_fixa(descricao, categoria, data, valor, status, forma_pagamento):
    df = carregar_ou_criar_df(ARQUIVO_DESPESAS_FIXAS, COLUNAS_DESPESAS_FIXAS)
    novo_registro = pd.DataFrame([{'Descricao': descricao, 'Categoria': categoria, 'Data': data, 'Valor': valor, 'Status': status, 'Forma_Pagamento': forma_pagamento}])
    df_atualizado = pd.concat([df, novo_registro], ignore_index=True)
    df_atualizado.to_csv(ARQUIVO_DESPESAS_FIXAS, index=False)

def adicionar_despesa_variavel(descricao, categoria, data, valor, forma_pagamento, cartao, parcelas):
    df = carregar_ou_criar_df(ARQUIVO_DESPESAS_VARIAVEIS, COLUNAS_DESPESAS_VARIAVEIS)
    novo_registro = pd.DataFrame([{'Descricao': descricao, 'Categoria': categoria, 'Data': data, 'Valor': valor, 'Forma_Pagamento': forma_pagamento, 'Cartao_Utilizado': cartao, 'Numero_Parcelas': parcelas}])
    df_atualizado = pd.concat([df, novo_registro], ignore_index=True)
    df_atualizado.to_csv(ARQUIVO_DESPESAS_VARIAVEIS, index=False)

def adicionar_divida(descricao, credor, data_pagamento, valor_parcela, valor_total, status):
    df = carregar_ou_criar_df(ARQUIVO_DIVIDAS, COLUNAS_DIVIDAS)
    novo_registro = pd.DataFrame([{'Descricao': descricao, 'Credor': credor, 'Data_Pagamento': data_pagamento, 'Valor_Parcela': valor_parcela, 'Valor_Total': valor_total, 'Status': status}])
    df_atualizado = pd.concat([df, novo_registro], ignore_index=True)
    df_atualizado.to_csv(ARQUIVO_DIVIDAS, index=False)

def adicionar_investimento(produto, corretora, tipo, valor_aportado, data_aporte):
    df = carregar_ou_criar_df(ARQUIVO_INVESTIMENTOS, COLUNAS_INVESTIMENTOS)
    novo_registro = pd.DataFrame([{'Produto': produto, 'Corretora': corretora, 'Tipo': tipo, 'Valor_Aportado': valor_aportado, 'Data_Aporte': data_aporte}])
    df_atualizado = pd.concat([df, novo_registro], ignore_index=True)
    df_atualizado.to_csv(ARQUIVO_INVESTIMENTOS, index=False)

def adicionar_cartao(nome, limite, dia_vencimento):
    df = carregar_ou_criar_df(ARQUIVO_CARTOES, COLUNAS_CARTOES)
    if not df[df['Nome_Cartao'].str.lower() == nome.lower()].empty:
        print(f"❌ Erro: O cartão '{nome}' já está cadastrado.")
        return
    novo_cartao = pd.DataFrame([{'Nome_Cartao': nome, 'Limite': limite, 'Dia_Vencimento': dia_vencimento}])
    df_atualizado = pd.concat([df, novo_cartao], ignore_index=True)
    df_atualizado.to_csv(ARQUIVO_CARTOES, index=False)
    print(f"✅ Cartão '{nome}' adicionado com sucesso!")

def adicionar_meta(objetivo, valor_alvo, data_alvo):
    df = carregar_ou_criar_df(ARQUIVO_METAS, COLUNAS_METAS)
    nova_meta = pd.DataFrame([{'Objetivo': objetivo, 'Valor_Alvo': valor_alvo, 'Data_Alvo': data_alvo}])
    df_atualizado = pd.concat([df, nova_meta], ignore_index=True)
    df_atualizado.to_csv(ARQUIVO_METAS, index=False)
    print(f"✅ Meta '{objetivo}' adicionada ao seu Mural dos Sonhos!")


# --- Funções de Leitura e Análise ---
def listar_cartoes():
    df = carregar_ou_criar_df(ARQUIVO_CARTOES, COLUNAS_CARTOES)
    if df.empty:
        print("\nNenhum cartão cadastrado.")
        return
    print("\n--- 💳 Seus Cartões de Crédito ---")
    df_sorted = df.sort_values(by='Nome_Cartao').reset_index(drop=True)
    for idx, row in enumerate(df_sorted.itertuples(index=False), 1):
        limite_str = f"R$ {row.Limite:,.2f}"
        print(f"{idx}. Nome: {row.Nome_Cartao:<15} | Limite: {limite_str:<15} | Vencimento: Dia {row.Dia_Vencimento}")
    print("-" * 65)

def excluir_cartao():
    df = carregar_ou_criar_df(ARQUIVO_CARTOES, COLUNAS_CARTOES)
    df_sorted = df.sort_values(by='Nome_Cartao').reset_index(drop=True)
    print("\n-- Excluir Cartão --")
    if df_sorted.empty:
        print("Nenhum cartão cadastrado para excluir.")
        return
    for idx, row in enumerate(df_sorted.iterrows(), 1):
        print(f"{idx}. {row[1]['Nome_Cartao']}")
    print("-" * 25)
    while True:
        try:
            escolha = int(input("Digite o número do cartão que deseja excluir (ou 0 para cancelar): "))
            if escolha == 0:
                print("Operação cancelada."); return
            if 1 <= escolha <= len(df_sorted):
                indice_para_excluir = escolha - 1
                cartao_selecionado = df_sorted.loc[indice_para_excluir]
                break
            else:
                print("❌ Número fora do intervalo. Tente novamente.")
        except ValueError:
            print("❌ Erro: Por favor, digite um número.")
    confirmacao = input(f"Você tem certeza que deseja excluir o cartão '{cartao_selecionado['Nome_Cartao']}'? (s/n): ")
    if confirmacao.lower() == 's':
        df_final = df[df['Nome_Cartao'] != cartao_selecionado['Nome_Cartao']]
        df_final.to_csv(ARQUIVO_CARTOES, index=False)
        print(f"✅ Cartão '{cartao_selecionado['Nome_Cartao']}' excluído com sucesso.")
    else:
        print("Exclusão cancelada.")

def listar_metas():
    df = carregar_ou_criar_df(ARQUIVO_METAS, COLUNAS_METAS)
    if df.empty:
        print("\nVocê ainda não tem nenhuma meta cadastrada. Comece a sonhar!")
        return
    print("\n" + "="*50); print("✨ Seu Mural dos Sonhos ✨".center(50)); print("="*50)
    hoje = datetime.now()
    for _, row in df.iterrows():
        try:
            data_alvo = datetime.strptime(row['Data_Alvo'], '%Y-%m')
            meses_restantes = (data_alvo.year - hoje.year) * 12 + data_alvo.month - hoje.month
            print(f"\n🎯 Objetivo: {row['Objetivo']}"); print(f"💰 Valor Alvo: R$ {row['Valor_Alvo']:,.2f}"); print(f"🗓️ Data Alvo: {data_alvo.strftime('%B de %Y')}")
            if meses_restantes > 0:
                poupanca_mensal = row['Valor_Alvo'] / meses_restantes
                print(f"⏳ Tempo Restante: {meses_restantes} meses"); print(f"💸 Economia Mensal Necessária: R$ {poupanca_mensal:,.2f}")
            elif meses_restantes == 0:
                 print("🚨 Último mês para alcançar sua meta!")
            else:
                print("⚠️ Prazo da meta expirado.")
            print("-" * 50)
        except (ValueError, TypeError):
            print(f"\n⚠️ Erro ao processar a meta '{row['Objetivo']}'. Verifique o formato da data (deve ser AAAA-MM)."); print("-" * 50)

def criar_resumo_mensal():
    df_ganhos = carregar_ou_criar_df(ARQUIVO_GANHOS, COLUNAS_GANHOS)
    df_fixas = carregar_ou_criar_df(ARQUIVO_DESPESAS_FIXAS, COLUNAS_DESPESAS_FIXAS)
    df_variaveis = carregar_ou_criar_df(ARQUIVO_DESPESAS_VARIAVEIS, COLUNAS_DESPESAS_VARIAVEIS)
    df_dividas = carregar_ou_criar_df(ARQUIVO_DIVIDAS, COLUNAS_DIVIDAS)
    df_dividas = df_dividas.rename(columns={'Data_Pagamento': 'Data', 'Valor_Parcela': 'Valor'})
    resumos = []
    for df, nome_coluna in [(df_ganhos, 'Total de Ganhos'), (df_fixas, 'Total de Despesas Fixas'), (df_variaveis, 'Total de Despesas Variáveis'), (df_dividas, 'Total de Dívidas')]:
        if not df.empty and 'Data' in df.columns and 'Valor' in df.columns:
            df['Data'] = pd.to_datetime(df['Data'], errors='coerce'); df.dropna(subset=['Data'], inplace=True); df['Mes'] = df['Data'].dt.to_period('M'); resumo_mes = df.groupby('Mes')['Valor'].sum().rename(nome_coluna); resumos.append(resumo_mes)
    if not resumos: return pd.DataFrame()
    tabela_resumo = pd.concat(resumos, axis=1).fillna(0); colunas_principais = ['Total de Ganhos', 'Total de Despesas Fixas', 'Total de Despesas Variáveis', 'Total de Dívidas']
    for col in colunas_principais:
        if col not in tabela_resumo.columns: tabela_resumo[col] = 0.0
    tabela_resumo['Balanço'] = (tabela_resumo['Total de Ganhos'] - tabela_resumo['Total de Despesas Fixas'] - tabela_resumo['Total de Despesas Variáveis'] - tabela_resumo['Total de Dívidas']); return tabela_resumo.sort_index()

def verificar_limites(mes_periodo):
    df_fixas = carregar_ou_criar_df(ARQUIVO_DESPESAS_FIXAS, COLUNAS_DESPESAS_FIXAS); df_variaveis = carregar_ou_criar_df(ARQUIVO_DESPESAS_VARIAVEIS, COLUNAS_DESPESAS_VARIAVEIS); df_despesas = pd.concat([df_fixas, df_variaveis], ignore_index=True);
    if df_despesas.empty: print("Nenhuma despesa registrada para verificar limites."); return
    df_despesas['Data'] = pd.to_datetime(df_despesas['Data'], errors='coerce'); df_despesas.dropna(subset=['Data'], inplace=True); df_despesas['Mes'] = df_despesas['Data'].dt.to_period('M'); despesas_mes_atual = df_despesas[df_despesas['Mes'] == mes_periodo];
    if despesas_mes_atual.empty: print(f"Nenhuma despesa registrada para o mês de {mes_periodo}."); return
    gastos_por_categoria = despesas_mes_atual.groupby('Categoria')['Valor'].sum(); print(f"\n--- Limites de Gastos para {mes_periodo} ---"); print(f"{'Categoria':<20} | {'Gasto':>12} | {'Limite':>12} | {'Status':>10}"); print("-" * 65)
    for categoria, limite in LIMITES_CATEGORIAS.items():
        gasto = gastos_por_categoria.get(categoria, 0); status = "✅ OK" if gasto <= limite else "❌ EXCEDIDO"; gasto_str = f"R$ {gasto:,.2f}"; limite_str = f"R$ {limite:,.2f}"; print(f"{categoria:<20} | {gasto_str:>12} | {limite_str:>12} | {status:>10}")
    print("-" * 65)

def exibir_calendario_vencimentos():
    hoje = datetime.now(); limite_data = hoje + timedelta(days=30); df_fixas = carregar_ou_criar_df(ARQUIVO_DESPESAS_FIXAS, COLUNAS_DESPESAS_FIXAS); df_dividas = carregar_ou_criar_df(ARQUIVO_DIVIDAS, COLUNAS_DIVIDAS); df_fixas_pend = df_fixas.rename(columns={'Valor': 'Valor_Pagar'}); df_dividas_pend = df_dividas.rename(columns={'Data_Pagamento': 'Data', 'Valor_Parcela': 'Valor_Pagar'}); vencimentos = []
    if not df_fixas_pend.empty: df_fixas_pend = df_fixas_pend[df_fixas_pend['Status'].str.lower() == 'pendente']; df_fixas_pend['Data'] = pd.to_datetime(df_fixas_pend['Data'], errors='coerce'); df_fixas_pend.dropna(subset=['Data'], inplace=True); vencimentos.append(df_fixas_pend[['Data', 'Descricao', 'Valor_Pagar']])
    if not df_dividas_pend.empty: df_dividas_pend = df_dividas_pend[df_dividas_pend['Status'].str.lower() == 'pendente']; df_dividas_pend['Data'] = pd.to_datetime(df_dividas_pend['Data'], errors='coerce'); df_dividas_pend.dropna(subset=['Data'], inplace=True); vencimentos.append(df_dividas_pend[['Data', 'Descricao', 'Valor_Pagar']])
    if not vencimentos: print("\nNenhuma conta pendente encontrada."); return
    df_vencimentos = pd.concat(vencimentos, ignore_index=True); df_vencimentos = df_vencimentos[(df_vencimentos['Data'] >= hoje) & (df_vencimentos['Data'] <= limite_data)];
    if df_vencimentos.empty: print("\n🎉 Nenhuma conta pendente a vencer nos próximos 30 dias!"); return
    df_vencimentos = df_vencimentos.sort_values(by='Data'); print("\n--- 🗓️ Contas a Vencer nos Próximos 30 Dias ---")
    for _, row in df_vencimentos.iterrows():
        data_venc = row['Data'].strftime('%d/%m/%Y (%a)'); descricao = row['Descricao']; valor = row['Valor_Pagar']; dias_restantes = (row['Data'] - hoje).days; print(f"🗓️ Vence em {dias_restantes} dias ({data_venc}): {descricao} - R$ {valor:,.2f}")
    print("-" * 55)


# --- Funções do Menu ---
def aguardar_enter():
    input("\nPressione Enter para voltar ao menu...")
def obter_valor_float(mensagem):
    while True:
        entrada = input(mensagem)
        try:
            limpa = entrada.replace('.', '').replace(',', '.')
            return float(limpa)
        except ValueError:
            print("❌ Erro: Por favor, digite um número válido.")
def obter_valor_int(mensagem):
    while True:
        try: return int(input(mensagem))
        except ValueError: print("❌ Erro: Por favor, digite um número inteiro.")
def escolher_categoria():
    print("\n-- Escolha a Categoria da Despesa --")
    for i, cat in enumerate(CATEGORIAS_DESPESA, 1):
        print(f"{i}. {cat}")
    while True:
        try:
            escolha = int(input("Digite o número da categoria: "))
            if 1 <= escolha <= len(CATEGORIAS_DESPESA): return CATEGORIAS_DESPESA[escolha - 1]
            else: print("❌ Número fora do intervalo. Tente novamente.")
        except ValueError: print("❌ Erro: Por favor, digite um número.")

# --- Menus e Sub-menus ---
def exibir_menu_principal():
    print("\n" + "="*40); print("   MENU PRINCIPAL - CONTROLE FINANCEIRO"); print("="*40)
    print("1. Adicionar Ganho\n2. Adicionar Despesa Fixa\n3. Adicionar Despesa Variável")
    print("4. Adicionar Dívida (Pagamento de Parcela)\n5. Adicionar Investimento\n6. Ver Resumo Mensal")
    print("7. Calendário de Vencimentos\n8. Mural dos Sonhos (Metas)")
    print("9. Configurações e Gerenciamento")
    print("10. Sair")
    print("="*40)

def menu_gerenciamento_cartoes():
    while True:
        print("\n--- ⚙️ Gerenciamento de Cartões ---")
        print("1. Listar Cartões Cadastrados\n2. Adicionar Novo Cartão\n3. Excluir Cartão\n4. Voltar ao Menu Principal")
        print("-" * 35)
        escolha = input("Escolha uma opção: ")
        if escolha == '1': listar_cartoes(); aguardar_enter()
        elif escolha == '2': print("\n-- Adicionar Novo Cartão --"); nome = input("Nome do Cartão: "); limite = obter_valor_float("Limite: "); dia_vencimento = obter_valor_int("Dia do Vencimento: "); adicionar_cartao(nome, limite, dia_vencimento); aguardar_enter()
        elif escolha == '3': excluir_cartao(); aguardar_enter()
        elif escolha == '4': print("Voltando ao menu principal..."); break
        else: print("\n❌ Opção inválida. Tente novamente."); time.sleep(2)

def menu_metas_financeiras():
    while True:
        print("\n--- ✨ Mural dos Sonhos ---")
        print("1. Ver Minhas Metas\n2. Adicionar Nova Meta\n3. Voltar ao Menu Principal")
        print("-" * 30)
        escolha = input("Escolha uma opção: ")
        if escolha == '1': listar_metas(); aguardar_enter()
        elif escolha == '2':
            print("\n-- Adicionar Nova Meta ao Mural --")
            objetivo = input("Qual o seu sonho/objetivo? "); valor_alvo = obter_valor_float("Quanto ele custa? R$ "); data_alvo = input("Para quando você quer conquistá-lo? (AAAA-MM): "); adicionar_meta(objetivo, valor_alvo, data_alvo); aguardar_enter()
        elif escolha == '3': print("Voltando ao menu principal..."); break
        else: print("\n❌ Opção inválida. Tente novamente."); time.sleep(2)


# --- Bloco Principal Interativo ---
if __name__ == "__main__":
    while True:
        exibir_menu_principal()
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            print("\n-- Adicionar Novo Ganho --"); desc = input("Descrição: "); data = input("Data (AAAA-MM-DD): "); val = obter_valor_float("Valor: "); adicionar_ganho(desc, data, val); print("\n✅ Ganho adicionado!"); aguardar_enter()
        elif escolha == '2':
            print("\n-- Adicionar Despesa Fixa --"); desc = input("Descrição: "); cat = escolher_categoria(); data = input("Data: "); val = obter_valor_float("Valor: "); stat = input("Status: "); form = input("Forma de Pagamento: "); adicionar_despesa_fixa(desc, cat, data, val, stat, form); print("\n✅ Despesa adicionada!"); aguardar_enter()
        elif escolha == '3':
            print("\n-- Adicionar Despesa Variável --"); desc = input("Descrição: "); cat = escolher_categoria(); data = input("Data: "); val = obter_valor_float("Valor: "); form = input("Forma de Pagamento: "); cart = input("Cartão: "); parc = obter_valor_int("Parcelas: "); adicionar_despesa_variavel(desc, cat, data, val, form, cart, parc); print("\n✅ Despesa adicionada!"); aguardar_enter()
        elif escolha == '4':
            print("\n-- Adicionar Pagamento de Dívida --"); desc = input("Descrição: "); cred = input("Credor: "); data = input("Data Pagamento: "); val_p = obter_valor_float("Valor da Parcela: "); val_t = obter_valor_float("Valor Total: "); stat = input("Status: "); adicionar_divida(desc, cred, data, val_p, val_t, stat); print("\n✅ Dívida adicionada!"); aguardar_enter()
        elif escolha == '5':
            print("\n-- Adicionar Investimento --"); prod = input("Produto: "); corr = input("Corretora: "); tipo = input("Tipo: "); val_ap = obter_valor_float("Valor Aportado: "); data_ap = input("Data do Aporte: "); adicionar_investimento(prod, corr, tipo, val_ap, data_ap); print("\n✅ Investimento adicionado!"); aguardar_enter()
        elif escolha == '6':
            print("\n-- Resumo Mensal --"); resumo = criar_resumo_mensal()
            if resumo.empty: print("Nenhum dado para exibir.")
            else:
                resumo_f = resumo.copy()
                for c in resumo_f.columns: resumo_f[c] = resumo_f[c].apply(lambda x: f"R$ {x:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
                print(resumo_f)
            verificar_limites(pd.Timestamp.now().to_period('M')); aguardar_enter()
        elif escolha == '7':
            exibir_calendario_vencimentos(); aguardar_enter()
        elif escolha == '8':
            menu_metas_financeiras()
        elif escolha == '9':
            menu_gerenciamento_cartoes()
        elif escolha == '10':
            print("\nSaindo do programa. Até logo! 👋"); break
        else:
            print("\n❌ Opção inválida. Por favor, tente novamente."); time.sleep(2)