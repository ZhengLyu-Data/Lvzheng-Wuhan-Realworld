-- 1️⃣ Drop existing tables
DROP TABLE IF EXISTS job_postings;
DROP TABLE IF EXISTS job_skills;

-- 2️⃣ Create job_postings table
CREATE TABLE job_postings (
    job_link TEXT,
    job_title TEXT,
    company TEXT,
    job_location TEXT,
    search_country TEXT,
    job_level TEXT,
    job_type TEXT
);

-- 3️⃣ Create job_skills table
CREATE TABLE job_skills (
    job_link TEXT,
    skill TEXT
);

-- 4️⃣ Insert sample data (for demo purposes)
INSERT INTO job_postings VALUES 
('link001', 'Data Analyst', 'Company A', 'Austin, TX', 'USA', 'Entry', 'Remote'),
('link002', 'Data Scientist', 'Company B', 'Toronto, ON', 'Canada', 'Mid', 'Hybrid'),
('link003', 'ML Engineer', 'Company C', 'Remote', 'USA', 'Senior', 'Remote');

INSERT INTO job_skills VALUES 
('link001', 'Python'),
('link001', 'SQL'),
('link002', 'Machine Learning'),
('link002', 'R'),
('link003', 'Python'),
('link003', 'Deep Learning');

-- 5️⃣ Table 1: Skill Frequency
SELECT skill, COUNT(*) AS frequency
FROM job_skills
GROUP BY skill
ORDER BY frequency DESC;

-- 6️⃣ Table 2: Top Hiring Companies
SELECT company, COUNT(*) AS job_postings
FROM job_postings
GROUP BY company
ORDER BY job_postings DESC;

-- 7️⃣ Table 3: Job Count by State
SELECT
  SUBSTR(job_location, -2) AS state,
  COUNT(*) AS job_count
FROM job_postings
WHERE LENGTH(job_location) >= 2
GROUP BY state
ORDER BY job_count DESC;

-- 8️⃣ Table 4: Job Level vs Job Type
SELECT job_level, job_type, COUNT(*) AS count
FROM job_postings
GROUP BY job_level, job_type
ORDER BY job_level, job_type;

-- 9️⃣ Table 5: Skill Frequency by Country
SELECT jp.search_country, js.skill, COUNT(*) AS count
FROM job_postings jp
JOIN job_skills js ON jp.job_link = js.job_link
GROUP BY jp.search_country, js.skill
ORDER BY count DESC;

-- 🔟 Table 6: Company + Job Title Summary
SELECT company, job_title, COUNT(*) AS postings
FROM job_postings
GROUP BY company, job_title
ORDER BY postings DESC;
