  # Lifesum technical assignment
  
  ## Prerequisites
  
  All of this project was built under python `Anaconda` environnement (version 2.7)
  You also need to install and use Jupyter Notebook` to vizualize the analysis results. 
  
  ## Project architecture
  
  Main parts are divided into folders `data` and `notebooks`and the database dump which contain 
  tables and views used to analyse the data sets provided.
  
  #### 1 - Data
  
  Original datasets provided with the instruction pdf are stored here. 
  I also have dumped some MySQL view from the database. These csv files are in the sub folder
  `from_DB`. 
  
  #### 2 - Notebooks
  
  All of my code was developped over Jupyter Notebook under the default conda env. 
  - _drafts_: contained few notebooks about data exploring. I put them in this place because 
  they testify about some research but they're finally not so much relevant for the analysis purpose.
   
  - _exploring_: It was just about the first data exploring. This was the opportunity to identify some few steps about 
  pre-processing data and save all of the four csv file in the database, as tables. 
  
  - And you will also find four notebooks whith the name of mains analysis angle which are 
  mentionned in the question part of the instruction file. 
  
  #### 3 - The MySQL database dump
  
  I used MySQL to create some join between datasets. I felt more comfortable to do  it in SQL. 
  You can find all of dumps as VIEWS in the database exporte archived at this project root.
  
  #### 4 - Instructions
  
  You may answer any number of these, in any order:
1. Demographics.Describeourouruserbase.Whatdoesatypicaluserlooklike? What goals do they have? How do these goals vary by demographics or need? (tip: consider calculating BMI)
2. Habits.DopeopletrackthreemealsperdaywithLifesum?Howlikelyareyouto track tomorrow if you tracked today?
3. Success.Howdoestrackingfoodandausersweightrelatetoeachother?Can you find any meaningful patterns or relationships?
4. Nutrition.Explorethemacronutrientbalance(protein,carbs,fat)ofpeople's main meals. What proportion of calories comes from each category? Does it vary by gender? By country? (tip: use common calorie conversions for macronutrients)

  
  