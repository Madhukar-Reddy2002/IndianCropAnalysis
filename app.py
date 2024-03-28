import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
@st.cache
def load_data():
    df = pd.read_csv('India Agriculture Crop Production.csv')
    # Perform any necessary data cleaning and preprocessing
    df.dropna(inplace=True)
    return df

# Filter data based on user selections
def filter_data(df, state, crop):
    filtered_df = df[(df['State'] == state) & (df['Crop'] == crop)]
    return filtered_df

# Create visualizations with customization options
def create_visualizations(filtered_df):
    sns.set_style("whitegrid")

    # Customizable bar plot: Area under cultivation by district
    fig1, ax1 = plt.subplots(figsize=(10, 6))
    filtered_df.groupby('District')['Area'].sum().sort_values(ascending=False).plot(kind='bar', color='skyblue', ax=ax1)
    ax1.set_title('Area under Cultivation by District', fontsize=16)
    ax1.set_xlabel('District', fontsize=14)
    ax1.set_ylabel('Area (Hectares)', fontsize=14)

    # Customizable pie chart: Share of production by season
    fig2, ax2 = plt.subplots(figsize=(8, 8))
    filtered_df.groupby('Season')['Production'].sum().plot(kind='pie', autopct='%1.1f%%', startangle=140, ax=ax2)
    ax2.set_title('Share of Production by Season', fontsize=16)

    # Customizable line plot: Yield over the years
    fig3, ax3 = plt.subplots(figsize=(10, 6))
    filtered_df.groupby('Year')['Yield'].mean().plot(marker='o', ax=ax3)
    ax3.set_title('Average Yield over the Years', fontsize=16)
    ax3.set_xlabel('Year', fontsize=14)
    ax3.set_ylabel('Yield (Tonnes/Hectare)', fontsize=14)

    # Customizable scatter plot: Yield vs Production (with district coloring)
    fig4, ax4 = plt.subplots(figsize=(15, 8))
    top_districts = filtered_df.groupby('District')['Yield'].mean().sort_values(ascending=False).head(10).index
    filtered_df_top = filtered_df[filtered_df['District'].isin(top_districts)]
    sns.scatterplot(x='Production', y='Yield', hue='District', data=filtered_df_top, palette='viridis', ax=ax4)
    ax4.set_title('Yield vs Production (Top 10 Districts)', fontsize=16)
    ax4.set_xlabel('Production (Tonnes)', fontsize=14)
    ax4.set_ylabel('Yield (Tonnes/Hectare)', fontsize=14)

    return fig1, fig2, fig3, fig4

# Streamlit app
def main():
    st.title("Indian Agriculture Dashboard")
    st.subheader("Explore Agriculture Data")

    # Load the data
    data = load_data()

    # Create dropdown menus for user selections in the sidebar
    with st.sidebar:
        selected_state = st.selectbox("Select State", data['State'].unique())
        selected_crop = st.selectbox("Select Crop", data['Crop'].unique())

    # Filter the data based on user selections
    filtered_data = filter_data(data, selected_state, selected_crop)

    # Display summary
    st.write("**Summary:**")
    st.write("Selected State:", selected_state)
    st.write("Selected Crop:", selected_crop)
    st.write("Total Records:", len(filtered_data))

    # Create visualizations
    fig1, fig2, fig3, fig4 = create_visualizations(filtered_data)
    # Display the visualizations
    col1, col2 = st.columns(2)
    with col1:
        st.pyplot(fig1)
        st.pyplot(fig2)
    with col2:
        st.pyplot(fig3)
        st.pyplot(fig4)

if __name__ == "__main__":
    main()
