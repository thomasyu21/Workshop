# Eliza Knapp, Rachel Xiao, Thomas Yu
# SoftDev
# K05 -- Print A SoftDev Student's Name (Amalgamated)
# 2021-09-27

'''
Summary:
- How to approach the list of names
    - Read in names from a text file instead of having list created with names
    - Allows the lists to be changed easily
    - One text file per period
    - This had now been changed to precoded lists in the form of a dictionary
- Any exceptions to watch out for
    - The file not existing in the directory
    - The file being empty
    - Solve these issues with try and except
    - Would have to print outputs separately (to check for each list individually)
    - Exceptions no longer are an issue (aren't reading lines from text file)
- How to choose the name
    - randint to generate random index within bounds
Discoveries:
- Try catch blocks in python are try: except:
- without line.strip() it will keep the \n with the name, creating a new line in the output
- Python dictionaries and how to access the keys and values within the dictionary
Questions:
- How would we make it work for and infinite number of periods?
Comments:
- 
'''

import random

def generate_name():
  #NAMES = Python dictionary
  NAMES = {
    "pd1": ["Reng geng Zheng", "Edwin Zheng", "Angela Zhang", "Owen Yaggy",
            "Oscar Wang", "Lucas Tom wong", "Tami Takada", "Rayat Roy",
            "Tina Nguyen", "Julia Nelson", "Naomi Naranjo", "Justin Morrill",
            "Iwan Mijackia", "Gavin Mcginley", "Ishraq Mahid", "Deven Maheshwari",
            "Michelle Lo", "Christopher Liu", "Zhao yu Lin", "Lucas Lee", "Ivan Lam",
            "Ella Krechmer", "aryaman Goenka", "Sean Ging", "Haotian Gan", "Theodore Fahey",
            "Sadid Ethun", "Aaron Contreras", "Shyne Choi", "William Chen", "Emma Buller",
            "Shriya Anand", "Alejanro Alonso", "Tomas Acuna"],
    "pd2": ["Justin Zou", "Mark Zhu", "Han Zhang", "Annabel Zhang", "Thomas Yu",
            "Raymond Yeung", "Jessie Xie", "Rachel Xiao", "Yuqing Wu",
            "Jonathan Wu", "Liesel Wong", "Ryan Wang", "Daniel Sooknanan",
            "Roshani Shrestha", "Shadman Rakib", "Austin Ngan", "Cameron Nelson",
            "Sophie Liu", "Qina Liu", "Andy Lin", "Yaying Liang Li",
            "Josephine Lee", "Joshua Kloepfer", "Andrew Juang", "Hebe Huang"
            "Eric Guo", "Patrick Ging", "Wen hao Dong", "David Chong", "Yoonah Chang",
            "Kevin Cao", "Michael Borczuk", "Noakai Aronesty", "Alif Abdullah"]
  }

  # Generate random index within bounds for each list
  index1 = random.randint(0, len(NAMES["pd1"])-1)
  index2 = random.randint(0, len(NAMES["pd2"])-1)

  # Print names corresponding to indices generated earlier
  print("pd1: " + (NAMES["pd1"])[index1])
  print("pd2: " + (NAMES["pd2"])[index2])


generate_name()
