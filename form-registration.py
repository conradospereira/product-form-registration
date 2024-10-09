import streamlit as st
from auth import pagina_login, pagina_cadastro
from database import criar_tabelas
from forms import mostrar_formulario

# Criar a tabela de usuários no banco de dados ao iniciar a aplicação
criar_tabelas()

# Inicializa o estado de sessão
if "login_autenticado" not in st.session_state:
    st.session_state.login_autenticado = False

if "pagina_atual" not in st.session_state:
    st.session_state.pagina_atual = "login"  # Começa na página de login

# Lógica de navegação entre páginas
if st.session_state.pagina_atual == "login":
    pagina_login()  # Exibe a página de login

elif st.session_state.pagina_atual == "cadastro":
    pagina_cadastro()  # Exibe a página de cadastro

elif st.session_state.pagina_atual == "formulario" and st.session_state.login_autenticado:
    # Exibir o formulário completo baseado na função do usuário logado
    if "funcao_atual" in st.session_state:
        mostrar_formulario(st.session_state.funcao_atual)  # Mostra o formulário completo
    else:
        st.error("Erro: Função do usuário não definida.")
else:
    st.session_state.pagina_atual = "login"  # Se algo der errado, força o login
    st.experimental_rerun()  # Atualiza a página para o login