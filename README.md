# 🌍 Quality-of-life-2025

**Data analysis and visualization of Top‑20 cities by Quality of Life, Safety, and Health Care indexes (2025).**

---

## 📂 Project Structure
```
quality-of-life-2025/
├── data/
│ └── quality_of_life_2025.html      # Original HTML exported from Numbeo
├── quality_of_life_2025.ipynb       # Jupyter Notebook with full analysis
├── quality_of_life_2025.csv         # Cleaned dataset in CSV format
├── images/
│ ├── top_20_indexes_2025.png        # Final charts in PNG format
│ └── top_20_indexes_2025.svg        # Final charts in SVG format
└── README.md                        # Project documentation and overview
```
---

## 📖 Introduction

This mini-project analyzes the quality of life in major world cities for 2025.

To ensure geographic diversity, I selected the Top-20 cities, avoiding dominance by any single country.

The data was sourced from Numbeo. Since the table couldn’t be extracted via `requests`, I manually saved the HTML page and parsed it using `BeautifulSoup`.

From the full dataset, I focused on **three key indexes** for visualization:
- Quality of Life Index  
- Safety Index  
- Health Care Index  

These metrics best reflect overall comfort, security, and access to medical care.

---

## 🎯 Project Goal

***Project Goal*** — extract 2025 quality-of-life data for cities worldwide from an HTML document using web scraping, transform it with **pandas**, and visualize the **Top 20 cities**.

This project serves as practical training in **web scraping**, **data processing**, and **data visualization using Python**.

---

## 💼 Skills & Tools

- `Python`: core programming language  
- `pandas`: data transformation and cleaning  
- `BeautifulSoup`: HTML parsing and extraction  
- `matplotlib`: charting and visualization  
- `Jupyter Notebook`: interactive coding environment  
- `Git & GitHub`: version control and public repository hosting

---

## 🔗 Data Source  
The dataset was taken from:  
🌐 [https://www.numbeo.com/quality-of-life/rankings.jsp?title=2025](https://www.numbeo.com/quality-of-life/rankings.jsp?title=2025)

The table was saved manually and parsed from the local HTML file using BeautifulSoup.  
📄 [View local HTML file (`quality_of_life_2025.html`)](https://github.com/CloudDataPalina/quality-of-life-2025/blob/main/data/quality_of_life_2025.html)

---

## 📊 Visualizations

The project includes three horizontal bar charts:
- Top 20 cities by **Quality of Life**
- Top 20 cities by **Safety**
- Top 20 cities by **Health Care**

All charts were saved in both `.png` and `.svg` formats for presentation and scalable usage.

---

## 💾 Output Files

- [`quality_of_life_2025.csv`](./quality_of_life_2025.csv) — cleaned dataset ready for analysis
- [`top_20_indexes_2025.png`](./images/top_20_indexes_2025.png) — high-resolution image for reports or presentations
- [`top_20_indexes_2025.svg`](./images/top_20_indexes_2025.svg) — vector version for web or print use

---

## ✅ Summary

- Parsed a local HTML file using BeautifulSoup  
- Converted the extracted data into a pandas DataFrame  
- Analyzed the data and built three visualizations using matplotlib  
- Saved the results in CSV, PNG, and SVG formats

---

## 📌 Insights

- **The Netherlands** stands out as a consistent top performer across all indexes  
- **The Hague (Netherlands)** ranks in the Top-3 both for Quality of Life and Health Care — highlighting its strong overall appeal and balance  
- **Middle Eastern cities** rank high in safety but not in quality of life  
- **Taiwan and South Korea** lead in health care  
- Quality of life is a multi-factor concept — high safety doesn’t always mean high comfort

---

## 👩‍💻 Author

**Palina Krasiuk**  
Aspiring Cloud Data Engineer | ex-Senior Accountant  
[LinkedIn](https://www.linkedin.com/in/palina-krasiuk-954404372/) • [GitHub Portfolio](https://github.com/CloudDataPalina)
