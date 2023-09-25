# REDcap_ETL
For extracting, processing, and bulk uploading to redcap

## ELIMINATE
This REDcap database will need a redesign with a new data dictionary.

### Steps:
1. Extract Clinical Info from raw data
2. Extract Plasma Vial info from raw data
3. Extract DNA extraction info from raw data
4. Clear current dictionary
5. Upload new template dictionary
6. Add previous clinical data instrument to dictionary 
7. Transform plasma vial raw data for import into REDcap REST-API
8. Transform DNA extraction info for import into REDcap REST-API

[Jupyter Notebook for ELIMINATE](src/ELIMINATE/clin_etl.ipynb)