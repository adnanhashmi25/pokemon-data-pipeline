# Pokémon Data Pipeline  

🚀 **Overview:**  
This project is an **Apache Airflow ETL pipeline** that extracts Pokémon data from an API, processes it, and stores it in CSV format. The pipeline is designed for **scalability** and can be run **locally or inside a Docker container** using Airflow.  

🔒 **Note:**  
- **API Source:** Pokémon data is fetched from the [PokeAPI](https://pokeapi.co/).  
- **Storage:** The processed data is saved as a CSV file.  
- **Deployment:** The pipeline can be run **locally** or via **Docker + Airflow**.  

---

## 📌 Installation & Setup  

### 1️⃣ Prerequisites  
Ensure you have the following installed:  
- **Python 3.11**  
- **Apache Airflow** (for local execution)  
- **Docker & Docker Compose** (for containerized execution)  

### **💻 Running the Pipeline Locally**  
#### **2️⃣ Clone the Repository**  
git clone https://github.com/adnanhashmi25/pokemon-data-pipeline.git
cd pokemon-data-pipeline

#### 3️⃣ Install Dependencies
pip install -r requirements.txt

#### 4️⃣ Start Airflow & Trigger the DAG
airflow standalone
Open Airflow UI at http://localhost:8080
Enable & trigger the Pokémon Data Pipeline DAG
### 🐳 Running the Pipeline with Docker
#### 2️⃣ Set Up Docker & Airflow
cd docker
docker-compose up -d

#### 3️⃣ Access Airflow UI
Open: http://localhost:8080
Login: airflow / airflow

#### 4️⃣ Run the Pipeline
Go to DAGs section
Enable & trigger pokemon_data_pipeline

### 📈 Features
✔ Extracts Pokémon data via API
✔ Processes & stores data in CSV format
✔ Designed for local & Docker-based execution
✔ Automated scheduling via Apache Airflow

### 📜 Detailed Documentation
For a full project breakdown, visit the docs folder.
 - Project Summary
