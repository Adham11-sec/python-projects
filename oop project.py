from models import Car, Employee, Office

samy_car = Car(name="Fiat 128", fuel_rate=100, velocity=60)

samy = Employee(
    name="Samy",
    money=500,
    mood="neutral",
    health_rate=80,
    emp_id=1,
    car=samy_car,
    email="samy@iti.org",
    salary=3000,
    distance_to_work=20
)

iti_office = Office("ITI Smart Village")
iti_office.hire(samy)

samy.eat(2)
print(f"{samy.name}'s health rate after eating: {samy.health_rate}%")

samy.sleep(6)
print(f"{samy.name}'s mood after sleeping: {samy.mood}")

samy.buy(2)
print(f"{samy.name}'s money after shopping: {samy.money} LE")

print("\n--- Samy Driving to Work ---")
samy.drive(samy.distance_to_work)

status = iti_office.check_lateness(samy.emp_id, move_hour=8.5)
print(f"Samy's arrival status: {status}")
print(f"Samy's updated salary: {samy.salary} LE")

samy.work(8)
print(f"{samy.name}'s mood after work: {samy.mood}")
