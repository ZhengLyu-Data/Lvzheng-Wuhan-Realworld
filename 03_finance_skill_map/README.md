## 📊 Project 3: Financial Skill Map

This project analyzes and visualizes employee financial skill development data to identify training trends, departmental focus, and skill proficiency. It showcases practical skills in Python (data cleaning), Tableau (data visualization), and project documentation.

---

## 🧾 Dataset

- **File Name:** `cleaned_financial_skills.csv`
- **Fields:**
  - `EmployeeID`: Unique identifier for each employee
  - `Department`: Department of the employee
  - `Skill`: Financial skill learned
  - `TrainingHours`: Time spent learning the skill
  - `ProficiencyLevel`: Self-reported proficiency
  - `LearnedDate`: Date of skill acquisition
---

## 🛠️ Tools Used

| Tool | Purpose |
|------|---------|
| **Google Colab** | Python for data cleaning and feature engineering |
| **Tableau Desktop** | Interactive dashboards and visual storytelling |
| *(Optional)* SQLFiddle | Can be added to demonstrate SQL aggregation skills |

---

## 🧹 Data Cleaning

- Removed duplicates and missing values
- Converted `LearnedDate` to datetime format
- Verified numeric values in `TrainingHours`
- Exported clean data as `cleaned_financial_skills.csv`

---

## 📊 Tableau Visualizations

### 1️⃣ Average Training Hours per Skill

- **Chart Type:** Bar Chart
- **X-axis:** Skill
- **Y-axis:** Average Training Hours
- **Color Encoding:** Based on average hours
- **Insight:** Highlights the most time-intensive skills to learn

### 2️⃣ Training Hours by Department

- **Chart Type:** Stacked Bar Chart
- **X-axis:** Department
- **Y-axis:** Total Training Hours
- **Color:** Skill
- **Insight:** Shows skill distribution across departments

### 3️⃣ Skill Proficiency Distribution

- **Chart Type:** Pie Chart / Donut Chart
- **Segments:** Proficiency Levels (e.g., Beginner, Intermediate, Advanced)
- **Insight:** Illustrates self-reported expertise levels across all staff

### 📋 Dashboard

- Integrated the three charts into one interactive dashboard using **Tableau Desktop**
- **File uploaded:** `financial_skill_map.twbx`
- Download and view in Tableau Desktop
---
## 📁 Project Structure
```
03_financial_skill_map/
├── cleaned_financial_skills.csv         # Clean data file
├── financial_skill_map.twbx             # Tableau dashboard (packaged)
├── Financial Skill Map.twb              # Tableau project file (non-packaged)
├── notebook                             # Python notebook (data cleaning)
└── README.md                            # Project documentation
```
---

## 💬 Notebook Language Notice

> This project uses a file named Notebook.ipynb instead of a specific project-named notebook due to platform constraints.
It was executed and saved using Google Colab.
Please open the notebook in any Jupyter-based environment to view the step-by-step Python analysis.
---

## 🧠 Skills Demonstrated

- Data cleaning and validation using Python
- Tableau visual storytelling and interactivity
- Communication of insights with clean dashboard design
- GitHub-based version control and documentation

---

## 📌 Highlights

✅ Efficient cross-platform workflow (Python + Tableau)  
✅ Visualization-first project for interview storytelling  
✅ Fully reproducible and professional format

---
