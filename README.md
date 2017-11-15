# git-data

This api extracts: 
  i) 20 public repositories as per the queried keywords.
  ii) sort the libraries extracted from requirements.txt or requirements-dev.txt as per on the basis of their occurences.
  
Once you run the server
It accepts url as '127.0.0.1:8000/repos/allrepos/?q="your desired keyword" , eg : 127.0.0.1:8000/repos/allrepos/?q=django 
and will search the top 20 repositories queried on django and sorted by maximum number of stars.

provides the output in json format with the repository data and the packages count sorted by the maximum number of occurences.


