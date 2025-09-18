## IMDB Movie Analysis
IMDB Movie Analysis is a Python-based project that analyzes and visualizes movie data from IMDB. Users can explore movie trends, ratings, genres, and releases interactively via a Flask web app.
![Python](https://img.shields.io/badge/Python-3.11-blue?style=flat-square) 
![Flask](https://img.shields.io/badge/Flask-2.3-lightgrey?style=flat-square) 
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

##
## Features
- Clean and preprocess IMDB movie dataset
- Analyze movies by year, genre, rating, and decade
- Visualize trends using Matplotlib, Seaborn, and Plotly
- Interactive filters in the Flask web app
## Tech Stack
- Backend: Python, Flask, Pandas, NumPy
- Data Visualization: Matplotlib, Seaborn, Plotly
- Frontend: HTML, CSS, Bootstrap
## Installation

1. Clone the repository:
```bash
git clone https://github.com/Vaibhav-Tez-Shakya/IMDB-Movie-Data-Analysis
cd IMDB-Movie-Analysis
```
2. Create a Virtual Environment
   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/macOS
   venv\Scripts\activate      # Windows
3. Install Dependencies
   ```bash
   pip install -r requirements.txt
4. Run the App
   ```bash
   python App.py

---

## **Step 8: Add Project Structure**
- Show folder organization to make it easy for developers to understand:
```markdown
## Project Structure
IMDB-Movie-Analysis/
│
├─ App.py                 # Main Flask application
├─ movies.csv             # IMDB dataset
├─ templates/             # HTML templates
├─ static/                # CSS, JS, images
├─ plots/                 # Generated visualizations
├─ screenshots/           # Screenshots for README
├─ requirements.txt       # Dependencies
└─ README.md              # Documentation
```
## How It Works
1. Data Preprocessing: Clean dataset and calculate decades
2. Data Analysis & Visualization: Generate charts for ratings, genres, and decades
3. Flask App: Serve data to HTML templates with interactive filters


Conclusion

The IMDB Movie Analysis project demonstrates how Python, data visualization libraries, and web frameworks like Flask can be combined to analyze and present real-world datasets interactively.
It allows users to explore trends in movie releases, genres, and ratings over time, providing actionable insights from raw data.

This project also serves as a foundation for further enhancements, such as adding user authentication, sentiment analysis on reviews, or deploying the app online for public access.

By completing this project, one gains hands-on experience in data preprocessing, visualization, and web development, making it a valuable addition to any portfolio.
