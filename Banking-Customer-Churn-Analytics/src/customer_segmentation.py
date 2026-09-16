from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
RAW_FILE = PROJECT_ROOT / "data" / "raw" / "bank_customer_churn.csv"
OUTPUT_DIR = PROJECT_ROOT / "data" / "processed"
OUTPUT_FILE = OUTPUT_DIR / "customer_segments.csv"


def assign_risk_segment(row):
    risk_score = 0

    if row["active_member"] == 0:
        risk_score += 2

    if row["products_number"] >= 3:
        risk_score += 2

    if row["age"] >= 50:
        risk_score += 1

    if row["credit_score"] < 600:
        risk_score += 1

    if row["balance"] == 0:
        risk_score += 1

    if risk_score >= 4:
        return "High Risk"
    if risk_score >= 2:
        return "Medium Risk"

    return "Low Risk"


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    df = pd.read_csv(RAW_FILE)

    df["risk_segment"] = df.apply(assign_risk_segment, axis=1)

    segment_summary = (
        df.groupby("risk_segment", as_index=False)
        .agg(
            total_customers=("customer_id", "count"),
            churned_customers=("churn", "sum"),
            churn_rate=("churn", "mean"),
            average_age=("age", "mean"),
            average_balance=("balance", "mean"),
            average_credit_score=("credit_score", "mean"),
        )
    )

    segment_summary["churn_rate"] = (
        segment_summary["churn_rate"] * 100
    ).round(2)

    segment_summary["average_age"] = (
        segment_summary["average_age"].round(2)
    )

    segment_summary["average_balance"] = (
        segment_summary["average_balance"].round(2)
    )

    segment_summary["average_credit_score"] = (
        segment_summary["average_credit_score"].round(2)
    )

    risk_order = {
        "High Risk": 1,
        "Medium Risk": 2,
        "Low Risk": 3,
    }

    segment_summary["sort_order"] = (
        segment_summary["risk_segment"].map(risk_order)
    )

    segment_summary = (
        segment_summary
        .sort_values("sort_order")
        .drop(columns=["sort_order"])
    )

    df.to_csv(OUTPUT_FILE, index=False)

    print("Customer segmentation completed successfully.")
    print()
    print("Segment summary:")
    print(segment_summary.to_string(index=False))
    print()
    print(f"Segmented dataset saved to: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()