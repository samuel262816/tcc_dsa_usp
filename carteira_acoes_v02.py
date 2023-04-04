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
    df = fundamentus.get_resultado_raw()
    return df

# ------------------------------------------------------------------------------------------------------------

def data_cleaning( df ):
    # rename
    old_cols = ['Cotação', 'P/L', 'P/VP', 'PSR', 'Div.Yield', 'P/Ativo', 'P/Cap.Giro',
       'P/EBIT', 'P/Ativ Circ.Liq', 'EV/EBIT', 'EV/EBITDA', 'Mrg Ebit',
       'Marg_Liquida', 'Liq. Corr.', 'ROIC', 'ROE', 'Liq.2meses', 'Patrim. Líq',
       'Dív.Brut/ Patrim.', 'Cresc. Rec.5a']

    new_cols = [cols.lower() for cols in old_cols]
    df.columns = new_cols

    return df.reset_index()

# ------------------------------------------------------------------------------------------------------------

setores = {
    'agropecuaria': ['AGXY3', 'FRTA3', 'AGRO3', 'SLCE3', 'TTEN3', 'SOJA3'],
    'agua_e_saneamento': ['ORVR3', 'SAPR3', 'SAPR11', 'SAPR4', 'CSMG3', 'SBSP3', 'AMBP3'],
    'alimentos_processados': ['BRFS3','MRFG3','MNPR3','JBSS3','JALL3','CAML3','SMTO3','JOPA3','BEEF3','JOPA4','MDIA3','BAUH4'],
    'serv_medicos_analises_e_diagnasticos': ['ONCO3','HAPV3','DASA3','AALR3','KRSA3','QUAL3','ODPV3','PARD3','FLRY3','MATD3','RDOR3'],
    'automoveis_e_motocicletas': ['PLAS3', 'MYPK3', 'LEVE3'],
    'comercio': ['MGLU3', 'ESPA3', 'VIIA3', 'CEAB3', 'AMAR3', 'LLIS3', 'SLED4', 'SLED3', 'EPAR3', 'CGRA4', 'CGRA3', 'WLMM3', 'ALLD3', 'WLMM4', 'SBFG3', 
     'BTTL3', 'GUAR3', 'LREN3', 'ARZZ3', 'SOMA3', 'PETZ3', 'AMER3', 'LJQQ3'],
    'comercio_e_distribuicao': ['PCAR3', 'PFRM3', 'DMVF3', 'GMAT3', 'CRFB3', 'BLAU3', 'HYPE3', 'VVEO3', 'PGMN3', 'PNVL3', 'ASAI3', 'RADL3'],
    'computadores_e_equipamentos': ['POSI3', 'MLAS3', 'INTB3'],
    'construcao_civil': ['GFSA3', 'CRDE3', 'VIVR3', 'TCSA3', 'TEND3', 'JFEN3', 'AVLL3', 'RSID3', 'PDGR3', 'MDNE3', 'JHSF3', 'HBOR3', 'MELK3', 'CYRE3', 'CALI3', 
      'PLPL3', 'EVEN3', 'EZTC3', 'MRVE3', 'LAVV3', 'CURY3', 'MTRE3', 'TRIS3', 'DIRR3', 'RDNI3'],
    'construcao_e_engenharia': ['TCNO3', 'TCNO4', 'ETER3', 'HAGA4', 'SOND5', 'SOND6', 'PTBL3', 'HAGA3', 'AZEV4', 'AZEV3'],
    'diversos': ['YDUQ3', 'COGN3', 'SEER3', 'ANIM3', 'BAHI3', 'DOTZ3', 'MOVI3', 'MILS3', 'VAMO3', 'RENT3', 'CSED3', 'ARML3'],
    'embalagens': ['MTIG4'],
    'energia_eletrica': ['AESB3', 'CBEE3', 'LIGT3', 'RNEW4', 'RNEW3', 'RNEW11', 'CEBR3', 'CLSC3', 'CEBR5', 'CEBR6', 'CLSC4', 'NEOE3', 'GPAR3', 'AFLT3', 'ENBR3', 
      'TRPL4', 'CEEB5', 'CEEB3', 'ENGI4', 'COCE5', 'CMIG4', 'TAEE11', 'TAEE4', 'TAEE3', 'EKTR3', 'CSRN5', 'CSRN6', 'EKTR4', 'CSRN3', 'EQMA3B', 
      'TRPL3', 'CPFE3', 'ENGI11', 'REDE3', 'ALUP4', 'ALUP3', 'ALUP11', 'CMIG3', 'EQPA3', 'CEED4', 'CEED3', 'ENGI3', 'MEGA3', 'EQTL3', 'EQPA5', 
      'EQPA7', 'ENMT4', 'ENMT3', 'GEPA3', 'GEPA4', 'EGIE3', 'ENEV3', 'EMAE4', 'ELET3', 'CPLE3', 'ELET6', 'CPLE11', 'CPLE6', 'LIPR3', 'CEPE5', 
      'CEPE6', 'AURE3', 'CPLE5'],
    'equipamentos': ['BALM4', 'BALM3'],
    'exploracao_de_imoveis': ['SCAR3', 'BRPR3', 'IGBR3', 'NEXP3', 'GSHP3', 'SYNE3', 'HBRE3', 'LOGG3', 'BRML3', 'ALSO3', 'MULT3', 'JPSA3', 'LPSB3', 'HBTS5', 'IGTI3', 'IGTI11'],
    'gás': ['CGAS3', 'CGAS5'],
    'holdings_diversificadas': ['PEAB4', 'PEAB3', 'SIMH3', 'MOAR3'],
    'hoteis_e_restaurantes': ['ZAMP3', 'MEAL3', 'HOOT4'],
    'intermediarios_financeiros': ['BAZA3', 'BNBR3', 'DMFN3', 'BBAS3', 'ITSA4', 'ABCB4', 'BRSR6', 'BEES3', 'ITSA3', 'BMEB4', 'BMGB4', 'BEES4', 'BMEB3', 'BBDC3', 'BRSR3', 'SANB3', 
      'BRIV4', 'ITUB3', 'BBDC4', 'BRIV3', 'SANB11', 'SANB4', 'ITUB4', 'BPAC5', 'BSLI4', 'BRSR5', 'BRBI11', 'RPAD6', 'BGIP4', 'RPAD5', 'BMIN4', 'CRIV4',
      'CRIV3', 'RPAD3', 'BSLI3', 'BPAN4', 'BPAC11', 'BGIP3', 'BMIN3', 'PINE4', 'BPAC3', 'MERC4', 'MODL3', 'MERC3'],
    'madeira_e_papel': ['EUCA4', 'EUCA3', 'SUZB3', 'KLBN3', 'KLBN11', 'KLBN4', 'DXCO3', 'RANI3'],
    'maquinas_e_equipamentos': ['AERI3', 'NORD3', 'FRIO3', 'INEP4', 'INEP3', 'BDLL4', 'TASA4', 'TASA3', 'BDLL3', 'EALT4', 'MTSA4', 'EALT3', 'KEPL3', 'ROMI3', 'SHUL4', 'WEGE3'],
    'materiais_diversos': ['SNSY5'],
    'material_de_transporte': ['RCSL3', 'EMBR3', 'RCSL4', 'MWET4', 'MWET3', 'RAPT3', 'RAPT4', 'RSUL4', 'POMO3', 'TUPY3', 'POMO4', 'FRAS3'],
    'midia': ['ELMD3'],
    'mineracao': ['BRAP3', 'BRAP4', 'VALE3', 'AURA33', 'CBAV3', 'CMIN3'],
    'petroleo': ['DMMO3', 'LUPA3', 'RPMG3', 'OSXB3', 'OPCT3', 'PETR4', 'PETR3', 'ENAT3', 'VBBR3', 'PRIO3', 'UGPA3', 'RECV3', 'CSAN3', 'RAIZ4', 'RRRP3'],
    'previdencia_e_seguros': ['CSAB4', 'CSAB3', 'IRBR3', 'WIZS3', 'BRGE11', 'BRGE8', 'BRGE3', 'CXSE3', 'BRGE12', 'BRGE5', 'BRGE6', 'BBSE3', 'PSSA3', 'APER3', 'SULA3', 'SULA4', 'SULA11'],
    'uso_pessoal_e_limpeza': ['NTCO3', 'BOBR4'],
    'programas_e_servicos': ['TRAD3', 'CASH3', 'NINJ3', 'IFCM3', 'MBLY3', 'WEST3', 'ENJU3', 'LVTC3', 'BMOB3', 'TOTS3', 'SQIA3', 'NGRD3', 'LWSA3'],
    'servicos_diversos': ['DTCY3', 'SEQL3', 'ALPK3', 'ATMP3', 'PRNR3', 'CSUD3', 'GGPS3', 'VLID3'],
    'servicos_financeiros_diversos': ['CLSA3', 'GPIV33', 'GETT4', 'GETT3', 'BOAS3', 'CIEL3', 'B3SA3', 'PDTC3'],
    'siderurgia_e_metalurgia': ['PMAM3', 'MGEL4', 'USIM3', 'USIM5', 'GOAU3', 'GOAU4', 'GGBR3', 'USIM6', 'TKNO4', 'GGBR4', 'FESA4', 'FESA3', 'CSNA3', 'PATI3', 'PATI4'],
    'tecidos': ['CTKA3', 'CTKA4', 'CEDO3', 'CTSA3', 'CEDO4', 'CTSA4', 'CTNM3', 'TXRX4', 'CTNM4', 'SGPS3', 'MNDL3', 'TEKA4', 'PTNT4', 'TECN3', 'CAMB3', 'PTNT3', 'VULC3',
         'GRND3', 'VIVA3', 'DOHL4', 'TFCO4', 'ALPA3', 'ALPA4', 'DOHL3'],
    'telecomunicacoes': ['TELB3', 'TELB4', 'OIBR4', 'OIBR3', 'FIQE3', 'VIVT3', 'TIMS3', 'DESK3', 'BRIT3'],
    'transporte': ['RAIL3', 'TPIS3', 'HBSA3', 'AZUL4', 'GOLL4', 'CCRO3', 'TGMA3', 'JSLG3', 'MRSA6B', 'MRSA6B', 'MRSA3B', 'MRSA3B', 'STBP3', 'MRSA5B', 'MRSA5B', 'PORT3', 'ECOR3', 'LOGN3', 'LUXM4'],
    'utilidades_domesticas': ['HETA4', 'UCAS3', 'WHRL3', 'WHRL4']
    }

