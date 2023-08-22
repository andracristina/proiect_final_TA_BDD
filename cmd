pip install - U selenium
pip install behave
pip install behave-html-formatter


behave -f html -o behave-report.html --tags=smoke
behave -f html -o behave-report.html --tags=inventory
behave -f html -o behave-report.html --tags=sort
behave -f html -o behave-report.html --tags=logout

behave -f html -o behave-report.html --tags=regression

