# Instacart Log Generator

## install

`pip install instacart-log-generator`

## Code

```python
from instacart_log_generator.my_gen_log import InstacartLogGenerator

LOGGING_FILE_PATH = 'file_path_where_you_want.log'
LOG_PER_SECOND = 1

InstacartLogGenerator().logging(LOGGING_FILE_PATH, LOG_PER_SECOND)
```

## Result

```shell
162.232.228.1 - - [17/Jan/2022:17:11:16 +0900] "POST /order HTTP/1.1" 400 "-" "Mozilla/5.0 (iPhone; CPU iPhone OS 8_4 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) GSA/7.0.55539 Mobile/12H143 Safari/600.1.4"
162.232.228.1 - - [17/Jan/2022:17:11:16 +0900] {"order_id": 3375775, "product_id": 21903, "add_to_cart_order": 2, "reordered": 1, "aisle_id": 123, "department_id": 4, "order_number": 4, "order_dow": 4, "order_hour_of_day": 11, "days_since_prior_order": 17}
51.117.186.246 - - [17/Jan/2022:17:11:17 +0900] "GET /order HTTP/1.1" 200 "-" "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36"
```