def sectors_definition( df ):

    # Função lambda para mapear o nome do setor de acordo com o código
    mapeamento = (lambda x: next((setor for setor, codigos in setores.items()
                                  if x in codigos), 'setor_desconhecido'))

    # Criando a nova coluna com o nome do setor
    df['setor'] = df['papel'].apply(mapeamento)

    return df

# ------------------------------------------------------------------------------------------------------------

def data_filtering( df ):
    ## 3.2. Filtering Columns
    cols_selected = ['papel', 'setor', 'p/l', 'p/vp', 'div.yield', 
                    'cresc. rec.5a', 'marg_liquida', 'roe']
    
    df = df.loc[ :, cols_selected]

    # filtro setor desconhecido
    df = df.loc[ df['setor'] != 'setor_desconhecido']
    
    ## 3.2. Filtering Rows
    # filtro PL negativo
    df = df.loc[ df['p/l'] > 0 , :]

    # filtro PVP negativo
    df = df.loc[ df['p/vp'] > 0 , :]

    # filtro div_yield < 100
    df = df.loc[ df['div.yield'] < 100 , :]
    
    return df.set_index('papel')

# ------------------------------------------------------------------------------------------------------------

def separate_sectors( df4 ):

    setor_agropecuaria = df4[ df4['setor'] == 'agropecuaria'].drop('setor', axis=1)
    setor_agua_e_saneamento = df4[ df4['setor'] == 'agua_e_saneamento'].drop('setor', axis=1)
    setor_alimentos_processados = df4[ df4['setor'] == 'alimentos_processados'].drop('setor', axis=1)
    setor_serv_medicos_e_diagnasticos = df4[ df4['setor'] == 'serv_medicos_analises_e_diagnasticos'].drop('setor', axis=1)
    setor_automoveis_e_motocicletas = df4[ df4['setor'] == 'automoveis_e_motocicletas'].drop('setor', axis=1)
    setor_comercio = df4[ df4['setor'] == 'comercio'].drop('setor', axis=1)
    setor_comercio_e_distribuicao = df4[ df4['setor'] == 'comercio_e_distribuicao'].drop('setor', axis=1)
    setor_computadores_e_equipamentos = df4[ df4['setor'] == 'computadores_e_equipamentos'].drop('setor', axis=1)
    setor_construcao_civil = df4[ df4['setor'] == 'construcao_civil'].drop('setor', axis=1)
    setor_construcao_e_engenharia = df4[ df4['setor'] == 'construcao_e_engenharia'].drop('setor', axis=1)
    setor_diversos = df4[ df4['setor'] == 'diversos'].drop('setor', axis=1)
    setor_energia_eletrica = df4[ df4['setor'] == 'energia_eletrica'].drop('setor', axis=1)
    setor_embalagens = df4[ df4['setor'] == 'setor_embalagens'].drop('setor', axis=1)
    setor_equipamentos = df4[ df4['setor'] == 'equipamentos'].drop('setor', axis=1)
    setor_exploracao_de_imoveis = df4[ df4['setor'] == 'exploracao_de_imoveis'].drop('setor', axis=1)
    setor_gas = df4[ df4['setor'] == 'gas'].drop('setor', axis=1)
    setor_holdings_diversificadas = df4[ df4['setor'] == 'holdings_diversificadas'].drop('setor', axis=1)
    setor_hoteis_e_restaurantes= df4[ df4['setor'] == 'setor_hoteis_e_restaurantes'].drop('setor', axis=1)
    setor_intermediarios_financeiros = df4[ df4['setor'] == 'intermediarios_financeiros'].drop('setor', axis=1)
    setor_madeira_e_papel = df4[ df4['setor'] == 'madeira_e_papel'].drop('setor', axis=1)
    setor_maquinas_e_equipamentos = df4[ df4['setor'] == 'maquinas_e_equipamentos'].drop('setor', axis=1)
    setor_material_de_transporte = df4[ df4['setor'] == 'material_de_transporte'].drop('setor', axis=1)
    setor_materiais_diversos = df4[ df4['setor'] == 'setor_materiais_diversos'].drop('setor', axis=1)
    setor_midia = df4[ df4['setor'] == 'setor_midia'].drop('setor', axis=1)
    setor_mineracao = df4[ df4['setor'] == 'mineracao'].drop('setor', axis=1)
    setor_petroleo = df4[ df4['setor'] == 'petroleo'].drop('setor', axis=1)
    setor_gas_e_biocombustiveis = df4[ df4['setor'] == 'gas_e_biocombustiveis'].drop('setor', axis=1)
    setor_previdencia_e_seguros = df4[ df4['setor'] == 'previdencia_e_seguros'].drop('setor', axis=1)
    setor_programas_e_servicos = df4[ df4['setor'] == 'programas_e_servicos'].drop('setor', axis=1)
    setor_quimicos = df4[ df4['setor'] == 'quimicos'].drop('setor', axis=1)
    setor_servicos_diversos = df4[ df4['setor'] == 'servicos_diversos'].drop('setor', axis=1)
    setor_servicos_financeiros_diversos = df4[ df4['setor'] == 'servicos_financeiros_diversos'].drop('setor', axis=1)
    setor_siderurgia_e_metalurgia = df4[ df4['setor'] == 'siderurgia_e_metalurgia'].drop('setor', axis=1)
    setor_tecidos = df4[ df4['setor'] == 'tecidos'].drop('setor', axis=1)
    setor_uso_pessoal_e_limpeza = df4[ df4['setor'] == 'setor_uso_pessoal_e_limpeza'].drop('setor', axis=1)
    setor_vestuario_e_calcados = df4[ df4['setor'] == '_vestuario_e_calcados'].drop('setor', axis=1)
    setor_telecomunicacoes = df4[ df4['setor'] == 'telecomunicacoes'].drop('setor', axis=1)
    setor_transporte = df4[ df4['setor'] == 'transporte'].drop('setor', axis=1)
    setor_utilidades_domesticas = df4[ df4['setor'] == 'utilidades_domesticas'].drop('setor', axis=1)
    
    lista_setores = [
        setor_agropecuaria, setor_agua_e_saneamento, setor_alimentos_processados, setor_serv_medicos_e_diagnasticos,
        setor_automoveis_e_motocicletas, setor_comercio, setor_comercio_e_distribuicao, setor_computadores_e_equipamentos, 
        setor_construcao_civil, setor_construcao_e_engenharia, setor_diversos, setor_energia_eletrica, setor_embalagens, 
        setor_equipamentos, setor_exploracao_de_imoveis, setor_gas, setor_holdings_diversificadas, setor_hoteis_e_restaurantes, 
        setor_intermediarios_financeiros, setor_madeira_e_papel, setor_maquinas_e_equipamentos, setor_material_de_transporte, 
        setor_materiais_diversos, setor_midia, setor_mineracao, setor_petroleo, setor_gas_e_biocombustiveis, 
        setor_previdencia_e_seguros, setor_programas_e_servicos, setor_quimicos, setor_servicos_diversos,
        setor_servicos_financeiros_diversos, setor_siderurgia_e_metalurgia, setor_tecidos, setor_uso_pessoal_e_limpeza, 
        setor_vestuario_e_calcados, setor_telecomunicacoes, setor_transporte, setor_utilidades_domesticas ]
    
    return lista_setores

