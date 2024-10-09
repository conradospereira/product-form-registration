
import streamlit as st
from database import salvar_dados_formulario
from validator import validar_formulario

def formulario():
    with st.form("Cadastro de Produto", clear_on_submit=True):
        if st.session_state.funcao_atual != "Fornecedor":  # Exibe os campos apenas para comerciais
            st.subheader("Dados do Fornecedor")
            departamento = st.text_input("DEPARTAMENTO")
            categoria = st.text_input("CATEGORIA")
            subcategoria = st.text_input("SUBCATEGORIA")
            segmento = st.text_input("SEGMENTO")
            margem_lucro = st.number_input("MARGEM DE LUCRO %")
            cluster = st.selectbox("CLUSTER A-B-C-D", options=["A", "B", "C", "D"])
            tipo_suprimento = st.selectbox("TIPO DE SUPRIMENTO", options=["Seleção inversa", "Centralizado", "Direto loja"])
            fracionado = 1 if st.selectbox("FRACIONADO", options=["Sim", "Não"]) == "Sim" else 0
        else:
            # Valores padrões para o fornecedor (opcionais, se necessário)
            departamento = None
            categoria = None
            subcategoria = None
            segmento = None
            margem_lucro = None
            cluster = None
            tipo_suprimento = None
            fracionado = None

        # Campos visíveis para todos (comercial e fornecedor)
        ean_13 = st.text_input("EAN 13 (UNIDADE)")
        cod_display = st.text_input("CÓD DISPLAY (SE TIVER)")
        quantidade_display = st.number_input("QUANTIDADE (DISPLAY)", min_value=0, step=1, format="%d")
        ean_14 = st.text_input("EAN 14 (CAIXA)")
        quantidade_caixa = st.number_input("QUANTIDADE (CAIXA)", min_value=0, step=1, format="%d")
        altura_cm = st.number_input("ALTURA CM (CAIXA)")
        largura_cm = st.number_input("LARGURA CM")
        comprimento_cm = st.number_input("COMPRIMENTO CM")
        peso_bruto_kg = st.number_input("PESO BRUTO KG")
        lastro = st.number_input("LASTRO", min_value=0, step=1, format="%d")
        camada = st.number_input("CAMADA", min_value=0, step=1, format="%d")
        validade_dias = st.number_input("VALIDADE EM DIAS", min_value=0, step=1, format="%d")
        preco_compra_un = st.number_input("PREÇO DE COMPRA UN")

        enviar_botao = st.form_submit_button("Enviar")

        if enviar_botao:
            erros = validar_formulario(departamento, categoria, subcategoria, segmento, margem_lucro, cluster, tipo_suprimento, fracionado, ean_13, cod_display, quantidade_display, ean_14, quantidade_caixa, altura_cm, largura_cm, comprimento_cm, peso_bruto_kg, preco_compra_un)

            if erros:
                for erro in erros:
                    st.error(erro)
            else:
                dados_produto = (
                    ean_13, cod_display, quantidade_display, ean_14, quantidade_caixa,
                    altura_cm, largura_cm, comprimento_cm, peso_bruto_kg, lastro,
                    camada, validade_dias, preco_compra_un
                )
                salvar_dados_formulario(dados_produto)
                st.success("Dados do Fornecedor cadastrados com sucesso!")

    # Botão "Voltar" para retornar à página de login
    if st.button("Voltar"):
        st.session_state.pagina_atual = "login"
        st.rerun()

def mostrar_formulario(funcao_usuario):
    """Mostra o formulário apropriado com base na função do usuário"""
    if funcao_usuario == "Fornecedor":
        formulario()
    elif funcao_usuario == "Comercial":
        formulario()
    else:
        st.error("Função do usuário não reconhecida.")
