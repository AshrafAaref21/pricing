import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image


img = Image.open("etman_logo.ico")    
st.set_page_config(
    page_title="Etman Group",
    page_icon=img,
    layout="wide",
    )

st.header('Etman Scotch Pricing\nMade by Eng\\ ***Ashraf Aaref***')
st.write('-----------------------------------')



sheet_bx = st.selectbox('Select',['Select The Pricing Type','Temporary','Final'],index=0)

if sheet_bx == 'Temporary':

    df = pd.read_excel(
        r'temporary _grace.xlsx',
        sheet_name='new',
        )

    df.ID = df.ID.astype(int)
    df = df.set_index('ID')


    goods_cost = st.number_input('Cost of Goods (1 ton)')


    import_slider = st.selectbox('Select Import Container',[40,20])
    shipping_import = st.number_input('Shipping Cost for Import')

    export_slider = st.selectbox('Select Export Container',[40,20])
    shipping_export = st.number_input('Shipping Cost for Export')


    btn = st.button('Calculate')


    if btn:
        eq = goods_cost + (1.03*shipping_import/df.loc[import_slider,'Quantity']) + shipping_export/(df.loc[export_slider,'Quantity']) + df.loc[export_slider,df.columns[1]] + df.loc[export_slider,df.columns[2]]
        st.write(f"$  {int(np.ceil(eq))}")  

            # file = 'my_csv.csv'

            # def appendDFToCSV_void(df, csvFilePath, sep=",",encoding='utf-8'):
            #     try:
            #         if not os.path.isfile(csvFilePath):
            #             df.to_csv(csvFilePath, mode='a', index=False, sep=sep)
            #         elif len(df.columns) != len(pd.read_csv(csvFilePath, nrows=1, sep=sep).columns):
            #             raise Exception("Columns do not match!! Dataframe has " + str(len(df.columns)) + " columns. CSV file has " + str(len(pd.read_csv(csvFilePath, nrows=1, sep=sep).columns)) + " columns.")
            #         elif not (df.columns == pd.read_csv(csvFilePath, nrows=1, sep=sep).columns).all():
            #             raise Exception("Columns and column order of dataframe and csv file do not match!!")
            #         else:
            #             df.to_csv(csvFilePath, mode='a', index=False, sep=sep, header=False)
            #     except PermissionError:
            #         pass

            # appendDFToCSV_void(df,file)

            
if sheet_bx == 'Final':

    df = pd.read_excel(
    r'temporary _grace.xlsx',
    sheet_name='new',
    )

    # st.dataframe(df)

    df.ID = df.ID.astype(int)
    df = df.set_index('ID')


    goods_cost = st.number_input('Cost of Goods (1 ton)')


    import_slider = st.selectbox('Select Import Container',['1 x 40 ft','2 x 20 ft'])
    if import_slider == '1 x 40 ft':
        con_ft = 40
        n = 1
    elif import_slider == '2 x 20 ft':
        con_ft = 20
        n = 2
    shipping_import = st.number_input('Shipping Cost')

    dollar_price = st.number_input('Dollar Price In Egypt',value=41)

    btn = st.button('Calculate')

    if btn:
        eq = dollar_price * goods_cost + dollar_price*(shipping_import/(n * df.loc[con_ft,'Quantity'])) + df.loc[con_ft,'total_final']
        st.write(f"{int(np.ceil(1.03*eq))} LE")
