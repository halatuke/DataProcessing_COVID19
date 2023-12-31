"""Covid19_Data_Final"""

# # Data Imports

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

#Importing Data: One for original and the other covi19 is where we will prepare the data for analysis
original = pd.read_csv("COVID-19BehaviorData_CAN_USA.csv")
covid19 = pd.read_csv("COVID-19BehaviorData_CAN_USA.csv")

# # Initial Data Review

# Number of records and variables
covid19.shape

# First 10 data records
covid19.head(10)

# List of variable data types
covid19.dtypes

# Number of float variables
float_list = list(covid19.select_dtypes(['float64']).columns)
len(float_list)

# Number of integer variables
integer_list = list(covid19.select_dtypes(['int64']).columns)
len(integer_list)

# Number of object variables
object_list = list(covid19.select_dtypes(['object']).columns)
len(object_list)

# Brief overview of data
covid19.describe()

# Checking for duplicate records. None are found.
pd.DataFrame.duplicated(covid19).any()

# # Transforming Numerical Variables

# Plotting all numerical variables on a density plot
# For the following numerical variables, we see that the following variables are right skewed:
#     i1_health,i2_health,i7a_health,i13_health,weight
covid19.plot(figsize=(14,10), kind = 'density', subplots=True, layout=(4,4),sharex=False)

# Skewness for each numerical variables
# The skewness of the identified variables are very high indicating right skewness
covid19.skew(axis = 0, skipna = True)

# Transforming i1_health to reduce skewness
covid19['i1_health'] = np.log(covid19['i1_health']+1)
sns.kdeplot(covid19['i1_health'])

# Transforming i2_health to reduce skewness
covid19['i2_health'] = np.log(covid19['i2_health']+1)
sns.kdeplot(covid19['i2_health'])

# Transforming i7a_health to reduce skewness
covid19['i7a_health'] = np.log(covid19['i7a_health']+1)
sns.kdeplot(covid19['i7a_health'])

# Transforming i13_health to reduce skewness
covid19['i13_health'] = np.log(covid19['i13_health']+1)
sns.kdeplot(covid19['i13_health'])

# Transforming weight to reduce skewness
covid19['weight'] = np.log(covid19['weight'])
sns.kdeplot(covid19["weight"])

#Rechecking skewness
# All numerical variables are now close to 0
covid19.skew(axis = 0, skipna = True)

# Plotting all numerical variables on  density plot
covid19.plot(figsize=(14,10), kind = 'density', subplots=True, layout=(4,4),sharex=False)

## Transforming Categorical Variables

# The function for changing uncertain values to missing values

uncertain_option = ['Not sure','Prefer not to say',"Don't know"]

def missing_value_rescale(column_value):
    if column_value in uncertain_option:
        return None
    else:
        return column_value

missing_value_rescale('Not sure')

# Applying the function to variables that have uncertain values

covid19['i4_health'] = covid19['i4_health'].apply(missing_value_rescale)

covid19['i5a_health'] = covid19['i5a_health'].apply(missing_value_rescale)

covid19['i8_health'] = covid19['i8_health'].apply(missing_value_rescale)

covid19['i9_health'] = covid19['i9_health'].apply(missing_value_rescale)

covid19['i10_health'] = covid19['i10_health'].apply(missing_value_rescale)

covid19['i11_health'] = covid19['i11_health'].apply(missing_value_rescale)

covid19['household_size'] = covid19['household_size'].apply(missing_value_rescale)

covid19['household_children'] = covid19['household_children'].apply(missing_value_rescale)

# The function for changing binary variables to dummy variables

def two_value_rescale(column_value):
    if column_value == None or column_value == ' ':
        return None
    elif column_value == 'Yes':
        return 1
    else:
        return 0

# Applying the function to binary variables

covid19['i5_health_1'] = covid19['i5_health_1'].apply(two_value_rescale)

covid19['i5_health_2'] = covid19['i5_health_2'].apply(two_value_rescale)

