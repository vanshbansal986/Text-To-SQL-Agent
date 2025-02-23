## Question: 
List all actors' first and last names.
### Result
The query returned a list of actors' first and last names.  Due to the large number of results (more than 100), only a sample is shown below:

| first_name | last_name     |
|------------|----------------|
| PENELOPE   | GUINESS        |
| NICK       | WAHLBERG       |
| ED         | CHASE          |
| JENNIFER   | DAVIS          |
| JOHNNY     | LOLLOBRIGIDA   |
| BETTE      | NICHOLSON      |
| GRACE      | MOSTEL         |
| MATTHEW    | JOHANSSON      |
| JOE        | SWANK          |
| CHRISTIAN  | GABLE          |
| ZERO       | CAGE           |
| ...        | ...            |


### Query used
```sql
SELECT first_name, last_name 
FROM actor;
```


## Question
Show the titles of all films in the database.

### Result
The query returned 1000 film titles.  Here are the first 50:

ACADEMY DINOSAUR
ACE GOLDFINGER
ADAPTATION HOLES
AFFAIR PREJUDICE
AFRICAN EGG
AGENT TRUMAN
AIRPLANE SIERRA
AIRPORT POLLOCK
ALABAMA DEVIL
ALADDIN CALENDAR
ALAMO VIDEOTAPE
ALASKA PHANTOM
DATE SPEED
ALI FOREVER
ALICE FANTASIA
ALIEN CENTER
ALLEY EVOLUTION
ALONE TRIP
ALTER VICTORY
AMADEUS HOLY
AMELIE HELLFIGHTERS
AMERICAN CIRCUS
AMISTAD MIDSUMMER
ANACONDA CONFESSIONS
ANALYZE HOOSIERS
ANGELS LIFE
ANNIE IDENTITY
ANONYMOUS HUMAN
ANTHEM LUKE
ANTITRUST TOMATOES
ANYTHING SAVANNAH
APACHE DIVINE
APOCALYPSE FLAMINGOS
APOLLO TEEN
ARABIA DOGMA
ARACHNOPHOBIA ROLLERCOASTER
ARGONAUTS TOWN
ARIZONA BANG
ARK RIDGEMONT
ARMAGEDDON LOST
ARMY FLINTSTONES
ARSENIC INDEPENDENCE
ARTIST COLDBLOODED
ATLANTIS CAUSE
ATTACKS HATE
ATTRACTION NEWTON
AUTUMN CROW
BABY HALL
BACKLASH UNDEFEATED


...and 950 more.


### Query used
SELECT title FROM film;


## Question
Get the names of all cities.
### Result
A selection of cities from the query results:
* A Corua (La Corua)
* Abu Dhabi
* Addis Abeba
* Ahmadnagar
* Akron
* Alessandria
* Alvorada
* Amersfoort
* Angra dos Reis
* Antofagasta
* Aparecida de Goinia
* Arlington
* Ashdod
* Asuncin
* Athenai
* Augusta-Richmond County
* Aurora
* Bag
* Baku
* Balikesir
* Bandar Seri Begawan
* Barcelona
* Basel
* Bat Yam
* Baybay
* Beira
* Bellevue
* Belm
* Bergamo
* Bern
* Bhavnagar
* Bhopal
* Bijapur
* Bilbays
* Blumenau
* Boa Vista
* Boksburg
* Bradford
* Braslia
* Bratislava
* Brescia
* Brest
* Brindisi
* Bucuresti
* Bydgoszcz
* Callao
* Caracas
* Carmen
* Cayenee
* Celaya
* ...and many more.


### Query used
SELECT city FROM city;


## Question: 
List all categories available for films.
### Result
The following categories are available for films:

* Sports
* Classics
* New
* Family
* Comedy
* Animation
* Travel
* Music
* Horror
* Drama
* Sci-Fi
* Games
* Documentary
* Foreign
* Action
* Children

### Query used
```sql
SELECT DISTINCT name FROM category;
```


## Question
Show the first name and last name of all customers.

