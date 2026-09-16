from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
RAW_FILE = PROJECT_ROOT / "data" / "raw" / "bank_customer_churn.csv"
FIGURES_DIR = PROJECT_ROOT / "reports" / "figures"


def save_bar_chart(
    data,
    category_column,
    value_column,
    title,
    x_label,
    y_label,
    filename,
    rotate_labels=False,
):
    plt.figure(figsize=(10, 6))

    plt.bar(data[category_column].astype(str), data[value_column])

    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.tight_layout()

    if rotate_labels:
        plt.xticks(rotation=30, ha="right")

    output_file = FIGURES_DIR / filename
    plt.savefig(output_file, dpi=150)
    plt.close()

    print(f"Saved: {output_file}")


def main():
    FIGURES_DIR.mkdir(parents=True, exist_ok=True)

    df = pd.read_csv(RAW_FILE)

    df["churn_label"] = df["churn"].map(
        {
            0: "Retained",
            1: "Churned",
        }
    )

    # 1. Overall churn distribution
    churn_counts = (
        df["churn_label"]
        .value_counts()
        .rename_axis("status")
        .reset_index(name="customers")
    )

    save_bar_chart(
        data=churn_counts,
        category_column="status",
        value_column="customers",
        title="Customer Retention vs Churn",
        x_label="Customer Status",
        y_label="Number of Customers",
        filename="01_overall_churn.png",
    )

    # 2. Churn rate by country
    country_churn = (
        df.groupby("country", as_index=False)["churn"]
        .mean()
        .assign(churn_rate=lambda data: data["churn"] * 100)
        .sort_values("churn_rate", ascending=False)
    )

    save_bar_chart(
        data=country_churn,
        category_column="country",
        value_column="churn_rate",
        title="Churn Rate by Country",
        x_label="Country",
        y_label="Churn Rate (%)",
        filename="02_churn_by_country.png",
    )

    # 3. Churn rate by gender
    gender_churn = (
        df.groupby("gender", as_index=False)["churn"]
        .mean()
        .assign(churn_rate=lambda data: data["churn"] * 100)
        .sort_values("churn_rate", ascending=False)
    )

    save_bar_chart(
        data=gender_churn,
        category_column="gender",
        value_column="churn_rate",
        title="Churn Rate by Gender",
        x_label="Gender",
        y_label="Churn Rate (%)",
        filename="03_churn_by_gender.png",
    )

    # 4. Churn rate by active membership
    membership_churn = (
        df.groupby("active_member", as_index=False)["churn"]
        .mean()
        .assign(
            membership_status=lambda data: data["active_member"].map(
                {
                    0: "Inactive",
                    1: "Active",
                }
            ),
            churn_rate=lambda data: data["churn"] * 100,
        )
        .sort_values("churn_rate", ascending=False)
    )

    save_bar_chart(
        data=membership_churn,
        category_column="membership_status",
        value_column="churn_rate",
        title="Churn Rate by Membership Status",
        x_label="Membership Status",
        y_label="Churn Rate (%)",
        filename="04_churn_by_membership.png",
    )

    # 5. Churn rate by number of products
    product_churn = (
        df.groupby("products_number", as_index=False)["churn"]
        .mean()
        .assign(churn_rate=lambda data: data["churn"] * 100)
        .sort_values("products_number")
    )

    save_bar_chart(
        data=product_churn,
        category_column="products_number",
        value_column="churn_rate",
        title="Churn Rate by Number of Products",
        x_label="Number of Products",
        y_label="Churn Rate (%)",
        filename="05_churn_by_products.png",
    )

    # 6. Churn rate by credit card ownership
    credit_card_churn = (
        df.groupby("credit_card", as_index=False)["churn"]
        .mean()
        .assign(
            card_status=lambda data: data["credit_card"].map(
                {
                    0: "No Credit Card",
                    1: "Has Credit Card",
                }
            ),
            churn_rate=lambda data: data["churn"] * 100,
        )
        .sort_values("churn_rate", ascending=False)
    )

    save_bar_chart(
        data=credit_card_churn,
        category_column="card_status",
        value_column="churn_rate",
        title="Churn Rate by Credit Card Ownership",
        x_label="Credit Card Status",
        y_label="Churn Rate (%)",
        filename="06_churn_by_credit_card.png",
    )

    # 7. Churn rate by balance segment
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

    df["balance_segment"] = df["balance"].apply(classify_balance)

    balance_order = [
        "Zero Balance",
        "Below 50K",
        "50K-100K",
        "100K-150K",
        "150K+",
    ]

    balance_churn = (
        df.groupby("balance_segment", as_index=False)["churn"]
        .mean()
        .assign(churn_rate=lambda data: data["churn"] * 100)
    )

    balance_churn["balance_segment"] = pd.Categorical(
        balance_churn["balance_segment"],
        categories=balance_order,
        ordered=True,
    )

    balance_churn = balance_churn.sort_values("balance_segment")

    save_bar_chart(
        data=balance_churn,
        category_column="balance_segment",
        value_column="churn_rate",
        title="Churn Rate by Balance Segment",
        x_label="Balance Segment",
        y_label="Churn Rate (%)",
        filename="07_churn_by_balance.png",
        rotate_labels=True,
    )

    print()
    print("Exploratory analysis completed successfully.")
    print(f"Charts saved in: {FIGURES_DIR}")


if __name__ == "__main__":
    main()