covid19['i5_health_3'] = covid19['i5_health_3'].apply(two_value_rescale)

covid19['i5_health_4'] = covid19['i5_health_4'].apply(two_value_rescale)

covid19['i5_health_5'] = covid19['i5_health_5'].apply(two_value_rescale)

covid19['i5_health_99'] = covid19['i5_health_99'].apply(two_value_rescale)

covid19['i5a_health'] = covid19['i5a_health'].apply(two_value_rescale)

covid19['i7b_health'] = covid19['i7b_health'].apply(two_value_rescale)

covid19['i8_health'] = covid19['i8_health'].apply(two_value_rescale)

covid19['i9_health'] = covid19['i9_health'].apply(two_value_rescale)

covid19['i14_health_1'] = covid19['i14_health_1'].apply(two_value_rescale)

covid19['i14_health_2'] = covid19['i14_health_2'].apply(two_value_rescale)

covid19['i14_health_3'] = covid19['i14_health_3'].apply(two_value_rescale)

covid19['i14_health_4'] = covid19['i14_health_4'].apply(two_value_rescale)

covid19['i14_health_5'] = covid19['i14_health_5'].apply(two_value_rescale)

covid19['i14_health_6'] = covid19['i14_health_6'].apply(two_value_rescale)

covid19['i14_health_7'] = covid19['i14_health_7'].apply(two_value_rescale)

covid19['i14_health_8'] = covid19['i14_health_8'].apply(two_value_rescale)

covid19['i14_health_9'] = covid19['i14_health_9'].apply(two_value_rescale)

covid19['i14_health_10'] = covid19['i14_health_10'].apply(two_value_rescale)

covid19['i14_health_96'] = covid19['i14_health_96'].apply(two_value_rescale)

covid19['i14_health_98'] = covid19['i14_health_98'].apply(two_value_rescale)

covid19['i14_health_99'] = covid19['i14_health_99'].apply(two_value_rescale)

covid19['d1_health_1'] = covid19['d1_health_1'].apply(two_value_rescale)

covid19['d1_health_2'] = covid19['d1_health_2'].apply(two_value_rescale)

covid19['d1_health_3'] = covid19['d1_health_3'].apply(two_value_rescale)

covid19['d1_health_4'] = covid19['d1_health_4'].apply(two_value_rescale)

covid19['d1_health_5'] = covid19['d1_health_5'].apply(two_value_rescale)

covid19['d1_health_6'] = covid19['d1_health_6'].apply(two_value_rescale)

covid19['d1_health_7'] = covid19['d1_health_7'].apply(two_value_rescale)

covid19['d1_health_8'] = covid19['d1_health_8'].apply(two_value_rescale)

covid19['d1_health_9'] = covid19['d1_health_9'].apply(two_value_rescale)

covid19['d1_health_10'] = covid19['d1_health_10'].apply(two_value_rescale)

covid19['d1_health_11'] = covid19['d1_health_11'].apply(two_value_rescale)

covid19['d1_health_12'] = covid19['d1_health_12'].apply(two_value_rescale)

covid19['d1_health_13'] = covid19['d1_health_13'].apply(two_value_rescale)

covid19['d1_health_98'] = covid19['d1_health_98'].apply(two_value_rescale)

covid19['d1_health_99'] = covid19['d1_health_99'].apply(two_value_rescale)

# The function for changing  variables with sequenced options to a scaled variable
five_option1 = ['Very easy','Very willing','Always']
five_option2 = ['Somewhat easy', 'Somewhat willing','Frequently']
five_option3 = ['Neither easy nor difficult','Neither willing nor unwilling','Sometimes']
five_option4 = ['Somewhat difficult','Somewhat unwilling','Rarely']

def five_value_rescale(column_value):
    if column_value == None or column_value == ' ':
        return None
    elif column_value in five_option1:
        return 1
    elif column_value in five_option2:
        return 2
    elif column_value in five_option3:
        return 3
    elif column_value in five_option4:
        return 4
    else:
        return 5

