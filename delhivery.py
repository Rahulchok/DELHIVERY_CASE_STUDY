# -*- coding: utf-8 -*-
"""DELHIVERY

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QHC1ymKLNKuk1DgTT5Ig5_zZEeymWyeX

# PROBLEM STATEMENT
# Delhivery is the largest and fastest-growing fully integrated player in India by revenue in Fiscal 2021. They aim to build the operating system for commerce using the insides of the data set.

# INSIDES
1. SHAPE OF THE DATA (144867, 24)

2. DATA IS MOST LIKELY TOBE FOR SEPTEMBER 2018 TO OCTOBER 2018

3. Gurgaon_Bilaspur_HB (Haryana) to MAA_Poonamallee_HB (Tamil Nadu,Gurgaon_Bilaspur_HB (Haryana) to Kolkata_Dankuni_HB (West Bengal),
Gurgaon_Bilaspur_HB (Haryana) to Bangalore_Nelmngla_H ARE THE SAGMENTS WHERE ACTUAL TIME CONSUME IS MORE BUT ORSM SYSTEM SHOWS  Chandigarh_Mehmdpur_H (Punjab) to Bangalore_Nelmngla_H (Karnataka), 
Kolkata_Dankuni_HB (West Bengal) to Bhiwandi_Mankoli_HB (Maharashtra),  Guwahati_Hub (Assam) to Delhi_Airport_H (Delhi) ARE THE SAGMENT WHERE THE TIME CONSUME IS MORE

4. Chandigarh_Mehmdpur_H (Punjab) to Bangalore_Nelmngla_H (Karnataka), Gurgaon_Bilaspur_HB (Haryana) to MAA_Poonamallee_HB (Tamil Nadu), Gurgaon_Bilaspur_HB (Haryana) to Bangalore_Nelmngla_H (Karnataka) ARE THE SAGMENT WHERE THE DISTANCE IS MAXIMUM BUT THE ORSM SYSTEM SHOWS Chandigarh_Mehmdpur_H (Punjab) to Bangalore_Nelmngla_H (Karnataka), Gurgaon_Bilaspur_HB (Haryana) to MAA_Poonamallee_HB (Tamil Nadu), Bangalore_Nelmngla_H (Karnataka) to Gurgaon_Bilaspur_HB (Haryana) ARE THE SAGMENT WHERE THE DISTANCES ARE MAXIMUM

5. FOR THE STATE OF MAHARASHTRA,KARNATAKA,HARIYANA MOST TRIPS ARE OCCURRED ie THERE ARE MORE NUMBERS OF ORDERS FROM THIS STATES

6. FOR THE CITY BANGALURU,MUMBAI,GUARGAON MOST TRIP ARE OCCURRED ie THERE ARE MORE NUMBERS OF ORDERS FROM THIS CITIES

7. IN REALITY TRIPURA,HIMACHAL PRADESH,BIHAR TAKE MORE TIME FOR A TRIP
BUT THE ORSM SYSTEM SHOWS TRIPURA,HIMACHAL PRADESH,ANDHRA PRADESH TAKES MORE TIME

8. IN REALITY TRIPURA,ANDHRA PRADESH,HIMACHAL PRADESH IS THE LONGEST ROUTE THE ORSM SYSTEM ALSO SHOWS  THE SAME

9. ACTUAL TIME,ORSM TIME,ACTUAL DISTANCE,ORSM DISTANCE ARE LOGNORMALY DISTRIBUTED

10. There is a significant difference between OSRM and actual parameters.

**HYPOTHISIS TEST RESULT**
11. for  t value : 64.2193495364768
reject the null hypothisis ie  there is diffrence in the mean ie               **actual time != orsm time**

12. t value : 0.26323309914294246
fail to reject the null hypothisis ie **od_time_diff_hour =start_scan_to_end_scan**

13. t value : 0.8381648951065266
fail to reject the null hypothisis ie                                      **actual time = segment_actual_time aggregated value**

14. t value : -5.394101351961479
reject the null hypothisis ie  there is diffrence in the mean ie              **osrm distance != segment_osrm_distance aggregated value**

15. t value : -69.2629826252443
reject the null hypothisis ie  there is diffrence in the mean ie           **osrm time < segment_actual_time  aggregated value**

16. for segment  t value : -0.12947099971100354
fail to reject the null hypothisis ie no diffrence in mean ie **od_time_diff_hour = start_scan_to_end_scan'**

# RECOMANDATION
1. THE ORSM DATA ARE NOT RELIABLE COMPARE TO REAL CASE SENARIO

2. USE NEW RECOMANDING SYSTEM

3. NEDD TO IMPROVE THE SYPLY_CHAIN ESPACIALY FOR THE HILLY REGIONS AND FOR THE NORTH EASTERN STATES

4. FOR THE STATE OF MAHARASHTRA,KARNATAKA,HARIYANA MOST TRIPS ARE OCCURRED SO THE IS NEED TO IMPROVE THE SURVICES FOR GOOD CUSTOMER SATISFACTION

5. FOR THE CITY BANGALURU,MUMBAI,GUARGAON MOST TRIP ARE OCCURRED SO THERE IS A STROG SUPLLY CHAIN

6. FOR TRIPURA,ANDHRA PRADESH,HIMACHAL PRADESH IS THE LONGEST ROUTE SO THERE IS A NEED TO FIND SHORTEST WAY FOR SEEDY DELHIVARY

7. FOR TRIPURA,ANDHRA PRADESH,HIMACHAL NEED TO START THE SERVICES LIKE FIRST DELIVARY OPTION WITH NOMINAL FEES

8. Chandigarh_Mehmdpur_H (Punjab) to Bangalore_Nelmngla_H (Karnataka), Gurgaon_Bilaspur_HB (Haryana) to MAA_Poonamallee_HB (Tamil Nadu), Gurgaon_Bilaspur_HB (Haryana) to Bangalore_Nelmngla_H (Karnataka) ARE THE SAGMENT WHERE THE DISTANCE IS MAXIMUM BUT THE ORSM SYSTEM SHOWS Chandigarh_Mehmdpur_H (Punjab) to Bangalore_Nelmngla_H (Karnataka), Gurgaon_Bilaspur_HB (Haryana) to MAA_Poonamallee_HB (Tamil Nadu), Bangalore_Nelmngla_H (Karnataka) to Gurgaon_Bilaspur_HB (Haryana) ARE THE SAGMENT WHERE THE DISTANCES ARE MAXIMUM SO THERE IS A NEED TO FIND THE WAY OF SHORTES ROUTE FOR SEEDY DEHIVERY

9. Gurgaon_Bilaspur_HB (Haryana) to MAA_Poonamallee_HB (Tamil Nadu,Gurgaon_Bilaspur_HB (Haryana) to Kolkata_Dankuni_HB (West Bengal), Gurgaon_Bilaspur_HB (Haryana) to Bangalore_Nelmngla_H ARE THE SAGMENTS WHERE ACTUAL TIME CONSUME IS MORE BUT ORSM SYSTEM SHOWS Chandigarh_Mehmdpur_H (Punjab) to Bangalore_Nelmngla_H (Karnataka), Kolkata_Dankuni_HB (West Bengal) to Bhiwandi_Mankoli_HB (Maharashtra), Guwahati_Hub (Assam) to Delhi_Airport_H (Delhi) ARE THE SAGMENT WHERE THE TIME CONSUME IS MORE NEED TO IMPROVE THE SERVICES THERE FOR SPEEEDY DELHIVERY

10. Storage, warehousing and materials handling NEED TO BE GOOD FOR MAHARASHTRA,KARNATAKA,HARIYANA
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

"""# IMPORTING DATA SET"""

