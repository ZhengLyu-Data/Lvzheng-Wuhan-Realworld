CREATE TABLE bank_marketing (
  "age" INTEGER,
  "job" TEXT,
  "marital" TEXT,
  "education" TEXT,
  "default" TEXT,
  "housing" TEXT,
  "loan" TEXT,
  "contact" TEXT,
  "month" TEXT,
  "day_of_week" TEXT,
  "campaign" INTEGER,
  "pdays" INTEGER,
  "previous" INTEGER,
  "poutcome" TEXT,
  "emp.var.rate" REAL,
  "cons.price.idx" REAL,
  "cons.conf.idx" REAL,
  "euribor3m" REAL,
  "nr.employed" REAL,
  "y" TEXT
);


INSERT INTO bank_marketing VALUES (56, 'housemaid', 'married', 'basic.4y', 'no', 'no', 'no', 'telephone', 'may', 'mon', 1, 999, 0, 'nonexistent', 1.1, 93.994, -36.4, 4.857, 5191, 'no');
INSERT INTO bank_marketing VALUES (57, 'services', 'married', 'high.school', 'unknown', 'no', 'no', 'telephone', 'may', 'mon', 1, 999, 0, 'nonexistent', 1.1, 93.994, -36.4, 4.857, 5191, 'no');
INSERT INTO bank_marketing VALUES (37, 'services', 'married', 'high.school', 'no', 'yes', 'no', 'telephone', 'may', 'mon', 1, 999, 0, 'nonexistent', 1.1, 93.994, -36.4, 4.857, 5191, 'no');
INSERT INTO bank_marketing VALUES (40, 'admin.', 'married', 'basic.6y', 'no', 'no', 'no', 'telephone', 'may', 'mon', 1, 999, 0, 'nonexistent', 1.1, 93.994, -36.4, 4.857, 5191, 'no');
INSERT INTO bank_marketing VALUES (56, 'services', 'married', 'high.school', 'no', 'no', 'no', 'telephone', 'may', 'mon', 1, 999, 0, 'nonexistent', 1.1, 93.994, -36.4, 4.857, 5191, 'no');

SELECT * FROM bank_marketing;

SELECT education,
       COUNT(*) AS total_customers,
       SUM(CASE WHEN y = 'yes' THEN 1 ELSE 0 END) AS subscribed,
       ROUND(100.0 * SUM(CASE WHEN y = 'yes' THEN 1 ELSE 0 END) / COUNT(*), 2) AS subscription_rate_pct
FROM bank_marketing
GROUP BY education
ORDER BY subscription_rate_pct DESC;