### Result
| first_name | last_name |
|---|---|
| MARY | SMITH |
| PATRICIA | JOHNSON |
| LINDA | WILLIAMS |
| BARBARA | JONES |
| ELIZABETH | BROWN |
| JENNIFER | DAVIS |
| MARIA | MILLER |
| SUSAN | WILSON |
| MARGARET | MOORE |
| DOROTHY | TAYLOR |
| LISA | ANDERSON |
| NANCY | THOMAS |
| KAREN | JACKSON |
| BETTY | WHITE |
| HELEN | HARRIS |
| SANDRA | MARTIN |
| DONNA | THOMPSON |
| CAROL | GARCIA |
| RUTH | MARTINEZ |
| SHARON | ROBINSON |
... (truncated for brevity,  there are many more rows)


### Query used
SELECT first_name, last_name FROM customer;


## Question
Show all films released in 2006.

### Result
The query returned 1000 rows, representing all films released in 2006.  Due to the length of the full result set, only a sample is shown below:

| film_id | title             | description                                                                                  | release_year | ...other columns... |
|---------|----------------------|----------------------------------------------------------------------------------------------|---------------|--------------------|
| 1       | ACADEMY DINOSAUR    | A Epic Drama of a Feminist And a Mad Scientist who must Battle a Teacher in The Canadian Rockies | 2006           | ...                 |
| 2       | ACE GOLDFINGER      | A Astounding Epistle of a Database Administrator And a Explorer who must Find a Car in Ancient China | 2006           | ...                 |
| 3       | ADAPTATION HOLES     | A Astounding Reflection of a Lumberjack And a Car who must Sink a Lumberjack in A Baloon Factory | 2006           | ...                 |
| ...     | ...                 | ...                                                                                          | ...            | ...                 |
| 1000    | ZORRO ARK           | A Intrepid Panorama of a Mad Scientist And a Boy who must Redeem a Boy in A Monastery           | 2006           | ...                 |


### Query used
SELECT * FROM film WHERE release_year = 2006;


## Question
Find all actors with the last name "Smith."
### Result
No actors with the last name "Smith" were found in the database.

### Query used
```sql
SELECT * FROM actor WHERE last_name = 'Smith';
```


## Question
List all customers who are from the city of “New York.”

### Result
No customers from New York City were found in the database.

### Query used
```sql
SELECT c.first_name, c.last_name
FROM customer c
JOIN address a ON c.address_id = a.address_id
JOIN city cy ON a.city_id = cy.city_id
WHERE cy.city = 'New York';
```



## Question: 
Get all stores located in the country “India.”

### Result:

No stores were found in India.


### Query used:

```sql
SELECT store.* 
FROM store
JOIN address ON store.address_id = address.address_id
JOIN city ON address.city_id = city.city_id
JOIN country ON city.country_id = country.country_id
WHERE country.country = 'India';
```


## Question
Show all films with a rental rate greater than $2.99.
### Result
The query returned 1000 rows representing films with a rental rate greater than 2.99.  Due to the large size of the result set, only a partial representation of the data is provided in the Observation section.  All films listed in the Observation have a rental rate greater than $2.99.

### Query used
```
SELECT * FROM film WHERE rental_rate > 2.99;
```


## Question
How many films are there in each category?

### Result
| Category Name | Film Count |
|---|---|
| Action | 64 |
| Animation | 66 |
| Children | 60 |
| Classics | 57 |
| Comedy | 58 |
| Documentary | 68 |
| Drama | 62 |
| Family | 69 |
| Foreign | 73 |
| Games | 61 |
| Horror | 56 |
| Music | 51 |
| New | 63 |
| Sci-Fi | 61 |
| Sports | 74 |
| Travel | 57 |

### Query used
```sql
SELECT c.name, COUNT(fc.film_id) AS film_count
FROM category c
JOIN film_category fc ON c.category_id = fc.category_id
GROUP BY c.name
ORDER BY c.name;
```



## Question
What is the total number of actors?
### Result
The total number of actors is 200.
### Query used
```sql
SELECT COUNT(*) FROM actor;
```



## Question
Get the total payment received in June 2022.
### Result
The total payment received in June 2022 is $10566.26.