# ------------------------------------------------------------------------------------------------------------

def ahp_gaussiano( df, top_stocks ):

    # inverter valores monotômicos de custo
    df['p/l'] = df['p/l'].apply( lambda x: 1/x )
    df['p/vp'] = df['p/vp'].apply( lambda x: 1/x )

    # normalização
    setor_normalizado = ( df[['p/l', 'p/vp', 'div.yield', 'cresc. rec.5a', 'marg_liquida', 'roe']]
                        .apply( lambda x: x/sum(x)) )

    # criação fator gaussiano
    fator_gaussiano = setor_normalizado.std() / setor_normalizado.mean()
    fator_normalizado = fator_gaussiano / fator_gaussiano.sum()

    # ponderação da matriz normalizada
    setor_normalizado['p/l']           = setor_normalizado['p/l'] * fator_normalizado['p/l']
    setor_normalizado['p/vp']          = setor_normalizado['p/vp'] * fator_normalizado['p/vp']
    setor_normalizado['div.yield']    = setor_normalizado['div.yield'] * fator_normalizado['div.yield']
    setor_normalizado['cresc. rec.5a'] = setor_normalizado['cresc. rec.5a'] * fator_normalizado['cresc. rec.5a']
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
        df_final = pd.merge( df_result, df_filtered['setor'], how='left', 
        right_index= True, left_index=True).sort_values( 'setor' )
    
    else:
        df_final = ( pd.merge( df_result['ranking_(%)'], df_filtered, how='left', 
                                left_index=True, right_index= True ).sort_values( 'setor' ))
        
        df_final = df_final[['p/l', 'p/vp', 'div.yield', 'cresc. rec.5a', 'marg_liquida', 'roe', 'ranking_(%)', 'setor']]
        
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
    
    op1 = st.sidebar.checkbox( 'agropecuária', value= botao ) 
    if op1:
        lista_teste.append( 'agropecuaria' )

    op2 = st.sidebar.checkbox( 'água_e_saneamento' , value= botao)
    if op2:
        lista_teste.append( 'agua_e_saneamento' )

    op3 = st.sidebar.checkbox( 'alimentos_processados' , value= botao)
    if op3:
        lista_teste.append( 'alimentos_processados' )

    op4 = st.sidebar.checkbox( 'serv.méd._e_diagnosticos' , value= botao)
    if op4:
        lista_teste.append( 'serv.med.hospit._analises_e_diagnosticos' )
    
    op5 = st.sidebar.checkbox( 'automóveis_e_motocicletas' , value= botao)
    if op5:
        lista_teste.append( 'automoveis_e_motocicletas' )

    op6 = st.sidebar.checkbox( 'comércio' , value= botao)
    if op6:
        lista_teste.append( 'comercio' )
    
    op7 = st.sidebar.checkbox( 'comércio_e_distribuição' , value= botao)
    if op7:
        lista_teste.append( 'comercio_e_distribuicao' )
    
    op8 = st.sidebar.checkbox( 'computadores_e_equip.' , value= botao)
    if op8:
        lista_teste.append( 'computadores_e_equipamentos' )

    op9 = st.sidebar.checkbox( 'construção_civil' , value= botao)
    if op9:
        lista_teste.append( 'construção_civil' )

    op10 = st.sidebar.checkbox( 'construção_e_engenharia' , value= botao)
    if op10:
        lista_teste.append( 'construcao_e_engenharia' )

    op11 = st.sidebar.checkbox( 'diversos' , value= botao)
    if op11:
        lista_teste.append( 'diversos' )

    op12 = st.sidebar.checkbox( 'energia_elétrica' , value= botao)
    if op12:
        lista_teste.append( 'energia_eletrica' )

    op13 = st.sidebar.checkbox( 'equipamentos' , value= botao)
    if op13:
        lista_teste.append( 'equipamentos' )

    op14 = st.sidebar.checkbox( 'exploração_de_imóveis' , value= botao)
    if op14:
        lista_teste.append( 'exploracao_de_imoveis' )

    op15 = st.sidebar.checkbox( 'gás' , value= botao)
    if op15:
        lista_teste.append( 'gas' )

    op16 = st.sidebar.checkbox( 'holdings_diversificadas' , value= botao)
    if op16:
        lista_teste.append( 'holdings_diversificadas' )

    op17 = st.sidebar.checkbox( 'intermediários_financeiros' , value= botao)
    if op17:
        lista_teste.append( 'intermediarios_financeiros' )

    op18 = st.sidebar.checkbox( 'madeira_e_papel' , value= botao)
    if op18:
        lista_teste.append( 'madeira_e_papel' )

    op19 = st.sidebar.checkbox( 'máquinas_e_equipamentos' , value= botao)
    if op19:
        lista_teste.append( 'maquinas_e_equipamentos' )

    op20 = st.sidebar.checkbox( 'material_de_transporte' , value= botao)
    if op20:
        lista_teste.append( 'material_de_transporte' )

    op22 = st.sidebar.checkbox( 'mineração' , value= botao)
    if op22:
        lista_teste.append( 'mineracao' )

    op23 = st.sidebar.checkbox( 'petróleo' , value= botao)
    if op23:
        lista_teste.append( 'petroleo' )

    op24 = st.sidebar.checkbox( 'gás_e_biocombustíveis' , value= botao)
    if op24:
        lista_teste.append( 'gas_e_biocombustiveis' )

    op25 = st.sidebar.checkbox( 'previdência_e_seguros' , value= botao)
    if op25:
        lista_teste.append( 'previdencia_e_seguros' )

    op26 = st.sidebar.checkbox( 'programas_e_serviços' , value= botao)
    if op26:
        lista_teste.append( 'programas_e_servicos' )

    op27 = st.sidebar.checkbox( 'químicos' , value= botao)
    if op27:
        lista_teste.append( 'quimicos' )

    op28 = st.sidebar.checkbox( 'serviços_diversos' , value= botao)
    if op28:
        lista_teste.append( 'servicos_diversos' )

    op29 = st.sidebar.checkbox( 'serviços_financeiros_diversos' , value= botao)
    if op29:
        lista_teste.append( 'servicos_financeiros_diversos' )

    op30 = st.sidebar.checkbox( 'siderurgia_e_metalurgia' , value= botao)
    if op30:
        lista_teste.append( 'siderurgia_e_metalurgia' )

    op31 = st.sidebar.checkbox( 'tecidos' , value= botao)
    if op31:
        lista_teste.append( 'tecidos' )

    op32 = st.sidebar.checkbox( 'vestuário_e_calçados' , value= botao)
    if op32:
        lista_teste.append( '_vestuario_e_calcados' )

    op33 = st.sidebar.checkbox( 'telecomunicações' , value= botao)
    if op33:
        lista_teste.append( 'telecomunicacoes' )

    op34 = st.sidebar.checkbox( 'transporte' , value= botao)
    if op34:
        lista_teste.append( 'transporte' )

    op35 = st.sidebar.checkbox( 'utilidades_domésticas' , value= botao)
    if op35:
        lista_teste.append( 'utilidades_domesticas' )

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

