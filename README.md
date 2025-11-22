# DAB111 Final Project – Group Web Page

This project showcases our group’s work for the DAB111 course. It includes a Flask-based web application, organized folder structure, and a professional presentation of our team and project goals.

---

## 📁 Project Structure

```text
DAB111_Final_Project/
├── data/               # Raw datasets (CSV, Excel, JSON)
├── notebooks/          # Jupyter notebooks for analysis
├── static/             # CSS, JS, images for web app
├── templates/          # HTML templates rendered by Flask
├── src/                # Flask app logic, data scripts, helpers
│   ├── app.py
│   ├── routes.py
│   ├── clean_data.py
│   └── helpers.py
├── requirements.txt    # Python dependencies
└── README.md           # Project overview and instructions
data: Store raw datasets like CSV, Excel, or JSON.

notebooks: Jupyter notebooks for EDA, visualization, and prototyping.

static: Front-end assets (CSS, JavaScript, images).

templates: HTML templates rendered by Flask (index.html, dashboard.html).

src: Core code for the app and data processing.

requirements.txt: Reproducible environment dependencies.

README.md: Project overview and collaboration guide.

This structure made collaboration easier and ensured our instructor could navigate the project quickly.
---

🛠️ How We Built the Project
1. Setting up the environment We began by creating a virtual environment to isolate our dependencies. This ensured that everyone on the team could work with the same versions of Python packages.
**Activate virtual environment**  
   ```bash
   source .venv/Scripts/activate
   pip install -r requirements.txt
   python app.py
   python -m venv .venv


2. Installing dependencies Once the environment was active, we installed all required packages using requirements.txt. This included Flask for the web app and pandas for data analysis.
pip install -r requirements.txt

3. Organizing the folder structure To keep the project clean and professional, we agreed on a standardized folder layout:

data/ for raw datasets (CSV, Excel, JSON)

notebooks/ for Jupyter notebooks used in analysis

static/ for CSS, JavaScript, and images

templates/ for HTML files rendered by Flask

4. Developing the Flask app We wrote the main application logic in src/app.py. Routes were defined in routes.py, while data cleaning and helper functions were separated into their own scripts for clarity. This modular approach allowed us to troubleshoot and update individual components without breaking the whole app.

5. Running and testing the app With everything in place, we launched the Flask server:
python src/app.py

6. We then opened the app in the browser at http://127.0.0.1:5000/ to test the homepage and dashboard. Each team member verified that the templates rendered correctly and that the static files (CSS) were loading as expected.
## Accessing the Website

Before running the project locally, make sure you have Python installed. Then:

Create and activate a virtual environment (this will be on your own machine):
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # Mac/Linux
   .venv\Scripts\activate      # Windows
Install the required packages:

bash
pip install -r requirements.txt
Start the Flask server:

bash
flask run
Open your browser and go to: http://127.0.0.1:5000/

This will run the project locally using your own environment, but with the code cloned from this repository. The homepage and dashboard should render correctly, with templates and static files (CSS) loading as expected.

7. Final polish and documentation After confirming functionality, we updated the README.md to include instructions for setup, running the app, and troubleshooting. We also added a section for team members and project notes to highlight our collaborative effort.


Notes:
We emphasized clarity and reproducibility throughout the project.

Documentation was treated as seriously as the code itself, ensuring future users can replicate our work.

Git was used for version control, with commits kept concise and descriptive to track progress transparently.


