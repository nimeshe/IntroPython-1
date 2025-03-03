# This is a simple project created for Uni Discussion Topic

# Scenario for Discussion
A local medical clinic wants to improve its patient intake process. Currently, patients fill out paper forms, which the staff then manually enter into the computer system. The clinic’s manager wants a simple automated solution to speed up this process and reduce errors.

The first step in creating the solution is to design a program that collects basic patient information and stores it in an organised format.

# Flowchart for logic
Please check the Miro Board (with view only access): https://miro.com/app/board/uXjVIWrvPcM=/?moveToWidget=3458764619352680640&cot=14

# What I have done
I wanted to use TDD approach as engineering team of the company I work for is using strict TDD. 
I wrote methods to validate patient information entered, and tests to test those methods. 
I couldn't figure out mocking my data, so separated validations into separate validators.py and only tested them. main.py is not tested for user input. Could be the next improvement on this. 

# Dependencies
I'm using uv - https://docs.astral.sh/uv/ (It's a little like npm if you've worked with node.js)
You would require to install python, and uv.
Do a uv.init which will install pytest.
Do the configuration and environment setup (using venv) in VS Code

# My Request to you
You may clone this repo or fork, if you like you can also suggest changes through a pull request. 