### Query used
```sql
SELECT SUM(amount) 
FROM payment 
WHERE payment_date BETWEEN '2022-06-01' AND '2022-06-30';
```






## Question: 
Find the total number of rentals made last month.

### Result: 
0

### Query used:
```sql
SELECT COUNT(*) 
FROM rental 
WHERE rental_date >= DATE_TRUNC('month', CURRENT_DATE - INTERVAL '1 month') 
  AND rental_date < DATE_TRUNC('month', CURRENT_DATE);
```


## Question: 
How many films have a rating of “PG-13”?
### Result: 
223
### Query used:
```sql
SELECT COUNT(*) 
FROM film 
WHERE rating = 'PG-13';
```


## Question
List all films along with their category names.

### Result
Here's a sample of the film titles and their corresponding categories:

| Film Title             | Category Name |
|-------------------------|----------------|
| ACADEMY DINOSAUR        | Documentary     |
| ACE GOLDFINGER          | Horror          |
| ADAPTATION HOLES        | Documentary     |
| AFFAIR PREJUDICE        | Horror          |
| AFRICAN EGG             | Family          |
| ...                     | ...             |


The full list contains many more entries.  The complete data is available in the previous tool's observation.


### Query used
```sql
SELECT f.title, c.name AS category_name
FROM film f
JOIN film_category fc ON f.film_id = fc.film_id
JOIN category c ON fc.category_id = c.category_id;
```



## Question: 
Show all actors who appeared in the film "Inception."

### Result:

No actors were found in the film "Inception".  The database does not appear to contain a film with this title or any similar titles.  Please check the database for correctness and/or try a different search term.


### Query used:

```sql
SELECT a.first_name, a.last_name
FROM actor a
JOIN film_actor fa ON a.actor_id = fa.actor_id
JOIN film f ON fa.film_id = f.film_id
WHERE f.title ILIKE '%Inception%';
```



## Question
Get a list of all customers and the films they have rented.

### Result
| customer_id | customer_first_name | customer_last_name | film_title       |
|--------------|----------------------|---------------------|-------------------|
| 459          | TOMMY                 | COLLAZO             | FREAKY POCUS      |
| 408          | MANUEL                | MURRELL              | GRADUATE LORD     |
| 333          | ANDREW                | PURDY                | LOVE SUICIDES     |
| 222          | DELORES                | HANSEN               | IDOLS SNATCHERS   |
| 549          | NELSON                | CHRISTENSON          | MYSTIC TRUMAN     |
| 269          | CASSANDRA             | WALTERS              | SWARM GOLD        |
| 239          | MINNIE                | ROMERO               | LAWLESS VISION    |
| 126          | ELLEN                 | SIMPSON              | MATRIX SNOWMAN    |
| 399          | DANNY                 | ISOM                 | HANGING DEEP      |
| 142          | APRIL                 | BURNS                | WHALE BIKINI      |
...and many more rows...

