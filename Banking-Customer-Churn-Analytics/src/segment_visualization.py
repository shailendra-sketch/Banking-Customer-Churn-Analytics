from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
SEGMENT_FILE = PROJECT_ROOT / "data" / "processed" / "customer_segments.csv"
FIGURES_DIR = PROJECT_ROOT / "reports" / "figures"


def main():
    FIGURES_DIR.mkdir(parents=True, exist_ok=True)

    df = pd.read_csv(SEGMENT_FILE)

    segment_summary = (
        df.groupby("risk_segment", as_index=False)
        .agg(
            total_customers=("customer_id", "count"),
            churned_customers=("churn", "sum"),
            churn_rate=("churn", "mean"),
        )
    )

    segment_summary["churn_rate"] = (
        segment_summary["churn_rate"] * 100
    )

    risk_order = ["High Risk", "Medium Risk", "Low Risk"]

    segment_summary["risk_segment"] = pd.Categorical(
        segment_summary["risk_segment"],
        categories=risk_order,
        ordered=True,
    )

    segment_summary = segment_summary.sort_values("risk_segment")

    # Chart 1: Customers by risk segment
    plt.figure(figsize=(10, 6))

    plt.bar(
        segment_summary["risk_segment"].astype(str),
        segment_summary["total_customers"],
    )

    plt.title("Customers by Risk Segment")
    plt.xlabel("Risk Segment")
    plt.ylabel("Number of Customers")
    plt.tight_layout()

    output_file = FIGURES_DIR / "08_customers_by_risk_segment.png"
    plt.savefig(output_file, dpi=150)
    plt.close()

    print(f"Saved: {output_file}")

    # Chart 2: Churn rate by risk segment
    plt.figure(figsize=(10, 6))

    plt.bar(
        segment_summary["risk_segment"].astype(str),
        segment_summary["churn_rate"],
    )

    plt.title("Churn Rate by Risk Segment")
    plt.xlabel("Risk Segment")
    plt.ylabel("Churn Rate (%)")
    plt.tight_layout()

    output_file = FIGURES_DIR / "09_churn_rate_by_risk_segment.png"
    plt.savefig(output_file, dpi=150)
    plt.close()

    print(f"Saved: {output_file}")

    print()
    print("Risk-segment visualization completed successfully.")


if __name__ == "__main__":
    main()