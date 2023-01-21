# =======================================================
# BIBLIOTECAS
# =======================================================

import pandas as pd
import numpy as np
import fundamentus
import streamlit as st
import plotly.express as px



st.set_page_config(
    page_title= 'Carteira de Ações',
    layout= 'wide' )

# =======================================================
# FUNÇÕES
# =======================================================

@st.cache
def data_collect( ):
    lista_grupos = [
    'AGXY3', 'FRTA3', 'AGRO3', 'SLCE3', 'TTEN3', 'SOJA3', 'ORVR3', 'SAPR3', 'SAPR11', 'SAPR4', 'CSMG3', 'SBSP3', 
    'BRFS3', 'MRFG3', 'MNPR3', 'JBSS3', 'JALL3', 'CAML3', 'SMTO3', 'JOPA3', 'BEEF3', 'JOPA4', 'MDIA3', 'BAUH4',
    'ONCO3', 'HAPV3', 'DASA3', 'AALR3', 'KRSA3', 'QUAL3', 'ODPV3', 'PARD3', 'FLRY3', 'MATD3', 'RDOR3', 'AMBP3',
    'PLAS3', 'MYPK3', 'LEVE3','ABEV3', 'MGLU3', 'ESPA3', 'VIIA3', 'CEAB3', 'AMAR3', 'LLIS3', 'SLED4', 'SLED3', 
    'EPAR3', 'CGRA4', 'CGRA3', 'WLMM3', 'ALLD3', 'WLMM4', 'SBFG3', 'BTTL3', 'GUAR3', 'LREN3', 'ARZZ3', 'SOMA3',
    'PETZ3', 'AMER3', 'LJQQ3', 'PCAR3', 'PFRM3', 'DMVF3', 'GMAT3', 'CRFB3', 'BLAU3', 'HYPE3', 'VVEO3', 'PGMN3', 
    'PNVL3', 'ASAI3', 'RADL3', 'POSI3', 'MLAS3', 'INTB3', 'GFSA3', 'CRDE3', 'VIVR3', 'TCSA3', 'TEND3', 'JFEN3', 
    'AVLL3', 'RSID3', 'PDGR3', 'MDNE3', 'JHSF3', 'HBOR3', 'MELK3', 'CYRE3', 'CALI3', 'PLPL3', 'EVEN3', 'EZTC3', 
    'MRVE3', 'LAVV3', 'CURY3', 'MTRE3', 'TRIS3', 'DIRR3', 'RDNI3','TCNO3', 'TCNO4', 'ETER3', 'HAGA4', 'SOND5', 
    'SOND6', 'PTBL3', 'HAGA3', 'AZEV4', 'AZEV3', 'YDUQ3', 'COGN3', 'SEER3', 'ANIM3', 'BAHI3', 'DOTZ3', 'MOVI3', 
    'MILS3', 'VAMO3', 'RENT3', 'CSED3', 'ARML3', 'MTIG4', 'AESB3', 'CBEE3', 'LIGT3', 'RNEW4', 'RNEW3', 'RNEW11',
    'CEBR3', 'CLSC3', 'CEBR5', 'CEBR6', 'CLSC4', 'NEOE3', 'GPAR3', 'AFLT3', 'ENBR3', 'TRPL4', 'CEEB5', 'CEEB3', 
    'ENGI4', 'COCE5', 'CMIG4', 'TAEE11', 'TAEE4', 'TAEE3', 'EKTR3', 'CSRN5', 'CSRN6', 'EKTR4', 'CSRN3', 'EQMA3B',
    'TRPL3', 'CPFE3', 'ENGI11', 'REDE3', 'ALUP4', 'ALUP3', 'ALUP11', 'CMIG3', 'EQPA3', 'CEED4', 'CEED3', 'ENGI3',
    'MEGA3', 'EQTL3', 'EQPA5', 'EQPA7', 'ENMT4', 'ENMT3', 'GEPA3', 'GEPA4', 'EGIE3', 'ENEV3', 'EMAE4', 'ELET3', 
    'ELET6', 'CPLE11', 'CPLE6', 'LIPR3', 'CEPE5', 'CEPE6', 'AURE3', 'CPLE5','BALM4', 'BALM3', 'SCAR3', 'BRPR3', 
    'IGBR3', 'NEXP3', 'GSHP3', 'SYNE3', 'HBRE3', 'LOGG3', 'BRML3', 'ALSO3', 'MULT3', 'JPSA3', 'LPSB3', 'HBTS5', 
    'IGTI3', 'IGTI11', 'CGAS3', 'CGAS5', 'PEAB4', 'PEAB3', 'SIMH3', 'MOAR3', 'ZAMP3', 'MEAL3', 'HOOT4', 'BAZA3', 
    'BNBR3', 'DMFN3', 'BBAS3', 'ITSA4', 'ABCB4', 'BRSR6', 'BEES3', 'ITSA3', 'BMEB4', 'BMGB4', 'BEES4', 'BMEB3', 
    'BBDC3', 'BRSR3', 'SANB3', 'BRIV4', 'ITUB3', 'BBDC4', 'BRIV3', 'SANB11', 'SANB4', 'ITUB4', 'BPAC5', 'BSLI4',
    'BRSR5', 'BRBI11', 'RPAD6', 'BGIP4', 'RPAD5', 'BMIN4', 'CRIV4', 'CRIV3', 'RPAD3', 'BSLI3', 'BPAN4', 'BPAC11', 
    'BGIP3', 'BMIN3', 'PINE4', 'BPAC3', 'MERC4', 'MODL3', 'MERC3', 'EUCA4', 'EUCA3', 'SUZB3', 'KLBN3', 'KLBN11', 
    'KLBN4', 'DXCO3', 'RANI3', 'AERI3', 'NORD3', 'FRIO3', 'INEP4', 'INEP3', 'BDLL4', 'TASA4', 'TASA3', 'BDLL3', 'CPLE3',
    'EALT4', 'MTSA4', 'EALT3', 'KEPL3', 'ROMI3', 'SHUL4', 'WEGE3', 'SNSY5', 'RCSL3', 'EMBR3', 'RCSL4', 'MWET4', 'MWET3',
    'RAPT3', 'RAPT4', 'RSUL4', 'POMO3', 'TUPY3', 'POMO4', 'FRAS3','BIOM3', 'OFSA3', 'ELMD3','BRAP3', 'BRAP4', 'VALE3', 
    'AURA33', 'CBAV3', 'CMIN3', 'BLUT3', 'BLUT4', 'ATOM3', 'DMMO3', 'LUPA3', 'RPMG3', 'OSXB3', 'OPCT3', 'PETR4', 'PETR3',
    'ENAT3', 'VBBR3', 'PRIO3', 'UGPA3', 'RECV3', 'CSAN3', 'RAIZ4', 'RRRP3','CSAB4', 'CSAB3', 'IRBR3', 'WIZS3', 'BRGE11',  
    'BRGE3', 'CXSE3', 'BRGE12', 'BRGE5', 'BRGE6', 'BBSE3', 'PSSA3', 'APER3', 'SULA3', 'SULA4', 'SULA11', 'NTCO3', 'BOBR4',
    'TRAD3', 'CASH3', 'NINJ3', 'IFCM3', 'MBLY3', 'WEST3', 'ENJU3', 'LVTC3', 'BMOB3', 'TOTS3', 'SQIA3', 'NGRD3', 'LWSA3',
    'FHER3', 'DEXP4', 'DEXP3', 'UNIP3', 'UNIP6', 'UNIP5', 'CRPG6', 'CRPG5', 'BRKM5', 'BRKM3', 'BRKM6', 'VITT3', 'CRPG3',
    'DTCY3', 'SEQL3', 'ALPK3', 'ATMP3', 'PRNR3', 'CSUD3', 'GGPS3', 'VLID3', 'CLSA3', 'GPIV33', 'GETT4', 'GETT3', 'BOAS3', 
    'CIEL3', 'B3SA3', 'PDTC3', 'PMAM3', 'MGEL4', 'USIM3', 'USIM5', 'GOAU3', 'GOAU4', 'GGBR3', 'USIM6', 'TKNO4', 'GGBR4', 
    'FESA4', 'FESA3', 'CSNA3', 'PATI3', 'PATI4', 'CTKA3', 'CTKA4', 'CEDO3', 'CTSA3', 'CEDO4', 'CTSA4', 'CTNM3', 'TXRX4', 
    'CTNM4', 'SGPS3', 'MNDL3', 'TEKA4', 'PTNT4', 'TECN3', 'CAMB3', 'PTNT3', 'VULC3', 'GRND3', 'VIVA3', 'DOHL4', 'TFCO4', 
    'ALPA3', 'ALPA4', 'DOHL3', 'TELB3', 'TELB4', 'OIBR4', 'OIBR3', 'FIQE3', 'VIVT3', 'TIMS3', 'DESK3', 'BRIT3', 'RAIL3', 
    'TPIS3', 'HBSA3', 'AZUL4', 'GOLL4', 'CCRO3', 'TGMA3', 'JSLG3', 'MRSA6B', 'MRSA6B', 'MRSA3B', 'MRSA3B', 'STBP3', 'MRSA5B','BRGE8',
    'MRSA5B', 'PORT3', 'ECOR3', 'LOGN3', 'LUXM4','HETA4', 'UCAS3', 'WHRL3', 'WHRL4', 'SMFT3', 'SHOW3', 'AHEB3', 'CVCB3', 'ESTR4', 'BMKS3'
    ]
    
    df_raw = pd.DataFrame()

    for grupo in lista_grupos:
        df_aux = fundamentus.get_papel( grupo )
        df_raw = pd.concat( [df_raw, df_aux] )
    
    return df_raw

