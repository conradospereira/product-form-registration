
import sqlite3

def conectar_banco():
    conn = sqlite3.connect("product-registration.db")
    return conn

# Função para criar as tabelas separadas para fornecedores e comerciais
def criar_tabelas():
    conn = conectar_banco()
    cursor = conn.cursor()

    # Criação da tabela de usuários
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario TEXT NOT NULL UNIQUE,
        company_name TEXT NOT NULL,
        cnpj_cpf_company TEXT NOT NULL,
        senha TEXT NOT NULL,
        funcao TEXT NOT NULL
    )
    ''')

    # Criação da tabela de produtos do fornecedor
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS produtos_fornecedor (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        departamento TEXT,
        categoria TEXT,
        subcategoria TEXT,
        segmento TEXT,
        margem_lucro REAL,
        cluster TEXT,
        tipo_suprimento TEXT,
        fracionado INTEGER
        ean13 TEXT,
        cod_display TEXT,
        quantidade_display INTEGER,
        ean14 TEXT,
        quantidade_caixa INTEGER,
        altura_cm REAL,
        largura_cm REAL,
        comprimento_cm REAL,
        peso_bruto_kg REAL,
        lastro INTEGER,
        camada INTEGER,
        validade_dias INTEGER,
        preco_compra_un REAL
        status TEXT DEFAULT "Pendente"
    )
    ''')

    conn.commit()
    conn.close()

# Função para salvar os dados do fornecedor
def salvar_dados_formulario(dados):
    conn = conectar_banco()
    cursor = conn.cursor()
    query = '''
    INSERT INTO produtos_fornecedor (departamento, categoria, subcategoria, segmento, 
    margem_lucro, cluster, tipo_suprimento, fracionado, ean13, cod_display, quantidade_display, ean14, quantidade_caixa, altura_cm, 
    largura_cm, comprimento_cm, peso_bruto_kg, lastro, camada, validade_dias, preco_compra_un)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    '''
    cursor.execute(query, dados)
    conn.commit()
    conn.close()

# Função para cadastrar novos usuários no banco de dados
def cadastrar_usuario(usuario, senha, funcao, company_name, cnpj_cpf_company):
    conn = conectar_banco()
    cursor = conn.cursor()

    # Verifica se o usuário já existe
    cursor.execute("SELECT usuario FROM usuarios WHERE usuario = ?", (usuario,))
    resultado = cursor.fetchone()

    if resultado:
        conn.close()
        return False  # Usuário já existe

    # Insere o novo usuário
    query = "INSERT INTO usuarios (usuario, senha, funcao, company_name, cnpj_cpf_company) VALUES (?, ?, ?, ?, ?)"
    cursor.execute(query, (usuario, senha, funcao, company_name, cnpj_cpf_company))
    conn.commit()
    conn.close()
    return True  # Cadastro realizado com sucesso