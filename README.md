# GAFL_RESTORE_MKM
This is where most of my code for the course would be in0
```markdown
# Cocoa Productivity in Côte d’Ivoire  
**Repository for Jack Jacobs**  

Welcome to the GitHub repo for my semester‐long project on smallholder cocoa productivity. I know it’s not perfectly organized—time ran away from me—but this README should point you to exactly what you need.

---

## 📂 Directory Structure

```

/
├── data/
│   ├── raw/                   ← Original RESTORE survey files
│   └── processed/             ← Cleaned/merged .dta & .csv used in analysis
│       ├── cdi\_household\_clean\_nopii.dta
│       └── ...
│
├── notebooks/                 ← Jupyter notebooks with code & outputs
│   ├── 01\_data\_preparation.ipynb
│   ├── 02\_feature\_engineering.ipynb
│   ├── 07\_feature\_importance.ipynb 
│
└── README.md                   ← You are here

````

---

## 🔑 Key Files & Folders

1. **`data/processed/cdi_household_clean_nopii.dta`**  
   - The cleaned dataset I used throughout.  

2. **`notebooks/06_modified_dataset.ipynb`**  
   - Migrating all important features to a stable CSV file.

2. **`notebooks/07_feature_importance.ipynb`**  
   - Random-Forest screening, selection of top 10 predictors.
   - OLS Regression
   - Spatial analysis 

---

## 🚀 Getting Started

1. **Clone the repo**  
   ```bash
   git clone https://github.com/THEMKM/GAFL_RESTORE_MKM.git
   cd cocoa-productivity-ivoire
````

2. **Environment**

   * Python 3.9
   * Key packages: `pandas`, `scikit-learn`, `statsmodels`, `geopandas`, `matplotlib`

3. **Run the notebooks** in order:

   1. `06_modified_dataset.ipynb`
   2. `07_feature_importance.ipynb`

   All code should run “as-is” on the last commit.

---

## 🤷‍♂️ A Note on Organization

* **Ignore** anything in `data/raw/` beyond the one cleaned file in `processed/`.
* **Focus** on the three notebooks above.
* Other files are intermediate outputs or exploratory drafts—no need to dig into them.

---

## 📞 Questions or Issues

If you hit any errors or can’t find something, please ping me directly:

Mohammed Abobakr
✉️ [mkmx72@upenn.edu](mailto:mkmx72@upenn.edu)

Thanks for reviewing—hope this helps you dive right in!