# ------------------------------------------------------------------------------------------------------------

def data_cleaning( df ):
    # rename
    old_cols = ['Papel', 'Tipo', 'Empresa', 'Setor', 'Subsetor', 'Cotacao', 'Data_ult_cot', 'Min_52_sem', 'Max_52_sem', 
                'Vol_med_2m', 'Valor_de_mercado', 'Valor_da_firma', 'Ult_balanco_processado', 'Nro_Acoes', 'PL', 'PVP',
                'PEBIT', 'PSR', 'PAtivos', 'PCap_Giro', 'PAtiv_Circ_Liq', 'Div_Yield', 'EV_EBITDA', 'EV_EBIT', 'Cres_Rec_5a',
                'LPA', 'VPA', 'Marg_Bruta', 'Marg_EBIT', 'Marg_Liquida', 'EBIT_Ativo', 'ROIC', 'ROE', 'Liquidez_Corr', 
                'Div_Br_Patrim', 'Giro_Ativos', 'Ativo', 'Disponibilidades', 'Ativo_Circulante', 'Div_Bruta', 'Div_Liquida',
                'Patrim_Liq', 'Receita_Liquida_12m', 'EBIT_12m', 'Lucro_Liquido_12m', 'Receita_Liquida_3m', 'EBIT_3m', 
                'Lucro_Liquido_3m', 'Cart_de_Credito', 'Depositos', 'Result_Int_Financ_12m', 'Rec_Servicos_12m',
                'Result_Int_Financ_3m', 'Rec_Servicos_3m']

    new_cols = [cols.lower() for cols in old_cols]
    df.columns = new_cols

    ## 1.3 Data Cleaning
    # Removing lines with '-' (NA)
    df = df.loc[ df['cres_rec_5a'] != '-' , :]
    df = df.loc[ df['marg_liquida'] != '-' , :]
    df = df.loc[ df['roe'] != '-' , :]

    # removing %
    df['div_yield'] = df['div_yield'].str.replace('%', '')
    df['cres_rec_5a'] = df['cres_rec_5a'].str.replace('%', '')
    df['marg_liquida'] = df['marg_liquida'].str.replace('%', '')
    df['roe'] = df['roe'].str.replace('%', '')

    # removing ' '
    df['empresa'] = df['empresa'].str.lower().str.replace(' ', '_')
    df['setor'] = df['setor'].str.lower().str.replace(' ', '_')

    ## 1.4 Data Types
    df['pl'] = df['pl'].astype('float')
    df['pvp'] = df['pvp'].astype('float')
    df['div_yield'] = df['div_yield'].astype('float')
    df['cres_rec_5a'] = df['cres_rec_5a'].astype('float')
    df['marg_liquida'] = df['marg_liquida'].astype('float')
    df['roe'] = df['roe'].astype('float')
    
    return df

