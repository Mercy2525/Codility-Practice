# Kata Task
# I have a cat and a dog.
# I got them at the same time as kitten/puppy. That was humanYears years ago.
# Return their respective ages now as [humanYears,catYears,dogYears]
# NOTES:
# humanYears >= 1
# humanYears are whole numbers only
# Cat Years
# 15 cat years for first year
# +9 cat years for second year
# +4 cat years for each year after that
# Dog Years
# 15 dog years for first year
# +9 dog years for second year
# +5 dog years for each year after that

# https://www.codewars.com/kata/5a6663e9fd56cb5ab800008b


def human_years_cat_years_dog_years(human_years):
    cat_age=0
    dog_age=0
    
    if human_years==1:
        cat_age +=15
        dog_age +=15
    elif human_years==2:
        cat_age +=24
        dog_age +=24
    elif human_years>=3:
        cat_age=24+ 4*(human_years-2)
        dog_age=24+ 5*(human_years-2)
    return [human_years,cat_age,dog_age]

print(human_years_cat_years_dog_years(2))