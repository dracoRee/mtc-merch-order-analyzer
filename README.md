# READ ME
This is a simple python program designed to analyze merchandise orders, based on the 2025 Merchandise Pre-Order Google Form.
This repository comes with the anaylzer itself, a sample .tsv file and a README file (this file.)

The code may be reused for future years, if and only if the Google Form for future preorders remain the same. 

## The most important thing to note of when using this merch analyzer program is:
1. The format of the sizes and quantities (i.e. **M(2), S(5)**);
2. and the extension of the file to be read (i.e. **.tsv**)

The analyzer will **ONLY** work if the file given is a TSV (tab-separated values) as I'm too lazy to work on CSV functionalities (due to the format of size and quantities including commas, breaking the CSV data).

### Note: If you are creating a new Google Form for the merch, you may refer to the Regular Expression used to enforce the format for the size and quantity (i.e. *Size(Quantity)*)

**Cotton:**
`^(S|M|L|XL|2XL|3XL)\([1-9][0-9]*\)(, (S|M|L|XL|2XL|3XL)\([1-9][0-9]*\))*\s*$`

**Dri-Fit**
`^(2XS|XS|S|M|L|XL|2XL|3XL|5XL|7XL)\([1-9][0-9]*\)(, (2XS|XS|S|M|L|XL|2XL|3XL|5XL|7XL)\([1-9][0-9]*\))*\s*$`

Do contact me if there are extra functionalities that you would like to add or suggest, alongside fixes for the code.