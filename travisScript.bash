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
check_file "api.py"
check_file "test_functions.py"

cd models
check_file "__init__.py"
check_file "models.py"
check_file "models_test.py"
check_file "models.html"
cd ..

cd 'test'
check_file "__init__.py"
check_file "tests.py"
check_file "tests.out"
cd ..
cd ..



echo "Running tests"

coverage3 run app/test/tests.py 2> app/test/tests.out
coverage3 run app/models/models_test.py >> app/test/tests.out
coverage3 report -m app/test/tests.py >> app/test/tests.out


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