# 📊 DataFuse – CSV & Excel Merger App

## 📘 Project Overview
**DataFuse** is a Streamlit-based web application that allows users to upload multiple CSV and Excel files and seamlessly merge them into a single dataset.  
It intelligently **aligns column headers**, handles missing or extra columns, and consolidates data into a clean output file — all without requiring any coding.  

This tool is especially useful for working with large, fragmented datasets (such as reports from different years or systems) and combining them into one structured file for analysis.

---

## 🧩 Libraries Used
- **streamlit** – for building the interactive web interface  
- **pandas** – for data manipulation, cleaning, and merging  
- **openpyxl** – for reading Excel files (`.xlsx`)  

---

## 🔍 Key Features
- Upload multiple files (`.csv` and `.xlsx`) at once  
- Automatically normalizes and aligns column headers  
- Supports Excel files with multiple sheets  
- Handles missing and extra columns across files  
- Adds file and sheet tracking for traceability  
- Provides preview of merged data  
- One-click download as `merged-output.csv`  

---

## 🚀 How It Works
1. Upload your CSV and/or Excel files  
2. Click **Merge Files**  
3. DataFuse processes and aligns all columns  
4. Preview the merged dataset  
5. Download the final combined file  

---

## 🎯 Use Cases
- Merging yearly reports (e.g., FY22–FY25 data)  
- Combining SAP exports (IW68 / IW28 reports)  
- Consolidating datasets from multiple sources  
- Preparing data for analysis, dashboards, or machine learning  

---