### Query used
```
SELECT c.customer_id, c.first_name AS customer_first_name, c.last_name AS customer_last_name, f.title AS film_title FROM customer c JOIN rental r ON c.customer_id = r.customer_id JOIN inventory i ON r.inventory_id = i.inventory_id JOIN film f ON i.film_id = f.film_id;`
```

## Question
List all staff members along with the stores they work at.

### Result
| First Name | Last Name | Store ID |
|---|---|---|
| Mike | Hillyer | 1 |
| Jon | Stephens | 2 |


### Query used
```sql
SELECT staff.first_name, staff.last_name, store.store_id
FROM staff
INNER JOIN store
ON staff.store_id = store.store_id;
```


## Question: 
Find all films rented by customer "John Doe."

### Result: 
No films were rented by a customer named "John Doe".

### Query used:
```sql
SELECT f.title
FROM film f
JOIN inventory i ON f.film_id = i.film_id
JOIN rental r ON i.inventory_id = r.inventory_id
JOIN customer c ON r.customer_id = c.customer_id
WHERE c.first_name = 'JOHN' AND c.last_name = 'DOE';
```


## Question: 
Show the top 5 films rented the most across all stores.

### Result

| Film Title             | Total Rentals |
|------------------------|----------------|
| BUCKET BROTHERHOOD      | 34             |
| ROCKETEER MOTHER       | 33             |
| RIDGEMONT SUBMARINE    | 32             |
| SCALAWAG DUCK          | 32             |
| FORWARD TEMPLE         | 32             |


### Query used
```sql
SELECT f.title, COUNT(r.rental_id) AS total_rentals
FROM film f
JOIN inventory i ON f.film_id = i.film_id
JOIN rental r ON i.inventory_id = r.inventory_id
GROUP BY f.title
ORDER BY total_rentals DESC
LIMIT 5;
```



## Question
List all customers who have rented films in both store 1 and store 2.

### Result
The query returned a list of customer IDs, first names, and last names who have rented films from both store 1 and store 2.  Due to the length of the full result set (191 customers), only a sample is shown below:


| customer_id | first_name | last_name |
|---|---|---|
| 388 | CRAIG | MORRELL |
| 348 | ROGER | QUINTANILLA |
| 51 | ALICE | STEWART |
| 347 | RYAN | SALISBURY |
| 135 | JUANITA | MASON |
| ... | ... | ... |


### Query used
SELECT c.customer_id, c.first_name, c.last_name FROM customer c JOIN rental r ON c.customer_id = r.customer_id JOIN inventory i ON r.inventory_id = i.inventory_id WHERE i.store_id = 1 INTERSECT SELECT c.customer_id, c.first_name, c.last_name FROM customer c JOIN rental r ON c.customer_id = r.customer_id JOIN inventory i ON r.inventory_id = i.inventory_id WHERE i.store_id = 2;


## Question: 
Find all actors who have appeared in more than 10 films.
### Result
The following actors appeared in more than 10 films:

PENELOPE GUINESS, NICK WAHLBERG, ED CHASE, JENNIFER DAVIS, JOHNNY LOLLOBRIGIDA, BETTE NICHOLSON, GRACE MOSTEL, MATTHEW JOHANSSON, JOE SWANK, CHRISTIAN GABLE, ZERO CAGE, ...and many more.


### Query used
```sql
SELECT first_name, last_name
FROM actor
WHERE actor_id IN (
    SELECT actor_id
    FROM film_actor
    GROUP BY actor_id
    HAVING COUNT(*) > 10
);
```


## Question
Get a list of customers who have made more than 5 payments.

### Result
A total of 298 customers have made more than 5 payments.  A partial list of customer IDs includes: 184, 87, 477, 273, 550, 394, 51, 272, 70, 190... and many more.

### Query used
```sql
SELECT customer_id
FROM payment
GROUP BY customer_id
HAVING COUNT(*) > 5;
```


## Question
List all films that are in both the "Action" and "Comedy" categories.

### Result
No films were found that belong to both the "Action" and "Comedy" categories.

### Query used
```sql
SELECT f.title
FROM film f
JOIN film_category fc ON f.film_id = fc.film_id
JOIN category c ON fc.category_id = c.category_id
WHERE c.name = 'Action'
INTERSECT
SELECT f.title
FROM film f
JOIN film_category fc ON f.film_id = fc.film_id
JOIN category c ON fc.category_id = c.category_id
WHERE c.name = 'Comedy';
```


## Question
Show all rentals made in the last 7 days.

### Result
No rentals were found in the last 7 days.

### Query used
```sql
SELECT * 
FROM rental 
WHERE rental_date >= NOW() - INTERVAL '7 days';
```


## Question
Get all payments made in February 2022.

### Result
The query returned a large number of payments made in February 2022.  Here's a sample of the results:

| payment_id | customer_id | staff_id | rental_id | amount    | payment_date                       |
|------------|-------------|----------|-----------|-----------|-----------------------------------|
| 16850      | 83          | 2        | 222       | 0.99      | 2022-02-01 02:15:03.268858+04:00   |
| 16851      | 83          | 2        | 950       | 0.99      | 2022-02-01 00:32:34.114471+04:00   |
| 17922      | 451         | 1        | 1940      | 6.99      | 2022-02-01 00:19:41.53708+04:00   |
| ...        | ...         | ...      | ...       | ...       | ...                                 |


A total of 172 payments were found.  The full list is too long to display here.


### Query used
```
SELECT * FROM payment WHERE payment_date BETWEEN '2022-02-01' AND '2022-02-28';
```

## Question:
List all films that have not been rented in the last 30 days.
### Result:
No films have not been rented in the last 30 days.


### Query used:
```sql
SELECT f.title
FROM film f
LEFT JOIN inventory i ON f.film_id = i.film_id
LEFT JOIN rental r ON i.inventory_id = r.inventory_id
WHERE r.rental_date < NOW() - INTERVAL '30 days'
GROUP BY f.title
HAVING count(*) = 0;
```



## Question: 
Find all customers who registered in the last 6 months.

### Result:

No customers were found who registered in the last 6 months.

### Query used:

```sql
SELECT * 
FROM customer 
WHERE create_date >= NOW() - INTERVAL '6 months';
```


## Question
Show all staff members hired before January 1, 2020.

### Result
No staff members were hired before January 1, 2020 according to the database.

### Query used
```sql
SELECT * 
FROM staff 
WHERE last_update < '2020-01-01';
```



## Question
List the top 3 customers who have spent the most in each country.

### Result
| customer_id | customer_name        | total_spent | country_name                     |
|-------------|-----------------------|-------------|---------------------------------|
| 218         | VERA MCCOY            | 67.82        | Afghanistan                      |
| 176         | JUNE CARROLL          | 173.63       | Algeria                          |
| 441         | MARIO CHEATHAM        | 112.72       | Algeria                          |
| ...         | ...                    | ...          | ...                              |
| 470         | GORDON ALLARD         | 160.68       | Yemen                            |
| 7           | MARIA MILLER          | 151.67       | Yugoslavia                       |


### Query used
```sql
WITH customer_country_spending AS (
  SELECT
    c.customer_id,
    c.first_name || ' ' || c.last_name AS customer_name,
    COALESCE(SUM(p.amount), 0) AS total_spent,
    country.country AS country_name
  FROM customer AS c
  JOIN address AS a
    ON c.address_id = a.address_id
  JOIN city AS ci
    ON a.city_id = ci.city_id
  JOIN country AS country
    ON ci.country_id = country.country_id
  LEFT JOIN rental AS r
    ON c.customer_id = r.customer_id
  LEFT JOIN payment AS p
    ON r.rental_id = p.rental_id
  GROUP BY
    c.customer_id,
    customer_name,
    country_name
), ranked_spending AS (
  SELECT
    customer_id,
    customer_name,
    total_spent,
    country_name,
    RANK() OVER (PARTITION BY country_name ORDER BY total_spent DESC) AS rank
  FROM customer_country_spending
)
SELECT
  customer_id,
  customer_name,
  total_spent,
  country_name