df=pd.read_csv("https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/001/551/original/delhivery_data.csv?1642751181")
df.head()

df[df['trip_uuid']=='trip-153741093647649320'][['source_name','destination_name']]

"""# BASIC MATRICSES"""

df.shape

df.info()

df.nunique(axis=0)

df.isnull().sum()

df = df.dropna(how='any')
df = df.reset_index(drop=True)

df.isnull().sum()

"""# MANUPULATING DATA TYPE"""

#Converting time columns into pandas datetime
df['od_start_time'] = pd.to_datetime(df['od_start_time'])
df['od_end_time'] = pd.to_datetime(df['od_end_time'])
df.head()

df.info()

"""# CREATING NEW FEATURES"""

#cumulate the value of sagments column time
df['segment_key'] = df['trip_uuid'] + df['source_center'] + df['destination_center']

segment_cols = ['segment_actual_time', 'segment_osrm_distance', 'segment_osrm_time']

for col in segment_cols:
    df[col + '_sum'] = df.groupby('segment_key')[col].cumsum()
    
df[[col + '_sum' for col in segment_cols]]

create_segment_dict = {
    
    'data' : 'first',
    'trip_creation_time' : 'first',
    'route_schedule_uuid' : 'first',
    'route_type' : 'first',
    'trip_uuid' : 'first',
    'source_center' : 'first',
    'source_name' : 'first',
    
    'destination_center' : 'last',
    'destination_name' : 'last',
    
    'od_start_time' : 'first',
    'od_end_time' : 'first',
    'start_scan_to_end_scan' : 'first',
    
    'actual_distance_to_destination' : 'last',
    'actual_time' : 'last',
    
    'osrm_time' : 'last',
    'osrm_distance' : 'last',
    
    'segment_actual_time_sum' : 'last',
    'segment_osrm_distance_sum' : 'last',
    'segment_osrm_time_sum' : 'last',
    
}

