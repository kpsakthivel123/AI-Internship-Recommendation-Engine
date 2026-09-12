import pandas as pd
import streamlit as st

st.set_page_config(page_title="AI Recommendation Engine", page_icon="🎯", layout="wide")

st.title("🎯 AI Recommendation Engine")
st.write("Get personalized internship, project, and learning resource recommendations based on your skills and interests.")

@st.cache_data
def load_data():
    internships = pd.read_csv("data/internships.csv")
    projects = pd.read_csv("data/projects.csv")
    resources = pd.read_csv("data/resources.csv")
    return internships, projects, resources

def score_item(item, skills, interest, level):
    item_skills = {s.strip().lower() for s in str(item["skills"]).split(",")}
    user_skills = {s.strip().lower() for s in skills}
    skill_score = len(item_skills.intersection(user_skills))
    interest_score = 2 if interest.lower() in str(item["interest"]).lower() else 0
    level_score = 1 if level.lower() == str(item["level"]).lower() else 0
    return skill_score * 3 + interest_score + level_score

def recommend(df, skills, interest, level):
    result = df.copy()
    result["score"] = result.apply(lambda row: score_item(row, skills, interest, level), axis=1)
    return result.sort_values("score", ascending=False).head(5)

internships, projects, resources = load_data()

st.sidebar.header("Student Profile")
skills_text = st.sidebar.text_input("Skills", "Python, Machine Learning")
interest = st.sidebar.selectbox("Interest", ["AI", "Data Science", "Web Development", "Cyber Security"])
level = st.sidebar.selectbox("Level", ["Beginner", "Intermediate", "Advanced"])

skills = [x.strip() for x in skills_text.split(",") if x.strip()]

if st.button("🚀 Get Recommendations", type="primary"):
    tab1, tab2, tab3 = st.tabs(["💼 Internships", "🛠️ Projects", "📚 Learning Resources"])

    with tab1:
        rec = recommend(internships, skills, interest, level)
        st.dataframe(rec[["title", "company", "interest", "level", "skills", "description", "score"]], use_container_width=True, hide_index=True)

    with tab2:
        rec = recommend(projects, skills, interest, level)
        st.dataframe(rec[["title", "interest", "level", "skills", "description", "score"]], use_container_width=True, hide_index=True)

    with tab3:
        rec = recommend(resources, skills, interest, level)
        st.dataframe(rec[["title", "platform", "interest", "level", "skills", "description", "score"]], use_container_width=True, hide_index=True)

st.info("This version works offline because all recommendation data is stored locally in CSV files.")