FROM ranked_spending
WHERE
  rank <= 3
ORDER BY
  country_name,
  rank;
```


## Question 
Find the films that have been rented more times than the average number of rentals per film.
### Result
The following films have been rented more times than the average number of rentals per film:  ITALIAN AFRICAN, FICTION CHRISTMAS, BADMAN DAWN, LEGALLY SECRETARY, PELICAN COMFORTS, SEARCHERS WAIT, FRONTIER CABIN, STALLION SUNDANCE, TERMINATOR CLUB, WRONG BEHAVIOR, CITIZEN SHREK, WEREWOLF LOLA, COWBOY DOOM, DIARY PANIC, PULP BEVERLY, PIANIST OUTFIELD, OUTBREAK DIVINE, ROCK INSTINCT, GIANT TROOPERS, CARIBBEAN LIBERTY, ...and many more.  Due to the large number of results, only a partial list is shown.

### Query used
```sql
SELECT f.title
FROM film f
JOIN inventory i ON f.film_id = i.film_id
JOIN rental r ON i.inventory_id = r.inventory_id
GROUP BY f.title
HAVING COUNT(*) > (SELECT AVG(rental_count) FROM (SELECT COUNT(*) AS rental_count FROM rental GROUP BY inventory_id) AS rental_counts);
```


## Question
For each actor, show their name and the percentage of films they've acted in compared to the total films.

### Result
| Actor Name        | Percentage of Films |
|--------------------|----------------------|
| SUSAN DAVIS        | 5.4                  |
| GINA DEGENERES     | 4.2                  |
| WALTER TORN        | 4.1                  |
| MARY KEITEL        | 4.0                  |
| MATTHEW CARREY     | 3.9                  |
| SANDRA KILMER      | 3.7                  |
| SCARLETT DAMON     | 3.6                  |
| VAL BOLGER         | 3.5                  |
| HENRY BERRY        | 3.5                  |
| GROUCHO DUNST      | 3.5                  |


(truncated for brevity; full results are available in the observation above)

### Query used
```
SELECT a.first_name || ' ' || a.last_name AS actor_name, CAST(COUNT(fa.film_id) AS REAL) * 100 / (SELECT COUNT(*) FROM film) AS percentage_of_films 
FROM actor a 
LEFT JOIN film_actor fa ON a.actor_id = fa.actor_id 
GROUP BY actor_name 
ORDER BY percentage_of_films DESC;
```


## Question
Show the average payment amount for each customer.

### Result
| customer_id | first_name | last_name | average_payment_amount |
|---|---|---|---|
| 184 | VIVIAN | RUIZ | 3.95 |
| 87 | WANDA | PATTERSON | 4.86 |
| 477 | DAN | PAINE | 4.99 |
| 273 | PRISCILLA | LOWE | 4.50 |
| 550 | GUY | BROWNLEE | 4.99 |
| 394 | CHRIS | BROTHERS | 3.85 |
| 51 | ALICE | STEWART | 4.20 |
| 272 | KAY | CALDWELL | 4.94 |
| ...and 584 more rows...


### Query used
```
SELECT c.customer_id, c.first_name, c.last_name, AVG(p.amount) AS average_payment_amount
FROM customer c
JOIN payment p ON c.customer_id = p.customer_id
GROUP BY c.customer_id, c.first_name, c.last_name;
```

## Question: 
List all actors who have appeared in at least one film in each category.

### Result

| First Name | Last Name |
|---|---|
| UMA | WOOD |
| SEAN | WILLIAMS |
| DARYL | WAHLBERG |
| GROUCHO | DUNST |
| GINA | DEGENERES |
| KEVIN | GARLAND |
| EWAN | GOODING |
| IAN | TANDY |
| HARVEY | HOPE |
| MICHAEL | BOLGER |
| REESE | WEST |


### Query used

```sql
SELECT a.first_name, a.last_name
FROM actor a
JOIN film_actor fa ON a.actor_id = fa.actor_id
JOIN film_category fc ON fa.film_id = fc.film_id
GROUP BY a.actor_id
HAVING count(DISTINCT fc.category_id) = (SELECT count(*) FROM category);
```


## Question 
Find customers who have rented more films this year than last year.
### Result 
No customers rented more films this year than last year.
### Query used 
```sql
WITH yearly_rentals AS (
    SELECT 
        customer_id,
        EXTRACT(YEAR FROM rental_date) AS rental_year,
        COUNT(*) AS rental_count
    FROM rental
    WHERE EXTRACT(YEAR FROM rental_date) IN (EXTRACT(YEAR FROM NOW()), EXTRACT(YEAR FROM NOW()) - INTERVAL '1 year')
    GROUP BY customer_id, rental_year
)
SELECT yr.customer_id
FROM yearly_rentals yr
WHERE yr.rental_year = EXTRACT(YEAR FROM NOW())
  AND ( NOT EXISTS (
    SELECT 1
    FROM yearly_rentals yr_last
    WHERE yr_last.customer_id = yr.customer_id
      AND yr_last.rental_year = EXTRACT(YEAR FROM NOW()) - INTERVAL '1 year'
  ) OR EXISTS (
    SELECT 1
    FROM yearly_rentals yr_last
    WHERE yr_last.customer_id = yr.customer_id
      AND yr_last.rental_year = EXTRACT(YEAR FROM NOW()) - INTERVAL '1 year'
      AND yr.rental_count > yr_last.rental_count
  ));