# ------------------------------------------------------------------------------------------------------------

def data_filtering( df ):
    ## 3.2. Filtering Columns
    cols_selected = ['setor', 'pl', 'pvp', 'div_yield', 'cres_rec_5a', 'marg_liquida', 'roe']
    df = df.loc[ :, cols_selected]

    ## 3.2. Filtering Rows
    # filtro PL negativo
    df = df.loc[ df['pl'] > 0 , :]

    # filtro PVP negativo
    df = df.loc[ df['pvp'] > 0 , :]

    # filtro div_yield < 100
    df = df.loc[ df['div_yield'] < 100 , :]
    
    return df

# ------------------------------------------------------------------------------------------------------------

def separate_sectors( df ):

    agropecuaria = df[ df['setor'] == 'agropecuária'].drop('setor', axis=1)
    agua_e_saneamento = df[ df['setor'] == 'água_e_saneamento'].drop('setor', axis=1)
    alimentos_processados = df[ df['setor'] == 'alimentos_processados'].drop('setor', axis=1)
    serv_medicos_analises_e_diagnasticos = df[ df['setor'] == 'serv.méd.hospit._análises_e_diagnósticos'].drop('setor', axis=1)
    automoveis_e_motocicletas = df[ df['setor'] == 'automóveis_e_motocicletas'].drop('setor', axis=1)
    comercio = df[ df['setor'] == 'comércio'].drop('setor', axis=1)
    comercio_e_distribuicao = df[ df['setor'] == 'comércio_e_distribuição'].drop('setor', axis=1)
    computadores_e_equipamentos = df[ df['setor'] == 'computadores_e_equipamentos'].drop('setor', axis=1)
    construcao_civil = df[ df['setor'] == 'construção_civil'].drop('setor', axis=1)
    construcao_e_engenharia = df[ df['setor'] == 'construção_e_engenharia'].drop('setor', axis=1)
    diversos = df[ df['setor'] == 'diversos'].drop('setor', axis=1)
    energia_eletrica = df[ df['setor'] == 'energia_elétrica'].drop('setor', axis=1)
    equipamentos = df[ df['setor'] == 'equipamentos'].drop('setor', axis=1)
    exploracao_de_imoveis = df[ df['setor'] == 'exploração_de_imóveis'].drop('setor', axis=1)
    gas = df[ df['setor'] == 'gás'].drop('setor', axis=1)
    holdings_diversificadas = df[ df['setor'] == 'holdings_diversificadas'].drop('setor', axis=1)
    intermediarios_financeiros = df[ df['setor'] == 'intermediários_financeiros'].drop('setor', axis=1)
    madeira_e_papel = df[ df['setor'] == 'madeira_e_papel'].drop('setor', axis=1)
    maquinas_e_equipamentos = df[ df['setor'] == 'máquinas_e_equipamentos'].drop('setor', axis=1)
    material_de_transporte = df[ df['setor'] == 'material_de_transporte'].drop('setor', axis=1)
    mineracao = df[ df['setor'] == 'mineração'].drop('setor', axis=1)
    petroleo = df[ df['setor'] == 'petróleo'].drop('setor', axis=1)
    gas_e_biocombustiveis = df[ df['setor'] == '_gás_e_biocombustíveis'].drop('setor', axis=1)
    previdencia_e_seguros = df[ df['setor'] == 'previdência_e_seguros'].drop('setor', axis=1)
    programas_e_servicos = df[ df['setor'] == 'programas_e_serviços'].drop('setor', axis=1)
    quimicos = df[ df['setor'] == 'químicos'].drop('setor', axis=1)
    servicos_diversos = df[ df['setor'] == 'serviços_diversos'].drop('setor', axis=1)
    servicos_financeiros_diversos = df[ df['setor'] == 'serviços_financeiros_diversos'].drop('setor', axis=1)
    siderurgia_e_metalurgia = df[ df['setor'] == 'siderurgia_e_metalurgia'].drop('setor', axis=1)
    tecidos = df[ df['setor'] == 'tecidos'].drop('setor', axis=1)
    vestuario_e_calcados = df[ df['setor'] == '_vestuário_e_calçados'].drop('setor', axis=1)
    telecomunicacoes = df[ df['setor'] == 'telecomunicações'].drop('setor', axis=1)
    transporte = df[ df['setor'] == 'transporte'].drop('setor', axis=1)
    utilidades_domesticas = df[ df['setor'] == 'utilidades_domésticas'].drop('setor', axis=1)

    lista_setores = [
        agropecuaria, agua_e_saneamento, alimentos_processados, serv_medicos_analises_e_diagnasticos, automoveis_e_motocicletas,
        comercio, comercio_e_distribuicao, computadores_e_equipamentos, construcao_civil, construcao_e_engenharia, diversos, 
        energia_eletrica, equipamentos, exploracao_de_imoveis, gas, holdings_diversificadas, intermediarios_financeiros, 
        madeira_e_papel, maquinas_e_equipamentos, material_de_transporte, mineracao, petroleo, gas_e_biocombustiveis, 
        previdencia_e_seguros, programas_e_servicos, quimicos, servicos_diversos, servicos_financeiros_diversos, 
        siderurgia_e_metalurgia, tecidos, vestuario_e_calcados, telecomunicacoes, transporte, utilidades_domesticas ]
            
    return lista_setores

