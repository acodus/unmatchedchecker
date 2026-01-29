# unmatchedchecker

Databricks application for unmatched data checking and validation.

## Project Structure

```
unmatchedchecker/
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

## Deploying to Databricks

1. Upload the `src/` directory to your Databricks workspace
2. Import notebooks from `notebooks/`
3. Configure jobs using definitions in `workflows/`
