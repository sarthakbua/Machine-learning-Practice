# Problem Statement

Airbnb provides a platform for hosts to accommodate guests with short-term lodging and tourism-related activities. Since 2008, guests and hosts have used Airbnb to travel in a more unique, personalized way. As part of the Airbnb Inside initiative, this data describes the listing activity & pricing of home-stays in Seattle & Boston. We are trying to see if there are any similarities or glaring differences in terms of listings and pricing over a years time.

## Data Understanding
The following Airbnb activity is included in Seattle & Boston datasets:
1.	Listings, including other features that are available in the listing and also the review score
2.	Reviews, includes the listing and the detailed comments
3.	Calendar, containing the listing and the price associated.

## Questions
1.	What do we understand about the availability of litings and their price over time
2.	What are the most common amenities
3.	Which areas are popular by way of rating score
4.	What do we understand from the sentiments of people writing reviews

## Data Preparation
1.	Cleanup
i.	Imputing "available" to 1 & 0 from t and f
ii.	Change data type to date
iii.	Removing comma & $ sign from price and converting NaN to zero
2.	Categorical Variables Handling
i.	Once the first subset of fields was identified, dummies were created and imputation was done for null and binary values in the idea of applying algorithms at a later point
ii.	Treatment and cleanup of categorical fields like example - host_is_a_superhost, host_acceptance_rate, host_response_rate, security_deposit, price, celaning_fee and amenities. I thought these would be important towards selection of a place to stay. Except for amenities all other fields had unnecessary charaters removed, null values imputed and also dummies created
iii.	Amenities field -- multivalued -- it has several values separated by a delimiter. we created a list of the top to amernies based on the count(most common)
iv.	Fields with maximum null values have been removed
v.	As part of the comparative analysis, no machine learning algorithm was applied but based on my analysis of Seattle's data, there were multiple errors i recieved as the algorithm will not accept null values and works well. Most of the ML Algorithms accept only Numerical data as input. Null values adversely affect the performance and accuracy of any ML algorithm
vi.	Deleting license because of null, and other fields like 'experiences_offered','market','jurisdiction_names' as they may not have significant influence
3.	Identifying features that significantly influence pricing. Used Pearson Correlation to get a sense of the attrbutes that correlate more with pricing. Use the remaining columns and do another round of cleanup

## Result
1.	Availability & Price over Time Overall it seems Seattle has listings available consistently across the year when compared to Boston. In terms of pricing, Boston seems to match or is more pricey during the year except the big dip when compared to prices in Seattle. Average price of Boston listing over the year is $ 98 and $92.5 in Seattle Seattle has more listings, perhaps being the reason for lower price than Boston Boston has more listings concentrated towards the city and could be the reason for increased pricing More reviews have been posted for listings in Seattle than that of Boston, probably because of the number of listings and could also be the visiting preference Seattle has more private rooms and home listings than Boston
2.	Popularity by Review score rating and Sentiment analysis
We listed the popular places to stay with listing includes location with at least 10 reviews. This is based on review rating score In Seattle popular listings seem to be distributed across south and cetral areas whereas in Boston all are certally located
3.	Sentiment Analysis
Sentiment Analysis using polarity score does not tell us whether Good review correlates with prices. However it does show that moving from those places with good polarity scores to lower polarity scores does show a slight decline in prices. A lot of the higher priced locales seem to have a very low polarity score. So any conclusion here requires more analysis Sentiment Analysis reinforces the findings from review score rating. the top neighborhoods are an almost match in terms of where people have expressed positive comments

Extra --
Modeling for Seattle
1.	Create train and test data sets using the cleansed features
2.	Important Features - "neighbourhood_cleansed","guests_included", "property_type","room_type", "accommodates", "bathrooms", "bedrooms", "beds", "price", "number_of_reviews", "cancellation_policy", 'security_deposit', "reviews_per_month", 'cleaning_fee', 'amenities'
3.	Applied Linear regression Based on the chart, the model is not doing really well in predicting the price.We should analyze more and apply other algorithms like Random Forest to see what the outcome is.


