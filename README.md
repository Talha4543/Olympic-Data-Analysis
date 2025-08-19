# Olympic-Data-Analysis
1\. Introduction
----------------

The Olympic Games are the leading international sporting event, bringing together athletes from across the globe. This project analyzes the historical **Olympic dataset** (athlete\_events.csv) combined with **National Olympic Committees dataset** (noc\_regions.csv).

The analysis provides insights into **medal tallies, participation trends, athlete performance, and country-wise comparisons** using **Python, Pandas, Seaborn, Matplotlib, Plotly, and Streamlit**.

2\. Dataset Overview
--------------------

### **athlete\_events.csv**

*   271,116 rows × 15 columns
    
*   Key Columns:
    
    *   Name → Athlete name
        
    *   Sex → Gender (M/F)
        
    *   Age, Height, Weight → Athlete physical stats
        
    *   Team, NOC → Country representation
        
    *   Games, Year, Season, City → Event details
        
    *   Sport, Event → Sport and event categories
        
    *   Medal → Gold, Silver, Bronze, or NaN
        

### **noc\_regions.csv**

*   230 rows × 3 columns
    
*   Maps NOC codes (e.g., USA, PAK, IND) to region/country names.
    

### Preprocessing

*   Filtered for **Summer Olympics only**
    
*   Merged datasets on NOC to get country/region info
    
*   One-hot encoded medal counts (Gold, Silver, Bronze)
    
*   Removed duplicates
    

3\. Key Insights
----------------

### 3.1 Overall Statistics

*   **Editions**: 28 (from 1896 to 2016, Summer Olympics only)
    
*   **Hosts**: 23 unique cities
    
*   **Sports**: 52 unique sports
    
*   **Events**: 651 unique events
    
*   **Athletes**: ~116,000 unique participants
    
*   **Nations**: 206 countries/regions
    

### 3.2 Participation Trends

*   **Nations Over Time** → Number of participating countries increased steadily, especially after 1950.
    
*   **Events Over Time** → A consistent rise in the number of sports/events.
    
*   **Athletes Over Time** → Massive growth, with female participation increasing significantly post-1970s.
    

### 3.3 Medal Tally

*   **USA** dominates with the highest number of Gold and overall medals.
    
*   Former Soviet Union, UK, and Germany also consistently performed well.
    
*   Smaller nations like Jamaica and Kenya excel in niche sports (Athletics, Sprinting, Marathon).
    

### 3.4 Country-wise Analysis

*   **China**: Major rise in performance post-2000.
    
*   **India**: High participation but fewer medals, with strengths in Hockey, Wrestling, and Shooting.
    
*   **Pakistan**: Most Olympic medals came from Hockey (before 1994).
    

### 3.5 Athlete-wise Analysis

*   **Most Successful Athletes**:
    
    *   Michael Phelps (USA, Swimming) → 23 Golds
        
    *   Larisa Latynina (USSR, Gymnastics) → 18 medals
        
    *   Paavo Nurmi (Finland, Athletics) → 12 medals
        
*   **Age Distribution**:
    
    *   Most athletes between **20–30 years**.
        
    *   Gymnastics athletes peak earlier (~15–20).
        
    *   Shooting and Equestrian see older medalists (30–40+).
        
*   **Height vs Weight Analysis**:
    
    *   Clear sport-specific trends (e.g., Basketball players taller, Gymnasts lighter).
        

4\. Visualizations
------------------

*   📈 **Line Charts** → Participation trends of athletes, events, nations over time
    
*   🔥 **Heatmaps** → Events per sport per year, country medal performance
    
*   🏆 **Tables** → Medal tallies by year/country/sport
    
*   📊 **Scatterplots** → Height vs Weight by sport/medal
    
*   🎯 **Distribution Plots** → Age distribution of athletes & medal winners
    

5\. Tools & Technologies
------------------------

*   **Python** (Pandas, Numpy, Matplotlib, Seaborn, Plotly)
    
*   **Streamlit** → Interactive dashboard
    
*   **Data Source**: Kaggle – 120 Years of Olympic History: Athletes and Results
    

6\. Conclusion
--------------

*   Olympic participation has grown significantly over time in terms of **countries, athletes, and sports**.
    
*   Certain countries (USA, USSR, China) consistently dominate the medal tally.
    
*   Athletes’ performance varies strongly across sports in terms of **age, physique, and medal distribution**.
    
*   The analysis highlights not just medal counts, but also **global inclusivity and diversity in sports**.
    

7\. Future Work
---------------

*   Apply **machine learning** to predict medal winners.
    
*   Perform **gender equality analysis** over the years.
    
*   Build a **real-time Olympic dashboard** for Paris 2024 / LA 2028.

*   Repository:
