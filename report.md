Query: List the top 5 films with the highest revenue.

Response:
### Question: List the top 5 films with the highest revenue.

### Result
| Film Title           | Total Revenue |
|-----------------------|----------------|
| TELEGRAPH VOYAGE      | 231.73         |
| WIFE TURN            | 223.69         |
| ZORRO ARK            | 214.69         |
| GOODFELLAS SALUTE    | 209.69         |
| SATURDAY LAMBS       | 204.72         |

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
```


