import streamlit as st

print("oi")


bugs = st.Page("report/1_apage1.py", title="Calculadora Atuarial de Aposentadoria")
page1 = st.Page("tool/1_page1.py", title="Ativos Financeiros")
page2 = st.Page("tool/2_page2.py", title="Page 2")
page3 = st.Page("tool/3_page3_test.py", title="wallet test")


pg = st.navigation({            
                    "Atuarial": [bugs],
                    "Wallet": [page1, page2, page3]
        })

pg.run()