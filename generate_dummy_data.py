# Purpose: Generate dummy data using faker, structured to match your .proto definitions.

from faker import Faker
from pizzeria.recipe_pb2 import Recipe
from google.protobuf.json_format import MessageToJson

fake = Faker()

def generate_sample_recipe():
    recipe = Recipe(
        name=fake.sentence(),
        shelf_life=fake.random_int(1, 30),
        servings=fake.random_int(1, 10),
        base_cost=fake.pyfloat(left_digits=2, right_digits=2, positive=True),
        margin=fake.pyfloat(left_digits=1, right_digits=2, positive=True),
        preparation_time=fake.random_int(5, 60),
        cook_time=fake.random_int(5, 120)
    )
    return MessageToJson(recipe)

# Generate and print JSON data
if __name__ == "__main__":
    print(generate_sample_recipe())