segment = df.groupby('segment_key').agg(create_segment_dict).reset_index()
segment = segment.sort_values(by=['segment_key','od_end_time'], ascending=True).reset_index()

segment

"""## Calculate the time taken between od_start_time and od_end_time and keep it as a feature. Drop the original columns, if required"""

segment['od_time_diff_hour'] = (segment['od_end_time'] - segment['od_start_time']).dt.total_seconds() /(60)
segment

segment[['start_scan_to_end_scan','od_time_diff_hour']]

"""## Compare the difference between  od_time_diff_hour(od_start_time and od_end_time)and start_scan_to_end_scan  BY hypothesis testing/ Visual analysis to check. """

plt.figure(figsize=(10,5))
plt.subplot(1,2,1)
sns.boxplot(data=segment,y=segment["start_scan_to_end_scan"])
plt.subplot(1,2,2)
sns.boxplot(data=segment,y=segment["od_time_diff_hour"])
plt.show()

"""# looks like both of them has same median to confirm it let do the T test

# H0 :there is no diffrence in the mean ie od_time_diff_hour = start_scan_to_end_scan'
# Ha : there is diffrence in the mean ie mean of od_time_diff_hour > mean of start_scan_to_end_scan'
# significance (alpha) :0.05
"""

from scipy.stats import ttest_ind
stats,p_value=ttest_ind(segment['start_scan_to_end_scan'],segment['od_time_diff_hour'],alternative="less")
print("t value :",stats)
if p_value>0.05:
  print("fail to reject the null hypothisis ie no diffrence in mean od_time_diff_hour = start_scan_to_end_scan'")
else:
  print("reject the null hypothisis ie  there is diffrence in the mean ie mean of od_time_diff_hour > mean of start_scan_to_end_scan")

"""# BIVARIATE ANALYSIS OF SAGMENT"""

