from pathlib import Path
import pandas as pd


# Project paths
PROJECT_ROOT = Path(__file__).resolve().parents[1]
RAW_FILE = PROJECT_ROOT / "data" / "raw" / "bank_customer_churn.csv"
REPORT_DIR = PROJECT_ROOT / "reports"
REPORT_FILE = REPORT_DIR / "data_quality_report.md"


def main():
    REPORT_DIR.mkdir(parents=True, exist_ok=True)

    df = pd.read_csv(RAW_FILE)

    missing_values = df.isnull().sum()
    duplicate_rows = df.duplicated().sum()
    duplicate_customer_ids = df["customer_id"].duplicated().sum()

    report_lines = [
        "# Banking Customer Churn Analytics",
        "",
        "## Data Quality Report",
        "",
        "### Dataset Overview",
        "",
        f"- Number of rows: **{df.shape[0]:,}**",
        f"- Number of columns: **{df.shape[1]}**",
        f"- Duplicate rows: **{duplicate_rows:,}**",
        f"- Duplicate customer IDs: **{duplicate_customer_ids:,}**",
        "",
        "### Columns",
        "",
    ]

    for column in df.columns:
        report_lines.append(f"- `{column}`")

    report_lines.extend(
        [
            "",
            "### Missing Values",
            "",
        ]
    )

    for column, missing_count in missing_values.items():
        report_lines.append(f"- `{column}`: **{missing_count:,}**")

    report_lines.extend(
        [
            "",
            "### Data Types",
            "",
        ]
    )

    for column, data_type in df.dtypes.items():
        report_lines.append(f"- `{column}`: `{data_type}`")

    report_lines.extend(
        [
            "",
            "### Numeric Summary",
            "",
            "```text",
            df.describe().round(2).to_string(),
            "```",
            "",
            "### Categorical Values",
            "",
        ]
    )

    for column in ["country", "gender"]:
        report_lines.append(f"#### `{column}`")
        report_lines.append("")
        report_lines.append("```text")
        report_lines.append(df[column].value_counts().to_string())
        report_lines.append("```")
        report_lines.append("")

    report_lines.extend(
        [
            "#### Binary Columns",
            "",
            "The following columns should contain binary values:",
            "",
            "- `credit_card`",
            "- `active_member`",
            "- `churn`",
            "",
        ]
    )

    for column in ["credit_card", "active_member", "churn"]:
        unique_values = sorted(df[column].dropna().unique().tolist())
        report_lines.append(f"- `{column}` unique values: `{unique_values}`")

    REPORT_FILE.write_text("\n".join(report_lines), encoding="utf-8")

    print("Data-quality analysis completed.")
    print(f"Rows: {df.shape[0]:,}")
    print(f"Columns: {df.shape[1]}")
    print(f"Duplicate rows: {duplicate_rows:,}")
    print(f"Duplicate customer IDs: {duplicate_customer_ids:,}")
    print(f"Report saved to: {REPORT_FILE}")


if __name__ == "__main__":
    main()