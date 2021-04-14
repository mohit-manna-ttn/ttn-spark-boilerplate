> How to run the code?  


**Step 1:** Create a virtual environment. Preferablly virtualenv  
`$ virtualenv venv`  
Activate the environment. Move to project folder.   
`$ . venv/bin/activate`  

**Step 2:** Install the libraries from the given requirement file  
`$ pip install -r requirements.txt`  

**Step 3:** Simply Run  
`$ export DEBUG=1`  
`$ zip -ru9 packages.zip dependencies -x dependencies/__pycache__/\* ; zip -ru9 packages.zip utils -x utils/__pycache__/\* ; spark-submit --master local[*]  --py-files packages.zip --files configs/dev_config.json --packages 'org.mongodb.spark:mongo-spark-connector_2.12:2.4.2'  jobs/reconciliation.py '{"db":"default","spark.mongodb.input.uri":"mongodb://<user>:<password>@<ip>:27017","spark.mongodb.output.uri":"mongodb://<user>:<pwd>@<ip>:27017","task_id":"601788e24407641ddcb151b7"}'`  

get all the parameters using `dict(spark.sparkContext.getConf().getAll())` or simply use json.  
> UnitTests  
  
Create files in tests folder. one is created and execute using following command  
`$ python -m unittest tests/test_*.py`  
  
> Testing a Function   
  
E.g. jobs.reconciliation.main()  
  
`$ python`  
`>>> from jobs.reconciliation import main`  
`>>> main()`  
  
> Before pushing the code.  
  
`$ pip freeze > requirements.txt`  
