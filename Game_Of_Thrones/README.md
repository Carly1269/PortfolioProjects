# Game of Thrones Analysis


## Introduction

For this project we are working on the analytics for the Game of Thrones television series. The dataset can be downloaded by 
[clicking here](https://www.kaggle.com/datasets/iamsouravbanerjee/game-of-thrones-dataset)

For the purpose of this project we will be using **Python** with the **NumPy** and **Pandas** libaries. We will also use the datetime library for some data type conversions.

## ASK


There are some specific questions that need to be anwered for this dataset. These questions are:
What is the average viewership per Season? 
What is the longest and shortest season in terms or running time?
What is the best and worst rated season? In IMDB, Rotten Tomatoes and Metatritic?

## Python
### Preparing the dataset

eason 	No. of Episode (Season) 	No. of Episode (Overall) 	Title of the Episode 	Running Time (Minutes) 	Directed by 	Written by 	Original Air Date 	U.S. Viewers (Millions) 	Music by 	Cinematography by 	Editing by 	IMDb Rating 	Rotten Tomatoes Rating (Percentage) 	Metacritic Ratings 	Ordered 	Filming Duration 	Novel(s) Adapted 	Synopsis
0 	1 	1 	1 	Winter Is Coming 	61 	Tim Van Patten 	David Benioff, D. B. Weiss 	4/17/2011 	2.22 	Ramin Djawadi 	Alik Sakharov 	Oral Norrie Ottey 	8.9 	100 	9.1 	3/2/2010 	Second half of 2010 	A Game of Thrones 	North of the Seven Kingdoms of Westeros, Night...
1 	1 	2 	2 	The Kingsroad 	55 	Tim Van Patten 	David Benioff, D. B. Weiss 	4/24/2011 	2.20 	Ramin Djawadi 	Alik Sakharov 	Oral Norrie Ottey 	8.6 	100 	8.9 	3/2/2010 	Second half of 2010 	A Game of Thrones 	Ned, the new Hand of the King, travels to King...
2 	1 	3 	3 	Lord Snow 	57 	Brian Kirk 	David Benioff, D. B. Weiss 	5/1/2011 	2.44 	Ramin Djawadi 	Marco Pontecorvo 	Frances Parker 	8.5 	81 	8.7 	3/2/2010 	Second half of 2010 	A Game of Thrones 	Ned attends the King's Small Council and learn...
3 	1 	4 	4 	Cripples, Bastards, and Broken Things 	55 	Brian Kirk 	Bryan Cogman 	5/8/2011 	2.45 	Ramin Djawadi 	Marco Pontecorvo 	Frances Parker 	8.6 	100 	9.1 	3/2/2010 	Second half of 2010 	A Game of Thrones 	While returning to King's Landing, Tyrion stop...
4 	1 	5 	5 	The Wolf and the Lion 	54 	Brian Kirk 	David Benioff, D. B. Weiss 	5/15/2011 	2.58 	Ramin Djawadi 	Marco Pontecorvo 	Frances Parker 	9.0 	95 	9.0 	3/2/2010 	Second half of 2010 	A Game of Thrones 	King Robert's eunuch spy, Varys, has uncovered...
