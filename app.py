import streamlit as st
import pandas as pd
import joblib

# Configuração da página do Streamlit
st.set_page_config(
    page_title="Predição de Doença Cardíaca",
    page_icon="❤️",
    layout="centered",
    initial_sidebar_state="expanded"
)

st.markdown("""
    <style>
    .main {
        background-color: #fdfbf7;
    }
    .stButton>button {
        width: 100%;
        background-color: #e63946;
        color: white;
        font-weight: bold;
        border-radius: 8px;
        border: none;
        padding: 10px 20px;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #c1121f;
        color: white;
    }
    .reportview-container .main .block-container{
        padding-top: 2rem;
    }
    h1 {
        color: #1d3557;
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
    }
    h3 {
        color: #457b9d;
    }
    div[data-testid="stExpander"] {
        border: 1px solid #e1dbd6;
        border-radius: 8px;
        background-color: #ffffff;
    }
    </style>
""", unsafe_allow_html=True)

# Título Principal e o Subtítulo
st.title("❤️ Predição de Doença Cardíaca")
st.markdown("---")
st.write("Este app utiliza Inteligência Artificial para analisar o risco ou presença de doença cardíaca com base nos dados clínicos fornecidos pelo paciente.")

# Carregamento do modelo e do scaler com tratamento de erros
@st.cache_resource
def carregar_artefatos():
    try:
        modelo = joblib.load("modelo_doenca_cardiaca.joblib")
        escala = joblib.load("scaler_modelo_doenca_cardiaca.joblib")
        return modelo, escala
    except Exception as e:
        st.error(f"Erro ao carregar os arquivos do modelo: {e}")
        return None, None

modelo, escala = carregar_artefatos()

if modelo is not None and escala is not None:
    st.sidebar.header("Informações do Projeto")
    st.sidebar.markdown("""
    **Instituição:** UNIMAR  
    **Curso:** ADS - Análise e Desenvolvimento de Sistemas  
    **Avaliação:** P2 - Projeto Avaliativo  
    **Modelo:** SVC (Scikit-Learn)
    """)
    
    st.subheader("Dados Clínicos do Paciente")
    
    # Organiza os campos de entrada em colunas e seções
    with st.expander("1. Informações de Estastisticas e Sintomas Primários", expanded=True):
        col1, col2 = st.columns(2)
        with col1:
            age = st.number_input("Idade", min_value=18, max_value=100, value=50, help="Idade cronológica do paciente.")
        with col2:
            sex = st.selectbox("Sexo", [0, 1], format_func=lambda x: "Feminino" if x == 0 else "Masculino", help="Sexo biológico do paciente.")
            
        cp = st.selectbox(
            "Tipo de Dor no Peito (cp)", 
            [0, 1, 2, 3],
            format_func=lambda x: {
                0: "0: Angina Típica",
                1: "1: Angina Atípica",
                2: "2: Dor Não-Anginosa",
                3: "3: Assintomático"
            }[x],
            help="Mapeamento do tipo de desconforto torácico relatado."
        )

    with st.expander("2. Sinais Vitais e Exames Laboratoriais", expanded=True):
        col3, col4 = st.columns(2)
        with col3:
            trestbps = st.number_input("Pressão Arterial em Repouso (mm Hg)", min_value=80, max_value=250, value=120)
            chol = st.number_input("Colesterol Sérico (mg/dl)", min_value=100, max_value=700, value=200)
        with col4:
            fbs = st.selectbox("Glicemia em Jejum > 120 mg/dl", [0, 1], format_func=lambda x: "Não" if x == 0 else "Sim")
            restecg = st.selectbox(
                "Resultado do ECG em Repouso", 
                [0, 1, 2],
                format_func=lambda x: {
                    0: "0: Normal",
                    1: "1: Anormalidades de ST-T",
                    2: "2: Hipertrofia Ventricular Esquerda"
                }[x]
            )

    with st.expander("3. Teste de Esforço Cardiológico", expanded=True):
        col5, col6 = st.columns(2)
        with col5:
            thalch = st.number_input("Frequência Cardíaca Máxima Atingida", min_value=60, max_value=250, value=150)
            exang = st.selectbox("Angina Induzida por Exercício", [0, 1], format_func=lambda x: "Não" if x == 0 else "Sim")
        with col6:
            oldpeak = st.number_input("Depressão de ST Induzida por Exercício (Oldpeak)", min_value=0.0, max_value=10.0, value=1.0, step=0.1)
            slope = st.selectbox(
                "Inclinação do Segmento ST (Slope)", 
                [0, 1, 2],
                format_func=lambda x: {
                    0: "0: Inclinação Para Cima (Upsloping)",
                    1: "1: Plano (Flat)",
                    2: "2: Inclinação Para Baixo (Downsloping)"
                }[x]
            )

    with st.expander("4. Marcadores Adicionais (Fluoroscopia e Cintilografia)", expanded=True):
        ca = st.selectbox("Número de Vasos Principais Coloridos por Fluoroscopia", [0, 1, 2, 3, 4])
        thal = st.selectbox(
            "Resultado do Teste de Estresse (Thal)", 
            [0, 1, 2, 3],
            format_func=lambda x: {
                0: "0: Normal",
                1: "1: Defeito Fixo",
                2: "2: Defeito Reversível",
                3: "3: Não Disponível"
            }[x]
        )

    st.markdown("<br>", unsafe_allow_html=True)
    
    # Botão de Execução
    if st.button("Realizar Predição"):
        dados_usuario ={
            'age': age,
            'sex': sex,
            'cp': cp,
            'trestbps': trestbps,
            'chol': chol,
            'fbs': fbs,
            'restecg': restecg,
            'thalch': thalch,
            'exang': exang,
            'oldpeak': oldpeak,
            'slope': slope,
            'ca': ca,
            'thal': thal
        }

        entrada = pd.DataFrame([dados_usuario])
        
        # Colunas que requerem a aplicação do StandardScaler
        cols_escala = ['age', 'trestbps', 'chol', 'thalch', 'oldpeak']
        
        # Garante a ordem correta para o fatiamento e transformação do scaler
        dados_para_escala = entrada[cols_escala]
        entrada[cols_escala] = escala.transform(dados_para_escala)
        
        # Faz a Previsão do modelo
        resultado = modelo.predict(entrada)[0]
        
        st.markdown("---")
        st.subheader("Resultado da Análise")
        
        if resultado == 1:
            st.error("**Possível presença de doença cardíaca.**")
            st.markdown("""
            * **Recomendação:** Os dados clínicos fornecidos sugerem padrões associados a condições cardíacas. 
            Recomenda-se que o paciente consulte um cardiologista para uma avaliação detalhada.
            """)
        else:
            st.success("✅ **Sem indícios de doença cardíaca.** ✅")
            st.markdown("""
            * **Interpretação:** Com base nos parâmetros informados pelo paciente, o modelo não identificou marcadores de risco elevados para doença cardíaca no momento. 
            """)