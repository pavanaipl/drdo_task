# pivottable_task
System Requirements
Python 3+
Anaconda 3
1. Create of virtual environment
Open the terminal and enter the following command:
$ conda create -n <environment_name> python=3.7
Once the environment has been created, activate the environment:
$ conda activate <environment_name>

2. Clone project to the local machine
In the terminal, navigate to the location where the project folder has to be created. Then enter the git command to clone the project:
$ git clone https://github.com/pavanaipl/pivottable_task.git


3. Install the project requirements
Install the python packages listed in the requirements.txt file. Enter the following command in the terminal:
$ pip install -r requirements.txt

4. Run the development server
To start the development server, run the following command:
$ python manage.py runserver
By default the server runs on port8000
Check whether the server is running by going to localhost:8000/admin
