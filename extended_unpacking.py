

address = ['200', 'Elm St.', 'Ames', 'Iowa']

number, street, city, state = address

people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', 'NeXT', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'),
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', 'Git', '1969-12-28'),
    ('John', 'Strickler', 'The Internet', 'Pet Rocks', 'Plutonium', '1956-10-31'),
]

for first_name, last_name, *product, dob in people:
    print(first_name, last_name, product)

