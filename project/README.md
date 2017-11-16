# The Post Mortem Cult of Celebrities  

# COMMENT

Super idée à mon avis ! Vous pourriez même compléter en essayant d'également "clusteré" les morts similaires pour voir s'il en resort des groupes particuliers par exemple. Attention toutefois à ne pas perdre trop de temps à miner wikipedia, uniquement ce qui est nécessaire. En poussant d'avantage, vous pourriez même peut-être détecter la mort d'auteur/chanteur basée sur les signaux que vous analysez.

# Abstract
At each celebrity's death, there is ...

# Research questions
* When a author/artist died, What trend of popularity occurs on their related product on amazon? (For an author; it's book, for an actor; related movies,... etc)
* What's this impact in function of the type of artwork the author/artist did? (musics/books/films/...)


# Dataset
We want to use the Amazon datasets provided in the course, both the review and the metadata dataset. (So at most 20 + 3.1 gb in Json). 
But we will use only specific categories related the creation by an author/artist. (musics/books/films/...)
Since we're very interested in the amount of reviews as a metric of interest, we will restrict our data to the 5-core dataset, as to have at least a few reviews per product.
The interest rate in function of time will be computed with the help of the review content and their dates. (text analysis)
To correlate this interest rate, we will need artists'/authors' death and their corresponding work. For this we will use Wikipedia and scrap the useful data needed for our project.
One hard part will be to match  the works of an artist/author to corresponding product on amazon. 


# A list of internal milestones up until project milestone 2
* Define the useful feature
* Select the categories of product in Amazon containing works of authors/artists (Amazon has 24 categories of item)
* Scrap the death of artists/authors of the N last years, match it with all it's work, then match it with all corresponding amazon product.
* Clean the data
* Think about how to present the project in term of data visualization
* Have our first results


# Questions for TAa
* Is this project realisable under the topic “data science for social good”?
* It's unclear wether salesRanks are computed "per category"  or over all categories.(in the Amazon metadata db) Specifically, we understood that it is an indicator for the amount of sales that we can compare among items to find out which were the most sold. Can we compare it across categories, or is this parameter comparable only within a product category
* We concluded there's no better way to measure the number of sales than the 'salesRank' parameter. Is this correct ? 
* Isn't it strange to have homeworks and project at the same time regarding the amount of work?


