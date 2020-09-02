import pandas as pd

userCarbPercent, userProteinPercent, userFatPercent = 0,0,0
mealUserMacros = {}

dfBreakfast = pd.read_csv("Eat_Skinny/Skinny_Breakfast_Recipes.csv")
dfBreakfast_2 = pd.read_csv("Skinny_Taste/Skinny_Taste_Breakfast_Recipes.csv")
dfBreakfast = dfBreakfast.append(dfBreakfast_2, ignore_index = True)

dfLunch = pd.read_csv("Eat_Skinny/Skinny_Lunch_Recipes.csv")
dfLunch_2 = pd.read_csv("Skinny_Taste/Skinny_Taste_Lunch_Recipes.csv")
dfLunch = dfLunch.append(dfLunch_2, ignore_index = True)

dfDinner = pd.read_csv("Eat_Skinny/Skinny_Dinner_Recipes.csv")
dfDinner_2 = pd.read_csv("Skinny_Taste/Skinny_Taste_Dinner_Recipes.csv")
dfDinner = dfDinner.append(dfDinner_2, ignore_index = True)


print("\n Type in your top 5 favorite foods you would eat NO MATTER WHAT HAPPENED - omake sure to seperate with commas")
print("Try to be as generic as possible yet specific. REMEMBER COMMAS!: ")
Foods = (input("Answer: ").lower()).replace(" ", "")
favoriteFoods = Foods.split(",")

userCal = int(input("How many Calories do you want in your meal Plan?: "))
while(userCarbPercent + userProteinPercent + userFatPercent) != 100:
  if ((userCarbPercent + userProteinPercent + userFatPercent) != 100):
    print("\n Input Macronutrient Percentage Values in order of Carbs, Protein, and Fats - only numbers seperated with commas")
    print("EXAMPLE: 30,30,40")
    print("If you get this message again then your percentages don't add up to 100")
    macroPercentage = input("Input Macronutrient Percentage: ")

  try:
    userCarbPercent, userProteinPercent, userFatPercent = map(int, macroPercentage.split(","))
  except:
    print("\n You didn't type in the values correctly. Remeber no %, just numbers, seperated with commas. TRY AGAIN")
    
userCarbGrams = (userCal * (userCarbPercent / 100))// 4
userProteinGrams = (userCal * (userProteinPercent / 100))// 4
userFatGrams = (userCal * (userFatPercent / 100))// 9

print("\nYour meal plan will have near " + str(userCarbGrams) + " grams of Carbs, " + str(userProteinGrams) + " grams of protein, and " + str(userFatGrams) + " grams of Fat")

numberUserMeals = int(input("How many meals would you want in a day, just put in a number: "))

for i in range(0,numberUserMeals):
  userCarb = 0
  userProtein = 0
  userFat = 0
  while (userCarb == 0 and userProtein == 0 and userFat == 0):
    print("\nWhat type of meal do you want for Meal #" + str(i+1))
    mealType = (input("Choose 'Breakfast', 'Lunch', or 'Dinner'. Type it EXACTLY!: ")).lower()
    print("\nInput your macros in GRAMS just in number form in the the order of carbs, protein, and fats. Make sure to seperate each number with commas.")
    tempMarcos = input("What are your preffered macros for Meal #" + str(i+1) + ": ")
    try:
      userCarb, userProtein, userFat = map(int, tempMarcos.split(","))
    except:
      print("\n You didn't type in the values correctly. Remeber no 'grams', just numbers, seperated with commas. TRY AGAIN")
  totalCal = ((userCarb + userProtein) * 4) + (userFat * 9)
  mealUserMacros["Meal #" + str(i+1)] = [userCarb, userProtein, userFat, mealType, totalCal]

#Abstraction
def Range(target, number, lowPercentage, highPercentage):
  lowBound = (target * lowPercentage)
  highBound = (target * highPercentage)

  if (number > lowBound and number < highBound):
    return (True)
  else:
    return (False)

def sortFavorites():
  global dfBreakfast_01
  global dfLunch_01
  global dfDinner_01

  dfBreakfast_01 = dfBreakfast.copy()
  dfLunch_01 = dfLunch.copy()
  dfDinner_01 = dfDinner.copy()

  dfBreakfast_01["Score"] = 0
  dfLunch_01["Score"] = 0
  dfDinner_01["Score"] = 0

  for index, row in dfBreakfast_01.iterrows():
    for food in favoriteFoods:
      tempIngred = food in (dfBreakfast_01.Ingredients[index])
      tempTitle = food in (dfBreakfast_01.Name[index])
      if(tempIngred or tempTitle):
         dfBreakfast_01.loc[index, "Score"] = dfBreakfast_01.loc[index, "Score"] + 1

  for index, row in dfLunch_01.iterrows():
    for food in favoriteFoods:
      tempIngred = food in (dfLunch_01.Ingredients[index])
      tempTitle = food in (dfLunch_01.Name[index])
      if (tempIngred or tempTitle):
        dfLunch_01.loc[index, "Score"] = dfLunch_01.loc[index, "Score"] + 1
      
  for index, row in dfDinner_01.iterrows():
    for food in favoriteFoods:
      tempIngred = food in (dfDinner_01.Ingredients[index])
      tempTitle = food in (dfDinner_01.Name[index])
      if (tempIngred or tempTitle):
        dfDinner_01.loc[index, "Score"] = dfDinner_01.loc[index, "Score"] + 1

  dfBreakfast_01 = dfBreakfast_01.sort_values(by = "Score", ascending = False)
  dfBreakfast_01 = dfBreakfast_01.reset_index(drop = True)

  dfLunch_01 = dfLunch_01.sort_values(by = "Score", ascending = False)
  dfLunch_01 = dfLunch_01.reset_index(drop = True)

  dfDinner_01.sort_values(by = "Score", ascending = False)
  dfDinner_01 = dfDinner_01.reset_index(drop = True)

