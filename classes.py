class Person:
    def __init__(self, name, money, mood, health_rate):
        self.name = name
        self.money = money
        self.mood = mood
        self.health_rate = max(0, min(health_rate, 100))

    def sleep(self, hours):
        if hours == 7:
            self.mood = "happy"
        elif hours < 7:
            self.mood = "tired"
        else:
            self.mood = "lazy"

    def eat(self, meals):
        if meals == 3:
            self.health_rate = 100
        elif meals == 2:
            self.health_rate = 75
        elif meals == 1:
            self.health_rate = 50

    def buy(self, items):
        self.money -= items * 10


class Car:
    def __init__(self, name, fuel_rate, velocity):
        self.name = name
        self.fuel_rate = max(0, min(fuel_rate, 100))
        self.velocity = max(0, min(velocity, 200))

    def run(self, velocity, distance):
        self.velocity = velocity
        fuel_needed = distance / 10 * 10
        self.fuel_rate -= fuel_needed
        if self.fuel_rate <= 0:
            remain_distance = distance - ((self.fuel_rate + fuel_needed) / 10 * 10)
            self.stop(remain_distance)
        else:
            self.stop(0)

    def stop(self, remain_distance):
        self.velocity = 0
        if remain_distance > 0:
            print(f"Car stopped. Could not complete the journey. {remain_distance} km remaining.")
        else:
            print("Car arrived at destination.")


class Employee(Person):
    def __init__(self, name, money, mood, health_rate, emp_id, car, email, salary, distance_to_work):
        super().__init__(name, money, mood, health_rate)
        self.emp_id = emp_id
        self.car = car
        self.email = email
        self.salary = max(salary, 1000)
        self.distance_to_work = distance_to_work

    def work(self, hours):
        if hours == 8:
            self.mood = "happy"
        elif hours > 8:
            self.mood = "tired"
        else:
            self.mood = "lazy"

    def drive(self, distance):
        self.car.run(self.car.velocity, distance)

    def refuel(self, gas_amount=100):
        self.car.fuel_rate = min(100, self.car.fuel_rate + gas_amount)

    def send_mail(self, to, subject, body, receiver_name):
        with open("emails.txt", "a") as f:
            f.write(f"To: {to}\nSubject: {subject}\nReceiver: {receiver_name}\nMessage: {body}\n\n")


class Office:
    employees_num = 0

    def __init__(self, name):
        self.name = name
        self.employees = []

    def hire(self, employee):
        self.employees.append(employee)
        Office.employees_num += 1

    def fire(self, emp_id):
        self.employees = [e for e in self.employees if e.emp_id != emp_id]
        Office.employees_num -= 1

    def get_all_employees(self):
        return self.employees

    def get_employee(self, emp_id):
        for emp in self.employees:
            if emp.emp_id == emp_id:
                return emp
        return None

    def deduct(self, emp_id, deduction):
        emp = self.get_employee(emp_id)
        if emp:
            emp.salary -= deduction

    def reward(self, emp_id, bonus):
        emp = self.get_employee(emp_id)
        if emp:
            emp.salary += bonus

    def check_lateness(self, emp_id, move_hour):
        emp = self.get_employee(emp_id)
        if emp:
            arrive_time = move_hour + (emp.distance_to_work / emp.car.velocity)
            if arrive_time > 9:
                self.deduct(emp.emp_id, 10)
                return "Late"
            else:
                self.reward(emp.emp_id, 10)
                return "On Time"

    @staticmethod
    def calculate_lateness(target_hour, move_hour, distance, velocity):
        arrive_time = move_hour + (distance / velocity)
        return arrive_time > target_hour

    @classmethod
    def change_emps_num(cls, num):
        cls.employees_num = num
