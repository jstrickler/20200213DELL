#!/usr/bin/env python

emma_countries = ['Italy', 'France', 'Israel', 'UK', 'Canada']

eric_countries = ['Mexico', 'Canada', 'Germany', 'Austria', 'Kosovo',
      'Bulgaria', 'Kuwait', 'Iraq', 'France']


emma = set(emma_countries)
eric = set(eric_countries)

print(emma)
print(eric)

print("Both:", emma & eric)
print("Just one:", emma ^ eric)
print("All:", emma | eric)
print("Just Emma:", emma - eric)
print("Just Eric:", eric - emma)

all_food = ["spam", "spam", "spam", "spam", "spam", "spam",
    "eggs", "spam", "spam", "spam", "eggs", "brisket", "spam"]

food = set(all_food)
print(food)

