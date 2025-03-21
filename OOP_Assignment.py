# Assignment 1: Design Your Own Class

class Smartphone:
    def __init__(self, brand, model, battery_life):
        self.brand = brand
        self.model = model
        self.battery_life = battery_life  # in hours

    def get_info(self):
        return f"{self.brand} {self.model} with {self.battery_life} hours battery life."

    def charge(self):
        return f"{self.model} is charging... 🔋"

# Inheriting from Smartphone
class AdvancedSmartphone(Smartphone):
    def __init__(self, brand, model, battery_life, camera_megapixels, fast_charging):
        super().__init__(brand, model, battery_life)
        self.camera_megapixels = camera_megapixels
        self.fast_charging = fast_charging

    def take_photo(self):
        return f"📸 Taking a photo with {self.camera_megapixels} MP camera."

    def charge(self):
        return f"{self.model} supports fast charging: {self.fast_charging} ⚡"

# Creating objects
phone1 = Smartphone("Samsung", "Galaxy S21", 24)
phone2 = AdvancedSmartphone("Apple", "iPhone 14 Pro", 20, 48, True)

print(phone1.get_info())
print(phone2.get_info())
print(phone2.take_photo())
print(phone2.charge())

# Activity 2: Polymorphism Challenge

class Vehicle:
    def move(self):
        pass  # Abstract method

class Car(Vehicle):
    def move(self):
        return "🚗 Driving on the road."

class Plane(Vehicle):
    def move(self):
        return "✈️ Flying in the sky."

class Boat(Vehicle):
    def move(self):
        return "🚢 Sailing on water."

# Creating instances
vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    print(v.move())  # Calls the overridden method in each subclass