# ------------------------------------------------------------------------------------------------------------

def ahp_gaussiano( df, top_stocks ):

    # inverter valores monotômicos de custo
    df['pl'] = df['pl'].apply( lambda x: 1/x )
    df['pvp'] = df['pvp'].apply( lambda x: 1/x )

    # normalização
    setor_normalizado = df[['pl', 'pvp', 'div_yield', 'cres_rec_5a', 'marg_liquida', 'roe']].apply( lambda x: x/sum(x))

    # criação fator gaussiano
    fator_gaussiano = setor_normalizado.std() / setor_normalizado.mean()
    fator_normalizado = fator_gaussiano / fator_gaussiano.sum()

    # ponderação da matriz normalizada
    setor_normalizado['pl']           = setor_normalizado['pl'] * fator_normalizado['pl']
    setor_normalizado['pvp']          = setor_normalizado['pvp'] * fator_normalizado['pvp']
    setor_normalizado['div_yield']    = setor_normalizado['div_yield'] * fator_normalizado['div_yield']
    setor_normalizado['cres_rec_5a']  = setor_normalizado['cres_rec_5a'] * fator_normalizado['cres_rec_5a']
    setor_normalizado['marg_liquida'] = setor_normalizado['marg_liquida'] * fator_normalizado['marg_liquida']
    setor_normalizado['roe']          = setor_normalizado['roe'] * fator_normalizado['roe']

    # criação coluna ranking
    setor_normalizado['ranking_(%)'] = setor_normalizado.sum( axis=1 )*100
    setor_normalizado = setor_normalizado.sort_values('ranking_(%)', ascending= False).head( top_stocks )

    return setor_normalizado

