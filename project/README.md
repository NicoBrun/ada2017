# Amazon, the quest of the same products

# Abstract
Web-based marketplaces turned gigantic. As a result, a customer looking for a specific item will get hundreds of results, ranging from comparable to identic items. Our goal is to find out more about these duplicate items : among similar items, why is one version more frequently purchased than the others ? Is the choice more related to the price, ranking, or overall mood of the reviews ? Do the priorities change depending on the category the customers are interested in?  
We aim to answer these questions using the amazon products and reviews dataset.


# Research questions
* What correlations can we establish between the popularity of a product on amazon (i.e. its salesRank) and various parameters such as it's price, the customer's ratings, the mood of the review,...etc ?
* Can we find out peaks in interest in certain products (typically by measuring the number of review in a given time period) after certain important events? (e.g. natural disaster, worldwide sport contests, ...)
* Can we show a variation in the online shopping habits of people by looking at the interest in categories of items over an extended time period? (10 years or more)
* On Amazon, why an item is more popular and is sold more than its duplicate?
* What are the parameters that define that an item is better than its equivalent?


# Dataset
We want to use the Amazon datasets provided in the course, both the review and the metadata dataset. (So at most 20 + 3.1 gb in Json). 
In practice, we will probably aggregate the various "per-category" datasets, in order to be able to keep track of the origin of each item and keep as much information as possible.
Since we're very interested in the amount of reviews as a metric of interest, we will restrict our data to the 5-core dataset, as to have at least a few reviews per product.
We need to group all the Amazon items by duplicates and decide which are useful for our project. 
The popularity of sale of an item will be computed primrily with its salesRank parameter. 
The subtle part will be to find out which items are duplicates. For that we will use the title, price, also_viewed, also_bought, categories and brand as useful informations.


# A list of internal milestones up until project milestone 2
* Define the useful feature
* Select the categories of product we want to analyze (Amazon has 24 categories of item)
* Import data per category, add useful tracking informations, and merge together all selected categories
* Clean the data
* Think about how to present the project in term of data visualization
* Have our first results


# Questions for TAa
* Is this project realisable under the topic “data science for social good”?
* It's unclear wether salesRanks are computed "per category"  or over all categories. Specifically, we understood that it is an indicator for the amount of sales that we can compare among items to find out which were the most sold. Can we compare it across categories, or is this parameter comparable only within a product category
* We concluded there's no better way to measure the number of sales than the 'salesRank' parameter. Is this correct ? 
* Isn't it strange to have homeworks and project at the same time regarding the amount of work?


