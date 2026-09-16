from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
RAW_FILE = PROJECT_ROOT / "data" / "raw" / "bank_customer_churn.csv"
OUTPUT_DIR = PROJECT_ROOT / "data" / "processed"
OUTPUT_FILE = OUTPUT_DIR / "powerbi_customer_churn.csv"


def classify_balance(balance):
    if balance == 0:
        return "Zero Balance"
    if balance < 50000:
        return "Below 50K"
    if balance < 100000:
        return "50K-100K"
    if balance < 150000:
        return "100K-150K"
    return "150K+"


def classify_age(age):
    if age < 30:
        return "18-29"
    if age < 40:
        return "30-39"
    if age < 50:
        return "40-49"
    if age < 60:
        return "50-59"
    return "60+"


def classify_credit_score(score):
    if score < 580:
        return "Poor"
    if score < 670:
        return "Fair"
    if score < 740:
        return "Good"
    if score < 800:
        return "Very Good"
    return "Excellent"


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    df = pd.read_csv(RAW_FILE)

    df["churn_status"] = df["churn"].map(
        {
            0: "Retained",
            1: "Churned",
        }
    )

    df["membership_status"] = df["active_member"].map(
        {
            0: "Inactive",
            1: "Active",
        }
    )

    df["credit_card_status"] = df["credit_card"].map(
        {
            0: "No Credit Card",
            1: "Has Credit Card",
        }
    )

    df["balance_segment"] = df["balance"].apply(classify_balance)
    df["age_group"] = df["age"].apply(classify_age)
    df["credit_score_band"] = df["credit_score"].apply(
        classify_credit_score
    )

    df["high_value_customer"] = (
        (df["balance"] >= 100000) &
        (df["active_member"] == 1)
    ).map(
        {
            False: "No",
            True: "Yes",
        }
    )

    selected_columns = [
        "customer_id",
        "credit_score",
        "credit_score_band",
        "country",
        "gender",
        "age",
        "age_group",
        "tenure",
        "balance",
        "balance_segment",
        "products_number",
        "credit_card",
        "credit_card_status",
        "active_member",
        "membership_status",
        "estimated_salary",
        "high_value_customer",
        "churn",
        "churn_status",
    ]

    output_df = df[selected_columns]

    output_df.to_csv(OUTPUT_FILE, index=False)

    print("Power BI dataset prepared successfully.")
    print(f"Rows exported: {len(output_df):,}")
    print(f"Columns exported: {len(output_df.columns)}")
    print(f"Output file: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()