#Child Algorithm #1
def checkMacros(meal, carbs, protein, fat, calories, lowPercentage, highPercentage, servings):
  test = mealUserMacros.get(meal)
  carbsGrams = test[0] 
  proteinGrams = test[1]
  fatsGrams = test[2]
  actualCal = test[4]

  carbs = servings * carbs
  protein = servings * protein
  fat = servings * fat
  calories = servings * calories

  if (Range(carbsGrams, carbs, lowPercentage, highPercentage) and Range(proteinGrams, protein, lowPercentage, highPercentage) and Range(fatsGrams, fat, lowPercentage, highPercentage) and Range(actualCal, calories, lowPercentage, highPercentage)):
    return (True)
  else:
    return (False)

#Child Algorithm #2  
def getMealMacros(rowIndex, typeMeal):
  if (typeMeal == "breakfast"):
    carbs = dfBreakfast_01.loc[rowIndex, "Carbs Grams"]
    protein = dfBreakfast_01.loc[rowIndex, "Protein Grams"]
    fat = dfBreakfast_01.loc[rowIndex, "Fat Grams"]
    calories = dfBreakfast_01.loc[rowIndex, "Calories"]
    url = dfBreakfast_01.loc[rowIndex, "Url"]
    name = dfBreakfast_01.loc[rowIndex, "Name"]

  elif (typeMeal == "lunch"):
    carbs = dfLunch_01.loc[rowIndex, "Carbs Grams"]
    protein = dfLunch_01.loc[rowIndex, "Protein Grams"]
    fat = dfLunch_01.loc[rowIndex, "Fat Grams"]
    calories = dfLunch_01.loc[rowIndex, "Calories"]
    url = dfLunch_01.loc[rowIndex, "Url"]
    name = dfLunch_01.loc[rowIndex, "Name"]
    

  elif (typeMeal == "dinner"):
    carbs = dfDinner_01.loc[rowIndex, "Carbs Grams"]
    protein = dfDinner_01.loc[rowIndex, "Protein Grams"]
    fat = dfDinner_01.loc[rowIndex, "Fat Grams"]
    calories = dfDinner_01.loc[rowIndex, "Calories"]
    url = dfDinner_01.loc[rowIndex, "Url"]
    name = dfDinner_01.loc[rowIndex, "Name"]

  temp = [carbs, protein, fat, calories, url, name]
  return (temp)

#MAIN Algorithm
def generateMealPlan(mealTypes):
  global mealPlan
  global servings
  global lowPercentageList
  global highPercentageList

  lowPercentageList = []
  highPercentageList = []
  mealPlan = {}

  for index, meal in enumerate(mealUserMacros):
    lowPercentage = 0.9
    highPercentage = 1.1
    typeMeal = mealTypes[index]
   
    lookMeal = True
    rowIndex = 0
    if (typeMeal == "breakfast"):
      lenDf = len(dfBreakfast_01.index)
    if (typeMeal == "lunch"):
      lenDf = len(dfLunch_01.index)
    if (typeMeal == "dinner"):
      lenDf = len(dfDinner_01.index)
    
    while(lookMeal):
      servings = 0.5
      macros = getMealMacros(rowIndex, typeMeal)
      carbs = macros[0]
      protein = macros[1]
      fat = macros[2]
      calories = macros[3]
      url = macros[4]
      name = macros[5]

      for i in range(0,8):
        if (checkMacros(meal, carbs, protein, fat, calories, lowPercentage, highPercentage,servings)):
          lookMeal = False
          mealPlan[meal] = [url, name, typeMeal, servings]

          lowPercentageList.append((1 - lowPercentage) * 100)
          highPercentageList.append((highPercentage - 1) * 100)
        servings = servings + 0.5

      rowIndex = rowIndex + 1

      if (rowIndex == lenDf):
        rowIndex = 0
        lowPercentage = lowPercentage - (0.02)
        highPercentage = highPercentage + (0.02)
  print("\n" + str(mealPlan))

mealTypes = []
for meal in mealUserMacros:
  temp = mealUserMacros.get(meal)
  mealTypes.append(temp[3])

sortFavorites()
generateMealPlan(mealTypes)

print(lowPercentageList)
print(highPercentageList)

print("\nWant to change your meal types and number of meals?")
ans = input("Put 'Yes' for yes and 'No' for no:")

if (ans == "Yes"):
  print("\nPut Lunch, Dinner, or Breakfast in the order of the meals, but for the program to work the number of choices must equal the amount of meals you're having in a day")
  mealTypes = (input("Put either 'breakfast', 'lunch', or 'dinner' seprated by only commas:")).split(",")

  generateMealPlan(mealTypes)
else:
  print("\nCheck out the recipes in your meal plan with the urls")
  
  


