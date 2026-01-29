"""Hello World Databricks App using Streamlit for Azure Databricks."""

import streamlit as st
import pandas as pd
from databricks import sql
from databricks.sdk import WorkspaceClient
import os

# Page configuration
st.set_page_config(
    page_title="Hello World - Databricks App",
    page_icon="👋",
    layout="wide",
)


def get_greetings_data() -> pd.DataFrame:
    """Get hello world greetings in various languages."""
    return pd.DataFrame(
        {
            "language": [
                "English",
                "Spanish",
                "French",
                "German",
                "Japanese",
                "Italian",
                "Portuguese",
                "Russian",
                "Chinese",
                "Korean",
            ],
            "greeting": [
                "Hello, World!",
                "¡Hola, Mundo!",
                "Bonjour, le Monde!",
                "Hallo, Welt!",
                "こんにちは、世界！",
                "Ciao, Mondo!",
                "Olá, Mundo!",
                "Привет, мир!",
                "你好，世界！",
                "안녕하세요, 세계!",
            ],
        }
    )


def main():
    """Main application entry point."""
    # Header
    st.title("👋 Hello World - Databricks App")
    st.markdown("A simple demonstration of a Streamlit app running on Azure Databricks.")

    # Sidebar
    with st.sidebar:
        st.header("About")
        st.info(
            "This is a Hello World application built with Streamlit "
            "and deployed on Azure Databricks Apps."
        )
        st.markdown("---")
        st.markdown("**Framework:** Streamlit")
        st.markdown("**Platform:** Azure Databricks")

    # Main content
    col1, col2 = st.columns(2)

    with col1:
        st.header("🌍 Greetings from Around the World")

        # Get greetings data
        df = get_greetings_data()

        # Add greeting length
        df["length"] = df["greeting"].str.len()

        # Display as interactive table
        st.dataframe(
            df,
            use_container_width=True,
            hide_index=True,
            column_config={
                "language": st.column_config.TextColumn("Language", width="medium"),
                "greeting": st.column_config.TextColumn("Greeting", width="large"),
                "length": st.column_config.NumberColumn("Length", width="small"),
            },
        )

    with col2:
        st.header("📊 Statistics")

        # Metrics
        metrics_col1, metrics_col2, metrics_col3 = st.columns(3)
        with metrics_col1:
            st.metric("Total Languages", len(df))
        with metrics_col2:
            st.metric("Avg Length", f"{df['length'].mean():.1f}")
        with metrics_col3:
            st.metric("Max Length", df["length"].max())

        # Bar chart
        st.bar_chart(df.set_index("language")["length"])

    # Interactive section
    st.markdown("---")
    st.header("🎯 Try It Yourself")

    name = st.text_input("Enter your name:", placeholder="World")
    if st.button("Say Hello!", type="primary"):
        greeting_name = name if name else "World"
        st.success(f"Hello, {greeting_name}! 👋")
        st.balloons()

    # Filter section
    st.markdown("---")
    st.header("🔍 Filter Greetings")

    min_length = st.slider(
        "Minimum greeting length:",
        min_value=int(df["length"].min()),
        max_value=int(df["length"].max()),
        value=int(df["length"].min()),
    )

    filtered_df = df[df["length"] >= min_length]
    st.write(f"Showing {len(filtered_df)} greetings with length >= {min_length}")
    st.dataframe(filtered_df, use_container_width=True, hide_index=True)

    # Databricks connection info (when running on Databricks)
    st.markdown("---")
    with st.expander("🔧 Databricks Connection Info"):
        st.markdown("When running on Azure Databricks, this app can connect to:")
        st.markdown("- **Unity Catalog** tables and views")
        st.markdown("- **Databricks SQL** warehouses")
        st.markdown("- **Delta Lake** tables")
        st.markdown("- **ML Models** in the Model Registry")

        # Show environment info if available
        if os.getenv("DATABRICKS_HOST"):
            st.success(f"Connected to: {os.getenv('DATABRICKS_HOST')}")
        else:
            st.info("Running in local/development mode")


if __name__ == "__main__":
    main()
