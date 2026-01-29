"""Hello World module for Databricks application."""

from pyspark.sql import DataFrame, SparkSession
from pyspark.sql.functions import length, upper, current_timestamp, lit


def get_spark() -> SparkSession:
    """Get or create a SparkSession."""
    return SparkSession.builder.appName("HelloWorld").getOrCreate()


def create_greetings_df(spark: SparkSession) -> DataFrame:
    """Create a DataFrame with hello world greetings in various languages.

    Args:
        spark: SparkSession instance.

    Returns:
        DataFrame with language and greeting columns.
    """
    greetings = [
        ("English", "Hello, World!"),
        ("Spanish", "¡Hola, Mundo!"),
        ("French", "Bonjour, le Monde!"),
        ("German", "Hallo, Welt!"),
        ("Japanese", "こんにちは、世界！"),
        ("Italian", "Ciao, Mondo!"),
        ("Portuguese", "Olá, Mundo!"),
        ("Russian", "Привет, мир!"),
        ("Chinese", "你好，世界！"),
        ("Korean", "안녕하세요, 세계!"),
    ]
    return spark.createDataFrame(greetings, ["language", "greeting"])


def enrich_greetings(df: DataFrame) -> DataFrame:
    """Enrich greetings DataFrame with additional columns.

    Args:
        df: DataFrame with language and greeting columns.

    Returns:
        Enriched DataFrame with length, uppercase, and timestamp columns.
    """
    return (
        df.withColumn("greeting_length", length("greeting"))
        .withColumn("greeting_upper", upper("greeting"))
        .withColumn("processed_at", current_timestamp())
    )


def say_hello(name: str = "World") -> str:
    """Return a hello message.

    Args:
        name: Name to greet.

    Returns:
        Hello message string.
    """
    return f"Hello, {name}!"


def run_hello_world() -> None:
    """Run the complete Hello World demonstration."""
    spark = get_spark()

    print("=" * 50)
    print(say_hello("Databricks"))
    print("=" * 50)

    # Create and display greetings
    df = create_greetings_df(spark)
    print("\nGreetings from around the world:")
    df.show(truncate=False)

    # Enrich and display
    df_enriched = enrich_greetings(df)
    print("\nEnriched greetings:")
    df_enriched.show(truncate=False)

    # Summary
    print(f"\nTotal greetings: {df.count()}")
    print("Hello World complete!")


if __name__ == "__main__":
    run_hello_world()
