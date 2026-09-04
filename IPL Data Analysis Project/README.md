# 🏏 IPL Data Analysis

This project performs **Exploratory Data Analysis (EDA)** on IPL match data using **Pandas, NumPy, Seaborn, and Matplotlib**.

The main purpose of this project is to explore IPL match data and extract useful insights about teams, players, toss decisions, match victories, batting performances, bowling performances, venues, and winning margins.

## 📌 Project Objectives

* Analyze IPL match-winning teams
* Analyze toss decision trends
* Find how often the toss winner also wins the match
* Analyze how teams win matches (Runs/Wickets)
* Find the top Players of the Match
* Find the top 2 run scorers based on their recorded high scores
* Find the top 10 bowlers based on bowling figures
* Find venues where the most matches were played
* Find the match won by the highest run margin
* Find the highest individual score
* Find the best bowling figure

## 🛠️ Libraries Used

* **Pandas** – Data loading, cleaning, grouping, filtering, and analysis
* **NumPy** – Numerical operations
* **Seaborn** – Statistical data visualization
* **Matplotlib** – Creating and displaying plots

## 📂 Dataset

The project uses an IPL dataset named:

`ipl.22.csv`

The dataset contains information about IPL matches, including:

* Match ID
* Match winner
* Toss winner
* Toss decision
* Winning method
* Winning margin
* Venue
* Player of the Match
* Top scorer
* High score
* Best bowling
* Best bowling figures

## 🔍 Data Exploration

The project starts by loading the dataset and inspecting its structure.

```python
df = pd.read_csv('ipl.22.csv')

df.head()
df.info()

print(f"your rows are {df.shape[0]} and your columns are {df.shape[1]}")

print(df.isnull().sum())
```

This helps identify:

* Number of rows and columns
* Data types
* Missing values
* Basic structure of the dataset

## 📊 Data Visualization

### 1. Most Matches Won by Teams

A bar plot is used to identify which teams have won the most matches.

```python
match_win = df['match_winner'].value_counts()

sns.barplot(
    y=match_win.index,
    x=match_win.values
)
```

### 2. Toss Decision Trends

A count plot is used to analyze the decisions teams make after winning the toss.

```python
sns.countplot(x=df['toss_decision'])
```

This helps understand whether teams generally prefer **batting** or **fielding** after winning the toss.

### 3. Toss Winner vs Match Winner

The project calculates the percentage of matches where the team winning the toss also won the match.

```python
toss_and_winner_count = df[
    df["toss_winner"] == df["match_winner"]
]['match_id'].count()

mean = (toss_and_winner_count / df.shape[0]) * 100
```

### 4. How Do Teams Win?

A count plot is used to analyze whether teams usually win by:

* Runs
* Wickets

```python
sns.countplot(x=df['won_by'])
```

### 5. Top 10 Players of the Match

The project finds the 10 players who received the **Player of the Match** award most frequently.

```python
player_of_match = df["player_of_the_match"].value_counts().head(10)
```

A bar plot is then used to visualize the results.

### 6. Top 2 Scorers

The project groups the data by top scorer and calculates the sum of their recorded high scores.

```python
top_scorars = df.groupby('top_scorer')["highscore"] \
    .sum() \
    .sort_values(ascending=False) \
    .head(2)
```

### 7. Top 10 Bowlers

The bowling figures are processed to extract the number of wickets.

```python
def fa(a):
    return a.split('--')[0]

df['highest_wickets'] = df['best_bowling_figures'].apply(fa)
df['highest_wickets'] = df['highest_wickets'].astype(int)
```

The top 10 bowlers are then identified using `groupby()` and `sort_values()`.

### 8. Most Matches Played at a Venue

The project counts the number of matches played at each venue.

```python
venue_count = df['venue'].value_counts()
```

A bar plot is used to visualize the venues with the highest number of matches.

### 9. Highest Winning Margin by Runs

The project finds the match with the highest winning margin when the victory was by runs.

```python
df[df["won_by"] == 'Runs'] \
    .sort_values(by="margin", ascending=False) \
    .head(1)
```

### 10. Highest Individual Score

The player with the highest recorded individual score is identified using:

```python
df[df['highscore'] == df['highscore'].max()]
```

### 11. Best Bowling Figure

The project extracts the wicket count from the bowling figures and finds the highest bowling performance.

```python
df['highest_wickets'] = df['best_bowling_figures'].apply(fa)
df['highest_wickets'] = df['highest_wickets'].astype(int)
```

## 📚 Pandas Concepts Practiced

This project helped practice several important Pandas concepts:

* `read_csv()`
* `head()`
* `info()`
* `shape`
* `isnull().sum()`
* `value_counts()`
* `groupby()`
* `sum()`
* `sort_values()`
* `head()`
* Boolean filtering
* `apply()`
* `astype()`
* Creating new columns

## 📈 Visualization Concepts Practiced

* Bar plots
* Count plots
* Horizontal bar plots
* Matplotlib figure/subplot concepts
* Seaborn visualization

## 🎯 Key Learning

Through this project, I practiced how to:

1. Load a real-world dataset.
2. Explore its structure and missing values.
3. Filter and group data.
4. Perform calculations on columns.
5. Create new columns from existing data.
6. Extract useful information from string values.
7. Visualize categorical data.
8. Find useful insights from IPL match data.

## 🚀 Future Improvements

* Add more detailed statistical analysis.
* Analyze team performance season-wise.
* Analyze player performance across seasons.
* Create interactive dashboards.
* Add correlation analysis.
* Perform more advanced EDA.
* Add additional IPL datasets for deeper analysis.

## 👨‍💻 Author

**Basharat Jutt**

This project was created as part of my journey to learn **Python, Pandas, Data Analysis, and Data Visualization**.
