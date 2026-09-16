from pathlib import Path
import sqlite3

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
RAW_FILE = PROJECT_ROOT / "data" / "raw" / "bank_customer_churn.csv"
PROCESSED_DIR = PROJECT_ROOT / "data" / "processed"
DB_FILE = PROCESSED_DIR / "banking_churn.db"


def main():
    if not RAW_FILE.exists():
        raise FileNotFoundError(f"Dataset not found: {RAW_FILE}")

    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

    df = pd.read_csv(RAW_FILE)

    with sqlite3.connect(DB_FILE) as connection:
        df.to_sql(
            "customers",
            connection,
            if_exists="replace",
            index=False
        )

        row_count = connection.execute(
            "SELECT COUNT(*) FROM customers"
        ).fetchone()[0]

        column_count = connection.execute(
            "PRAGMA table_info(customers)"
        ).fetchall()

    print("SQLite database created successfully.")
    print(f"Rows loaded: {row_count:,}")
    print(f"Columns loaded: {len(column_count)}")
    print(f"Database location: {DB_FILE}")


if __name__ == "__main__":
    main()