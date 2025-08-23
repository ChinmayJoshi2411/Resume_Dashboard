import streamlit as st

# Page config
st.set_page_config(page_title="Chinmay Joshi - Resume Dashboard", layout="wide")

# Title
st.title("📊 Resume Dashboard - Chinmay Joshi")

# --- Sidebar ---
st.sidebar.title("Navigation")
section = st.sidebar.radio("Go to:", ["About Me", "Experience", "Projects", "Certifications", "Contact"])

# --- About Me ---
if section == "About Me":
    # About Me
    st.markdown("## 👨‍💻 About Me")
    st.write("""
    Hello! I'm **Chinmay Joshi**, a passionate and results-driven **Data Engineer** with over **2.4 years of experience** 
    building scalable data pipelines, automating workflows, and working with **big data technologies**.

    I specialize in designing and maintaining **ETL processes**, ensuring seamless data ingestion, transformation, 
    and integration across diverse systems. My expertise spans across **SQL, Python, PySpark, Airflow, Kafka, Hadoop, Spark, and AWS**, 
    with strong hands-on experience in **data warehousing** and **real-time streaming pipelines**.

    Some highlights of my journey so far:
    - ⚡ Improved data pipeline efficiency by **60%** through automation and optimization.  
    - 📊 Optimized query performance by **20%**, ensuring fast analytics and reporting.  
    - 🔒 Maintained **99.9% system uptime** for large-scale security systems across India.  
    - 🛠 Worked on projects ranging from **Netflix Analytics ETL** to **real-time ingestion with Kafka & Spark on AWS**.  

    Beyond my technical skills, I’m an **adaptable problem solver** who enjoys collaborating with teams, 
    exploring **cloud platforms** (AWS & Azure), and staying up-to-date with modern **data engineering practices**.  
    Currently, I’m also diving deeper into **LLM use cases** and their integration with data engineering.  

    🎵 Outside of my professional world, I am also a **musician** – I love to **sing** and play the **Tabla**, 
    blending rhythm and melody into my creative journey.  

    🌐 I enjoy learning emerging tech, experimenting with automation, and sharing knowledge with peers.  
    """)


# --- Experience ---
elif section == "Experience":
    st.header("💼 Experience")
    st.subheader("Data Engineer - Jio Platforms Ltd (2.8 years)")
    st.write("""
    - Built **scalable ETL pipelines** for security systems across India.  
    - Improved **pipeline efficiency by 60%** and query performance by 20%.  
    - Worked with **Cloudera, Hadoop, Kafka, Spark, Airflow, Docker**.  
    - Ensured **99.9% uptime** with automation for monitoring and ticketing.  
    """)

# --- Projects ---
elif section == "Projects":
    st.header("🚀 Projects")
    st.subheader("Amazon Music ETL Pipeline")
    st.write("""
    - Built an ETL pipeline with **Kafka, Spark, S3, Redshift, Glue, and Airflow**.  
    - Processed streaming data and transformed it into analytics-ready format.  
    """)
    
    st.subheader("Netflix Data Analysis with PySpark & Power BI")
    st.write("""
    - Used **PySpark** for transformations and created an interactive **Power BI dashboard**.  
    - Analyzed global viewing trends and content distribution.  
    """)
    
    st.subheader("College Admission Eligibility Checker")
    st.write("""
    - Developed a **FastAPI-based system** with SQLite, Pandas, NumPy, and Regex.  
    - Implemented robust input validation, logging, and exception handling.  
    """)

# --- Certifications ---
elif section == "Certifications":
    st.header("📜 Certifications")
    
    # IBM Certification
    st.subheader("IBM Data Engineering Professional Certificate")
    st.write("""
    A comprehensive certification consisting of **13 individual courses** and a **combined capstone certificate**.  
    This program covered **Relational Databases, SQL, ETL, Data Warehousing, Big Data, Spark, Airflow, and BI tools**.
    """)
    
    st.markdown("🔗 [View Combined Certificate](https://coursera.org/verify/professional-cert/IZ9BU2H5LC97)")
    
    st.write("### Individual Courses (13 Certificates):")
    cert_links = [
        ("Introduction to Data Engineering", "https://coursera.org/verify/Z7X2UUTTX6PN"),
        ("Python for Data Science, AI & Development", "https://coursera.org/verify/FHE6AWSYE6V4"),
        ("Python Project for Data Engineering", "https://coursera.org/verify/W5AZCBUVVD3X"),
        ("Introduction to Relational Databases (RDBMS)", "https://coursera.org/verify/265SSIZRKIO4"),
        ("Databases and SQL for Data Science with Python", "https://coursera.org/verify/D09621KM4K2O"),
        ("Hands-on Introduction to Linux Commands and Shell Scripting", "https://coursera.org/verify/W5VOW1CRRAU8"),
        ("Relational Database Administration (DBA)", "https://coursera.org/verify/G9WO12ZEOKMM"),
        ("ETL and Data Pipelines with Shell, Airflow and Kafka", "https://coursera.org/verify/8TYRHD7NLLXW"),
        ("Getting Started with Data Warehousing and BI Analytics", "https://coursera.org/verify/22MBVXNTCWNU"),
        ("Introduction to Big Data with Spark and Hadoop", "https://coursera.org/verify/MFDAESEJCXLA"),
        ("Data Engineering and Machine Learning using Spark", "https://coursera.org/verify/FZD5TEQNCPLE"),
        ("Data Engineering Capstone Project", "https://coursera.org/verify/BFGKDX7E3582"),
        ("Data Engineering Professional Certificate (Completion)", "https://coursera.org/verify/L13GKXN0NW8Q"),
    ]
    
    for course, link in cert_links:
        st.markdown(f"- [{course}]({link})")

# --- Contact ---
elif section == "Contact":
    st.header("📬 Contact")
    st.write("""
    - 📧 Email: chinmay.joshi@example.com  
    - 💼 LinkedIn: [linkedin.com/in/chinmayjoshi](https://linkedin.com/in/chinmayjoshi)  
    - 🐙 GitHub: [github.com/ChinmayJoshi2411](https://github.com/ChinmayJoshi2411)  
    """)
