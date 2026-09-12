# AI Recommendation Engine

## Project Title
AI Recommendation Engine for Internships, Projects, and Learning Resources

## Task Details
Task ID: AI-SS-002
Student Code: DAS009638
Task: AI Internship Recommendation Engine – AI-SS-002

## GitHub Repository
https://github.com/kpsakthivel123/AI-Internship-Recommendation-Engine

## Objective
Create a simple AI-powered recommendation system that suggests suitable internships, projects, and learning resources based on a student's skills, interests, and learning level.

## Features
- Student skill input
- Interest selection
- Beginner/Intermediate/Advanced level
- Internship recommendations
- Project recommendations
- Learning resource recommendations
- Simple scoring-based recommendation algorithm
- Offline operation using local CSV datasets
- Streamlit web interface

## Technologies
- Python
- Pandas
- Streamlit
- CSV

## Project Structure

recommendation_engine/
├── app.py
├── requirements.txt
├── README.md
└── data/
    ├── internships.csv
    ├── projects.csv
    └── resources.csv

## How to Run

### 1. Install Python
Use Python 3.9 or newer.

### 2. Install dependencies

pip install -r requirements.txt

### 3. Start the application

streamlit run app.py

### 4. Open the local URL

Streamlit will show a local address such as:

http://localhost:8501

## How the Recommendation Works

The system compares the student's skills with the skills required by each item.

### Scoring

- Matching skill = 3 points
- Matching interest = 2 points
- Matching level = 1 point

Items are sorted by score, and the top 5 recommendations are displayed.

## Internet Requirement

Internet is NOT required while running the project if the CSV files are stored locally.

Internet is required only if you later connect the system to live internship websites, online APIs, or external learning platforms.

## Example Input

Skills: Python, Machine Learning
Interest: AI
Level: Beginner

## Expected Output

The application displays the most relevant internships, projects, and learning resources.

## Future Improvements

- Machine learning recommendation model
- User login and profiles
- Database integration
- Real-time internship APIs
- Recommendation history
- More advanced NLP/semantic matching