segment_city_city=segment.copy()
segment_city_city['source_to_destibnation']=segment_city_city['source_name']+" to "+segment_city_city['destination_name']
segment_city_city_=segment_city_city[['source_to_destibnation','start_scan_to_end_scan','actual_distance_to_destination']].sort_values(by='start_scan_to_end_scan',ascending=False).reset_index().drop(['index'],axis=1).head(10)
segment_city_city__=segment_city_city[['source_to_destibnation','start_scan_to_end_scan','actual_distance_to_destination']].sort_values(by='actual_distance_to_destination',ascending=False).reset_index().drop(['index'],axis=1).drop_duplicates(subset="source_to_destibnation",keep="first").head(10)

plt.figure(figsize=(20,5))
plt.subplot(1,2,1)
sns.barplot(data=segment_city_city_,x='source_to_destibnation',y="start_scan_to_end_scan")
plt.xticks(rotation=90)
plt.subplot(1,2,2)
sns.barplot(data=segment_city_city__,x='source_to_destibnation',y="actual_distance_to_destination")
plt.xticks(rotation=90)
plt.show()

segment_city_city=segment.copy()
segment_city_city['source_to_destibnation']=segment_city_city['source_name']+" to "+segment_city_city['destination_name']
segment_city_city_=segment_city_city[['source_to_destibnation','segment_actual_time_sum','segment_osrm_time_sum']].sort_values(by='segment_actual_time_sum',ascending=False).reset_index().drop(['index'],axis=1).head(10)
segment_city_city__=segment_city_city[['source_to_destibnation','segment_actual_time_sum','segment_osrm_time_sum']].sort_values(by='segment_osrm_time_sum',ascending=False).reset_index().drop(['index'],axis=1).drop_duplicates(subset="source_to_destibnation",keep="first").head(10)

plt.figure(figsize=(20,5))
plt.subplot(1,2,1)
sns.barplot(data=segment_city_city_,x='source_to_destibnation',y="segment_actual_time_sum")
plt.xticks(rotation=90)
plt.subplot(1,2,2)
sns.barplot(data=segment_city_city__,x='source_to_destibnation',y="segment_osrm_time_sum")
plt.xticks(rotation=90)
plt.show()

"""Gurgaon_Bilaspur_HB (Haryana) to MAA_Poonamallee_HB (Tamil Nadu,Gurgaon_Bilaspur_HB (Haryana) to Kolkata_Dankuni_HB (West Bengal),
Gurgaon_Bilaspur_HB (Haryana) to Bangalore_Nelmngla_H ARE THE SAGMENTS WHERE ACTUAL TIME CONSUME IS MORE BUT ORSM SYSTEM SHOWS 	Chandigarh_Mehmdpur_H (Punjab) to Bangalore_Nelmngla_H (Karnataka),	
Kolkata_Dankuni_HB (West Bengal) to Bhiwandi_Mankoli_HB (Maharashtra),	Guwahati_Hub (Assam) to Delhi_Airport_H (Delhi) ARE THE SAGMENT WHERE THE TIME CONSUME IS MORE
"""

segment_city_city=segment.copy()
segment_city_city['source_to_destibnation']=segment_city_city['source_name']+" to "+segment_city_city['destination_name']
segment_city_city_=segment_city_city[['source_to_destibnation','actual_distance_to_destination','osrm_distance']].sort_values(by='actual_distance_to_destination',ascending=False).reset_index().drop(['index'],axis=1)
segment_city_city_=segment_city_city.groupby('source_to_destibnation')['actual_distance_to_destination'].mean().to_frame().sort_values(by='actual_distance_to_destination',ascending=False).reset_index().head(10)
segment_city_city__=segment_city_city[['source_to_destibnation','segment_actual_time_sum','osrm_distance']].sort_values(by='osrm_distance',ascending=False).reset_index().drop(['index'],axis=1).drop_duplicates(subset="source_to_destibnation",keep="first").head(10)

plt.figure(figsize=(20,5))
plt.subplot(1,2,1)
sns.barplot(data=segment_city_city_,x='source_to_destibnation',y="actual_distance_to_destination")
plt.xticks(rotation=90)
plt.subplot(1,2,2)
sns.barplot(data=segment_city_city__,x='source_to_destibnation',y="osrm_distance")
plt.xticks(rotation=90)
plt.show()

