#!/bin/bash

check_file () {
    if [ -f "$1" ]
    then
        echo "$1 found"
    else
        echo "$1 not found"
        exit -1
    fi
}

echo "Checking for all files"

cd documentation
check_file "UML.pdf"
check_file "apiary.apib"
check_file "IDB.log"
check_file "Report.pdf"
cd ..

cd app
check_file "funruns.py"
check_file "run_tests.py"
check_file "database_commands.txt"
check_file "test_output.txt"

cd api
check_file "api.py"
check_file "api_helpers.py"
check_file "api_test.py"
check_file "__init__.py"
check_file "test_output.txt"
cd ..

cd models
check_file "__init__.py"
check_file "models.py"
check_file "models_test.py"
check_file "models.html"
check_file "create_database.py"
check_file "test_output.txt"
cd ..
cd ..



echo "Running tests"

coverage3 run app/api/api_test.py 2> app/api/test_output.txt
coverage3 report app/api/api_test.py >> app/api/test_output.txt


coverage3 run app/models/models_test.py 2> app/models/test_output.txt
coverage3 report -m app/models/models_test.py >> app/models/test_output.txt


#models_test
#api_Tests

# echo "Making pydoc3"

# #need to do this 
# sphinx-apidoc . --full -o documentation -H 'Funruns' -A 'FlaskMeAnything' -V '1.0'
# cd documentation
# make html
# cd ..


# echo "Making IDB.log"

# commit_message=`git log -1 --pretty=%B`
# commit_author=`git log -1 --pretty=%cn`
# commit_email=`git log -1 --pretty=%ce`

# git config --global user.name "$commit_author"
# git config --global user.email "$commit_email"
# git config --global push.default simple
# git config --global credential.helper store
# echo "https://${GITHUB_KEY}:x-oauth-basic@github.com" >> ~/.git-credentials

# git checkout travis-ci
# git log > IDB.log
# git add -A
# git commit -m "Added IDB.log (Travis CI)"
# git reset --soft HEAD~1
# git commit -m "$commit_message"
# git push -f "https://github.com/anwilliams93/cs373-idb.git" HEAD:travis-ci

echo "Done."