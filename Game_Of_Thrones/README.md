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

For the first step of this exercise we need to import the pandas, numpy and datetime libraries for that we use the code below:


```python
import pandas as pd
import numpy as np
import datetime as dt
```


```python
GoT_df = pd.read_csv('https://www.dropbox.com/s/qx1r7c872qp776y/Game_of_Thrones.csv?dl=1')
```

In the previouse cell we named our dataframe 'GoT_df'. We use the .head() method to preview the dataframe:


```python
GoT_df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Season</th>
      <th>No. of Episode (Season)</th>
      <th>No. of Episode (Overall)</th>
      <th>Title of the Episode</th>
      <th>Running Time (Minutes)</th>
      <th>Directed by</th>
      <th>Written by</th>
      <th>Original Air Date</th>
      <th>U.S. Viewers (Millions)</th>
      <th>Music by</th>
      <th>Cinematography by</th>
      <th>Editing by</th>
      <th>IMDb Rating</th>
      <th>Rotten Tomatoes Rating (Percentage)</th>
      <th>Metacritic Ratings</th>
      <th>Ordered</th>
      <th>Filming Duration</th>
      <th>Novel(s) Adapted</th>
      <th>Synopsis</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>Winter Is Coming</td>
      <td>61</td>
      <td>Tim Van Patten</td>
      <td>David Benioff, D. B. Weiss</td>
      <td>4/17/2011</td>
      <td>2.22</td>
      <td>Ramin Djawadi</td>
      <td>Alik Sakharov</td>
      <td>Oral Norrie Ottey</td>
      <td>8.9</td>
      <td>100</td>
      <td>9.1</td>
      <td>3/2/2010</td>
      <td>Second half of 2010</td>
      <td>A Game of Thrones</td>
      <td>North of the Seven Kingdoms of Westeros, Night...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>2</td>
      <td>2</td>
      <td>The Kingsroad</td>
      <td>55</td>
      <td>Tim Van Patten</td>
      <td>David Benioff, D. B. Weiss</td>
      <td>4/24/2011</td>
      <td>2.20</td>
      <td>Ramin Djawadi</td>
      <td>Alik Sakharov</td>
      <td>Oral Norrie Ottey</td>
      <td>8.6</td>
      <td>100</td>
      <td>8.9</td>
      <td>3/2/2010</td>
      <td>Second half of 2010</td>
      <td>A Game of Thrones</td>
      <td>Ned, the new Hand of the King, travels to King...</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1</td>
      <td>3</td>
      <td>3</td>
      <td>Lord Snow</td>
      <td>57</td>
      <td>Brian Kirk</td>
      <td>David Benioff, D. B. Weiss</td>
      <td>5/1/2011</td>
      <td>2.44</td>
      <td>Ramin Djawadi</td>
      <td>Marco Pontecorvo</td>
      <td>Frances Parker</td>
      <td>8.5</td>
      <td>81</td>
      <td>8.7</td>
      <td>3/2/2010</td>
      <td>Second half of 2010</td>
      <td>A Game of Thrones</td>
      <td>Ned attends the King's Small Council and learn...</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1</td>
      <td>4</td>
      <td>4</td>
      <td>Cripples, Bastards, and Broken Things</td>
      <td>55</td>
      <td>Brian Kirk</td>
      <td>Bryan Cogman</td>
      <td>5/8/2011</td>
      <td>2.45</td>
      <td>Ramin Djawadi</td>
      <td>Marco Pontecorvo</td>
      <td>Frances Parker</td>
      <td>8.6</td>
      <td>100</td>
      <td>9.1</td>
      <td>3/2/2010</td>
      <td>Second half of 2010</td>
      <td>A Game of Thrones</td>
      <td>While returning to King's Landing, Tyrion stop...</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1</td>
      <td>5</td>
      <td>5</td>
      <td>The Wolf and the Lion</td>
      <td>54</td>
      <td>Brian Kirk</td>
      <td>David Benioff, D. B. Weiss</td>
      <td>5/15/2011</td>
      <td>2.58</td>
      <td>Ramin Djawadi</td>
      <td>Marco Pontecorvo</td>
      <td>Frances Parker</td>
      <td>9.0</td>
      <td>95</td>
      <td>9.0</td>
      <td>3/2/2010</td>
      <td>Second half of 2010</td>
      <td>A Game of Thrones</td>
      <td>King Robert's eunuch spy, Varys, has uncovered...</td>
    </tr>
  </tbody>
</table>
</div>



We will then check on the data types to see if we need to make any changes:


```python
GoT_df.dtypes
```




    Season                                   int64
    No. of Episode (Season)                  int64
    No. of Episode (Overall)                 int64
    Title of the Episode                    object
    Running Time (Minutes)                   int64
    Directed by                             object
    Written by                              object
    Original Air Date                       object
    U.S. Viewers (Millions)                float64
    Music by                                object
    Cinematography by                       object
    Editing by                              object
    IMDb Rating                            float64
    Rotten Tomatoes Rating (Percentage)      int64
    Metacritic Ratings                     float64
    Ordered                                 object
    Filming Duration                        object
    Novel(s) Adapted                        object
    Synopsis                                object
    dtype: object



We can see that the Original Air Date and Ordered columns are an 'object' data type. We need to change this to a date time format:


```python
GoT_df['Original Air Date'] = pd.to_datetime(GoT_df['Original Air Date'],format = "%m/%d/%Y")
GoT_df['Ordered'] = pd.to_datetime(GoT_df['Ordered'],format = "%m/%d/%Y")
```

We then run the .dtypes method again to verify that the column is the correct data type:


```python
GoT_df.dtypes
```




    Season                                          int64
    No. of Episode (Season)                         int64
    No. of Episode (Overall)                        int64
    Title of the Episode                           object
    Running Time (Minutes)                          int64
    Directed by                                    object
    Written by                                     object
    Original Air Date                      datetime64[ns]
    U.S. Viewers (Millions)                       float64
    Music by                                       object
    Cinematography by                              object
    Editing by                                     object
    IMDb Rating                                   float64
    Rotten Tomatoes Rating (Percentage)             int64
    Metacritic Ratings                            float64
    Ordered                                datetime64[ns]
    Filming Duration                               object
    Novel(s) Adapted                               object
    Synopsis                                       object
    dtype: object



With the columns on their correct data types we can start working on our analysis. The first question we need to answer is What is the average viewership per Season? We do that with the following function:


```python
GoT_df_Season_Info = GoT_df.groupby('Season')

GoT_df_Season_Info_Views = GoT_df_Season_Info['U.S. Viewers (Millions)'].agg(np.average)

print (GoT_df_Season_Info_Views)
```

    Season
    1     2.515000
    2     3.795000
    3     4.966000
    4     6.846000
    5     6.880000
    6     7.688000
    7    10.261429
    8    11.993333
    Name: U.S. Viewers (Millions), dtype: float64
    

The second question we need to answer is What is the longest and shortest season in terms or running time?. We do that with the following function:


```python
GoT_df_Season_Info_Time = GoT_df_Season_Info['Running Time (Minutes)'].agg(np.sum)

print (GoT_df_Season_Info_Time)
```

    Season
    1    557
    2    540
    3    551
    4    542
    5    555
    6    555
    7    434
    8    423
    Name: Running Time (Minutes), dtype: int64
    

The third question we need to answer is What is the best and worst rated season? In IMDB, Rotten Tomatoes and Metatritic?. We do that with the following function:


```python
GoT_df_Season_Info_Ratings = (GoT_df_Season_Info['IMDb Rating'].agg(np.average), 
GoT_df_Season_Info['Rotten Tomatoes Rating (Percentage)'].agg(np.average), 
GoT_df_Season_Info['Metacritic Ratings'].agg(np.average))

print (GoT_df_Season_Info_Ratings)
```

    (Season
    1    8.970000
    2    8.810000
    3    8.930000
    4    9.230000
    5    8.710000
    6    8.990000
    7    9.028571
    8    6.416667
    Name: IMDb Rating, dtype: float64, Season
    1    97.100000
    2    97.000000
    3    93.700000
    4    96.700000
    5    89.500000
    6    92.400000
    7    91.857143
    8    67.833333
    Name: Rotten Tomatoes Rating (Percentage), dtype: float64, Season
    1    9.120000
    2    8.700000
    3    8.750000
    4    8.950000
    5    8.300000
    6    6.700000
    7    5.857143
    8    4.083333
    Name: Metacritic Ratings, dtype: float64)
    

As we can see for all 3 ratign systems the top rated season was season 1. The lowest rated season was Season 8.

We can export the dataframes for further analysis elsewhere


```python
GoT_df_Season_Info_Views.to_csv("C:/Users/simpl/Desktop/GoT/GoT_df_Season_Info_Views.csv")
GoT_df_Season_Info_Time.to_csv("C:/Users/simpl/Desktop/GoT/GoT_df_Season_Info_Time.csv")
GoT_df_Season_Info_Ratings.to_csv("C:/Users/simpl/Desktop/GoT/GoT_df_Season_Info_Ratings.csv")
```


    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    Cell In [14], line 3
          1 GoT_df_Season_Info_Views.to_csv("C:/Users/simpl/Desktop/GoT/GoT_df_Season_Info_Views.csv")
          2 GoT_df_Season_Info_Time.to_csv("C:/Users/simpl/Desktop/GoT/GoT_df_Season_Info_Time.csv")
    ----> 3 GoT_df_Season_Info_Ratings.to_csv("C:/Users/simpl/Desktop/GoT/GoT_df_Season_Info_Ratings.csv")
    

    AttributeError: 'tuple' object has no attribute 'to_csv'



```python

```