"""Chandigarh_Mehmdpur_H (Punjab) to Bangalore_Nelmngla_H (Karnataka),	Gurgaon_Bilaspur_HB (Haryana) to MAA_Poonamallee_HB (Tamil Nadu),
Gurgaon_Bilaspur_HB (Haryana) to Bangalore_Nelmngla_H (Karnataka) ARE THE SAGMENT WHERE THE DISTANCE IS MAXIMUM BUT THE ORSM SYSTEM SHOWS Chandigarh_Mehmdpur_H (Punjab) to Bangalore_Nelmngla_H (Karnataka),
Gurgaon_Bilaspur_HB (Haryana) to MAA_Poonamallee_HB (Tamil Nadu),
Bangalore_Nelmngla_H (Karnataka) to Gurgaon_Bilaspur_HB (Haryana) ARE THE SAGMENT WHERE THE DISTANCES ARE MAXIMUM

# CREATING TRIPS AND ANALYS THE DATA
"""

create_trip_dict = {
    
    'data' : 'first',
    'trip_creation_time' : 'first',
    'route_schedule_uuid' : 'first',
    'route_type' : 'first',
    'trip_uuid' : 'first',
    
    'source_center' : 'first',
    'source_name' : 'first',
    
    'destination_center' : 'last',
    'destination_name' : 'last',
    
    'start_scan_to_end_scan' : 'sum',
    'od_time_diff_hour' : 'sum', 
    
    'actual_distance_to_destination' : 'sum',
    'actual_time' : 'sum',
    'osrm_time' : 'sum',
    'osrm_distance' : 'sum',
    
    'segment_actual_time_sum' : 'sum',
    'segment_osrm_distance_sum' : 'sum',
    'segment_osrm_time_sum' : 'sum',
    
}

trip = segment.groupby('trip_uuid').agg(create_trip_dict).reset_index(drop = True)
trip

trip[['actual_time', 'segment_actual_time_sum']].head()

"""# Build some features to prepare the data for actual analysis Extract features from the below fields:
# Destination Name: Split and extract features out of destination. City-place-code (State)
# Source Name: Split and extract features out of destination. City-place-code (State)
# Trip_creation_time: Extract features like month, year and day etc
"""

trip['destination_name'] = trip['destination_name'].str.lower() # lowering all columns
trip['source_name'] = trip['source_name']

def place2state(x):
    # transform "gurgaon_bilaspur_hb (haryana)" into "haryana"
    state = x.split('(')[1]
    
    return state[:-1] #removing ')' from ending

def place2city(x):
    #we will remove state
    city = x.split(' (')[0]
    
    city = city.split('_')[0]
    
    # Now daling with edge cases
          
    if city == 'pnq vadgaon sheri dpc': return 'vadgaonsheri'

    # ['PNQ Pashan DPC', 'Bhopal MP Nagar', 'HBR Layout PC',
    #  'PNQ Rahatani DPC', 'Pune Balaji Nagar', 'Mumbai Antop Hill']

    if city in ['pnq pashan dpc','pnq rahatani dpc', 'pune balaji nagar']:
        return 'pune'

    if city == 'hbr layout pc' :
        return 'bengaluru'
    if city == 'bhopal mp nagar':
        return 'bhopal'
    if city == 'mumbai antop hill':
        return 'mumbai'

    return city

def place2city_place(x):

    # we will remove state
    x = x.split('(')[0]

    len_ = len(x.split('_'))

    if len_ >= 3:
        return x.split('_')[1]

    # small cities have same city and place name
    if len_ == 2:
        return x.split('_')[0]

    # now we need to deal with edge cases or imporper name convention

    # if len(x.split('_')) == 2:

    return x.split(' ')[0]
    
def place2code(x):
    # we will remove state
    x = x.split('(')[0]

    if len(x.split('_')) >= 3:
        return x.split('_')[-1]

    return 'none'

