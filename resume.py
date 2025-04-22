import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime
import math

# Page configuration
st.set_page_config(page_title="Chinmay Joshi - Interactive Resume", layout="wide")

# Header
st.title("🧐 Chinmay Joshi - Data Engineer")

# Calculate dynamic experience duration
joining_date = datetime(2022, 12, 20)
today = datetime.today()
duration_years = (today - joining_date).days / 365.25
rounded_duration = math.ceil(duration_years * 10) / 10  # round up to next nearest decimal
formatted_duration = f"{rounded_duration:.1f} years"

st.write(f"Results-driven Data Engineer with {formatted_duration} of experience at Jio Platforms Ltd., specializing in data pipeline development, ETL workflows, and real-time data processing. Proficient in SQL, Python, PySpark, Apache Airflow, and Spark, with a strong focus on optimizing data workflows for efficiency and reliability. Successfully improved pipeline efficiency by 60%, enhanced query performance by 20%, and ensured 99.9% uptime. Currently pursuing Microsoft Azure Cloud Fundamentals to strengthen expertise in cloud-based data solutions.")

# Sidebar with contact details
st.sidebar.header("📬 Contact")
st.sidebar.write("📧 Email: chinmaytj241100@gmail.com")
st.sidebar.write("🔗 [LinkedIn](https://www.linkedin.com/in/chinmay-joshi-7495741b1/)")
st.sidebar.write("📁 [GitHub](https://github.com/ChinmayJoshi2411)")

# Experience Section
st.subheader("💼 Work Experience")
experience = pd.DataFrame({
    "Role": ["Data Engineer"],
    "Company": ["Jio Platforms Ltd"],
    "Duration": [formatted_duration],
    "Technologies Used": ["Python, SQL, PySpark, Apache Airflow, Kafka"]
})
st.table(experience)

# Skills Section
st.subheader("🛠️ Skills")
skills = pd.DataFrame({
    "Skills": ["Python", "SQL", "PySpark", "Apache Airflow", "ETL", "Data Warehousing", "Kafka"],
    "Proficiency": [90, 85, 75, 80, 85, 70, 65]
})
fig_skills = px.bar(skills, x="Skills", y="Proficiency", text_auto=True, title="Skill Proficiency")
st.plotly_chart(fig_skills, use_container_width=True)

# Certifications
st.subheader("📜 Certifications")
st.write("✔️ Microsoft Azure Fundamentals (In Progress)")
st.write("✔️ IBM Data Engineering Professional Certificate")

# Projects Section
st.subheader("🚀 Projects")

st.markdown("""
#### 🔹 Netflix Dataset Analysis  
Analyzed global content trends on Netflix using PySpark. Built an interactive dashboard in Power BI showcasing insights like content type distribution, country-wise availability, and genre trends. SQLite was used for structured data storage.

**Technologies Used**: PySpark, Power BI, SQLite  
**Skills Demonstrated**: Data cleaning, transformation, visualization, analytical storytelling.

---

#### 🔹 Real-time Weather ETL Pipeline  
Implemented a real-time ETL pipeline using the OpenWeather API. Ingested historical and current weather data, transformed it using Spark, and stored it in SQLite for downstream analysis.

**Technologies Used**: OpenWeather API, Spark, SQLite  
**Skills Demonstrated**: Real-time ingestion, REST API interaction, ETL orchestration.

---

#### 🔹 Kafka-based Real-time Streaming Pipeline  
Created a secure streaming data pipeline using Apache Kafka with SSL/TLS encryption. Ensured reliable data ingestion and transformation for multiple sources in a real-time environment.

**Technologies Used**: Apache Kafka, SSL/TLS, Python  
**Skills Demonstrated**: Secure data streaming, message broker setup, real-time processing.

---

#### 🔹 Automated ETL Pipeline with Apache Airflow  
Developed and automated an end-to-end ETL pipeline using Apache Airflow. Included retry logic, error handling, and email alerts. Scheduled jobs processed large-scale data sets daily with performance monitoring.

**Technologies Used**: Apache Airflow, Python, Bash  
**Skills Demonstrated**: Workflow automation, DAG design, error handling, scheduling.

---

#### 🔹 Consumer Analytics ETL Project  
Built a star schema-based data warehouse for a consumer electronics retail company. Created dimension and fact tables in PostgreSQL and optimized query performance using materialized views.

**Technologies Used**: PostgreSQL, Data Warehousing, SQL  
**Skills Demonstrated**: Schema design, query optimization, analytics readiness.
""")

# Education
st.subheader("🎓 Education")
st.write("Bachelor of Engineering in Computer Science (79.01%, CGPA 8.35) - RTM University, Nagpur")

# Footer
st.write("---")
st.write("🔹 *Interactive resume built using Streamlit* 🔹")
