# F1-ML-Prediction-Model 

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)]() [![XGBoost](https://img.shields.io/badge/XGBoost-1.7.5-orange.svg)]()

## Description 

This project implements an XGBoost ranking model designed to predict the finishing order of drivers in Formula 1 races. It leverages historical data, including constructor standings, race details, and driver performance metrics, to forecast race outcomes.

## Table of Contents 

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Usage](#usage)
- [How to Use](#how-to-use)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)
- [Footer](#footer)

## Features 

- **XGBoost Ranking Model:** Utilizes XGBoost's `XGBRanker` for effective learning-to-rank. Objectives like `rank:ndcg` and evaluation metrics like `ndcg` are employed for optimizing ranking performance.
- **Data Preprocessing:** Implements a data preprocessing pipeline to clean and transform raw F1 data into a format suitable for the ranking model. This includes merging data from various CSV sources, filtering by year, and creating new features.
- **Feature Engineering:** Generates relevant features such as `team_grid` (average grid position for a constructor in a race) and `skill_diff` (difference between a driver's grid position and their team's average grid position).
- **Model Training and Saving:** Trains the XGBoost model using historical race data and saves the trained model to a JSON file (`f1_ranking_model.json`) for later use.
- **Prediction and Analysis:** Includes a script (`test.py`) to load the trained model, make predictions on new data, and display ranked driver outcomes with predicted scores.

## Tech Stack
- **Languages:** Python
- **Libraries:** pandas, xgboost
- **Data Formats:** CSV, JSON

## Installation 

1. **Clone the repository:**
   ```bash
   git clone https://github.com/ZackPot/F1-ML-Prediction-Model.git
   cd F1-ML-Prediction-Model
   ```

2. **Install dependencies:**
   This project relies on `pandas` and `xgboost`. You can install them using pip:
   ```bash
   pip install pandas xgboost
   ```

## Usage 

This project can be used to train a model that predicts F1 race finishing orders and to make predictions on new race data.

**1. Data Preprocessing:**
   Run the `preprocessing.py` script to generate the `final_data.csv` file from the raw data sources.
   ```bash
   python preprocessing.py
   ```

**2. Model Training:**
   Execute `main.py` to train the XGBoost ranking model using the preprocessed data and save the model.
   ```bash
   python main.py
   ```
   This will create `f1_ranking_model.json` containing the trained model.

**3. Making Predictions:**
   Use the `test.py` script to load the trained model and predict driver rankings for a sample race scenario.
   ```bash
   python test.py
   ```
   The output will show a ranked list of drivers with their predicted scores.

## How to Use 

This model is designed for predicting the relative ranking of drivers within a Formula 1 race. By feeding in relevant features for drivers in a specific race (e.g., their grid position, constructor, historical points, team's average grid position), the model outputs a score indicating their likely finishing order. This can be valuable for fantasy sports, performance analysis, or simply exploring predictive capabilities in motorsport.

**Example Scenario:**

The `test.py` script provides a practical example. It simulates a race scenario with driver data from silverstone 2026 and uses the trained `f1_ranking_model.json` to predict the outcome. The output is a sorted list of drivers based on their predicted performance scores.

## Project Structure 

```
F1-ML-Prediction-Model/
├── .idea/
│   ├── F1RankingModel.iml
│   ├── inspectionProfiles/
│   │   ├── Project_Default.xml
│   │   └── profiles_settings.xml
│   ├── misc.xml
│   ├── modules.xml
│   └── vcs.xml
├── RawData/
│   ├── constructor_standings.csv
│   └── races.csv
├── f1_ranking_model.json
├── final_data.csv
├── main.py
├── preprocessing.py
├── README.md
└── test.py
```

## Contributing

Contributions are welcome! Please feel free to:

- Fork the repository.
- Submit pull requests.
- Open issues for bug reports or feature requests.

## License 

MIT License

## Footer

**F1-ML-Prediction-Model**

[![GitHub Repo Stars](https://img.shields.io/github/stars/ZackPot/F1-ML-Prediction-Model?style=social)]() [![GitHub Forks](https://img.shields.io/github/forks/ZackPot/F1-ML-Prediction-Model?style=social)]()
