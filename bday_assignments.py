
import random
people={'Gesa', 'Sebi', 'Tobi', 'Katschi', 'Anna', 'Marcel', 'Lars'}
emails:{'Gesa':'buffy-jeanne@hotmail.de', 'Sebi':'buffy-jeanne@hotmail.de', 'Tobi':'buffy-jeanne@hotmail.de', 'Katschi':'buffy-jeanne@hotmail.de', 'Anna':'buffy-jeanne@hotmail.de', 'Marcel':'buffy-jeanne@hotmail.de', 'Lars':'buffy-jeanne@hotmail.de'}

assignments={}
already_bday=set()

for person in people:
    people_list=list(people-{person}-already_bday)
    bdaychild=random.choice(people_list)
    assignments[person]=bdaychild
    already_bday.add(bdaychild)

#can fail if the last person gets only hisself. --> we have to implement if error try again from the start on