# Applying the function to variables with sequenced options

covid19['i6_health'] = covid19['i6_health'].apply(five_value_rescale)

covid19['i10_health'] = covid19['i10_health'].apply(five_value_rescale)

covid19['i11_health'] = covid19['i11_health'].apply(five_value_rescale)

covid19['i12_health_1'] = covid19['i12_health_1'].apply(five_value_rescale)

covid19['i12_health_2'] = covid19['i12_health_2'].apply(five_value_rescale)

covid19['i12_health_3'] = covid19['i12_health_3'].apply(five_value_rescale)

covid19['i12_health_4'] = covid19['i12_health_4'].apply(five_value_rescale)

covid19['i12_health_5'] = covid19['i12_health_5'].apply(five_value_rescale)

covid19['i12_health_6'] = covid19['i12_health_6'].apply(five_value_rescale)

covid19['i12_health_7'] = covid19['i12_health_7'].apply(five_value_rescale)

covid19['i12_health_8'] = covid19['i12_health_8'].apply(five_value_rescale)

covid19['i12_health_9'] = covid19['i12_health_9'].apply(five_value_rescale)

covid19['i12_health_10'] = covid19['i12_health_10'].apply(five_value_rescale)

covid19['i12_health_11'] = covid19['i12_health_11'].apply(five_value_rescale)

covid19['i12_health_12'] = covid19['i12_health_12'].apply(five_value_rescale)

covid19['i12_health_13'] = covid19['i12_health_13'].apply(five_value_rescale)

covid19['i12_health_14'] = covid19['i12_health_14'].apply(five_value_rescale)

covid19['i12_health_15'] = covid19['i12_health_15'].apply(five_value_rescale)

covid19['i12_health_16'] = covid19['i12_health_16'].apply(five_value_rescale)

covid19['i12_health_17'] = covid19['i12_health_17'].apply(five_value_rescale)

covid19['i12_health_18'] = covid19['i12_health_18'].apply(five_value_rescale)

covid19['i12_health_19'] = covid19['i12_health_19'].apply(five_value_rescale)

covid19['i12_health_20'] = covid19['i12_health_20'].apply(five_value_rescale)

# Rescaling qweek variable to as a scaled variable
def qweek_rescale(qweek):
    if qweek == None or qweek == ' ':
        return None
    else:
        last_str = len(qweek)
        str_num = qweek[last_str-1]
        num_int = int(str_num)
        return num_int

qweek_rescale('week 1')

covid19['qweek']=covid19['qweek'].apply(qweek_rescale)
covid19['qweek']

# Changing household_size to a numerical variable

def household_size_rescale(size):
    if size == None or size == '' :
        return None
    elif size == '8 or more':
        return 8
    else:
        num_int = int(size)
        return num_int

covid19['household_size']=covid19['household_size'].apply(household_size_rescale)
covid19['household_size']

# Changing household_children to a numerical variable

def household_children_rescale(children):
    if children == None or children == ' ':
        return None
    elif children == '5 or more':
        return 5
    else:
        num_int = int(children)
        return num_int

covid19['household_children']=covid19['household_children'].apply(household_children_rescale)
covid19['household_children']

# # Variable Reclassification

# reclassification of region_state based regions in Canada and USA

