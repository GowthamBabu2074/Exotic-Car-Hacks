use cars;

select * from cleaned_data;

-- 1. How many mustangs and shelby's
select Model, count(model)as count from cleaned_data group by Model; -- 7743 mustang and 648 shelby

-- 2. count cars where price is greater than 50,000
select count(*) from cleaned_data where price > 50000; -- 1131 cars

-- 3. select the kind of cars greater than 50,000
select Model, count(Model)as count from cleaned_data where price > 50000 group by Model; -- 735 mustangs and 396 shelby

-- 4. select the kind of cars greater than 50,000
select Model, Type, count(model)as count from cleaned_data where price > 50000 group by Model, Type; -- mustang mach-e's are most sold cars since they are recently launched and price doesnt depreciate as others.

-- 5. checking the most sold based on year.
select Year, Type , count(Type) as count from cleaned_data  group by Type, Year; -- mach-e in 2021 with 1037 cars. Since, it is recently released and proves the above statement.

-- 6. select the kind of cars greater than 100,000
select Model, count(model)as count from cleaned_data where price > 100000 group by Model; -- 36 mustang and 84 shelby, quite obvious since shelby's are costly.

-- 7. select cars where price is less than 10,000
select * from cleaned_data where price < 10000;
select count(*) from cleaned_data where price < 10000; -- 252 cars

-- 8. for above car, see the years and models.
select Model, Type, count(model)as count from cleaned_data where price < 10000 group by Model;

-- 9. select cars where mileage is greater than 100,000
select * from cleaned_data where mileage > 100000;
select count(*) from cleaned_data where mileage > 100000; -- 424 cars

-- 10. select cars where mileage is less than 10,000
select * from cleaned_data where mileage < 10000;
select count(*) from cleaned_data where mileage < 10000; -- 3044 cars, more cars

-- 11. most inflation rate for mustnag gt
with b as(with a as(select type, year, avg(price) as avvg
from cleaned_data
where type = 'GT'
group by type, year
order by year)
select *, lag(avvg, 1, avvg) over(order by year) as pre_sal
from a)
select *,(avvg-pre_sal)/(pre_sal) as per_increase from b; -- 2010 model cars have high inflation rates

-- 12. mileage variance wrt highways, cities and best mileage providing cars
select type, avg(city_mpg), avg(highway_mpg)
from cleaned_data 
group by type
order by avg(city_mpg) desc
limit 2; -- mache electric and ecobppst are most fuel efficient cars

-- 13. which type of car has the best price and mileage
with a as(select type, avg(city_mpg) as avg_cty, avg(price) as avg_price, avg(price) / avg(city_mpg) as qual
from cleaned_data 
group by type
order by type)
select * from a order by qual asc; -- as per the mpg, mach-e and ecoboost are the best, but performance varies