trip['destination_state'] = trip['destination_name'].apply(lambda x: place2state(x))
trip['destination_city']  = trip['destination_name'].apply(lambda x: place2city(x))
trip['destination_place'] = trip['destination_name'].apply(lambda x: place2city_place(x))
trip['destination_code']  = trip['destination_name'].apply(lambda x: place2code(x))

trip[['destination_state','destination_city','destination_place','destination_code']]

trip['trip_creation_time'] = pd.to_datetime(trip['trip_creation_time'])

trip['trip_year'] = trip['trip_creation_time'].dt.year
trip['trip_month'] = trip['trip_creation_time'].dt.month
trip['trip_hour'] = trip['trip_creation_time'].dt.hour
trip['trip_day'] = trip['trip_creation_time'].dt.day
trip['trip_week'] = trip['trip_creation_time'].dt.isocalendar().week
trip['trip_dayofweek'] = trip['trip_creation_time'].dt.dayofweek

trip[['trip_year','trip_month','trip_hour','trip_day','trip_week','trip_dayofweek']]

trip

"""## Find outliers in numericals variable"""

num_cols = ['start_scan_to_end_scan','actual_distance_to_destination','actual_time','osrm_time',
            'osrm_distance','segment_actual_time_sum','segment_osrm_distance_sum',
           'segment_osrm_time_sum', 'od_time_diff_hour']

trip[num_cols].boxplot(rot=25, figsize=(25,8))

"""## Handle the outliers """

Q1 = trip[num_cols].quantile(0.25)
Q3 = trip[num_cols].quantile(0.75)

IQR = Q3 - Q1
trip = trip[-((trip[num_cols] < (Q1 - 1.5 * IQR)) | (trip[num_cols] > (Q3 + 1.5 * IQR))).any(axis=1)]
trip = trip.reset_index(drop=True)

trip

trip[num_cols].boxplot(rot=25, figsize=(25,8))

"""# HYPOTHISIS TESTING

# Compare the difference between od_time_diff_hour(od_start_time and od_end_time)and start_scan_to_end_scan BY hypothesis testing/ Visual analysis to check
"""

trip[['od_time_diff_hour','start_scan_to_end_scan']]

plt.figure(figsize=(10,5))
plt.subplot(1,2,1)
sns.boxplot(data=trip,y=trip["od_time_diff_hour"])
plt.subplot(1,2,2)
sns.boxplot(data=trip,y=trip["start_scan_to_end_scan"])
plt.show()

"""# looks like actual time has higher median value then osrm time to confirm the statement let do T test
# H0 : means are same ie mean of od_time_diff_hour = start_scan_to_end_scan
# Ha : means are not same ie od_time_diff_hour != start_scan_to_end_scan
# significance(alpha)=0.05
"""

from scipy.stats import ttest_ind
stats,p_value=ttest_ind(trip["od_time_diff_hour"],trip["start_scan_to_end_scan"])
print("t value :",stats)
if p_value>0.05:
  print("fail to reject the null hypothisis ie  od_time_diff_hour =start_scan_to_end_scan")
else:
  print("reject the null hypothisis ie  there is diffrence in the mean ie  od_time_diff_hour!= start_scan_to_end_scan")

"""# Do hypothesis testing/ visual analysis between actual_time aggregated value and OSRM time aggregated value"""

trip[['actual_time','osrm_time']]

plt.figure(figsize=(10,5))
plt.subplot(1,2,1)
sns.boxplot(data=trip,y=trip["actual_time"])
plt.subplot(1,2,2)
sns.boxplot(data=trip,y=trip["osrm_time"])
plt.show()

"""# looks like actual time has higher median value then osrm time to confirm the statement let do T test

# H0 : means are same ie mean of actual time = orsm time
# Ha : means are not same ie actual time != orsm time
# significance(alpha)=0.05
"""

from scipy.stats import ttest_ind
stats,p_value=ttest_ind(trip["actual_time"],trip["osrm_time"])
print("t value :",stats)
if p_value>0.05:
  print("fail to reject the null hypothisis ie  actual time = orsm time")
