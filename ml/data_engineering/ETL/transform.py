'''
This is an abstract example of Transforming in an ETL pipeline. 

Inspired from the "Introduction to Data Engineering" course on Datacamp.com
Author: Alex Nakagawa
'''
# Get the rental rate column as a string
rental_rate_str = film_df.rental_rate.astype(str)

# Split up and expand the column
rental_rate_expanded = rental_rate_str.str.split('.', expand=True)

# Assign the columns to film_df
film_df = film_df.assign(
    rental_rate_dollar=rental_rate_expanded[0],
    rental_rate_cents=rental_rate_expanded[1],
)

# Use groupBy and mean to aggregate the column
ratings_per_film_df = rating_df.groupBy('film_id').mean('rating')

# Join the tables using the film_id column
film_df_with_ratings = film_df.join(
    ratings_per_film_df,
    film_df.film_id == ratings_per_film_df.film_id
)

# Show the 5 first results
print(film_df_with_ratings.show(5))