# ------------------------------------------------------------------------------------------------------------

def final_table( lista_setores, top_stocks, table_type = 'original' ): 
      
    df_result = pd.DataFrame()
    
    for setor in lista_setores:
        df_aux = ahp_gaussiano( setor, top_stocks )
        df_result = pd.concat( [df_result, df_aux] )
    
    if table_type == 'normalizada':
        df_final = pd.merge( df_result, df_filtered['setor'], how='left', right_index= True, left_index=True).sort_values( 'setor' )
    
    else:
        df_final = pd.merge( df_result['ranking_(%)'], df_filtered, how='left', left_index=True, right_index= True ).sort_values( 'setor' )
        df_final = df_final[['pl', 'pvp', 'div_yield', 'cres_rec_5a', 'marg_liquida', 'roe', 'ranking_(%)', 'setor']]
    return df_final



# =======================================================
# FUNÇÕES STREAMLIT
# =======================================================

def botao( ):
    botao = st.sidebar.radio('Habilitar / Desabilitar Seleção', ('Habilitar Todos', 'Desabilitar Todos'))
    if botao == 'Habilitar Todos':
        botao = True
    elif botao == 'Desabilitar Todos':
        botao = False

    return botao


def create_checkbox( botao ):
    lista_teste = []
    
    op1 = st.sidebar.checkbox( 'agropecuaria', value= botao ) 
    if op1:
        lista_teste.append( 'agropecuária' )

    op2 = st.sidebar.checkbox( 'agua_e_saneamento' , value= botao)
    if op2:
        lista_teste.append( 'água_e_saneamento' )

    op3 = st.sidebar.checkbox( 'alimentos_processados' , value= botao)
    if op3:
        lista_teste.append( 'alimentos_processados' )

    op4 = st.sidebar.checkbox( 'serv.méd._e_diagnosticos' , value= botao)
    if op4:
        lista_teste.append( 'serv.méd.hospit._análises_e_diagnósticos' )
    
    op5 = st.sidebar.checkbox( 'automóveis_e_motocicletas' , value= botao)
    if op5:
        lista_teste.append( 'automóveis_e_motocicletas' )

    op6 = st.sidebar.checkbox( 'comercio' , value= botao)
    if op6:
        lista_teste.append( 'comércio' )
    
    op7 = st.sidebar.checkbox( 'comércio_e_distribuição' , value= botao)
    if op7:
        lista_teste.append( 'comércio_e_distribuição' )
    
    op8 = st.sidebar.checkbox( 'computadores_e_equip.' , value= botao)
    if op8:
        lista_teste.append( 'computadores_e_equipamentos' )

    op9 = st.sidebar.checkbox( 'construção_civil' , value= botao)
    if op9:
        lista_teste.append( 'construção_civil' )

    op10 = st.sidebar.checkbox( 'construção_e_engenharia' , value= botao)
    if op10:
        lista_teste.append( 'construção_e_engenharia' )

    op11 = st.sidebar.checkbox( 'diversos' , value= botao)
    if op11:
        lista_teste.append( 'diversos' )

    op12 = st.sidebar.checkbox( 'energia_elétrica' , value= botao)
    if op12:
        lista_teste.append( 'energia_elétrica' )

    op13 = st.sidebar.checkbox( 'equipamentos' , value= botao)
    if op13:
        lista_teste.append( 'equipamentos' )

    op14 = st.sidebar.checkbox( 'exploração_de_imóveis' , value= botao)
    if op14:
        lista_teste.append( 'exploração_de_imóveis' )

    op15 = st.sidebar.checkbox( 'gás' , value= botao)
    if op15:
        lista_teste.append( 'gás' )

    op16 = st.sidebar.checkbox( 'holdings_diversificadas' , value= botao)
    if op16:
        lista_teste.append( 'holdings_diversificadas' )

    op17 = st.sidebar.checkbox( 'intermediários_financeiros' , value= botao)
    if op17:
        lista_teste.append( 'intermediários_financeiros' )

    op18 = st.sidebar.checkbox( 'madeira_e_papel' , value= botao)
    if op18:
        lista_teste.append( 'madeira_e_papel' )

    op19 = st.sidebar.checkbox( 'máquinas_e_equipamentos' , value= botao)
    if op19:
        lista_teste.append( 'máquinas_e_equipamentos' )

    op20 = st.sidebar.checkbox( 'material_de_transporte' , value= botao)
    if op20:
        lista_teste.append( 'material_de_transporte' )

    op22 = st.sidebar.checkbox( 'mineração' , value= botao)
    if op22:
        lista_teste.append( 'mineração' )

    op23 = st.sidebar.checkbox( 'petróleo' , value= botao)
    if op23:
        lista_teste.append( 'petróleo' )

    op24 = st.sidebar.checkbox( 'gás_e_biocombustíveis' , value= botao)
    if op24:
        lista_teste.append( '_gás_e_biocombustíveis' )

    op25 = st.sidebar.checkbox( 'previdência_e_seguros' , value= botao)
    if op25:
        lista_teste.append( 'previdência_e_seguros' )

    op26 = st.sidebar.checkbox( 'programas_e_serviços' , value= botao)
    if op26:
        lista_teste.append( 'programas_e_serviços' )

    op27 = st.sidebar.checkbox( 'químicos' , value= botao)
    if op27:
        lista_teste.append( 'químicos' )

    op28 = st.sidebar.checkbox( 'serviços_diversos' , value= botao)
    if op28:
        lista_teste.append( 'serviços_diversos' )

    op29 = st.sidebar.checkbox( 'serviços_financeiros_diversos' , value= botao)
    if op29:
        lista_teste.append( 'serviços_financeiros_diversos' )

    op30 = st.sidebar.checkbox( 'siderurgia_e_metalurgia' , value= botao)
    if op30:
        lista_teste.append( 'siderurgia_e_metalurgia' )

    op31 = st.sidebar.checkbox( 'tecidos' , value= botao)
    if op31:
        lista_teste.append( 'tecidos' )

    op32 = st.sidebar.checkbox( 'vestuário_e_calçados' , value= botao)
    if op32:
        lista_teste.append( '_vestuário_e_calçados' )

    op33 = st.sidebar.checkbox( 'telecomunicações' , value= botao)
    if op33:
        lista_teste.append( 'telecomunicações' )

    op34 = st.sidebar.checkbox( 'transporte' , value= botao)
    if op34:
        lista_teste.append( 'transporte' )

    op35 = st.sidebar.checkbox( 'utilidades_domésticas' , value= botao)
    if op35:
        lista_teste.append( 'utilidades_domésticas' )


    return lista_teste