canada_north = ['Northwest Territories / Territoires du Nord-Ouest','Nunavut','Yukon']
canada_west_prairies = ['Alberta','British Columbia / Colombie Britanique','Saskatchewan','Manitoba']
canada_east = ['New Brunswick / Nouveau-Brunswick','Nova Scotia / Nouvelle-Écosse','Newfoundland & Labrador / Terre-Neuve-et-Labrador', 'Prince Edward Island / Île-du-Prince-Édouard']
canada_central = ['Quebec / Québec','Ontario']
usa_northeast = ['Connecticut', 'Maine','Massachusetts', 'New Hampshire', 'Rhode Island', 'Vermont', 'New Jersey', 'New York', 'Pennsylvania']
usa_midwest = ['Indiana','Illinois','Michigan','Ohio','Wisconsin','Iowa','Nebraska','Kansas','North Dakota','Minnesota','South Dakota','Missouri']
usa_south = ['Delaware', 'District of Columbia', 'Florida','Georgia','Maryland','North Carolina','South Carolina','Virginia','West Virginia','Alabama','Kentucky','Mississippi','Tennessee','Arkansas','Louisiana','Oklahoma','Texas']
usa_west = ['Arizona', 'Colorado', 'Idaho', 'New Mexico', 'Montana', 'Utah', 'Nevada', 'Wyoming', 'Alaska', 'California', 'Hawaii', 'Oregon', 'Washington']

def region_recode(region_state):
    if region_state == None or region_state == ' ':
        return None
    elif region_state in canada_north:
        return 'canada_north'
    elif region_state in canada_west_prairies:
        return 'canada_west_prairies'
    elif region_state in canada_east:
        return 'canada_east'
    elif region_state in canada_central:
        return 'canada_central'
    elif region_state in usa_northeast:
        return 'usa_northeast'
    elif region_state in usa_midwest:
        return 'usa_midwest'
    elif region_state in usa_south:
        return 'usa_south'
    else:
        return 'usa_west'


covid19['region_state']=covid19['region_state'].apply(region_recode)
covid19['region_state']

## Adjusting i3_health and i4_health

# Changing i3_health to a numerical variable

def i3_rescale(column_value):
    if column_value == 'No, I have not':
        return 1
    elif column_value == 'Yes, and I have not received my results from the test yet':
        return 2
    elif column_value == 'Yes, and I tested negative':
        return 3
    elif column_value == 'Yes, and I tested positive':
        return 4

covid19['i3_health'] = covid19['i3_health'].apply(i3_rescale)

# Changing i4_health to a numerical variable
def i4_rescale(column_value):
    if column_value == 'No, they have not':
        return 1
    elif column_value == 'Yes, and they have not received their results from the test yet':
        return 2
    elif column_value == 'Yes, and they tested negative':
        return 3
    elif column_value == 'Yes, and they tested positive':
        return 4

covid19['i4_health'] = covid19['i4_health'].apply(i4_rescale)

np.random.seed(10)

covid19['i3_health'] = covid19['i3_health'].apply(lambda x: x if pd.notnull(x)
                                                  else np.random.randint(covid19['i3_health'].min(), covid19['i3_health'].max()))


covid19['i4_health'] = covid19['i4_health'].apply(lambda x: x if pd.notnull(x)
                                                  else np.random.randint(covid19['i4_health'].min(), covid19['i4_health'].max()))

def i3_rescale_back(column_value):
    if column_value == 1:
        return 'No, I have not'
    elif column_value == 2:
        return 'Yes, and I have not received my results from the test yet'
    elif column_value == 3:
        return 'Yes, and I tested negative'
    elif column_value == 4:
        return 'Yes, and I tested positive'

covid19['i3_health'] = covid19['i3_health'].apply(i3_rescale_back)

def i4_rescale_back(column_value):
    if column_value == 1:
        return 'No, they have not'
    elif column_value == 2:
        return 'Yes, and they have not received their results from the test yet'
    elif column_value == 3:
        return 'Yes, and they tested negative'
    elif column_value == 4:
        return 'Yes, and they tested positive'

covid19['i4_health'] = covid19['i4_health'].apply(i4_rescale_back)

## Missing Values

# Dealing with i5_health_1, i5_health_2, i5_health_3, i5_health_4, i5_health_5, i5_health_99, i9_health, i10_health, i11_health

