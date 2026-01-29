# unmatchedchecker

Databricks application for unmatched data checking and validation.

## Project Structure

```
unmatchedchecker/
├── app/                    # Databricks App (Streamlit)
│   ├── app.yaml           # Databricks App configuration
│   ├── main.py            # Streamlit application
│   └── requirements.txt   # App-specific dependencies
├── config/                 # Environment-specific configurations
│   ├── dev/               # Development environment
│   ├── staging/           # Staging environment
│   └── prod/              # Production environment
├── data/                   # Data files
│   ├── samples/           # Sample data for testing
│   └── schemas/           # Data schema definitions
├── docs/                   # Documentation
├── notebooks/              # Databricks notebooks
│   ├── exploration/       # Data exploration notebooks
│   ├── etl/               # ETL pipeline notebooks
│   └── ml/                # Machine learning notebooks
├── src/                    # Python source code
│   ├── common/            # Shared utilities
│   ├── etl/               # ETL modules
│   └── models/            # Data/ML models
├── tests/                  # Test suite
│   ├── integration/       # Integration tests
│   └── unit/              # Unit tests
├── workflows/              # Databricks job definitions
├── pyproject.toml         # Project configuration
├── requirements.txt       # Python dependencies
└── setup.py               # Package setup
```

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. For development:
   ```bash
   pip install -e ".[dev]"
   ```

## Configuration

Set the `ENV` environment variable to specify the environment:
- `dev` (default)
- `staging`
- `prod`

## Running Tests

```bash
pytest
```

## Running the Streamlit App Locally

```bash
cd app
pip install -r requirements.txt
streamlit run main.py
```

## Deploying to Azure Databricks

### Deploying the Databricks App (Streamlit UI)

1. In Azure Databricks workspace, go to **Compute** > **Apps**
2. Click **Create App**
3. Upload the `app/` directory or connect to your Git repository
4. The app will use `app.yaml` for configuration
5. Click **Deploy** to start the app

Alternatively, using Databricks CLI:
```bash
# Install Databricks CLI
pip install databricks-cli

# Configure authentication
databricks configure --token

# Deploy the app
databricks apps create --name hello-world --source-path ./app
```

### Deploying Notebooks and Jobs

1. Upload the `src/` directory to your Databricks workspace
2. Import notebooks from `notebooks/`
3. Configure jobs using definitions in `workflows/`

## Azure Databricks Apps Features

When deployed on Azure Databricks, the Streamlit app benefits from:
- **Unity Catalog** integration for data governance
- **Serverless compute** for automatic scaling
- **OAuth/OIDC** authentication
- **Built-in secrets management**
