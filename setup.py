from setuptools import setup, find_packages

setup(
    name="unmatchedchecker",
    version="0.1.0",
    description="Databricks application for unmatched data checking",
    author="",
    author_email="",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.9",
    install_requires=[
        "pyspark>=3.4.0",
        "delta-spark>=2.4.0",
        "pandas>=2.0.0",
        "numpy>=1.24.0",
        "pyyaml>=6.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.4.0",
            "pytest-cov>=4.1.0",
            "chispa>=0.9.0",
            "black>=23.0.0",
            "flake8>=6.0.0",
            "mypy>=1.4.0",
        ],
    },
)
