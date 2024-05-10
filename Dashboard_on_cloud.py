
import pandas as pd
import numpy as np
import plotly.express as px
import streamlit as st

#reading our dataset
df = pd.read_csv("new_sales_store_data.csv")

st.title("Sales Store Analysis")

st.header("Metrics")

c1 ,c2 , c3=st.columns(3)
with c1:
    st.metric(label = "Total Sales in M$" , value = (df["Sales"].sum() / 1000000).round(3) )
with c2:
    st.metric(label = "Total Profit in M$" , value = (df["Profit"].sum() / 1000000).round(3) )
with c3:
    st.metric(label = "Avg Discount Percentage Per Year %" , value = 15.5 )



st.header("Best Sellers Chart")

sub_cat_index = df["Sub-Category"].value_counts().head().index

sub_cat_df = df[ df["Sub-Category"].isin(sub_cat_index) ]

px1 = px.histogram(sub_cat_df , x = "Sub-Category" ,text_auto = True).update_xaxes(categoryorder = 'total descending')

st.plotly_chart(px1)



st.header("Category's Profit Over Regions")

pivot_table = pd.pivot_table(df , index = "Category" , columns = "Region" , values = "Profit" , aggfunc = sum )

c4,c5 = st.columns([4,1])

#heat map or bar plot to draw pivot table
with c4:
    px2 = px.imshow(pivot_table)
    st.plotly_chart(px2)
    
    
with c5:
    px3 = px.bar(data_frame = df , x = "Category" , y = "Profit" ,color = "Region",barmode = "group")
    st.plotly_chart(px3)
