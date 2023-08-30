import streamlit as st
import pandas as pd
import altair as alt

st.header("Problematische Einstellung von Männer")
st.subheader("Männer zwischen 18 und 35 Jahren")

source = pd.DataFrame({
        'Anteil(%)': [52, 52, 33],
        'Meinung': ['Der Mann ist verantwortlich fürs Geld verdienen', '... damit sich die Frau um den Haushalt und die Kindern kümmern kann', 'Im Streit ist es "akzeptabel" die Partnerin zu schlagen']
     })
 
bar_chart = alt.Chart(source).mark_bar().encode(
        y='Anteil(%):Q',
        x='Meinung:O',
    )
st.altair_chart(bar_chart, use_container_width=True)


txt = st.text_area('', '''
    Basis: 1000 Männer; März 2023
    ''')
st.text("Klicke an die Balken um die Daten genauer anzuschauen. Du kannst auch die Diagramm vergrößern und ein Bild davon machen")
st.text("Quelle:  Plan International")