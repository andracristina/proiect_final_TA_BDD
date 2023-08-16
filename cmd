pip install - U selenium
pip install behave
pip install behave-html-formatter

to run tests with tag @smoke
behave -f html -o behave-report.html --tags=smoke