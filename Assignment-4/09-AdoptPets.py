"""
Raina Wan
07-25-2023

Adopt a Pet:
An animal shelter that houses cats and dogs wants to ensure no pet has to wait too long for a forever home. 
Therefore, anyone who comes to adopt a pet can pick the species (cat or dog) but not the specific animal; 
they are assigned the animal of that species that has been in the shelter longest. If there are no animals 
available of the desired species, they must take the other species. You are given a list of pets in the shelter 
with their names, species, and time in the shelter at the start of a week. You receive a sequence of incoming 
people (to adopt pets) and animals (new additions to the shelter) one at a time. Print the names and species of 
the pets as they are adopted out.

Time Complexity: O (m * n) => m pets to add to queue and n adoptions to visit
Space Complexity: O(m + n) => creating two queues: one with m dogs and one with n cats

Time Spent:
35 minutes
"""


from collections import deque


def adopt_pet(pets, adoptions):
    dog, cat, res = [], [], []
    for name, animal, time in pets:
        if animal == 'dog':
            dog.append((time, name))
        else:
            cat.append((time, name))

    dog.sort() # sort by longest to shortest time in shelter
    cat.sort()
    dog = deque(dog)
    cat = deque(cat)
    
    for i in range(len(adoptions)):
        # person adopting
        if adoptions[i][1] == 'person':
            animal = adoptions[i][-1]
            
            # Option 1: pick dog
            if (animal == 'dog' and len(dog) != 0) or (animal == 'cat' and len(cat) == 0):
                if dog:
                    pet = dog.pop()
                    res.append((pet[-1], 'dog'))
            # Option 2: pick cat
            else:
                if cat:
                    pet = cat.popleft()
                    res.append((pet[-1], 'cat'))

        else:
            name, animal = adoptions[i][0], adoptions[i][1]
            if animal == 'dog':
                dog.append((time, name))
            else:
                cat.append((time, name))
    
    return res


if __name__ == "__main__":

    pets = [('Sadie', 'dog', 4), 
            ('Woof', 'cat', 7),
            ('Chirpy', 'dog', 2), 
            ('Lola', 'dog', 1)]

    adoptions = [('Bob', 'person', 'dog'), 
                 ('Floofy', 'cat'), 
                 ('Ji', 'person', 'cat'),
                 ('Sally', 'person', 'cat'), 
                 ('Ali', 'person', 'cat')]

    print(adopt_pet(pets, adoptions))



"""
    Input: ('Bob', 'person', 'dog')
    Output: ('Sadie', 'dog')

    Input: ('Floofy', 'cat')
    Output: 

    Input: ('Ji', 'person', 'cat')
    Output: ('Woof', 'cat')

    Input: ('Sally', 'person', 'cat')
    Output: ('Floofy', 'cat')

    Input: ('Ali', 'person', 'cat')
    Output: ('Chirpy', 'dog')
"""