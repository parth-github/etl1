select_check = '''
SELECT * FROM imdb_movies;
'''
transform_qry = '''
SELECT Title, Genre, Votes,
CASE 
    WHEN Votes > 100000 THEN 'Good'
    WHEN Votes > 10000 THEN 'Okay'
    ELSE 'Bad'
END remarks
FROM imdb_movies;
'''
select_queries = [select_check]