# definição dos setores
df_sectors = sectors_definition( df_cleaned )

# filtragem dos dados
df_filtered = data_filtering( df_sectors )

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
        aux = df_final.sort_values('p/l').reset_index().rename( columns= {'index': 'papel'}).head(10)
        fig = px.bar( aux, x= 'papel', y= 'p/l')
        st.plotly_chart( fig, use_container_width= True)

    with col2:
        # grafico menores PVP
        st.markdown( '##### Top 10 menores P/VP (Preço / Valor Patrimonial)')
        aux = df_final.sort_values('p/vp').reset_index().rename( columns= {'index': 'papel'}).head(10)
        fig = px.bar( aux, x= 'papel', y= 'p/vp')
        st.plotly_chart( fig, use_container_width= True)


with st.container():
    col1, col2 = st.columns(2)

    with col1:
        # grafico maiores Divendo
        st.markdown( '##### Top 10 maiores Dividendos')
        aux = df_final.sort_values('div.yield', ascending= False).reset_index().rename( columns= {'index': 'papel'}).head(10)
        fig = px.bar( aux, x= 'papel', y= 'div.yield')
        st.plotly_chart( fig, use_container_width= True)

    with col2:
        # grafico maiores Crescimento Receita
        st.markdown( '##### Top 10 maiores Crescimento de Receita')
        aux = df_final.sort_values('cresc. rec.5a', ascending= False).reset_index().rename( columns= {'index': 'papel'}).head(10)
        fig = px.bar( aux, x= 'papel', y= 'cresc. rec.5a')
        st.plotly_chart( fig, use_container_width= True)


with st.container():
    col1, col2 = st.columns(2)

    with col1:
        # grafico maiores Margem Líquida
        st.markdown( '##### Top 10 maiores Margem Líquida')
        aux = df_final.sort_values('marg_liquida', ascending= False).reset_index().rename( columns= {'index': 'papel'}).head(10)
        fig = px.bar( aux, x= 'papel', y= 'marg_liquida')
        st.plotly_chart( fig, use_container_width= True)

    with col2:
        # grafico maiores Roe
        st.markdown( '##### Top 10 maiores Roe ( Retorno sobre o Investimento)')
        aux = df_final.sort_values('roe', ascending= False).reset_index().rename( columns= {'index': 'empresa'}).head(10)
        fig = px.bar( aux, x= 'papel', y= 'roe')
        st.plotly_chart( fig, use_container_width= True)


# adicionar botao para rodar e baixar dados