# SecurePDFLib
Digital library, Malicious pdf detecton

## Getting Started

These instructions will help you set up and run the project on your local machine.

### Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.x
- [pip](https://pip.pypa.io/en/stable/installation/) (Python package manager)
- 
### Installation

1. Clone the repository:
2. 
   git clone https://github.com/manukirans/SecurePDFLib.git
  

1. Create a virtual environment (venv):
python -m venv venv

2.Activate the virtual environment (Windows):

venv\Scripts\activate

3.For macOS and Linux:

source venv/bin/activate

4.Install project dependencies from requirements.txt:

pip install -r requirements.txt

5.Perform database migrations:

python manage.py makemigrations
python manage.py migrate

6.Start the development server:

python manage.py runserver

The project should now be up and running locally. Access it in your web browser at http://localhost:8000/.


