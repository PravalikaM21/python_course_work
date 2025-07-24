#Hotstar Content Details:
'''
Content ID (int)    - Unique ID
Content Title (str) - Movie/Show name
Genre(s) (list)     - Comma-separated list
Rating (float)      - Viewer rating out of 10
Languages Available (set) - Comma-separated languages
Availability (tuple) - Subscribed or Free, and Region
Watch Percentage(float) - How much of the content is watched
Cast & Crew (dict)   - Director, Main Actor, Production House
Release Year (int)   - Year of release (e.g.: 2023)
Duration (minutes) (float) - Total length of content (e.g.: 145.5)
Content Type (str) - Movie or Web Series (e.g.: "Movie")
Seasons and Episodes (tuple) - If a series (e.g.: (2, 18) → 2 Seasons, 18 Episodes)
Awards Won (set) - Unique awardsn (e.g.: {"Best Director", "Best Script"})
User Reviews (list) - Viewer feedback (e.g.: ["Amazing", "Must-watch", "Great acting"])
Subscription Plans (dict) - Plan type with price (e.g.: {"Monthly": 299, "Yearly": 999})
Has Subtitles (bool) - True or False (e.g.: True)
Age Rating (str) - Censor board rating
'''

# 1. Content ID - int
content_id = int(input("Enter Content ID: "))
print("Content ID:", type(content_id))

# 2. Content Title - str
title = input("Enter Content Title: ")
print("Title:", type(title))

# 3. Rating - float
rating = float(input("Enter Rating out of 10: "))
print("Rating:", type(rating))

# 4. Genres - list
genres_input = input("Enter Genres (comma-separated): ")
genres = genres_input.split(',')  # Converts string to list
print("Genres:", type(genres))

# 5. Languages - set
languages_input = input("Enter Available Languages (comma-separated): ")
languages = set(languages_input.split(','))  # Converts to set to remove duplicates
print("Languages:", type(languages))

# 6. Availability - tuple
subscription = input("Enter Subscription Type (Free/Subscribed): ")
region = input("Enter Region: ")
availability = (subscription, region)  # Tuple
print("Availability:", type(availability))

# 7. Cast & Crew - dict
director = input("Enter Director Name: ")
actor = input("Enter Main Actor Name: ")
production = input("Enter Production House: ")
crew = {"Director": director,"Actor": actor,"Production": production}
print("Cast & Crew:", type(crew))

# 8.Release Year - int
release_year = int(input("Enter Release Year: "))

# 9.Duration - float
duration = float(input("Enter Duration in minutes: "))

# 10. Content Type -  str
content_type = input("Enter Content Type (Movie/Series): ")

# 11. Seasons and Episodes - tuple
seasons = int(input("Enter Number of Seasons: "))
episodes = int(input("Enter Number of Episodes: "))
seasons_episodes = (seasons, episodes)

# 12. Awards Won - set
awards = set(input("Enter Awards Won (comma-separated): ").split(','))

# 13. User Reviews - list 
reviews = input("Enter User Reviews (comma-separated): ").split(',')

# 14. Subscription Plans - dict
monthly_price = int(input("Enter Monthly Subscription Price: "))
yearly_price = int(input("Enter Yearly Subscription Price: "))
subscription_plans = {"Monthly": monthly_price, "Yearly": yearly_price}
has_subtitles = input("Does it have subtitles? (yes/no): ").lower() == 'yes'

# 15. Age Rating - str
age_rating = input("Enter Age Rating (e.g., U/A, PG-13): ")