else:
  print("reject the null hypothisis ie  there is diffrence in the mean ie  actual time != orsm time")

"""# Do hypothesis testing/ visual analysis between actual_time aggregated value and segment actual time aggregated value (aggregated values are the values you’ll get after merging the rows on the basis of trip_uuid)"""

trip[['actual_time','segment_actual_time_sum']]

plt.figure(figsize=(10,5))
plt.subplot(1,2,1)
sns.boxplot(data=trip,y=trip["actual_time"])
plt.subplot(1,2,2)
sns.boxplot(data=trip,y=trip["segment_actual_time_sum"])
plt.show()

"""# looks like the median for actual time and segment_actual_time aggregated value is same to confirm the statement let do T test

# H0 : means are same ie mean of actual time = segment_actual_time aggregated value
# Ha : means are not same ie actual time != segment_actual_time aggregated value
# significance(alpha)=0.05
"""

from scipy.stats import ttest_ind
stats,p_value=ttest_ind(trip["actual_time"],trip["segment_actual_time_sum"])
print("t value :",stats)
if p_value>0.05:
  print("fail to reject the null hypothisis ie  actual time = segment_actual_time aggregated value")
else:
  print("reject the null hypothisis ie  there is diffrence in the mean ie  actual time != segment_actual_time_aggregated value")

"""# Do hypothesis testing/ visual analysis between osrm distance aggregated value and segment osrm distance aggregated value (aggregated values are the values you’ll get after merging the rows on the basis of trip_uuid)"""

trip[['osrm_distance','segment_osrm_distance_sum']]

plt.figure(figsize=(10,5))
plt.subplot(1,2,1)
sns.boxplot(data=trip,y=trip["osrm_distance"])
plt.subplot(1,2,2)
sns.boxplot(data=trip,y=trip["segment_osrm_distance_sum"])
plt.show()

"""# looks like both has same median values to confirm it let do T test

# H0 : means are same ie mean of osrm_distance= segment_osrm_distance aggregated value
# Ha : means are not same ie osrm_distance != segment_osrm_distance aggregated value
# significance(alpha)=0.05
"""

from scipy.stats import ttest_ind
stats,p_value=ttest_ind(trip["osrm_distance"],trip["segment_osrm_distance_sum"])
print("t value :",stats)
if p_value>0.05:
  print("fail to reject the null hypothisis ie  osrm_distance = segment_osrm_distance aggregated value")
else:
  print("reject the null hypothisis ie  there is diffrence in the mean ie  osrm distance != segment_osrm_distance aggregated value")

"""# Do hypothesis testing/ visual analysis between osrm time aggregated value and segment osrm time aggregated value (aggregated values are the values you’ll get after merging the rows on the basis of trip_uuid)"""

trip[['osrm_time','segment_actual_time_sum']]

plt.figure(figsize=(10,5))
plt.subplot(1,2,1)
sns.boxplot(data=trip,y=trip["osrm_time"])
plt.subplot(1,2,2)
sns.boxplot(data=trip,y=trip["segment_actual_time_sum"])
plt.show()

"""# looks like there is a diffrence in the median to confirm it let do the PAIR LITTLE TEST

# H0 : means are same ie mean of osrm_time= segment_actual_time aggregated value
# Ha : means are not same ie osrm_time < segment_actual_time aggregated value
# significance(alpha)=0.05
"""

from scipy.stats import ttest_rel
stats,p_value=ttest_rel(trip["osrm_time"],trip["segment_osrm_distance_sum"],alternative="less")
print("t value :",stats)
if p_value>0.05:
  print("fail to reject the null hypothisis ie  osrm_time <= segment_actual_time  aggregated value")
else:
  print("reject the null hypothisis ie  there is diffrence in the mean ie  osrm time < segment_actual_time  aggregated value")

"""#UNIVARIATE ANALYSIS FOR THE TRIP """

