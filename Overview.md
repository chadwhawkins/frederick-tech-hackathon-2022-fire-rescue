GUI
- Select template?
  - This would automatically remember the output file path
  - The input to output column mapping and aggregations will be prepopulated, the user just needs to select the input CSV
  - Templates need to be deletable if the columns change

- Select input file
- Select output file
- Submit button to keep the changes

Backend

- Read CSV File
- Remember "template" which knows which input columns map to which output column
  - Remember the aggregations to perform on the dataset/columns
  - Column mapping logic (input to output)
  - Aggregations logic to perform operations on the input data

- Appending logic to append data to a certain columns in the output excel file
- Backup logic to create a copy of the original output file before writing to the new one