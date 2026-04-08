🚀 Book Management API Automation (Python)

📌 Overview

This project is an end-to-end API automation framework built using Python Requests to validate RESTful services. It focuses on testing book management workflows, including creating and deleting books via API endpoints.

The framework demonstrates real-world API testing practices, including configuration handling, data-driven testing, and response validation.
```
🛠️ Tech Stack
Python
Requests Library
MySQL (for test data handling)
ConfigParser (for environment configuration)
🎯 Features
✅ End-to-End API testing (Create → Validate → Delete)
✅ Data-driven testing using MySQL
✅ External configuration using .ini file
✅ Modular and reusable utility functions
✅ Clean project structure for scalability
📂 Project Structure
Book-Management-API-Tests/
│
├── API_MySql_E2E.py        # Main E2E test script
├── Utilities/
│   ├── configuaration.ini # Config file (base URL, DB details)
│   ├── requirements.py    # Helper functions
│   └── __init__.py
│
├── __init__.py
```
🔄 Test Workflow
```
Connect to MySQL database
Fetch test data
Send API request to Add Book
Validate response
Send API request to Delete Book
Verify successful deletion
```
⚙️ Configuration

All environment details are stored in:

Utilities/configuaration.ini
```
Example:

[API]
base_url = http://example.com

[DB]
host = localhost
database = APIDevelop
user = root
password = root
```
```
▶️ How to Run
1️⃣ Clone the repository
git clone https://github.com/avinashu199/Book-Management-API-Tests.git
cd Book-Management-API-Tests
2️⃣ Install dependencies
pip install requests mysql-connector-python
3️⃣ Run the script
python API_MySql_E2E.py
📊 Sample API Flow
POST → Add Book
GET/Response Validation
DELETE → Remove Book
```
🔐 Key Learnings

API automation using Python Requests
Handling database-driven test data
Structuring a scalable test framework
Managing configs using configparser
🚀 Future Enhancements
Add Pytest framework
Implement logging & reporting
Add CI/CD integration (GitHub Actions)
Add more CRUD test coverage

👨‍💻 Author

Avinash Uppalapati

⭐ If you like this project

Give it a ⭐ on GitHub!
