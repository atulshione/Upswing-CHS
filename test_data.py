from faker import Faker
import random
from datetime import datetime

fake = Faker()

def generate_test_data():
    """Generate and return fake test data."""
    full_name = f'{fake.first_name()} {fake.last_name()}'
    credit_card_number = fake.credit_card_number()
    username = full_name.replace(' ', '').lower()
    password = fake.password()
    random_ids = random.sample(range(1, 15), 3)
    country = fake.country()
    city = fake.city()
    rndint = fake.pyint(1, 12)
    month = rndint
    year = datetime.now().year + rndint
    
    return username, password, full_name, credit_card_number,country,city,rndint,month,year

# Generate data for use in tests
username, password, full_name, credit_card_number,country,city,rndint,month,year = generate_test_data()