# =======================================================
# 1. SIDEBAR
# =======================================================

# Título
st.sidebar.markdown( '# Selecione os Filtros' )
st.sidebar.markdown( '## ' )

# Filtros
# filtro_top_stocks = st.sidebar.radio( 'Quantidade de ações por setor:', (1, 2, 3) )
filtro_top_stocks = st.sidebar.selectbox( 'Quantidade de ações por setor:', (1,2,3) )
st.sidebar.markdown( '''___''' )

botao = botao( )

# Filtro por setores
st.sidebar.markdown( '## Selecione os setores: ')

selecao_setores = create_checkbox( botao )


# =======================================================
# ESTRUTURA LÓGICA DO CÓDIGO
# =======================================================

# coleta de dados
data_raw = data_collect()

# limpeza dos dados
df_cleaned = data_cleaning( data_raw )

# filtragem dos dados
df_filtered = data_filtering( df_cleaned )

# separação dos setores
df_separated = separate_sectors( df_filtered )

# tabela final ranqueada
df_final = final_table( df_separated, filtro_top_stocks, 'original' )

# filtro de setores
df_final = df_final.loc[ df_final['setor'].isin( selecao_setores ), : ]

# =======================================================
# 1. VISÃO CENTRAL
# =======================================================

# Tabela
st.markdown( '## Sugestão de Carteira de Ações')
st.dataframe( df_final, use_container_width= True )

