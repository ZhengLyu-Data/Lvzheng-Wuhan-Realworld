DROP TABLE IF EXISTS bank_data;

CREATE TABLE bank_data (
    age INTEGER,
    job TEXT,
    marital TEXT,
    education TEXT,
    "default" TEXT, 
    balance INTEGER,
    housing TEXT,
    loan TEXT,
    contact TEXT,
    day INTEGER,
    month TEXT,
    duration INTEGER,
    campaign INTEGER,
    pdays INTEGER,
    previous INTEGER,
    poutcome TEXT,
    y TEXT
);

INSERT INTO bank_data VALUES
(35, 'management', 'married', 'tertiary', 'no', 1200, 'yes', 'no', 'cellular', 5, 'may', 300, 2, 999, 0, 'unknown', 'yes'),
(47, 'technician', 'single', 'secondary', 'no', 500, 'yes', 'yes', 'telephone', 18, 'may', 250, 3, 999, 0, 'unknown', 'no');

-- Table 1: Subscription by Job
SELECT job, 
       ROUND(SUM(CASE WHEN y = 'yes' THEN 1 ELSE 0 END)*1.0 / COUNT(*), 2) AS subscribed_ratio
FROM bank_data
GROUP BY job;

-- Table 2: Loan Impact
SELECT loan, y, COUNT(*) AS count
FROM bank_data
GROUP BY loan, y;

-- Table 3: Campaign Effectiveness
SELECT campaign, y, COUNT(*) AS count
FROM bank_data
GROUP BY campaign, y;

-- Table 4: Education vs Subscription
SELECT education, 
       ROUND(SUM(CASE WHEN y = 'yes' THEN 1 ELSE 0 END)*1.0 / COUNT(*), 2) AS subscribed_ratio
FROM bank_data
GROUP BY education;

-- Table 5: Age Group Mapping
SELECT 
  CASE 
    WHEN age < 30 THEN '<30'
    WHEN age BETWEEN 30 AND 39 THEN '30-40'
    WHEN age BETWEEN 40 AND 49 THEN '40-50'
    WHEN age BETWEEN 50 AND 59 THEN '50-60'
    ELSE '60+'
  END AS age_group,
  y,
  COUNT(*) AS count
FROM bank_data
GROUP BY age_group, y;

-- Table 6: Monthly Subscription Trend (use CASE to sort months)
SELECT month, y, COUNT(*) AS count
FROM bank_data
GROUP BY month, y
ORDER BY 
  CASE month
    WHEN 'jan' THEN 1
    WHEN 'feb' THEN 2
    WHEN 'mar' THEN 3
    WHEN 'apr' THEN 4
    WHEN 'may' THEN 5
    WHEN 'jun' THEN 6
    WHEN 'jul' THEN 7
    WHEN 'aug' THEN 8
    WHEN 'sep' THEN 9
    WHEN 'oct' THEN 10
    WHEN 'nov' THEN 11
    WHEN 'dec' THEN 12
    ELSE 13
  END;
