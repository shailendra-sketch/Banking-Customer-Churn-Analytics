from pathlib import Path
import sqlite3


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DB_FILE = PROJECT_ROOT / "data" / "processed" / "banking_churn.db"
SQL_FILE = PROJECT_ROOT / "sql" / "01_customer_churn_analysis.sql"
REPORT_DIR = PROJECT_ROOT / "reports"
REPORT_FILE = REPORT_DIR / "sql_analysis_report.md"


def extract_query_title(statement, query_number):
    lines = statement.strip().splitlines()

    for line in lines:
        line = line.strip()

        if line.startswith("--"):
            title = line.replace("--", "").strip()

            if title:
                return title

    return f"Query {query_number}"


def format_results(columns, rows):
    if not rows:
        return "No results returned."

    output = []

    header = "| " + " | ".join(columns) + " |"
    separator = "| " + " | ".join(["---"] * len(columns)) + " |"

    output.append(header)
    output.append(separator)

    for row in rows:
        formatted_row = []

        for value in row:
            if isinstance(value, float):
                formatted_row.append(f"{value:,.2f}")
            elif value is None:
                formatted_row.append("NULL")
            else:
                formatted_row.append(str(value))

        output.append("| " + " | ".join(formatted_row) + " |")

    return "\n".join(output)


def main():
    if not DB_FILE.exists():
        raise FileNotFoundError(f"Database not found: {DB_FILE}")

    if not SQL_FILE.exists():
        raise FileNotFoundError(f"SQL file not found: {SQL_FILE}")

    REPORT_DIR.mkdir(parents=True, exist_ok=True)

    sql_text = SQL_FILE.read_text(encoding="utf-8")

    statements = [
        statement.strip()
        for statement in sql_text.split(";")
        if statement.strip()
    ]

    report_lines = [
        "# Banking Customer Churn Analytics",
        "",
        "## SQL Analysis Report",
        "",
        "This report contains the results of the customer churn analysis queries.",
        "",
    ]

    with sqlite3.connect(DB_FILE) as connection:
        for query_number, statement in enumerate(statements, start=1):
            title = extract_query_title(statement, query_number)

            cursor = connection.execute(statement)
            rows = cursor.fetchall()
            columns = [description[0] for description in cursor.description]

            report_lines.append(f"### {title}")
            report_lines.append("")
            report_lines.append(format_results(columns, rows))
            report_lines.append("")

            print(f"Completed: {title}")

    REPORT_FILE.write_text("\n".join(report_lines), encoding="utf-8")

    print()
    print("SQL analysis completed successfully.")
    print(f"Queries executed: {len(statements)}")
    print(f"Report saved to: {REPORT_FILE}")


if __name__ == "__main__":
    main()