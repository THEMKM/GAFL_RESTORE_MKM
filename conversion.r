library(haven)

# Read the Stata file
df <- read_dta("C:/Users/Mohamad/Documents/GitHub/GAFL_RESTORE_MKM/Data/raw/cdi_household_clean_nopii.dta")

# Display the first 6 rows of the data
head(df)
# Display the structure of the data
str(df)

# Extract variable labels for all columns
variable_labels <- sapply(df, function(x) attr(x, "label"))
print(variable_labels)
