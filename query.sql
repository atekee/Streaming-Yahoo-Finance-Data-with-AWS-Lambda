with cte as (
	select name as company_name,
		high as high_stock_price,
		cast (ts as timestamp) as datetime,
		extract (
			hour
			from cast (ts as timestamp)
		) as hour,
		row_number () over (
			partition by name,
			extract (
				hour
				from cast (ts as timestamp)
			)
			order by high desc
		) as row_num
	from dataproject03_bucket
)
select company_name,
	high_stock_price,
	hour,
	datetime
from cte
where row_num = 1
order by company_name,
	hour;