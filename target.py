import streamlit as st
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from PIL import Image



img = Image.open("etman_logo.ico")    
st.set_page_config(
    page_title="Etman Group",
    page_icon=img,
    layout="wide",
    )


st.header('Temporary Alowable Pricing of goods\nMade by Eng\\ ***Ashraf Aaref***')
st.write('-----------------------------------')
goods_cost = st.number_input('Cost of Goods (1 ton)')
# st.write(goods_cost)


import_slider = st.selectbox('Select Import Container',[40,20])
shipping_import = st.number_input('Shipping Cost for Import')

export_slider = st.selectbox('Select Export Container',[40,20])
shipping_export = st.number_input('Shipping Cost for Export')


btn = st.button('Calculate')

df = pd.read_excel(
    r'temporary _grace.xlsx',
    sheet_name='new',
    )

df.id = df.id.astype(int)
df = df.set_index('id')

if btn:

    eq = goods_cost + (1.03*shipping_import/df.loc[import_slider,'Quantity']) + shipping_export/(df.loc[export_slider,'Quantity']) + df.loc[export_slider,df.columns[1]] + df.loc[export_slider,df.columns[2]]
    st.write(f"$  {np.ceil(eq)}")  
        

