try:
    car_name = driver.find_element_by_xpath('/html/body/div[1]/div[2]/section[2]/section[1]/div[1]/div[1]/h1[2]').text
except NoSuchElementException:
    try:
        car_name = driver.find_element_by_xpath('/html/body/div[1]/div[2]/section[2]/section[1]/div[2]/div[1]/h1[2]').text
    except NoSuchElementException:
        try:
            car_name = driver.find_element_by_xpath('/html/body/div[1]/div[2]/section[2]/section[1]/div[3]/div[1]/h1[2]').text
        except NoSuchElementException:
            car_name = -1 
                    
                    
try:
    miles = driver.find_element_by_xpath('/html/body/div[1]/div[2]/section[2]/section[1]/div[2]').text[0:-6]
except NoSuchElementException:
    miles = -1 
          
            
            
try:
    price = driver.find_element_by_xpath('/html/body/div[1]/div[2]/section[2]/section[1]/div[3]/div/div[1]/div[1]/span').text[1:]
except NoSuchElementException:            
    price = -1 
            
            
        
try:
    colour = driver.find_element_by_xpath('/html/body/div[1]/div[2]/section[2]/section[2]/div[6]/div/ul/li[2]/span[1]').text
except NoSuchElementException:             
    try:
        colour = driver.find_element_by_xpath('/html/body/div[1]/div[2]/section[2]/section[2]/div[5]/div/ul/li[2]/span[1]').text
    except NoSuchElementException:             
        try:
            colour = driver.find_element_by_xpath('/html/body/div[1]/div[2]/section[2]/section[2]/div[4]/div/ul/li[2]/span[1]').text
        except NoSuchElementException:             
            try:
                colour = driver.find_element_by_xpath('/html/body/div[1]/div[2]/section[2]/section[2]/div[7]/div/ul/li[2]/span[1]').text
            except NoSuchElementException:             
                colour = -1
                        
                        
try:
    city_mpg = driver.find_element_by_xpath('/html/body/div[1]/div[2]/section[2]/section[2]/div[6]/div/ul/li[3]/span[1]').text
except NoSuchElementException:
    try:
        city_mpg = driver.find_element_by_xpath('/html/body/div[1]/div[2]/section[2]/section[2]/div[5]/div/ul/li[3]/span[1]').text
    except NoSuchElementException:
        try:
            city_mpg = driver.find_element_by_xpath('/html/body/div[1]/div[2]/section[2]/section[2]/div[4]/div/ul/li[3]/span[1]').text
        except NoSuchElementException:
            try:
                city_mpg = driver.find_element_by_xpath('/html/body/div[1]/div[2]/section[2]/section[2]/div[7]/div/ul/li[3]/span[1]').text
            except NoSuchElementException:
                city_mpg = -1
                        
                        
try:
    highway_mpg = driver.find_element_by_xpath('/html/body/div[1]/div[2]/section[2]/section[2]/div[6]/div/ul/li[3]/span[1]').text
except NoSuchElementException:
    try:
        highway_mpg = driver.find_element_by_xpath('/html/body/div[1]/div[2]/section[2]/section[2]/div[5]/div/ul/li[3]/span[1]').text
    except NoSuchElementException:
        try:
            highway_mpg = driver.find_element_by_xpath('/html/body/div[1]/div[2]/section[2]/section[2]/div[7]/div/ul/li[3]/span[1]').text
        except NoSuchElementException:
            try:
                highway_mpg = driver.find_element_by_xpath('/html/body/div[1]/div[2]/section[2]/section[2]/div[4]/div/ul/li[3]/span[1]').text
            except NoSuchElementException:
                highway_mpg = -1
                        
                        
try:
    drivetrain = driver.find_element_by_xpath('/html/body/div[1]/div[2]/section[2]/section[2]/div[6]/div/ul/li[7]/span[1]').text
except NoSuchElementException:
    try:
        drivetrain = driver.find_element_by_xpath('/html/body/div[1]/div[2]/section[2]/section[2]/div[5]/div/ul/li[7]/span[1]').text
    except NoSuchElementException:
        try:
            drivetrain = driver.find_element_by_xpath('/html/body/div[1]/div[2]/section[2]/section[2]/div[4]/div/ul/li[7]/span[1]').text
        except NoSuchElementException:
            try:
                drivetrain = driver.find_element_by_xpath('/html/body/div[1]/div[2]/section[2]/section[2]/div[7]/div/ul/li[7]/span[1]').text
            except NoSuchElementException:
                drivetrain = -1
                        
                        
try:
    gears = driver.find_element_by_xpath('/html/body/div[1]/div[2]/section[2]/section[2]/div[6]/div/ul/li[8]/span[1]').text
except NoSuchElementException:
    try:
        gears = driver.find_element_by_xpath('/html/body/div[1]/div[2]/section[2]/section[2]/div[5]/div/ul/li[8]/span[1]').text
    except NoSuchElementException:
        try:
            gears = driver.find_element_by_xpath('/html/body/div[1]/div[2]/section[2]/section[2]/div[7]/div/ul/li[8]/span[1]').text
        except NoSuchElementException:
            try:
                gears = driver.find_element_by_xpath('/html/body/div[1]/div[2]/section[2]/section[2]/div[4]/div/ul/li[8]/span[1]').text
            except NoSuchElementException:
                gears = -1
                        
                        
try:
    engine = driver.find_element_by_xpath('/html/body/div[1]/div[2]/section[2]/section[2]/div[6]/div/ul/li[9]/span[1]').text
except NoSuchElementException:
    try:
        engine = driver.find_element_by_xpath('/html/body/div[1]/div[2]/section[2]/section[2]/div[5]/div/ul/li[9]/span[1]').text
    except NoSuchElementException:
        try:
            engine = driver.find_element_by_xpath('/html/body/div[1]/div[2]/section[2]/section[2]/div[4]/div/ul/li[9]/span[1]').text
        except NoSuchElementException:
            try:
                engine = driver.find_element_by_xpath('/html/body/div[1]/div[2]/section[2]/section[2]/div[7]/div/ul/li[9]/span[1]').text
            except NoSuchElementException:
                engine = -1
                    
                        
try:
    location = driver.find_element_by_xpath('/html/body/div[1]/div[2]/section[2]/section[2]/div[1]/div[2]/div/a').text
except NoSuchElementException:
    location = -1
    
try:
    contact = driver.find_element_by_xpath('/html/body/div[1]/div[3]/section[1]/div/div[2]/div/div[2]/div[1]/span').text
except NoSuchElementException:
    contact = -1
           
            
cars.append({'car_name' : car_name,
                    'price' : price,
                    'mileage' :miles,
                    'colour': colour,
                    'city_mpg':city_mpg,
                    'highway_mpg': highway_mpg,
                    'drivetrain':drivetrain,
                    'gears':gears,
                    'engine':engine,
                    'location':location,
                    'contact':contact,
                    'url': ur})