st.markdown( '''___''')

# Gráficos
st.markdown( '## Gráficos dos indicadores')

with st.container():
    col1, col2 = st.columns(2)

    with col1:
        # grafico menores PL
        st.markdown( '##### Top 10 menores P/L (Preço / Lucro)')
        aux = df_final.sort_values('pl').reset_index().rename( columns= {'index': 'empresa'}).head(10)
        fig = px.bar( aux, x= 'empresa', y= 'pl')
        st.plotly_chart( fig, use_container_width= True)

    with col2:
        # grafico menores PVP
        st.markdown( '##### Top 10 menores P/VP (Preço / Valor Patrimonial)')
        aux = df_final.sort_values('pvp').reset_index().rename( columns= {'index': 'empresa'}).head(10)
        fig = px.bar( aux, x= 'empresa', y= 'pvp')
        st.plotly_chart( fig, use_container_width= True)


with st.container():
    col1, col2 = st.columns(2)

    with col1:
        # grafico maiores Divendo
        st.markdown( '##### Top 10 maiores Dividendos')
        aux = df_final.sort_values('div_yield', ascending= False).reset_index().rename( columns= {'index': 'empresa'}).head(10)
        fig = px.bar( aux, x= 'empresa', y= 'div_yield')
        st.plotly_chart( fig, use_container_width= True)

    with col2:
        # grafico maiores Crescimento Receita
        st.markdown( '##### Top 10 maiores Crescimento de Receita')
        aux = df_final.sort_values('cres_rec_5a', ascending= False).reset_index().rename( columns= {'index': 'empresa'}).head(10)
        fig = px.bar( aux, x= 'empresa', y= 'cres_rec_5a')
        st.plotly_chart( fig, use_container_width= True)


with st.container():
    col1, col2 = st.columns(2)

    with col1:
        # grafico maiores Margem Líquida
        st.markdown( '##### Top 10 maiores Margem Líquida')
        aux = df_final.sort_values('marg_liquida', ascending= False).reset_index().rename( columns= {'index': 'empresa'}).head(10)
        fig = px.bar( aux, x= 'empresa', y= 'marg_liquida')
        st.plotly_chart( fig, use_container_width= True)

    with col2:
        # grafico maiores Roe
        st.markdown( '##### Top 10 maiores Roe ( Retorno sobre o Investimento)')
        aux = df_final.sort_values('roe', ascending= False).reset_index().rename( columns= {'index': 'empresa'}).head(10)
        fig = px.bar( aux, x= 'empresa', y= 'roe')
        st.plotly_chart( fig, use_container_width= True)


# adicionar botao para rodar e baixar dados