plt.figure(figsize=(20,10))
plt.subplot(2,2,1)
plots=sns.countplot(x=trip["trip_year"])
plt.subplot(2,2,2)
plots=sns.countplot(x=trip["trip_month"])
plt.subplot(2,2,3)
plots=sns.countplot(x=trip['destination_state'])
plt.xticks(rotation=90)

plt.show()

"""THE INTERVEL FOR WHICH THE DATA IS GIVEN IS 2018 SEPTEMBER TO OCTOBER

FOR THE STATE OF MAHARASHTRA,KARNATAKA,HARIYANA MOST TRIPS ARE OCCURED

# BIVARIATE ANALYSIS
"""

trip_top_10=trip['destination_city'].value_counts().to_frame().reset_index().rename(columns={"index":'city',"destination_city":'number_of_trip'}).head(10)

sns.barplot(x=trip_top_10["city"],y=trip_top_10["number_of_trip"])
plt.xticks(rotation=90)
plt.show()

"""FOR THE CITY BANGALURU,MUMBAI,GUARGAON MOST TRIP ARE OCCURED IE THERE ARE MORE NUMBERS OF ORDERS FROM THIS STATES"""

trip_mean_time=trip.groupby(['destination_state'])[['actual_time','osrm_time']].mean().reset_index().sort_values(by='actual_time').reset_index(drop="index")

col=["actual_time","osrm_time"]
k=1
plt.figure(figsize=(20,5))
for i in col:
  
  plt.subplot(1,2,k)
  sns.barplot(x=trip_mean_time["destination_state"],y=trip_mean_time[i])
  k+=1
  plt.xticks(rotation=90)
plt.show()

"""IN REALITY TRIPURA,HIMACHAL PRADESH,BIHAR TAKE MORE TIME FOR A TRIP
BUT THE ORSM SYSTEM SHOWS TRIPURA,HIMACHAL PRADESH,ANDHRA PRADESH TAKES MORE TIME
"""

trip_mean_distance=trip.groupby(['destination_state'])[['actual_distance_to_destination','osrm_distance']].mean().reset_index().sort_values(by='actual_distance_to_destination',ascending=False).reset_index(drop="index")

col=["actual_distance_to_destination","osrm_distance"]
k=1
plt.figure(figsize=(20,5))
for i in col:
  
  plt.subplot(1,2,k)
  sns.barplot(x=trip_mean_distance["destination_state"],y=trip_mean_distance[i])
  k+=1
  plt.xticks(rotation=90)
plt.show()

"""IN REALITY TRIPURA,ANDHRA PRADESH,HIMACHAL PRADESH IS THE LONGEST ROUTE THE ORSM SYSTEM ALSO SHOWS  THE SAME"""

col=["actual_time","osrm_time","actual_distance_to_destination","osrm_distance"]
k=1
fig=plt.figure(figsize=(20,5))
for i in col:
  plt.subplot(1,4,k)
  sns.histplot(data=trip,x=trip[i],bins=35,kde=True)
  plt.title('Distribution of'+" "+i)
  k+=1
plt.show()
plt.figure(figsize=(4,5))
sns.histplot(data=trip,x=trip["trip_hour"],bins=35,kde=True)
plt.title('Distribution of trip_hour')
plt.show()

"""ACTUAL TIME,ORSM TIME,ACTUAL DISTANCE,ORSM DISTANCE ARE LOGNORMALY DISTRIBUTED

## Handling Categorical Variables
"""

trip['route_type'].value_counts()

"""# Only two route_type-Do one hot encoding"""

trip['route_type'] = trip['route_type'].map({'FTL':0, 'Carting':1})

"""# Normalize/Standarize the numerical features using MinMaxScaler or StandardScaler"""

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
scaler.fit(trip[num_cols])

trip[num_cols] = scaler.transform(trip[num_cols])

trip[num_cols]

trip[num_cols].describe()

"""# There is a significant difference between OSRM and actual parameters."""