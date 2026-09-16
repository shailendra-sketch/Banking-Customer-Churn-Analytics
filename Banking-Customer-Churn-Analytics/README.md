\# Banking Customer Churn \& Retention Analytics



An end-to-end customer churn analytics project using \*\*Python, SQL, and Power BI\*\* to analyze banking customer behavior, identify churn patterns, segment customers by risk, and provide data-driven areas for retention analysis.



\---



\## Project Overview



Customer churn is a major business challenge for financial institutions because losing customers can reduce revenue, product usage, and long-term customer value.



This project analyzes a dataset of \*\*10,000 banking customers\*\* to understand:



\- Overall customer churn

\- Churn patterns across countries and genders

\- Active vs inactive customer behavior

\- Relationship between product ownership and churn

\- Credit card ownership and churn

\- Balance-based customer segments

\- Customer risk segmentation

\- Business areas that may require retention-focused investigation



The project combines \*\*Python for data analysis and preparation, SQL for structured analysis, and Power BI for interactive business reporting\*\*.



\---



\## Business Problem



The objective is to answer key business questions such as:



1\. What percentage of customers are churning?

2\. Which countries have the highest observed churn?

3\. How does customer activity relate to churn?

4\. Does the number of products held by a customer relate to churn?

5\. Are there meaningful differences in churn by gender?

6\. Does credit card ownership show a meaningful difference in churn?

7\. Which balance segments have higher observed churn?

8\. Which customers can be prioritized for further retention analysis?



\---



\## Dataset



The dataset contains \*\*10,000 customer records\*\* and \*\*12 attributes\*\*.



\### Features



| Feature | Description |

|---|---|

| `customer\_id` | Unique customer identifier |

| `credit\_score` | Customer credit score |

| `country` | Customer country |

| `gender` | Customer gender |

| `age` | Customer age |

| `tenure` | Number of years with the bank |

| `balance` | Account balance |

| `products\_number` | Number of bank products owned |

| `credit\_card` | Credit card ownership indicator |

| `active\_member` | Active membership indicator |

| `estimated\_salary` | Estimated customer salary |

| `churn` | Churn indicator: 1 = Churned, 0 = Retained |



\---



\## Data Quality



Initial data-quality analysis was performed using Python.



\### Results



\- \*\*Rows:\*\* 10,000

\- \*\*Columns:\*\* 12

\- \*\*Missing values:\*\* 0

\- \*\*Duplicate rows:\*\* 0

\- \*\*Duplicate customer IDs:\*\* 0



The dataset was checked for structural quality before performing the business analysis.



Generated report:



```text

reports/data\_quality\_report.md

