import pandas as pd
import datetime as dt
#load dataset
data=pd.read_excel('data\Online_Retail.xlsx")
#Remove Null value
data.isna().any()
data=data.dropna(subset=['CustomerID'])
#Remove -ve vlues
data=data[(data['Quantity']>0)&(data['UnitPrice']>0)]
data['TotalSum']=data['Quantity']*data['UnitPrice']
#print(data['totalsum'])
data['InvoiceDate']=pd.to_datetime(data['InvoiceDate'])
#print(data['InvoiceDate'])
print(data.shape[0])
# Create a snapshot date (one day after the last purchase in the dataset)
snapshot_date = data['InvoiceDate'].max() + dt.timedelta(days=1)
print(snapshot_date)
# Aggregate data by CustomerID
rfm_data = data.groupby('CustomerID').agg({
    'InvoiceDate': lambda x: (snapshot_date - x.max()).days,
    'InvoiceNo': 'count',
    'TotalSum': 'sum'
})
# Rename columns to be human-readable
rfm_data.rename(columns={
    'InvoiceDate': 'Recency',
    'InvoiceNo': 'Frequency',
    'TotalSum': 'Monetary'
}, inplace=True)
print(data.shape)
r_labels=range(5,0,-1)
f_labels=range(1,6)
m_labels=range(1,6)
rfm_data['R']=pd.qcut(rfm_data['Recency'],q=5,labels=r_labels)
rfm_data['F']=pd.qcut(rfm_data['Frequency'].rank(method='first'),q=5,labels=f_labels)
rfm_data['M']=pd.qcut(rfm_data['Monetary'],q=5,labels=r_labels)
rfm_data['RFM_Score']=rfm_data.R.astype(str)+rfm_data.F.astype(str)+rfm_data.M.astype(str)
#defining RFM segments
def segment_me(data):
    if data['RFM_Score'] == '555':
        return 'Champions'
    elif data['F']==5:
        return 'Loyal customers'
    elif data['R'] == 5:
        return 'New Customers'
    elif data['R']<= 2 and data['M'] == 5:
        return 'At Risk'
    elif data['M'] == 1:
        return 'Low Value'
    else:
        return 'Regulars'
rfm_data['Customer_Tag'] = rfm_data.apply(segment_me, axis=1)
# Count how many customers are in each segment
segment_counts = rfm_data['Customer_Tag'].value_counts()
print(rfm_data.head())
#exporting processed data
final_export=data.merge(rfm_data,on='CustomerID',how='left')
final_export.to_csv('master_rfm.csv',index=False)
print(f"file saved successfully with{len(final_export)}rows.")


