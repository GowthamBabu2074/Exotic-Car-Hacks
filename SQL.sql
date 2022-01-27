select * from [dbo].[cars_data]

-- How many mustangs and shelby's
select Model, count(model)as count from dbo.cars_data group by Model -- 7743 mustang and 648 shelby

-- select cars where price is greater than 50,000
select * from dbo.cars_data where price > 50000
select count(*) from dbo.cars_data where price > 50000 -- 1131 cars

--select the kind of cars greater than 50,000
select Model, count(Model)as count from dbo.cars_data where price > 50000 group by Model -- 735 mustangs and 396 shelby

--select the kind of cars greater than 50,000
select Model, Type, count(model)as count from dbo.cars_data where price > 50000 group by Model, Type -- mustang mach-e's are most sold cars since they are recently launched and price doesnt depreciate as others.

-- checking the most sold based on year.
select Year, Type , count(Type) as count from dbo.cars_data  group by Type, Year -- mach-e in 2021 with 1037 cars. Since, it is recently released and proves the above statement.




--select the kind of cars greater than 100,000
select Model, count(model)as count from dbo.cars_data where price > 100000 group by Model -- 36 mustang and 84 shelby, quite obvious since shelby's are costly.




-- select cars where price is less than 10,000
select * from dbo.cars_data where price < 10000
select count(*) from dbo.cars_data where price < 10000 -- 252 cars

--for above car, see the years and models.
select Model, [Type], count(model)as count from dbo.cars_data where price < 10000 group by Model

-- select cars where mileage is greater than 100,000
select * from dbo.cars_data where mileage > 100000
select count(*) from dbo.cars_data where mileage > 100000 -- 424 cars

-- select cars where mileage is less than 10,000
select * from dbo.cars_data where mileage < 10000
select count(*) from dbo.cars_data where mileage < 10000 -- 3044 cars, more cars



