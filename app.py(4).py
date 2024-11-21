# visualization
import streamlit as st
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
df = px.df.tips()

fig = px.scatter(df, x='total_bill', y='tip', color='sex', title='Relation ship btn total bill vs tip')
st.plotly_chart(fig) 

fig_2 = plt.figure()
sns.violinplot(x=df['sex'], y=df['total_bill'])
plt.title("Distrbution of total bill across Genders")
plt.xlabel("Gender")
plt.ylabel("total bill")
plt.grid()
st.pyplot(fig_2) 
