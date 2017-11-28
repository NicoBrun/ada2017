# The Post Mortem Cult of Celebrities  

# Abstract

It is often said, ironically, that Van Gogh never sold a painting in his lifetime while he is one of the most famous painters in history.
Is this an isolated case? Is it possible that society has a greater interest in the works of deceased personalities rather than those of their contemporaries? And if so, is this interest more marked when the news is still fresh?
The following project aims to analyze the effect of artists / authors’ death on sales of their own work. 
It starts with the hypothesis that a real societal phenomenon exists, which we will call "post-mortem worship", according to which people feel more interested in the works of artists / authors after their recent decease.
The second assumption, is that this phenomenon can be reduced to the artistic and literary community, which are those concerned with mass celebrity. The last assumption is that the current means of communication allow the whole society concerned, in this case American, to know the news few time after the event. Especially if it is about well-known people.

By working on data from Amazon, the giant of online commerce, and Wikipedia, the most famous encyclopedia of the web, it is possible to test the post-mortem worship effect.
Indeed, the first part of this project consisted of the extraction of the data of interest from Amazon and Wikipedia. This required to filter Amazon data to contain only the required cathegories, clean it and store it in a convenient format for future implementations.
Otherwise, the list of authors deceased in the time interval corresponding to Amazon's data, was scrapped from Wikipedia and stored in a compact and easy-to-use format.  
The second part of the research will be based on the extraction of quantifiable features (interest in the form of number of reviews, appraisal index of reviews, temporal dimensionnality...) in order to allow a mathematical analysis of the data.
The last conclusions will be drawn based on mathematical results and hypothesis testing.


# Research questions
* When a author/artist died, What trend of popularity occurs on their related product on amazon? (For an author; it's book, for an actor; related movies,... etc)
* What's this impact in function of the type of artwork the author/artist did? (musics/books/films/...)


# Dataset
We want to use the Amazon datasets provided in the course, both the review and the metadata dataset. (So at most 20 + 3.1 gb in Json). 
But we will use only specific categories related the creation by an author/artist. (musics/books/films/...)
Since we're very interested in the amount of reviews as a metric of interest, we will restrict our data to the 5-core dataset, as to have at least a few reviews per product.
The interest rate in function of time will be computed with the help of the review content and their dates. (text analysis)
To correlate this interest rate, we will need artists'/authors' death and their corresponding work. For this we will use Wikipedia and scrap the useful data needed for our project.

To match the works of an artist/author to his corresponding product on amazon, we will extends the metadata dataset with the Amazon product API. This way is far easier than any scraping we could do. 


# A list of internal milestones up until project milestone 2
* Define the useful features *finished 100%*
* Select the categories of product in Amazon containing works of authors/artists (Amazon has 24 categories of item) *finished 100%*
* Scrap the death of artists/authors of the N last years *finished 100%*
* Match the dead artist with all corresponding amazon product. *finished 50% (code is 90% done but it needs **runtime**(3-4 days) to build the dataset locally)*
* Clean the data *finished 70% (need the built dataset locally)*

# A list of internal milestones up until project milestone 3

* Filtering:
* * keep only the artists which allow an unbiased analysis, i.e with enough total reviews and comparable time availability of reviews before and after death
* Extracting features:
* * compute interest metrics using reviews frequency/ratings/.. before and after death
* * look for mentions showing interest for the artist, or interest for its recent death in the reviews text
* * compare the before/after results with statistical tests
* * make the analysis at a higher level: per-category results, global result
* write the 4-pages PDF report


