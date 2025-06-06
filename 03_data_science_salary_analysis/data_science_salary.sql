-- Create table for raw data
CREATE TABLE data_science_salaries_raw (
    work_year INTEGER,
    experience_level TEXT,
    employment_type TEXT,
    job_title TEXT,
    salary_in_usd INTEGER,
    employee_residence TEXT,
    remote_ratio INTEGER,
    company_location TEXT,
    company_size TEXT
);

-- Insert sample data (5 records)
INSERT INTO data_science_salaries_raw VALUES
(2020, 'SE', 'FT', 'Data Scientist', 80000, 'US', 100, 'US', 'L'),
(2021, 'MI', 'FT', 'Data Engineer', 72000, 'GB', 50, 'GB', 'M'),
(2022, 'EN', 'FT', 'Data Analyst', 60000, 'IN', 0, 'IN', 'S'),
(2023, 'EX', 'CT', 'ML Engineer', 150000, 'CA', 100, 'CA', 'L'),
(2021, 'SE', 'FT', 'Data Scientist', 85000, 'US', 50, 'US', 'M');

-- Clean and transform raw data into a new table
CREATE TABLE data_science_salaries_cleaned AS
SELECT
    work_year AS Year,
    CASE experience_level
        WHEN 'EN' THEN 'Entry'
        WHEN 'MI' THEN 'Mid'
        WHEN 'SE' THEN 'Senior'
        WHEN 'EX' THEN 'Executive'
        ELSE experience_level
    END AS Experience_Level,
    employment_type AS Employment_Type,
    job_title AS Job_Title,
    salary_in_usd AS Salary_USD,
    employee_residence AS Employee_Residence,
    remote_ratio AS Remote_Ratio,
    company_location AS Company_Location,
    company_size AS Company_Size
FROM data_science_salaries_raw;

-- View cleaned data
SELECT * FROM data_science_salaries_cleaned;
