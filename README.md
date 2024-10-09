# Depreciation-Method-Based-on-Perceived-Information-Asymmetry
This repository contains the source code and data from the study "Depreciation Method Based on Perceived Information Asymmetry: A Case of Electric Vehicles in Colombia." It includes depreciation analysis using traditional models and a new approach based on data from e-commerce platforms.

## Methodology
### Execution of the scraping.py script:
The process begins by running the scraping.py script, which is designed to extract data from various e-commerce platforms. This script scrapes electric vehicle information, capturing key data such as brand, model, price, year of manufacture, mileage, among others. The output is a CSV file named PREPRODUCTOS.csv, which contains all the raw, unprocessed data.

### Initial data cleaning and classification process:
After obtaining PREPRODUCTOS.csv, the first level of data cleaning and classification is performed, removing inconsistencies and normalizing certain fields. This process is manual, as it requires a thorough review of the information to identify incomplete or incorrect data. The initial cleaning also includes classifying by vehicle type, year, and other relevant variables. The result of this stage is a hybrid file between a spreadsheet and a CSV file, saved as PREPRODUCTOS.csv.xlsx, facilitating the manipulation of data in both CSV and Excel formats.

### Second level of data cleaning and refinement:
From the file PREPRODUCTOS.csv.xlsx, a second level of more detailed cleaning is conducted, also manually, where the data’s coherence and completeness are further refined. This stage ensures that residual errors are corrected and missing values are filled with reliable data. The final result of this phase is a cleaned and ready-to-analyze file named Datos_Completos VE(csv).xlsx.

### Defining the context window and advanced preprocessing:
To ensure a contextualized and precise analysis, a temporal window from 2019 to 2024 is defined, focusing on the most relevant electric vehicle models in this period. At this stage, a third level of preprocessing is performed, including the application of advanced data treatment techniques, such as trend analysis and the classification of vehicles based on their depreciation, using the Sum-of-Years Digits (SYD) method. The result is a processed file named Datos_Modificados VE(SYD).xlsx, which serves as the base or "target data" used for the analysis in the article.
