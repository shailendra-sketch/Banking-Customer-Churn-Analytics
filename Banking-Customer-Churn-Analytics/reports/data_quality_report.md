# Banking Customer Churn Analytics

## Data Quality Report

### Dataset Overview

- Number of rows: **10,000**
- Number of columns: **12**
- Duplicate rows: **0**
- Duplicate customer IDs: **0**

### Columns

- `customer_id`
- `credit_score`
- `country`
- `gender`
- `age`
- `tenure`
- `balance`
- `products_number`
- `credit_card`
- `active_member`
- `estimated_salary`
- `churn`

### Missing Values

- `customer_id`: **0**
- `credit_score`: **0**
- `country`: **0**
- `gender`: **0**
- `age`: **0**
- `tenure`: **0**
- `balance`: **0**
- `products_number`: **0**
- `credit_card`: **0**
- `active_member`: **0**
- `estimated_salary`: **0**
- `churn`: **0**

### Data Types

- `customer_id`: `int64`
- `credit_score`: `int64`
- `country`: `str`
- `gender`: `str`
- `age`: `int64`
- `tenure`: `int64`
- `balance`: `float64`
- `products_number`: `int64`
- `credit_card`: `int64`
- `active_member`: `int64`
- `estimated_salary`: `float64`
- `churn`: `int64`

### Numeric Summary

```text
       customer_id  credit_score       age    tenure    balance  products_number  credit_card  active_member  estimated_salary    churn
count     10000.00      10000.00  10000.00  10000.00   10000.00         10000.00     10000.00       10000.00          10000.00  10000.0
mean   15690940.57        650.53     38.92      5.01   76485.89             1.53         0.71           0.52         100090.24      0.2
std       71936.19         96.65     10.49      2.89   62397.41             0.58         0.46           0.50          57510.49      0.4
min    15565701.00        350.00     18.00      0.00       0.00             1.00         0.00           0.00             11.58      0.0
25%    15628528.25        584.00     32.00      3.00       0.00             1.00         0.00           0.00          51002.11      0.0
50%    15690738.00        652.00     37.00      5.00   97198.54             1.00         1.00           1.00         100193.92      0.0
75%    15753233.75        718.00     44.00      7.00  127644.24             2.00         1.00           1.00         149388.25      0.0
max    15815690.00        850.00     92.00     10.00  250898.09             4.00         1.00           1.00         199992.48      1.0
```

### Categorical Values

#### `country`

```text
country
France     5014
Germany    2509
Spain      2477
```

#### `gender`

```text
gender
Male      5457
Female    4543
```

#### Binary Columns

The following columns should contain binary values:

- `credit_card`
- `active_member`
- `churn`

- `credit_card` unique values: `[0, 1]`
- `active_member` unique values: `[0, 1]`
- `churn` unique values: `[0, 1]`