"""Unit tests for the hello_world module."""

import pytest

from hello_world import say_hello, create_greetings_df, enrich_greetings


def test_say_hello_default():
    """Test say_hello with default parameter."""
    result = say_hello()
    assert result == "Hello, World!"


def test_say_hello_with_name():
    """Test say_hello with a custom name."""
    result = say_hello("Databricks")
    assert result == "Hello, Databricks!"


def test_create_greetings_df(spark_session):
    """Test that greetings DataFrame is created correctly."""
    df = create_greetings_df(spark_session)

    # Check schema
    assert "language" in df.columns
    assert "greeting" in df.columns

    # Check row count
    assert df.count() == 10

    # Check that English greeting exists
    english_greeting = df.filter(df.language == "English").collect()[0]
    assert english_greeting.greeting == "Hello, World!"


def test_enrich_greetings(spark_session):
    """Test that greetings are enriched correctly."""
    df = create_greetings_df(spark_session)
    enriched = enrich_greetings(df)

    # Check new columns exist
    assert "greeting_length" in enriched.columns
    assert "greeting_upper" in enriched.columns
    assert "processed_at" in enriched.columns

    # Check greeting length calculation
    english = enriched.filter(enriched.language == "English").collect()[0]
    assert english.greeting_length == len("Hello, World!")
    assert english.greeting_upper == "HELLO, WORLD!"
