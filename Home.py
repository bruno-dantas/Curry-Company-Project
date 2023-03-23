import streamlit as st
from PIL import Image

st.set_page_config( 
    page_title="Home"
)

image_path = 'C:\\Users\\brunn\\Documents\\repos\\FTC_jupyterlab\\images'
image = Image.open( image_path + '\\logo.png' )
st.sidebar.image( image, use_column_width='auto')

st.sidebar.markdown( '# Curry Company' )
st.sidebar.markdown( '## Fastest Delivery in Town' )
st.sidebar.markdown( """---""" )

st.write( "# Curry Company Growth Dashboard" )
st.empty()       
st.write("\nGrowth Dashboard foi construído para acompanhar as métricas de crescimento dos Entregadores e Restaurantes.")
st.markdown('''---''')
st.markdown(
   

    """
    ### Como utilizar esse Growth Dashboard?
    - Visão Empresa:
        - Visão Gerencial: Métricas gerais de comportamento.
        - Visão Tática: Indicadores semanais de crescimento.
        - Visão Geográfica: Insights de geolocalização.
    - Visão Entregador:
        - Acompanhamento dos indicadores semanais de crescimento
    - Visão Restaurante:
        - Indicadores semanais de crescimento dos restaurantes
    ### Ask for Help
    - Time de Data Science no Discord
        - @brvno
""" )