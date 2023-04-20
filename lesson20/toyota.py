class Toyota:
    cat1 = "Cars"
    cat2 = "Electrified"
    cat3 = "Crossovers"
    cat4 = "SUVs"
    cat5 = "Trucks"
    cat6 = "Minivan"
    
    def __init__(self, finished_price, basic_price, model, year, picurl):
        self.finished_price = finished_price
        self.basic_price = basic_price
        self.model = model
        self.year = year
        self.pic = picurl
        
    def __str__(self):
        return f"For the car model: {self.model} and year: {self.year}, basic price:{self.basic_price}"
        
    
car1 = Toyota("$34,550", "$28,770", "Prius Prime", "2022", "https://www.toyota.com/priusprime")
car2 = Toyota("$52,350", "$39,950", "Toyota Crown", "2023", "https://www.toyota.com/toyotacrown")
car3 = Toyota("$23,315", "$21,550", "Corolla", "2023", "https://www.toyota.com/corolla")
cars = [car1, car2, car3]
for _ in cars:
    print(_)



