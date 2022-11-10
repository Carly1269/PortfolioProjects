{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "8e2c4072-2a1d-450e-a2be-e0c611c4725c",
   "metadata": {},
   "source": [
    "## Game of Thrones Analysis\n",
    "\n",
    "For the first step of this exercise we need to import the pandas, numpy and datetime libraries for that we use the code below:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "715a0e70-353f-4150-993e-3c0f276fcf5a",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "import datetime as dt"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "baa8ffc9-b97f-48f1-b5d7-7f62ee2ec491",
   "metadata": {},
   "source": [
    "The dataset is stored in Dropbox. We import it using the following code:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "d4153b6f-eec3-4667-adef-df4ae1b418cc",
   "metadata": {},
   "outputs": [],
   "source": [
    "GoT_df = pd.read_csv('https://www.dropbox.com/s/qx1r7c872qp776y/Game_of_Thrones.csv?dl=1')"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e872170f-5347-42ab-88a1-bc4c22a127db",
   "metadata": {},
   "source": [
    "In the previouse cell we named our dataframe 'GoT_df'. We use the .head() method to preview the dataframe:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "ecb8f70d-aa3d-4831-92b6-27919fddb93e",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Season</th>\n",
       "      <th>No. of Episode (Season)</th>\n",
       "      <th>No. of Episode (Overall)</th>\n",
       "      <th>Title of the Episode</th>\n",
       "      <th>Running Time (Minutes)</th>\n",
       "      <th>Directed by</th>\n",
       "      <th>Written by</th>\n",
       "      <th>Original Air Date</th>\n",
       "      <th>U.S. Viewers (Millions)</th>\n",
       "      <th>Music by</th>\n",
       "      <th>Cinematography by</th>\n",
       "      <th>Editing by</th>\n",
       "      <th>IMDb Rating</th>\n",
       "      <th>Rotten Tomatoes Rating (Percentage)</th>\n",
       "      <th>Metacritic Ratings</th>\n",
       "      <th>Ordered</th>\n",
       "      <th>Filming Duration</th>\n",
       "      <th>Novel(s) Adapted</th>\n",
       "      <th>Synopsis</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>Winter Is Coming</td>\n",
       "      <td>61</td>\n",
       "      <td>Tim Van Patten</td>\n",
       "      <td>David Benioff, D. B. Weiss</td>\n",
       "      <td>4/17/2011</td>\n",
       "      <td>2.22</td>\n",
       "      <td>Ramin Djawadi</td>\n",
       "      <td>Alik Sakharov</td>\n",
       "      <td>Oral Norrie Ottey</td>\n",
       "      <td>8.9</td>\n",
       "      <td>100</td>\n",
       "      <td>9.1</td>\n",
       "      <td>3/2/2010</td>\n",
       "      <td>Second half of 2010</td>\n",
       "      <td>A Game of Thrones</td>\n",
       "      <td>North of the Seven Kingdoms of Westeros, Night...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "      <td>2</td>\n",
       "      <td>The Kingsroad</td>\n",
       "      <td>55</td>\n",
       "      <td>Tim Van Patten</td>\n",
       "      <td>David Benioff, D. B. Weiss</td>\n",
       "      <td>4/24/2011</td>\n",
       "      <td>2.20</td>\n",
       "      <td>Ramin Djawadi</td>\n",
       "      <td>Alik Sakharov</td>\n",
       "      <td>Oral Norrie Ottey</td>\n",
       "      <td>8.6</td>\n",
       "      <td>100</td>\n",
       "      <td>8.9</td>\n",
       "      <td>3/2/2010</td>\n",
       "      <td>Second half of 2010</td>\n",
       "      <td>A Game of Thrones</td>\n",
       "      <td>Ned, the new Hand of the King, travels to King...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "      <td>3</td>\n",
       "      <td>Lord Snow</td>\n",
       "      <td>57</td>\n",
       "      <td>Brian Kirk</td>\n",
       "      <td>David Benioff, D. B. Weiss</td>\n",
       "      <td>5/1/2011</td>\n",
       "      <td>2.44</td>\n",
       "      <td>Ramin Djawadi</td>\n",
       "      <td>Marco Pontecorvo</td>\n",
       "      <td>Frances Parker</td>\n",
       "      <td>8.5</td>\n",
       "      <td>81</td>\n",
       "      <td>8.7</td>\n",
       "      <td>3/2/2010</td>\n",
       "      <td>Second half of 2010</td>\n",
       "      <td>A Game of Thrones</td>\n",
       "      <td>Ned attends the King's Small Council and learn...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>1</td>\n",
       "      <td>4</td>\n",
       "      <td>4</td>\n",
       "      <td>Cripples, Bastards, and Broken Things</td>\n",
       "      <td>55</td>\n",
       "      <td>Brian Kirk</td>\n",
       "      <td>Bryan Cogman</td>\n",
       "      <td>5/8/2011</td>\n",
       "      <td>2.45</td>\n",
       "      <td>Ramin Djawadi</td>\n",
       "      <td>Marco Pontecorvo</td>\n",
       "      <td>Frances Parker</td>\n",
       "      <td>8.6</td>\n",
       "      <td>100</td>\n",
       "      <td>9.1</td>\n",
       "      <td>3/2/2010</td>\n",
       "      <td>Second half of 2010</td>\n",
       "      <td>A Game of Thrones</td>\n",
       "      <td>While returning to King's Landing, Tyrion stop...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>1</td>\n",
       "      <td>5</td>\n",
       "      <td>5</td>\n",
       "      <td>The Wolf and the Lion</td>\n",
       "      <td>54</td>\n",
       "      <td>Brian Kirk</td>\n",
       "      <td>David Benioff, D. B. Weiss</td>\n",
       "      <td>5/15/2011</td>\n",
       "      <td>2.58</td>\n",
       "      <td>Ramin Djawadi</td>\n",
       "      <td>Marco Pontecorvo</td>\n",
       "      <td>Frances Parker</td>\n",
       "      <td>9.0</td>\n",
       "      <td>95</td>\n",
       "      <td>9.0</td>\n",
       "      <td>3/2/2010</td>\n",
       "      <td>Second half of 2010</td>\n",
       "      <td>A Game of Thrones</td>\n",
       "      <td>King Robert's eunuch spy, Varys, has uncovered...</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Season  No. of Episode (Season)  No. of Episode (Overall)  \\\n",
       "0       1                        1                         1   \n",
       "1       1                        2                         2   \n",
       "2       1                        3                         3   \n",
       "3       1                        4                         4   \n",
       "4       1                        5                         5   \n",
       "\n",
       "                    Title of the Episode  Running Time (Minutes)  \\\n",
       "0                       Winter Is Coming                      61   \n",
       "1                          The Kingsroad                      55   \n",
       "2                              Lord Snow                      57   \n",
       "3  Cripples, Bastards, and Broken Things                      55   \n",
       "4                  The Wolf and the Lion                      54   \n",
       "\n",
       "      Directed by                  Written by Original Air Date  \\\n",
       "0  Tim Van Patten  David Benioff, D. B. Weiss         4/17/2011   \n",
       "1  Tim Van Patten  David Benioff, D. B. Weiss         4/24/2011   \n",
       "2      Brian Kirk  David Benioff, D. B. Weiss          5/1/2011   \n",
       "3      Brian Kirk                Bryan Cogman          5/8/2011   \n",
       "4      Brian Kirk  David Benioff, D. B. Weiss         5/15/2011   \n",
       "\n",
       "   U.S. Viewers (Millions)       Music by Cinematography by  \\\n",
       "0                     2.22  Ramin Djawadi     Alik Sakharov   \n",
       "1                     2.20  Ramin Djawadi     Alik Sakharov   \n",
       "2                     2.44  Ramin Djawadi  Marco Pontecorvo   \n",
       "3                     2.45  Ramin Djawadi  Marco Pontecorvo   \n",
       "4                     2.58  Ramin Djawadi  Marco Pontecorvo   \n",
       "\n",
       "          Editing by  IMDb Rating  Rotten Tomatoes Rating (Percentage)  \\\n",
       "0  Oral Norrie Ottey          8.9                                  100   \n",
       "1  Oral Norrie Ottey          8.6                                  100   \n",
       "2     Frances Parker          8.5                                   81   \n",
       "3     Frances Parker          8.6                                  100   \n",
       "4     Frances Parker          9.0                                   95   \n",
       "\n",
       "   Metacritic Ratings   Ordered     Filming Duration   Novel(s) Adapted  \\\n",
       "0                 9.1  3/2/2010  Second half of 2010  A Game of Thrones   \n",
       "1                 8.9  3/2/2010  Second half of 2010  A Game of Thrones   \n",
       "2                 8.7  3/2/2010  Second half of 2010  A Game of Thrones   \n",
       "3                 9.1  3/2/2010  Second half of 2010  A Game of Thrones   \n",
       "4                 9.0  3/2/2010  Second half of 2010  A Game of Thrones   \n",
       "\n",
       "                                            Synopsis  \n",
       "0  North of the Seven Kingdoms of Westeros, Night...  \n",
       "1  Ned, the new Hand of the King, travels to King...  \n",
       "2  Ned attends the King's Small Council and learn...  \n",
       "3  While returning to King's Landing, Tyrion stop...  \n",
       "4  King Robert's eunuch spy, Varys, has uncovered...  "
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "GoT_df.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c0aa1d60-4f88-477e-b489-278f4de5f6c7",
   "metadata": {},
   "source": [
    "We will then check on the data types to see if we need to make any changes:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "7eae873f-0cea-44c6-9844-21e0c9533b54",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Season                                   int64\n",
       "No. of Episode (Season)                  int64\n",
       "No. of Episode (Overall)                 int64\n",
       "Title of the Episode                    object\n",
       "Running Time (Minutes)                   int64\n",
       "Directed by                             object\n",
       "Written by                              object\n",
       "Original Air Date                       object\n",
       "U.S. Viewers (Millions)                float64\n",
       "Music by                                object\n",
       "Cinematography by                       object\n",
       "Editing by                              object\n",
       "IMDb Rating                            float64\n",
       "Rotten Tomatoes Rating (Percentage)      int64\n",
       "Metacritic Ratings                     float64\n",
       "Ordered                                 object\n",
       "Filming Duration                        object\n",
       "Novel(s) Adapted                        object\n",
       "Synopsis                                object\n",
       "dtype: object"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "GoT_df.dtypes"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f7601ce5-38f8-4b2b-a09d-1e6d37900f48",
   "metadata": {},
   "source": [
    "We can see that the Original Air Date and Ordered columns are an 'object' data type. We need to change this to a date time format:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "7ba310fd-d950-474e-b661-69fc3de0c257",
   "metadata": {},
   "outputs": [],
   "source": [
    "GoT_df['Original Air Date'] = pd.to_datetime(GoT_df['Original Air Date'],format = \"%m/%d/%Y\")\n",
    "GoT_df['Ordered'] = pd.to_datetime(GoT_df['Ordered'],format = \"%m/%d/%Y\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ab67ef78-0b91-494f-a2ab-69fd7255af35",
   "metadata": {},
   "source": [
    "We then run the .dtypes method again to verify that the column is the correct data type:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "93a8fcf8-3738-4cbc-ae33-1b7827bc929e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Season                                          int64\n",
       "No. of Episode (Season)                         int64\n",
       "No. of Episode (Overall)                        int64\n",
       "Title of the Episode                           object\n",
       "Running Time (Minutes)                          int64\n",
       "Directed by                                    object\n",
       "Written by                                     object\n",
       "Original Air Date                      datetime64[ns]\n",
       "U.S. Viewers (Millions)                       float64\n",
       "Music by                                       object\n",
       "Cinematography by                              object\n",
       "Editing by                                     object\n",
       "IMDb Rating                                   float64\n",
       "Rotten Tomatoes Rating (Percentage)             int64\n",
       "Metacritic Ratings                            float64\n",
       "Ordered                                datetime64[ns]\n",
       "Filming Duration                               object\n",
       "Novel(s) Adapted                               object\n",
       "Synopsis                                       object\n",
       "dtype: object"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "GoT_df.dtypes"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d6a8f09a-8d57-4afe-9e14-002a81004335",
   "metadata": {},
   "source": [
    "With the columns on their correct data types we can start working on our analysis. The first question we need to answer is What is the average viewership per Season. We do that with the following function:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "fe74ff86-f08c-4589-bbc5-442f97cf6210",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Season\n",
      "1     2.515000\n",
      "2     3.795000\n",
      "3     4.966000\n",
      "4     6.846000\n",
      "5     6.880000\n",
      "6     7.688000\n",
      "7    10.261429\n",
      "8    11.993333\n",
      "Name: U.S. Viewers (Millions), dtype: float64\n"
     ]
    }
   ],
   "source": [
    "GoT_df_Season_Info = GoT_df.groupby('Season')\n",
    "\n",
    "GoT_df_Season_Info_Views = GoT_df_Season_Info['U.S. Viewers (Millions)'].agg(np.average)\n",
    "\n",
    "print (GoT_df_Season_Info_Views)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "afbab8a4-41e7-4952-85f2-ae43b181f015",
   "metadata": {
    "tags": []
   },
   "source": [
    "The second question we need to answer is What is the longest and shortest season in terms or running time?. We do that with the following function:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "ffb79fa0-f24d-4e4f-85c3-085dc0c44104",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Season\n",
      "1    557\n",
      "2    540\n",
      "3    551\n",
      "4    542\n",
      "5    555\n",
      "6    555\n",
      "7    434\n",
      "8    423\n",
      "Name: Running Time (Minutes), dtype: int64\n"
     ]
    }
   ],
   "source": [
    "GoT_df_Season_Info_Time = GoT_df_Season_Info['Running Time (Minutes)'].agg(np.sum)\n",
    "\n",
    "print (GoT_df_Season_Info_Time)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "243486d4-f1bc-4c4e-bc85-ab00647fe376",
   "metadata": {
    "tags": []
   },
   "source": [
    "The third question we need to answer is What is the best and worst rated season? In both IMDB, Rotten Tomatoes and Metatritic?. We do that with the following function:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "fe309847-ae6b-4579-aceb-603ef3f31d89",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(Season\n",
      "1    8.970000\n",
      "2    8.810000\n",
      "3    8.930000\n",
      "4    9.230000\n",
      "5    8.710000\n",
      "6    8.990000\n",
      "7    9.028571\n",
      "8    6.416667\n",
      "Name: IMDb Rating, dtype: float64, Season\n",
      "1    97.100000\n",
      "2    97.000000\n",
      "3    93.700000\n",
      "4    96.700000\n",
      "5    89.500000\n",
      "6    92.400000\n",
      "7    91.857143\n",
      "8    67.833333\n",
      "Name: Rotten Tomatoes Rating (Percentage), dtype: float64, Season\n",
      "1    9.120000\n",
      "2    8.700000\n",
      "3    8.750000\n",
      "4    8.950000\n",
      "5    8.300000\n",
      "6    6.700000\n",
      "7    5.857143\n",
      "8    4.083333\n",
      "Name: Metacritic Ratings, dtype: float64)\n"
     ]
    }
   ],
   "source": [
    "GoT_df_Season_Info_Ratings = (GoT_df_Season_Info['IMDb Rating'].agg(np.average), \n",
    "GoT_df_Season_Info['Rotten Tomatoes Rating (Percentage)'].agg(np.average), \n",
    "GoT_df_Season_Info['Metacritic Ratings'].agg(np.average))\n",
    "\n",
    "print (GoT_df_Season_Info_Ratings)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0e303e1c-19be-4592-be3b-6fd9c138d79d",
   "metadata": {},
   "source": [
    "As we can see for all 3 ratign systems the top rated season was season 1. The lowest rated season was Season 8"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
