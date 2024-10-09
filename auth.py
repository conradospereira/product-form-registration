
import sqlite3
import streamlit as st
import time
from database import cadastrar_usuario
from validator import validar_cnpj

def conectar_banco():
    conn = sqlite3.connect("product-registration.db")
    return conn

def autenticar(usuario, senha):
    conn = conectar_banco()
    cursor = conn.cursor()
    cursor.execute("SELECT senha, funcao FROM usuarios WHERE usuario = ?", (usuario,))
    resultado = cursor.fetchone()
    conn.close()

    if resultado and resultado[0] == senha:  # senha é igual
        st.session_state["funcao_atual"] = resultado[1]  # Armazena a função no estado da sessão
        return True
    return False

def pagina_cadastro():
    st.title("Cadastro de Novo Usuário")

    if "funcao" not in st.session_state:
        st.session_state.funcao = ""
    if "company_name" not in st.session_state:
        st.session_state.company_name = ""
    if "cnpj_cpf_company" not in st.session_state:
        st.session_state.cnpj_cpf_company = 0

    funcao = st.selectbox("Função", options=["", "Comercial", "Fornecedor"])

    st.session_state.funcao = funcao

    novo_usuario = st.text_input("Novo Usuário")
    nova_senha = st.text_input("Nova Senha", type="password")

    # Habilitar ou desabilitar campos com base na função selecionada
    if st.session_state.funcao == "Fornecedor":
        st.session_state.company_name = st.text_input("Nome da empresa em que trabalha", disabled=False)
        cnpj_cpf_company = st.text_input("Informe o CNPJ da empresa", disabled=False)

        # Validação de CNPJ
        if cnpj_cpf_company:
            if len(cnpj_cpf_company) != 14:
                st.error("O CNPJ deve ter 14 dígitos.")
            elif not validar_cnpj(cnpj_cpf_company):
                st.error("CNPJ inválido. Por favor, verifique o número.")
        st.session_state.cnpj_cpf_company = cnpj_cpf_company

    elif st.session_state.funcao == "Comercial":
        st.session_state.company_name = st.text_input("Razão social da empresa em que trabalha", disabled=True, value="-")
        st.session_state.cnpj_cpf_company = st.number_input("Informe o CNPJ ou CPF da empresa", disabled=True, value=0)

    if st.button("Cadastrar"):
        if novo_usuario and nova_senha and st.session_state.funcao:
            if st.session_state.funcao == "Fornecedor" and (not st.session_state.company_name or not st.session_state.cnpj_cpf_company):
                st.warning("Por favor, preencha todos os campos da empresa para o fornecedor!")
            else:
                if st.session_state.funcao == "Comercial":
                    st.session_state.company_name = "-"
                    st.session_state.cnpj_cpf_company = "-"

                resultado = cadastrar_usuario(novo_usuario, nova_senha, st.session_state.funcao, st.session_state.company_name, st.session_state.cnpj_cpf_company)
                if resultado:
                    st.success(f"Usuário {novo_usuario} cadastrado com sucesso!")
                    time.sleep(2)
                    st.session_state.pagina_atual = "login"
                    st.rerun()
                else:
                    st.error("Erro: Usuário já existe!")
        else:
            st.warning("Por favor, preencha todos os campos!")

    if st.button("Voltar"):
        st.session_state.pagina_atual = "login"
        st.rerun()

def pagina_login():
    st.title("Login")

    # Criando um formulário para o login
    with st.form("login_form"):
        usuario = st.text_input("Usuário")
        senha = st.text_input("Senha", type="password")
        login_botao = st.form_submit_button("Entrar")

        if login_botao:
            if autenticar(usuario, senha):
                st.session_state.login_autenticado = True
                st.session_state.pagina_atual = "formulario"
                st.rerun()
            else:
                st.error("Usuário ou senha incorretos!")

    if st.button("Criar Conta"):
        st.session_state.pagina_atual = "cadastro"
        st.rerun()