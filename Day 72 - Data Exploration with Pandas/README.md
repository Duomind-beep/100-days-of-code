# 💼 College Major vs. Salary (Data Exploration with Pandas)

This project explores the relationship between **college majors** and **post-university salaries** using a dataset from **PayScale (2008)**. The data spans salaries over the prior 10 years, and was used to practice core **Pandas data analysis techniques** within a **Google Colaboratory** notebook environment.

## 📊 Objective

To apply data exploration and transformation techniques using Pandas, focusing on:
- Cleaning and inspecting real-world datasets
- Extracting meaningful insights from salary data
- Comparing college majors by their salary potential and financial risk

---

## 🧠 What I Learned

- **Loading & Previewing Data**
  - Uploaded and read CSV files using `pandas.read_csv()`
  - Used `.head()`, `.tail()`, and `.shape` to inspect structure

- **Accessing Data**
  - Accessed columns and individual cells
  - Identified and handled missing (`NaN`) values

- **Data Cleaning & Transformation**
  - Sorted values by highest and lowest salaries
  - Added new columns to represent custom metrics, like:
    - **Risk factor** (spread between mid-career 10th and 90th percentile salaries)
    - The smaller the spread, the lower the career risk

- **Analytical Thinking**
  - Interpreted the relationship between financial risk and choice of major
  - Created a “potential vs. stability” comparison using custom metrics

- **Grouping & Pivoting**
  - Grouped data by major categories
  - Counted entries per category to analyze dataset coverage

- **Data Output & Formatting**
  - Cleaned outputs for readability
  - Applied number formatting where necessary

---

## 🗂 Dataset

- Source: [PayScale](https://www.payscale.com/)
- Year: 2008 (10-year lookback)
- Columns include:
  - `Undergraduate Major`
  - `Starting Median Salary`
  - `Mid-Career Median Salary`
  - `Mid-Career 10th Percentile Salary`
  - `Mid-Career 90th Percentile Salary`

---

## 🧪 Tools Used

- **Python**
- **Pandas**
- **Google Colaboratory** (Notebook Environment)

---

## 📌 Key Takeaway

This was an introductory project in exploring structured datasets using Pandas. It helped me understand the tradeoffs between salary potential and financial risk across college majors—and most importantly, it taught me how to use data to support that understanding.

---
