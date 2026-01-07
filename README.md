# E-commerce Customer Segmentation using RFM Analysis

## 📌 Project Overview
In this project, I analyzed a real-world transactional dataset containing over 500,000 records from a UK-based online retailer. Using the **RFM (Recency, Frequency, Monetary)** framework, I segmented the customer base into distinct behavioral groups to help the marketing team drive personalized strategies and increase revenue.

## 🛠️ Technical Tools
- **Language:** Python 3.9.6
- **Libraries:** Pandas (Data Manipulation),Datetime (Time-series analysis)
- **Environment:** IDLE Python 3.9.6
- **Dataset:** [UCI Machine Learning Repository - Online Retail](https://archive.ics.uci.edu/ml/datasets/Online+Retail)

## 📊 The RFM Approach
1. **Recency ($R$):** Days since the last purchase (Lower is better).
2. **Frequency ($F$):** Total number of transactions (Higher is better).
3. **Monetary ($M$):** Total value spent (Higher is better).

### Data Cleaning Process
To ensure data integrity, I performed the following steps:
- Removed rows with missing `CustomerID`.
- Filtered out negative `Quantity` values (cancellations/returns).
- Created a `TotalSpend` column by multiplying `Quantity` and `UnitPrice`.
- Handled date-time formatting to establish a "Snapshot Date" for recency calculations.
- 

## 📈 Key Insights & Visualizations
* **Champions (Score 555):** Our most loyal customers who shop frequently and spend the most.
* **Loyal Customers:** customers who made multiple transactions
* **New Customers:** Recently acquired customers with low frequency; a prime target for welcome campaigns.
* **At-Risk Customers:** High-spending customers who haven't made a purchase in over 6 months.
* **Low Value:** One-time shopper.

### 🖥️ Power BI Implementation
I developed an interactive dashboard to visualize the RFM segments. 
- **Key Metrics:** Total Revenue, Customer Count by Segment, and Average Recency.
- **Interactivity:** Users can filter by Country to see segment distribution.
![Dashboard Preview](https://github.com/thabitha2129/ECommerce-Customer-Segmentation-RFM-Analysis./blob/main/RFM%20Dashboard.png)

## Business Questions & Insights
* **1. Who are our most valuable customers, and what is their profile?**
   - *Insight:* By filtering for Champions (RFM 555), we identified the top 5% of customers who contribute to nearly 40% of total revenue.
   - *Action:* These customers should be invited to a VIP loyalty program to maintain their high engagement.
* **2. How many customers are we at risk of losing?**
   - *Insight:* The "At Risk" and "Hibernating" segments represent 25% of our database. These are customers who haven't shopped in 6+ months.
   - *Action:* A re-activation campaign with a "We Miss You" discount could recover lost revenue.
* **3. What is the difference between a "Loyal" and a "Regular" customer?**
   - *Insight:* Loyal Customers show high frequency but average monetary spend, while Regulars shop occasionally with predictable totals.
   - *Action:* Target Loyal customers with "Bundle deals" to increase their average order value (Monetary score).
* **4. Are our "New Customers" converting into repeat buyers?**
   - *Insight:* Analysis shows a high volume of customers with a Frequency of 1.
   - *Action: *This indicates a need for a "Welcome Series" email sequence to encourage a second purchase within the first 30 days.
     
## Power BI Dashboard
* <a href="https://github.com/thabitha2129/ECommerce-Customer-Segmentation-RFM-Analysis./blob/main/RFM%20Dashboard.png">Dashboard</a>


## 💡 Business Recommendations
- **Retain Champions:** Implement a VIP loyalty program or early access to new products.
- **Win Back "At-Risk":** Launch a personalized "We Miss You" email campaign with a 15-20% discount code.
- **Nurture New Customers:** Send a follow-up "How-to" guide or a second-purchase incentive.

---
## 🚀 How to Run the Code
1. Clone this repository.
2. Ensure you have `pandas` installed: `pip install pandas`.
3. Download the dataset from UCI and place it in the `/data` folder.
4. Run the `rfm_analysis.py`.