[covid19['i5_health_1'].isna().sum(),covid19['i5_health_2'].isna().sum(),covid19['i5_health_3'].isna().sum(),
 covid19['i5_health_4'].isna().sum(),covid19['i5_health_5'].isna().sum(),covid19['i5_health_99'].isna().sum(),
 covid19['i9_health'].isna().sum(), covid19['i10_health'].isna().sum(), covid19['i11_health'].isna().sum()]

covid19['i5_health_1'] = covid19['i5_health_1'].apply(lambda x: x if pd.notnull(x)
                                                  else np.random.randint(covid19['i5_health_1'].min(), covid19['i5_health_1'].max()))

covid19['i5_health_2'] = covid19['i5_health_2'].apply(lambda x: x if pd.notnull(x)
                                                  else np.random.randint(covid19['i5_health_2'].min(), covid19['i5_health_2'].max()))

covid19['i5_health_3'] = covid19['i5_health_3'].apply(lambda x: x if pd.notnull(x)
                                                  else np.random.randint(covid19['i5_health_3'].min(), covid19['i5_health_3'].max()))

covid19['i5_health_4'] = covid19['i5_health_4'].apply(lambda x: x if pd.notnull(x)
                                                  else np.random.randint(covid19['i5_health_4'].min(), covid19['i5_health_4'].max()))

covid19['i5_health_5'] = covid19['i5_health_5'].apply(lambda x: x if pd.notnull(x)
                                                  else np.random.randint(covid19['i5_health_5'].min(), covid19['i5_health_5'].max()))

covid19['i5_health_99'] = covid19['i5_health_99'].apply(lambda x: x if pd.notnull(x)
                                                  else np.random.randint(covid19['i5_health_99'].min(), covid19['i5_health_99'].max()))

covid19['i9_health'] = covid19['i9_health'].apply(lambda x: x if pd.notnull(x)
                                                  else np.random.randint(covid19['i9_health'].min(), covid19['i9_health'].max()))

covid19['i10_health'] = covid19['i10_health'].apply(lambda x: x if pd.notnull(x)
                                                  else np.random.randint(covid19['i10_health'].min(), covid19['i10_health'].max()))

covid19['i11_health'] = covid19['i11_health'].apply(lambda x: x if pd.notnull(x)
                                                  else np.random.randint(covid19['i11_health'].min(), covid19['i11_health'].max()))

# Dealing with i12_health_9. They are all not workforce: students, retired, unemployed
# They also cannot answer this quetion. we dont know what their answer will be. Use random.

covid19['i12_health_9'].isna().sum()

covid19['i12_health_9'] = covid19['i12_health_9'].apply(lambda x: x if pd.notnull(x)
                                                  else np.random.randint(covid19['i12_health_9'].min(), covid19['i12_health_9'].max()))

covid19['i12_health_9'].isna().sum()

# Dealing with i12_health_10: They dont have kids so they cannot answer this question about their kids.
# We will be filling with random values.

covid19['i12_health_10'].isna().sum()

covid19['i12_health_10'] = covid19['i12_health_10'].apply(lambda x: x if pd.notnull(x)
                                                  else np.random.randint(covid19['i12_health_10'].min(), covid19['i12_health_10'].max()))

covid19['i12_health_10'].isna().sum()

# Dealing with i14_health_1 to i14_health_99. The same situation as i12_health_9. But this time fill them with 0.

[covid19['i14_health_1'].isna().sum(),covid19['i14_health_2'].isna().sum(),covid19['i14_health_3'].isna().sum(),
 covid19['i14_health_4'].isna().sum(),covid19['i14_health_5'].isna().sum(),covid19['i14_health_6'].isna().sum(),
 covid19['i14_health_7'].isna().sum(),covid19['i14_health_8'].isna().sum(),covid19['i14_health_9'].isna().sum(),
 covid19['i14_health_10'].isna().sum(),covid19['i14_health_96'].isna().sum(),covid19['i14_health_98'].isna().sum(),
 covid19['i14_health_99'].isna().sum()]

