\# Banking Customer Churn \& Retention Analytics



\## Project Overview



This project analyzes customer churn for a banking customer dataset containing 10,000 customers.



The objective is to identify customer segments associated with higher churn rates, understand major churn patterns, and provide data-driven retention insights.



The project combines:



\- Python

\- SQL

\- Power BI

\- Pandas

\- Data visualization

\- Business analysis

\- Git \& GitHub



\---



\## Business Problem



Customer churn can reduce revenue and increase the cost of acquiring new customers.



The goal of this analysis is to answer questions such as:



\- What percentage of customers are churning?

\- Which countries have higher churn?

\- Does customer activity affect churn?

\- Does the number of products relate to churn?

\- Are there differences in churn by gender?

\- Does credit card ownership relate to churn?

\- How does customer balance relate to churn?

\- Which customer segments should receive additional retention attention?



\---



\## Dataset



The dataset contains 10,000 banking customers and 12 original variables.



\### Main Features



| Feature | Description |

|---|---|

| customer\_id | Unique customer identifier |

| credit\_score | Customer credit score |

| country | Customer country |

| gender | Customer gender |

| age | Customer age |

| tenure | Years with the bank |

| balance | Account balance |

| products\_number | Number of bank products |

| credit\_card | Credit card ownership indicator |

| active\_member | Active membership indicator |

| estimated\_salary | Estimated customer salary |

| churn | Customer churn indicator |



\---



\## Data Quality



The dataset was checked for:



\- Missing values

\- Duplicate rows

\- Duplicate customer IDs

\- Data types

\- Binary field validity

\- Numeric distributions

\- Categorical distributions



\### Results



\- Rows: 10,000

\- Columns: 12

\- Missing values: 0

\- Duplicate rows: 0

\- Duplicate customer IDs: 0

\- Overall churn rate: 20.37%



\---



\## SQL Analysis



SQL was used to analyze:



1\. Overall customer churn

2\. Churn by country

3\. Churn by gender

4\. Churn by active membership

5\. Churn by number of products

6\. Churn by credit card ownership

7\. Churn by balance segment



SQL outputs are stored in:



`reports/sql\_analysis\_report.md`



\---



\## Key Findings



\### Overall Churn



\- Total customers: 10,000

\- Churned customers: 2,037

\- Retained customers: 7,963

\- Churn rate: 20.37%



\### Country



Germany has the highest observed churn rate:



\- Germany: 32.44%

\- Spain: 16.67%

\- France: 16.15%



\### Membership Activity



Inactive customers show a higher observed churn rate:



\- Inactive: 26.85%

\- Active: 14.27%



\### Number of Products



Observed churn rates:



\- 1 product: 27.71%

\- 2 products: 7.58%

\- 3 products: 82.71%

\- 4 products: 100.00%



The three- and four-product groups are relatively small, so these percentages should be interpreted alongside customer counts.



\### Gender



\- Female: 25.07%

\- Male: 16.46%



\### Credit Card Ownership



\- Has credit card: 20.18%

\- No credit card: 20.81%



The difference is small, suggesting that credit card ownership alone is not a strong churn differentiator in this dataset.



\### Balance



Observed churn rates by balance segment:



\- Zero Balance: 13.82%

\- Below 50K: 34.67%

\- 50K-100K: 19.88%

\- 100K-150K: 25.77%

\- 150K+: 23.12%



The Below 50K group contains only 75 customers, so its churn percentage should be interpreted with its smaller sample size in mind.



\---



\## Customer Risk Segmentation



A rule-based customer segmentation model was created using:



\- Active membership

\- Number of products

\- Age

\- Credit score

\- Account balance



Customers were assigned to:



\- High Risk

\- Medium Risk

\- Low Risk



This segmentation is designed as an interpretable business-analysis framework rather than a machine-learning prediction model.



The segmented dataset is stored in:



`data/processed/customer\_segments.csv`



\---



\## Power BI Dashboard



The Power BI dashboard provides an interactive view of:



\- Total customers

\- Churned customers

\- Churn rate

\- Average balance

\- Average credit score

\- Churn rate by country

\- Churn rate by membership status

\- Churn rate by number of products

\- Churn rate by gender

\- Churn rate by balance segment



Interactive slicers allow analysis by:



\- Country

\- Gender

\- Membership status



Dashboard file:



`dashboard/banking\_customer\_churn\_dashboard.pbix`



\---



\## Business Recommendations



Based on the observed patterns:



1\. Investigate the high churn rate observed in Germany.

2\. Develop engagement and reactivation strategies for inactive customers.

3\. Investigate customers with three or more products to understand the reasons behind their high observed churn.

4\. Explore the factors associated with the higher churn rate among female customers.

5\. Investigate the 100K-150K balance segment because it combines a relatively high churn rate with a large customer population.

6\. Avoid using credit card ownership as a standalone churn targeting variable because the observed difference is small.



These recommendations identify areas for further investigation rather than establishing causal relationships.



\---



\## Project Structure



```text

Banking-Customer-Churn-Analytics/

│

├── data/

│   ├── raw/

│   │   └── bank\_customer\_churn.csv

│   │

│   └── processed/

│       ├── banking\_churn.db

│       ├── customer\_segments.csv

│       └── powerbi\_customer\_churn.csv

│

├── sql/

│   └── 01\_customer\_churn\_analysis.sql

│

├── src/

│   ├── data\_quality.py

│   ├── create\_database.py

│   ├── run\_sql\_analysis.py

│   ├── exploratory\_analysis.py

│   ├── customer\_segmentation.py

│   ├── segment\_visualization.py

│   └── prepare\_powerbi\_data.py

│

├── reports/

│   ├── data\_quality\_report.md

│   ├── sql\_analysis\_report.md

│   └── figures/

│

├── dashboard/

│   └── banking\_customer\_churn\_dashboard.pbix

│

├── docs/

│

├── README.md

└── .gitignore

