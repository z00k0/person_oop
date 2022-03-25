class Person(object):

    def __init__(self, sex, name, spouse=None):
        self.sex = sex
        self.name = name
        self.spouse = spouse

    def __str__(self):
        return f'{self.name}, {self.sex}'

    def __repr__(self) -> str:
        return f'{self.name}, {self.sex}'

    def _can_marry(self, person):
        if self.sex != person.sex:
            return True
        else:
            raise AttributeError('Однополые браки запрещены')

    def marry(self, person):
        try:
            self._can_marry(person)
            self.spouse = person
            person.spouse = self
        except AttributeError as ex:
            print(ex)

    def divorce(self):
        self.spouse.spouse = None
        self.spouse = None


petr = Person(sex='male', name='Petr')
print(f'{petr=}')

lena = Person(sex='female', name='Lena')
print(f'{lena=}')

print(f"{petr.name=}, {petr.sex=}, {petr.spouse=}")
print(f"{lena.name=}, {lena.sex=}, {lena.spouse=}")

print('Marry Petr & Lena')
petr.marry(lena)
print(f"{petr.name=}, {petr.sex=}, {petr.spouse=}")
print(f"{lena.name=}, {lena.sex=}, {lena.spouse=}")

print('Marry Petr & John')
john = Person('male', 'John')
john.marry(petr)

print('Divorce')
petr.divorce()
print(f"{petr.name=}, {petr.sex=}, {petr.spouse=}")
print(f"{lena.name=}, {lena.sex=}, {lena.spouse=}")
