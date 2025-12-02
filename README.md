1. BMI Calculator README

File: dale quincybmi.py
Description

This script calculates a user's Body Mass Index (BMI) using both Imperial (standard) and Metric systems. It demonstrates variable assignment, arithmetic operations, and string formatting in Python.
Features

    Input: Prompts user for height (inches) and weight (pounds).

    Conversion: Automatically converts the input height to meters and weight to kilograms.

    Calculation: Computes BMI using the standard formula: weight / (height ** 2) * 703.

    Formatting: detailed output using Python f-strings and the round() function to limit decimal places.

How to Run

    Run the script in a Python environment.

    Enter your height in inches when prompted.

    Enter your weight in pounds when prompted.

2. Simple Arithmetic Calculator README

File: homework 3(1).py
Description

A simple command-line calculator that takes two numbers and an operator to perform basic arithmetic.
Features

    Supported Operators: Addition (+), Subtraction (-), Multiplication (*), and Division (/).

    Error Handling:

        Includes a check to prevent division by zero.

        Uses a try/except block to catch ValueError if non-numeric data is entered.

How to Run

    Run the script.

    Enter the first number.

    Choose an operator (+, -, *, /).

    Enter the second number.

3. Student Grade Averager README

File: week 7 homework(1).py
Description

This program calculates the average of three test scores and provides qualitative feedback based on the result. It utilizes modular programming by defining specific functions for input gathering and logic checking.
Features

    Functions:

        get_average(): Collects three test scores and calculates the mean.

        check_average(average): Evaluates the score and prints a message (e.g., "Congratulations" for >90, "You almost failed" for 60-70).

    Grading Scale:

        90+: Best/Congratulations

        80-89: Great job

        70-79: Average

        60-69: Almost failed

        Below 60: Failed.

How to Run

    Run the script.

    Input the scores for Test 1, Test 2, and Test 3.

    View the calculated average and the corresponding feedback message.

4. Distance Calculator README

File: dale quicny distance.py
Description

A utility script to calculate the total distance traveled based on speed and time inputs.
Features

    Input: Accepts speed (MPH) and time (hours) as floating-point numbers.

    Calculation: Uses the formula distance = speed * time.

    Notes: The code includes comments referencing specific distances for "Local," "Parkway," and "Highway" routes.

How to Run

    Run the script.

    Enter the speed in Miles Per Hour (MPH).

    Enter the time traveled in hours.

5. Water State Checker README

File: week 4 homework(1).py
Description

This script converts a temperature from Fahrenheit to Celsius and determines the physical state of water (Solid, Liquid, or Gas) at that temperature.
Features

    Conversion: Converts input Fahrenheit to Celsius using the formula (temp - 32) * 5/9.

    State Logic:

        Solid: <= 0°C

        Liquid: Between 0°C and 100°C

        Gas: >= 100°C.

    Validation: Includes error handling for invalid non-numeric inputs.

How to Run

    Run the script.

    Enter the current temperature in Fahrenheit.

    The script will output the temperature in Celsius and the state of the water.

6. Resume-to-Job Matcher (Final Project) README

File: final project.py
Description

This is a comprehensive GUI application built with Tkinter that matches a user's resume and keywords against a database of job descriptions. It uses OpenAI Embeddings and Cosine Similarity to semantically rank job opportunities from best to worst fit.
Dependencies

This project requires the following libraries:

    tkinter (Standard Python GUI library)

    python-dotenv (For loading API keys)

    numpy

    scikit-learn (For cosine similarity)

    langchain_openai

Setup

    API Key: You must have an OpenAI API key. Create a .env file in the same directory as the script and add:

    OPENAI_API_KEY=your_api_key_here

    Environment: Ensure the .env file is loaded using load_dotenv() as implemented in the script.

Features

    GUI: Features a user-friendly interface to upload files and view results in a table format.

    Resume Upload: Supports reading text files (and basic file handling for PDF/DOCX placeholders).

    Semantic Search: Combines the resume text with user-defined keywords to create a "Candidate Profile," then embeds this profile to compare against hardcoded job descriptions (e.g., Nurse, Engineer, IT Support).

    Ranking: Displays jobs sorted by a similarity score (0.0 to 1.0).

How to Run

    Install dependencies: pip install python-dotenv numpy scikit-learn langchain-openai.

    Run the script: python final project.py.

    Click "Browse" to upload a resume file.

    (Optional) Enter additional skills or keywords.

    Click "Find Jobs" to see the ranked list of matching positions.
