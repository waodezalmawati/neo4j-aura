import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from neo4j import GraphDatabase
st.set_page_config(layout="wide")

plt.style.use('seaborn')

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

#Konekdi Database
drivers = GraphDatabase.driver(uri = "neo4j+s://d4f6a837.databases.neo4j.io", auth = ("neo4j","efnDAFw4yr2ODSk2cqfUBCD0BlsnAtxscFdVOVSx6Xc"))
session = drivers.session(database='neo4j')

#Query tarik data I
q1 = """
match (n:Sublead_CG1) return n.Rain as Rain, n.Holiday as Holiday, n.Customer_Problem as Customer_Problem, n.Slippery as Slippery, n.Produksi as Produksi
"""
result1 = session.run(q1)
data1 = result1.data()
result_cg1 = pd.DataFrame(data1)

st.write(result_cg1)