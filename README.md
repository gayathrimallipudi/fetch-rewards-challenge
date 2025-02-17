cat <<EOF > README.md
# Fetch Rewards Receipt Processor API

## 🚀 Overview
This FastAPI service processes receipts and calculates reward points based on predefined rules.

## 📌 Features
- Submit receipts via \`POST /receipts/process\`
- Retrieve points via \`GET /receipts/{id}/points\`
- Dockerized for easy deployment
- Includes automated tests with \`pytest\`

## 🛠️ Setup Instructions

### **1️⃣ Run Locally**
1. **Clone the repository**:
   \`\`\`bash
   git clone https://github.com/YOUR_USERNAME/fetch-rewards-challenge.git
   cd fetch-rewards-challenge
   \`\`\`
2. **Create and activate a virtual environment (Optional but recommended)**:
   \`\`\`bash
   python -m venv env
   source env/bin/activate  # For Mac/Linux
   \`\`\`
3. **Install dependencies**:
   \`\`\`bash
   pip install fastapi uvicorn pydantic pytest httpx   
   \`\`\`
4. **Start the API**:
   \`\`\`bash
   uvicorn app.main:app --reload
   \`\`\`
5. **Open API Docs**:
   \`\`\`
   http://127.0.0.1:8000/docs
   \`\`\`

### **2️⃣ Run with Docker**
1. **Build the Docker image**:
   \`\`\`bash
   docker build -t fetch-rewards-api .
   \`\`\`
2. **Run the container**:
   \`\`\`bash
   docker run -p 8000:8000 fetch-rewards-api
   \`\`\`
3. **Test the API in Swagger UI**:
   \`\`\`
   http://127.0.0.1:8000/docs
   \`\`\`

### **3️⃣ Running Automated Tests**
- Run locally:
  \`\`\`bash
  pytest tests/ -v
  \`\`\`
- Run inside Docker:
  \`\`\`bash
  docker run fetch-rewards-api pytest tests/
  \`\`\`


EOF