covid19['i14_health_1'] = covid19['i14_health_1'].apply(lambda x: x if pd.notnull(x) else 0)
covid19['i14_health_2'] = covid19['i14_health_2'].apply(lambda x: x if pd.notnull(x) else 0)
covid19['i14_health_3'] = covid19['i14_health_3'].apply(lambda x: x if pd.notnull(x) else 0)
covid19['i14_health_4'] = covid19['i14_health_4'].apply(lambda x: x if pd.notnull(x) else 0)
covid19['i14_health_5'] = covid19['i14_health_5'].apply(lambda x: x if pd.notnull(x) else 0)
covid19['i14_health_6'] = covid19['i14_health_6'].apply(lambda x: x if pd.notnull(x) else 0)
covid19['i14_health_7'] = covid19['i14_health_7'].apply(lambda x: x if pd.notnull(x) else 0)
covid19['i14_health_8'] = covid19['i14_health_8'].apply(lambda x: x if pd.notnull(x) else 0)
covid19['i14_health_9'] = covid19['i14_health_9'].apply(lambda x: x if pd.notnull(x) else 0)
covid19['i14_health_10'] = covid19['i14_health_10'].apply(lambda x: x if pd.notnull(x) else 0)
covid19['i14_health_96'] = covid19['i14_health_96'].apply(lambda x: x if pd.notnull(x) else 0)
covid19['i14_health_98'] = covid19['i14_health_98'].apply(lambda x: x if pd.notnull(x) else 0)
covid19['i14_health_99'] = covid19['i14_health_99'].apply(lambda x: x if pd.notnull(x) else 0)

[covid19['i14_health_1'].isna().sum(),covid19['i14_health_2'].isna().sum(),covid19['i14_health_3'].isna().sum(),
 covid19['i14_health_4'].isna().sum(),covid19['i14_health_5'].isna().sum(),covid19['i14_health_6'].isna().sum(),
 covid19['i14_health_7'].isna().sum(),covid19['i14_health_8'].isna().sum(),covid19['i14_health_9'].isna().sum(),
 covid19['i14_health_10'].isna().sum(),covid19['i14_health_96'].isna().sum(),covid19['i14_health_98'].isna().sum(),
 covid19['i14_health_99'].isna().sum()]

# Dealing with d1_health_1 to d1_health_99

[covid19['d1_health_1'].isna().sum(),covid19['d1_health_2'].isna().sum(),covid19['d1_health_3'].isna().sum(),
 covid19['d1_health_4'].isna().sum(),covid19['d1_health_5'].isna().sum(),covid19['d1_health_6'].isna().sum(),
 covid19['d1_health_7'].isna().sum(),covid19['d1_health_8'].isna().sum(),covid19['d1_health_9'].isna().sum(),
 covid19['d1_health_10'].isna().sum(),covid19['d1_health_11'].isna().sum(),covid19['d1_health_12'].isna().sum(),
 covid19['d1_health_13'].isna().sum(),covid19['d1_health_98'].isna().sum(), covid19['d1_health_99'].isna().sum()]

covid19['d1_health_1'] = covid19['d1_health_1'].apply(lambda x: x if pd.notnull(x)
                                                  else np.random.randint(covid19['d1_health_1'].min(), covid19['d1_health_1'].max()))

covid19['d1_health_2'] = covid19['d1_health_2'].apply(lambda x: x if pd.notnull(x)
                                                  else np.random.randint(covid19['d1_health_2'].min(), covid19['d1_health_2'].max()))

covid19['d1_health_3'] = covid19['d1_health_3'].apply(lambda x: x if pd.notnull(x)
                                                  else np.random.randint(covid19['d1_health_3'].min(), covid19['d1_health_3'].max()))

covid19['d1_health_4'] = covid19['d1_health_4'].apply(lambda x: x if pd.notnull(x)
                                                  else np.random.randint(covid19['d1_health_4'].min(), covid19['d1_health_4'].max()))

