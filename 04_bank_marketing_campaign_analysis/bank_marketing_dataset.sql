DROP TABLE IF EXISTS bank_marketing;

CREATE TABLE bank_marketing (
  age INT,
  job VARCHAR(255),
  marital VARCHAR(255),
  education VARCHAR(255),
  credit_default VARCHAR(255),
  housing VARCHAR(255),
  loan VARCHAR(255),
  contact VARCHAR(255),
  month VARCHAR(255),
  day_of_week VARCHAR(255),
  duration INT,
  campaign INT,
  pdays INT,
  previous INT,
  poutcome VARCHAR(255),
  emp_var_rate FLOAT,
  cons_price_idx FLOAT,
  cons_conf_idx FLOAT,
  euribor3m FLOAT,
  nr_employed FLOAT,
  y VARCHAR(10)
);

INSERT INTO bank_marketing (age, job, marital, education, credit_default, housing, loan, contact, month, day_of_week, campaign, pdays, previous, poutcome, emp_var_rate, cons_price_idx, cons_conf_idx, euribor3m, nr_employed, y) VALUES (56, 'housemaid', 'married', 'basic.4y', 'no', 'no', 'no', 'telephone', 'may', 'mon', 1, 999, 0, 'nonexistent', 1.1, 93.994, -36.4, 4.857, 5191.0, 'no');
INSERT INTO bank_marketing (age, job, marital, education, credit_default, housing, loan, contact, month, day_of_week, campaign, pdays, previous, poutcome, emp_var_rate, cons_price_idx, cons_conf_idx, euribor3m, nr_employed, y) VALUES (57, 'services', 'married', 'high.school', 'no', 'no', 'no', 'telephone', 'may', 'mon', 1, 999, 0, 'nonexistent', 1.1, 93.994, -36.4, 4.857, 5191.0, 'no');
INSERT INTO bank_marketing (age, job, marital, education, credit_default, housing, loan, contact, month, day_of_week, campaign, pdays, previous, poutcome, emp_var_rate, cons_price_idx, cons_conf_idx, euribor3m, nr_employed, y) VALUES (37, 'services', 'married', 'high.school', 'no', 'yes', 'no', 'telephone', 'may', 'mon', 1, 999, 0, 'nonexistent', 1.1, 93.994, -36.4, 4.857, 5191.0, 'no');
INSERT INTO bank_marketing (age, job, marital, education, credit_default, housing, loan, contact, month, day_of_week, campaign, pdays, previous, poutcome, emp_var_rate, cons_price_idx, cons_conf_idx, euribor3m, nr_employed, y) VALUES (40, 'admin.', 'married', 'basic.6y', 'no', 'no', 'no', 'telephone', 'may', 'mon', 1, 999, 0, 'nonexistent', 1.1, 93.994, -36.4, 4.857, 5191.0, 'no');
INSERT INTO bank_marketing (age, job, marital, education, credit_default, housing, loan, contact, month, day_of_week, campaign, pdays, previous, poutcome, emp_var_rate, cons_price_idx, cons_conf_idx, euribor3m, nr_employed, y) VALUES (56, 'services', 'married', 'high.school', 'no', 'no', 'yes', 'telephone', 'may', 'mon', 1, 999, 0, 'nonexistent', 1.1, 93.994, -36.4, 4.857, 5191.0, 'no');
INSERT INTO bank_marketing (age, job, marital, education, credit_default, housing, loan, contact, month, day_of_week, campaign, pdays, previous, poutcome, emp_var_rate, cons_price_idx, cons_conf_idx, euribor3m, nr_employed, y) VALUES (45, 'services', 'married', 'basic.9y', 'no', 'no', 'no', 'telephone', 'may', 'mon', 1, 999, 0, 'nonexistent', 1.1, 93.994, -36.4, 4.857, 5191.0, 'no');
INSERT INTO bank_marketing (age, job, marital, education, credit_default, housing, loan, contact, month, day_of_week, campaign, pdays, previous, poutcome, emp_var_rate, cons_price_idx, cons_conf_idx, euribor3m, nr_employed, y) VALUES (59, 'admin.', 'married', 'professional.course', 'no', 'no', 'no', 'telephone', 'may', 'mon', 1, 999, 0, 'nonexistent', 1.1, 93.994, -36.4, 4.857, 5191.0, 'no');
INSERT INTO bank_marketing (age, job, marital, education, credit_default, housing, loan, contact, month, day_of_week, campaign, pdays, previous, poutcome, emp_var_rate, cons_price_idx, cons_conf_idx, euribor3m, nr_employed, y) VALUES (41, 'blue-collar', 'married', 'university.degree', 'no', 'no', 'no', 'telephone', 'may', 'mon', 1, 999, 0, 'nonexistent', 1.1, 93.994, -36.4, 4.857, 5191.0, 'no');
INSERT INTO bank_marketing (age, job, marital, education, credit_default, housing, loan, contact, month, day_of_week, campaign, pdays, previous, poutcome, emp_var_rate, cons_price_idx, cons_conf_idx, euribor3m, nr_employed, y) VALUES (24, 'technician', 'single', 'professional.course', 'no', 'yes', 'no', 'telephone', 'may', 'mon', 1, 999, 0, 'nonexistent', 1.1, 93.994, -36.4, 4.857, 5191.0, 'no');
INSERT INTO bank_marketing (age, job, marital, education, credit_default, housing, loan, contact, month, day_of_week, campaign, pdays, previous, poutcome, emp_var_rate, cons_price_idx, cons_conf_idx, euribor3m, nr_employed, y) VALUES (25, 'services', 'single', 'high.school', 'no', 'yes', 'no', 'telephone', 'may', 'mon', 1, 999, 0, 'nonexistent', 1.1, 93.994, -36.4, 4.857, 5191.0, 'no');
SELECT COUNT(*) FROM bank_marketing;
SELECT * FROM bank_marketing LIMIT 10;
