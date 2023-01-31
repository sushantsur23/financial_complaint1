# financial_complaint1

### Data Ingestion Artifact
We will Data Ingestion artifact which will have Meta_info.yaml, Feature _store and Timestamp.
Meta_info.yaml will have the from and to date of the last run, will be needed while running the pipeline. The new from_date becomes the last run to_date. 
Timestamp will have 2 folders where files successfully downloadaed will be one folder and unsuccessful download will be in another folder.
In Feature Store all the successful downloaded files are coverted into one single parquet file.

### Data Ingestion Config
we will need data ingestion configuration which will lead to artifacts folder.
Data Ingestion config will have 
from_date, 
to_date,  
download_dir,
data_ingestion_dir, 
file_name(of the downloaded files), 
feature_store_dir, 
failed_dir, 
metadata_file_path(leads to meta_info.yaml), 
datasource_url.

### Data Ingestion Pipeline
1) All the above config will go to data ingestion component. This will check if the data pipeline ran today, if yes then no need to downlod new data. Directly prpare ingestion artifact and go further.
2) If pipeline didn't run today then download new data in download_dir. If download is a failure then the process will be retried 5 times then it will give up. Once sucessfully downloaded files then it will be go into feature store with parquet file format. 
3) Using class info Data ingestion meta it will overwrite the mdetadata information in the meta_info.yaml file.
4) Finally Data Ingestion artifact is created.

Data Ingestion Artifact will contain feature_store_path, metadata_file_path and download_dir.

In Training pipeline config we will get the data ingestion configuration as we define the entity, in the entity we have data ingestion config,

### Data Validation Component 
Training pipeline config will have will have get_data_validation_config 
Data validation config will have accepted_data_dir, rejected_data_dir and file_name depending on the process if the file is accepted or rejected.
Process :- 
1) Read data from the Feature Store
2) Dropping unwanted rows.
3) Checking if is_required clumn present
4) Finally prepare the data_validation_artifact containing accepted_file_path and rejected_dir. 
5) Return the data validation artifact.

#### Structure of Data Validation Artifact
Data_Validation_Artifact is divided into timestamps. Under timestamps we have accepted_data and rejected_data.