```


## Question
List the top 5 films with the highest revenue.

### Result
| Film Title             | Total Revenue |
|------------------------|----------------|
| TELEGRAPH VOYAGE       | 231.73         |
| WIFE TURN              | 223.69         |
| ZORRO ARK              | 214.69         |
| GOODFELLAS SALUTE      | 209.69         |
| SATURDAY LAMBS         | 204.72         |


### Query used
```sql
SELECT f.title, SUM(p.amount) AS total_revenue
FROM film f
JOIN inventory i ON f.film_id = i.film_id
JOIN rental r ON i.inventory_id = r.inventory_id
JOIN payment p ON r.rental_id = p.rental_id
GROUP BY f.title
ORDER BY total_revenue DESC
LIMIT 5;
```



## Question
For each customer, show the number of films rented in the last month compared to the previous month.

### Result
The query executed successfully but returned 0 rentals for all customers in both the last and previous month.  This is likely due to a lack of rental data for those time periods within the database.  Here's a sample of the results:

| customer_id | first_name | last_name | last_month_rentals | previous_month_rentals |
|---|---|---|---|---|
| 1 | MARY | SMITH | 0 | 0 |
| 2 | PATRICIA | JOHNSON | 0 | 0 |
| 3 | LINDA | WILLIAMS | 0 | 0 |
| ... | ... | ... | ... | ... |


### Query used
```sql
SELECT c.customer_id, c.first_name, c.last_name, COALESCE(last_month.rental_count, 0) AS last_month_rentals, COALESCE(previous_month.rental_count, 0) AS previous_month_rentals
FROM customer c
LEFT JOIN (
    SELECT customer_id, COUNT(*) AS rental_count
    FROM rental
    WHERE rental_date >= DATE_TRUNC('month', CURRENT_DATE - INTERVAL '1 month')
      AND rental_date < DATE_TRUNC('month', CURRENT_DATE)
    GROUP BY customer_id
) AS last_month ON c.customer_id = last_month.customer_id
LEFT JOIN (
    SELECT customer_id, COUNT(*) AS rental_count
    FROM rental
    WHERE rental_date >= DATE_TRUNC('month', CURRENT_DATE - INTERVAL '2 months')
      AND rental_date < DATE_TRUNC('month', CURRENT_DATE - INTERVAL '1 month')
    GROUP BY customer_id
) AS previous_month ON c.customer_id = previous_month.customer_id
ORDER BY c.customer_id;
```


## Question
Show the names of customers who have rented every film in the “Action” category.

### Result
No customers have rented every film in the Action category.

### Query used
```sql
SELECT c.first_name, c.last_name
FROM customer c
JOIN rental r ON c.customer_id = r.customer_id
JOIN inventory i ON r.inventory_id = i.inventory_id
JOIN film f ON i.film_id = f.film_id
JOIN film_category fc ON f.film_id = fc.film_id
JOIN category cat ON fc.category_id = cat.category_id
WHERE cat.name = 'Action'
GROUP BY c.customer_id
HAVING COUNT(DISTINCT f.film_id) = (SELECT COUNT(*)
                                    FROM film f2
                                    JOIN film_category fc2 ON f2.film_id = fc2.film_id
                                    JOIN category cat2 ON fc2.category_id = cat2.category_id
                                    WHERE cat2.name = 'Action');
```


## Question: 
List customers who have rented the same film more than 3 times.

### Result:

No customers were found who rented the same film more than 3 times.


### Query used:

```sql
SELECT c.first_name, c.last_name, f.title
FROM customer c
JOIN rental r ON c.customer_id = r.customer_id
JOIN inventory i ON r.inventory_id = i.inventory_id
JOIN film f ON i.film_id = f.film_id
GROUP BY c.customer_id, f.title
HAVING COUNT(*) > 3;
```
