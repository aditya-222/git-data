# git-data
Requirements:
  1) Install virtual environment in your pc/laptop using ''' sudo pip install virtualenv '''
  2) Create and Activate your virtual env  -  # '''   virtualenv environment_name '''   Creating
                                              # '''   source environment_name/bin/activate '''   Activating
  3) Install django in your virtualenv using - # ''' sudo pip install django  '''
                                                # ''' django-admin  --version '''   Check
                                                
  4)Download the zip file in your folder and extract the files.
  5) Run the server  = # ''' python manage.py runserver
  6) Check if there is any other package required for the working and install it by - # ''' pip install package_name  
  7) Once the server starts running without any errors, go to the browser and enter the 
          # ''' url - localhost:8000/repos/allrepos/?q=django '''   you can use any keyword as per your wish instead of django
 
 

This api extracts: 
  i) 20 public repositories as per the queried keywords.
  ii) sort the libraries extracted from requirements.txt or requirements-dev.txt as per on the basis of their occurences.
  
Once you run the server
It accepts url as '127.0.0.1:8000/repos/allrepos/?q="your desired keyword" , eg : 127.0.0.1:8000/repos/allrepos/?q=django 
and will search the top 20 repositories queried on django and sorted by maximum number of stars.

provides the output in json format with the repository data and the packages count sorted by the maximum number of occurences.

Might sometimes give the Error " Http error 403 forbidden" due to the API access limit within a certain time period. 
