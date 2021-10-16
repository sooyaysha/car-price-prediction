import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
# Define a function 'app()' which accepts 'car_df' as an input.
def app(car_df):
  st.header('Visualize Data')
  st.set_option('deprecation.showPyplotGlobalUse', False)
  st.subheader('Scatter Plot')
  features_list = st.multiselect('Select the x-axis values', ('carwidth', 'enginesize', 'horsepower', 'drivewheel_fwd', 'car_company_buick'))
  for feature in features_list:
    st.subheader(f'Scatter Plot between {feature} and price')
    plt.figure(figsize = (12,6))
    sns.scatterplot(x = feature, y = 'price', data = cars_df)
    st.pyplot()
  st.subheader('Visualization Selector')
  plot_types = st.multiselect('Select charts or plots', ('Histogram', 'Boxplot', 'Correlation Heatmap'))
  if 'Histogram' in plot_types:
    st.subheader('Histogram')
    columns = st.selectbox('Select the column to create its histogram', ('carwidth', 'enginesize', 'horsepower')) 
    plt.figure(figsize = (12,6))
    plt.title(f'Histogram for {columns}')
    plt.hist(car_df[columns], bins = 'sturges', edgecolor = 'k')
    st.pyplot()
  if 'Boxplot' in plot_types:
    st.subheader('Box Plot')
    columns = st.selectbox('Select the column to create its box plot', ('carwidth', 'enginesize', 'horsepower')) 
    plt.figure(figsize = (12,2))
    plt.title(f'Box Plot for {columns}')
    sns.boxplot(car_df[columns])
    st.pyplot()
  if 'Correlation Heatmap' in plot_types:
    st.subheader('Correlation Heatmap')
    plt.figure(figsize = (8,5))
    ax = sns.heatmap(cars_df.corr(), annot = True)
    bottom, top = ax.get_ylim()
    ax.set_ylim(bottom + 0.5, top - 0.5)
    st.pyplot()
