# 부모 클래스 Person 정의
class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def printInfo(self):
        print(f"ID: {self.id}, Name: {self.name}")

# Manager 클래스 (Person을 상속)
class Manager(Person):
    def __init__(self, id, name, title):
        super().__init__(id, name)
        self.title = title

    # printInfo 메서드를 오버라이딩하여 title도 출력
    def printInfo(self):
        print(f"ID: {self.id}, Name: {self.name}, Title: {self.title}")

# Employee 클래스 (Person을 상속)
class Employee(Person):
    def __init__(self, id, name, skill):
        super().__init__(id, name)
        self.skill = skill

    # printInfo 메서드를 오버라이딩하여 skill도 출력
    def printInfo(self):
        print(f"ID: {self.id}, Name: {self.name}, Skill: {self.skill}")

# 테스트 코드
if __name__ == "__main__":
    # 1. Person 클래스 테스트
    person1 = Person(1, "Alice")
    person1.printInfo()  # 출력: ID: 1, Name: Alice

    # 2. Person 클래스 두 번째 테스트
    person2 = Person(2, "Bob")
    person2.printInfo()  # 출력: ID: 2, Name: Bob

    # 3. Manager 클래스 테스트
    manager1 = Manager(3, "Charlie", "HR Manager")
    manager1.printInfo()  # 출력: ID: 3, Name: Charlie, Title: HR Manager

    # 4. Manager 클래스 두 번째 테스트
    manager2 = Manager(4, "David", "IT Manager")
    manager2.printInfo()  # 출력: ID: 4, Name: David, Title: IT Manager

    # 5. Employee 클래스 테스트
    employee1 = Employee(5, "Eve", "Python Developer")
    employee1.printInfo()  # 출력: ID: 5, Name: Eve, Skill: Python Developer

    # 6. Employee 클래스 두 번째 테스트
    employee2 = Employee(6, "Frank", "Data Analyst")
    employee2.printInfo()  # 출력: ID: 6, Name: Frank, Skill: Data Analyst

    # 7. Manager와 Employee 간의 차이 테스트
    manager3 = Manager(7, "Grace", "Marketing Manager")
    employee3 = Employee(8, "Hannah", "Web Developer")
    manager3.printInfo()  # 출력: ID: 7, Name: Grace, Title: Marketing Manager
    employee3.printInfo()  # 출력: ID: 8, Name: Hannah, Skill: Web Developer

    # 8. 다양한 이름과 ID 테스트
    person3 = Person(9, "Ivy")
    person3.printInfo()  # 출력: ID: 9, Name: Ivy

    # 9. Manager 객체에서 title 변경 후 출력 테스트
    manager4 = Manager(10, "Jack", "Finance Manager")
    manager4.title = "CFO"
    manager4.printInfo()  # 출력: ID: 10, Name: Jack, Title: CFO

    # 10. Employee 객체에서 skill 변경 후 출력 테스트
    employee4 = Employee(11, "Kate", "Java Developer")
    employee4.skill = "Kotlin Developer"
    employee4.printInfo()  # 출력: ID: 11, Name: Kate, Skill: Kotlin Developer
