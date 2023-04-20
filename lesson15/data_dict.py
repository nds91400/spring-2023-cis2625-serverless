data = {
    'No':[1,2,3,4,5],
    'Customer':['Intersection', 'Magnet', 'Perspective korp.', 'Driveway', 'Near'],
    'Type':['com.network', 'com.network', 'warehouse', 'enterprise', 'enterprise'],
    'Country':['USA', 'USA', 'Belarus', 'USA', 'USA'],
    'City':['New York', 'New York', 'Minsk', 'New York', 'Los Angeles'],
    'Contract Number':[2314589, 2432656, 2456983, 2408570, 2481553],
    'Date':['12.12.2012', '27.08.2014', '31.12.2014', '24.04.2014', '06.05.2015'],
    'Limitation Years':[2, 3, 2, 5, 2],
    'Contact Manager':['Aaron', 'Alex', 'Ashley', 'Aaron', 'Ashley']
}

import pandas as pd
customers = pd.DataFrame(data)
print(customers)