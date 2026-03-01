# Video Game Sales Analysis & Platform Metadata Project

## What This Project Is

For this project, I worked with a global video game sales dataset and improved it by adding extra platform information using pandas merges in Python.
The original dataset shows how much each game sold in different regions, but it doesn’t tell you much about the actual console. So I created a second dataset with platform details (like manufacturer, console type, release year, and generation) and joined it to the main dataset. 

The goal was to make the data more complete and better for analysis.


## Dataset Used

Video Game Sales Dataset (Kaggle):  
https://www.kaggle.com/datasets/gregorut/videogamesales/data  

The dataset includes:
- Game name
- Platform
- Year
- Genre
- Publisher
- Regional sales (NA, EU, JP, Other)
- Global sales


## What I Added

I created a second dataset that includes:
- Manufacturer (Sony, Microsoft, Nintendo, etc.)
- Console type (Home, Handheld, PC)
- Platform release year
- Console generation

This lets us analyze things like:
- Which company performs better overall
- Whether handheld or home consoles sell more
- If newer generations perform differently

## How I Joined the Data

I used a **left join** in pandas:


merged = pd.merge(vgsales, platform_meta, how="left", on="Platform")


## Key Outcome

The final merged dataset contains 16,598 rows and 15 columns.
The left join preserved all original game records while adding console metadata.
Some NA values appear when platform metadata did not exist for a key.
