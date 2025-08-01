# Spooky Books Author Identification - EDA & Baseline

Kaggle Playground Competition (2025): Predict the author of horror story excerpts  
**Authors:** Edgar Allan Poe (`EAP`), H.P. Lovecraft (`HPL`), Mary Shelley (`MWS`)

---

## 📓 Project Overview

This repository contains an interactive exploratory data analysis (EDA) notebook for the [Kaggle Spooky Books competition](https://www.kaggle.com/c/spooky-author-identification), along with the first steps towards building a classification model.

**Goal:**  
Given excerpts of horror texts, predict which of the three classic authors wrote each passage.

---

## 🗂️ Files

- `new.ipynb` — Main notebook: EDA, visualizations, feature engineering.
- `data/train/train.csv` — Training dataset (not included; download from Kaggle).

---

## 🚀 Workflow Summary

### Data Exploration (EDA)

- **Wordclouds per author:**  
  Visualize the most common words for each author to identify stylistic patterns.
- **Text length analysis:**  
  Distribution of text lengths per author using boxplots.
- **Punctuation frequency:**  
  Compare the number of punctuation marks in excerpts per author.
- **Top words per author:**  
  Identify and plot the most frequent words (excluding stopwords) for each author.

### Feature Engineering

- Add features such as:
    - Text length
    - Punctuation count
    - Most frequent words

---

## 🛠️ Requirements

- Python 3.8+
- pandas
- matplotlib
- seaborn
- wordcloud
- scikit-learn

**Install requirements:**
```bash
pip install pandas matplotlib seaborn wordcloud scikit-learn
```
---

## 📈 How to Use
- Clone the repository.
- Download the Kaggle dataset and place train.csv in data/train/.
- Open and run new.ipynb in Jupyter or VSCode.
- Explore the visualizations to gain insights into the data.
- Extend with your own models for the competition!

---

## 📝 Submission Instructions
For Kaggle submission, output a CSV with the format:
```bash
id,EAP,HPL,MWS
id07943,0.33,0.33,0.33
```
Each row must include probabilities for all three authors.
