# Ioet Schedule Coincidence

This repository contains the solution to the problem sent to me by Ioet.

# The exercise
The company ACME offers their employees the flexibility to work the hours they want. But due to some external circumstances they need to know what employees have been at the office within the same time frame

The goal of this exercise is to output a table containing pairs of employees and how often they have coincided in the office.

Input: the name of an employee and the schedule they worked, indicating the time and hours. This should be a .txt file with at least five sets of data. You can include the data from our examples below:

**Example 1:**

***INPUT:***  

    RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00- 21:00  
    ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00  
    ANDRES=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00

  
***OUTPUT:***  

    ASTRID-RENE: 2  
    ASTRID-ANDRES: 3  
    RENE-ANDRES: 2

**Example 2:**

***INPUT:***  

    RENE=MO10:15-12:00,TU10:00-12:00,TH13:00-13:15,SA14:00-18:00,SU20:00-21:00  
    ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00

***OUTPUT:***  

    RENE-ASTRID: 3

## About the solution

### Input
The first thing the solution do is to read the data from a file, validate it and parse it and generate a timeline with office events.  An event is when a employee comes or goes. To facilitate this task, the times are transformed to the number of minutes elapsed since Monday at 00:00.

For example, if 'Maria' starts to work at Monday 7:00 and ends at 10:00, we have two events:

> Maria arrives at the office in the minute 420.
> Maria leaves the office in the minute 600. 

 
### Process
Once we have our timeline, we should to ask: Who is in the office every time a new employee arrives?
For example:

> Maria arrives at the office in the minute 420.
> Roberto arrives at the office in the minute 600.

When Roberto arrives, Maria is in the office, so Maria-Roberto: 1.

 > Abigail arrives at the office in the minute 800.
 
 When Abigail arrives, Maria and Roberto are in the office, so Abigail-Maria: 1, Abigail-Roberto: 1.

> Abigail, Roberto and Maria leave the office in the minute 860.

The office is empty, and the solution is ready.

### Output
Finally the solution is printed according with the format required. The results are presented and the pairs of names will printed in alphabetical order.

## About the development
This solution was developed following the TDD's steps. The code to solve the problem is in the package 'solution', and the program can be executed using the module *main.py*.
The CI in this repository checks linter rules and tests every time the main branch got a push or pull request.

## Instructions to run
To run this project you should create a virtual enviroment for Python. For Windows use:

    python -m venv .venv

If you are tying Linux use:

    virtualenv .venv

The next step is install libraries. These ones are not required to run the solution but are necessary to run the tests and to guarantee a good quality code.

    pip install -r requirements/local.txt

Ok,  now you are all set. 🚀😉

### To run the solution
To run the solution use:

    python main.py

The input data is in the file *data.txt*.

### To run the tests
This project is configured to autodiscover test files, and is posible to run them directly from the command line.

    pytest

If you want to see more details use the option -vv

    pytest -vv

To see the coverage percent of the tests use the next commands. At this point, the project has a coverage percent over 95%.

    coverage run -m pytest
    coverage report -m