covid19['d1_health_5'] = covid19['d1_health_5'].apply(lambda x: x if pd.notnull(x)
                                                  else np.random.randint(covid19['d1_health_5'].min(), covid19['d1_health_5'].max()))

covid19['d1_health_6'] = covid19['d1_health_6'].apply(lambda x: x if pd.notnull(x)
                                                  else np.random.randint(covid19['d1_health_6'].min(), covid19['d1_health_6'].max()))

covid19['d1_health_7'] = covid19['d1_health_7'].apply(lambda x: x if pd.notnull(x)
                                                  else np.random.randint(covid19['d1_health_7'].min(), covid19['d1_health_7'].max()))

covid19['d1_health_8'] = covid19['d1_health_8'].apply(lambda x: x if pd.notnull(x)
                                                  else np.random.randint(covid19['d1_health_8'].min(), covid19['d1_health_8'].max()))

covid19['d1_health_9'] = covid19['d1_health_9'].apply(lambda x: x if pd.notnull(x)
                                                  else np.random.randint(covid19['d1_health_9'].min(), covid19['d1_health_9'].max()))

covid19['d1_health_10'] = covid19['d1_health_10'].apply(lambda x: x if pd.notnull(x)
                                                  else np.random.randint(covid19['d1_health_10'].min(), covid19['d1_health_10'].max()))

covid19['d1_health_11'] = covid19['d1_health_11'].apply(lambda x: x if pd.notnull(x)
                                                  else np.random.randint(covid19['d1_health_11'].min(), covid19['d1_health_11'].max()))

covid19['d1_health_12'] = covid19['d1_health_12'].apply(lambda x: x if pd.notnull(x)
                                                  else np.random.randint(covid19['d1_health_12'].min(), covid19['d1_health_12'].max()))

covid19['d1_health_13'] = covid19['d1_health_13'].apply(lambda x: x if pd.notnull(x)
                                                  else np.random.randint(covid19['d1_health_13'].min(), covid19['d1_health_13'].max()))

covid19['d1_health_98'] = covid19['d1_health_98'].apply(lambda x: x if pd.notnull(x)
                                                  else np.random.randint(covid19['d1_health_98'].min(), covid19['d1_health_98'].max()))

covid19['d1_health_99'] = covid19['d1_health_99'].apply(lambda x: x if pd.notnull(x)
                                                  else np.random.randint(covid19['d1_health_99'].min(), covid19['d1_health_99'].max()))

[covid19['d1_health_1'].isna().sum(),covid19['d1_health_2'].isna().sum(),covid19['d1_health_3'].isna().sum(),
 covid19['d1_health_4'].isna().sum(),covid19['d1_health_5'].isna().sum(),covid19['d1_health_6'].isna().sum(),
 covid19['d1_health_7'].isna().sum(),covid19['d1_health_8'].isna().sum(),covid19['d1_health_9'].isna().sum(),
 covid19['d1_health_10'].isna().sum(),covid19['d1_health_11'].isna().sum(),covid19['d1_health_12'].isna().sum(),
 covid19['d1_health_13'].isna().sum(),covid19['d1_health_98'].isna().sum(), covid19['d1_health_99'].isna().sum()]

# Dropping columns
covid19 = covid19.drop(['i5a_health', 'i6_health', 'i7b_health', 'i8_health', 'endtime',
                                    'i14_health_other'], axis = 1)

covid19_final = covid19

# # Final Data Review

# Brief overview of data
covid19_final.shape

# Brief overview of data
covid19_final.head(10)

float_list = list(covid19_final.select_dtypes(['float64']).columns)
len(float_list)

integer_list = list(covid19_final.select_dtypes(['int64']).columns)
len(integer_list)

object_list = list(covid19_final.select_dtypes(['object']).columns)
len(object_list)

covid19_final.skew(axis = 0, skipna = True)

#Export File

covid19_final.to_csv('covid19_transformed.csv')
