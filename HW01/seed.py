import psycopg2
from faker import Faker
import random

# Initialize Faker
fake = Faker()

# Database connection
conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="password",
    host="localhost",
    port="5432",
)
cursor = conn.cursor()

# Number of records to insert
num_users = 10
num_tasks = 20

# Insert users
for _ in range(num_users):
    fullname = fake.name()
    email = fake.unique.email()
    cursor.execute(
        "INSERT INTO users (fullname, email) VALUES (%s, %s)", (fullname, email)
    )

# Insert tasks
for _ in range(num_tasks):
    title = fake.sentence(nb_words=6)
    description = fake.paragraph(nb_sentences=3)
    status_id = random.randint(1, 3)  # Assuming there are 3 statuses
    user_id = random.randint(1, num_users)
    cursor.execute(
        "INSERT INTO tasks (title, description, status_id, user_id) VALUES (%s, %s, %s, %s)",
        (title, description, status_id, user_id),
    )

# Commit changes and close connection
conn.commit()
cursor.close()
conn.close()

print(f"Inserted {num_users} users and {num_tasks} tasks into the database.")
