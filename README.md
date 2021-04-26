# Term Project - Covid Website Implementation Instruction



## Credit: 	
This project is created by Agnes Xie, Cathy Ma, and Zhe Wang from MIS3640 Babson College, Spring 2021. 


## Inspiration:
We have some friends who are very interested in the horoscope that they check on their horoscope on a daily basis. They check their fortune forecast even more frequently than checking the weather. The horoscope doesn't only describe the fundamental characteristics of each constellation, but can also predict their fortune with astrology. 

## Project Description:
This project is a website for horoscope amateurs to tell today's fortune based on their constellations. Users can click on their constellation by birthday and look up the characteristics including description and date range. Based on the date of input, the system will forecast the user's fortune of the day including compatibility, mood, color, lucky number, and lucky time. Users can also input their birthday and the system will automatically take the user to their constellation page. And of course, users can look up other constellations as well. 

## Required Libraries
- [ ] flask
- [ ] requests
- [ ] bisect



## User Instruction

- [ ] Please go to [our codes on githubs](https://github.com/hma1/Project) and clone files to your computer.
- [ ] Please double check to make sure that you have all the required libraries.
- [ ] Please find the file *app.py* ([app](app.py))and run the code.
- [ ] After seeing *Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)*, please either 
    - [ ] Press CTRL and click the website link in your terminal window or 
    - [ ] Click [here](http://127.0.0.1:5000/).
- [ ] When you see the homepage, please enter your birthday as the example illustrates to find your horoscope.
    - [ ] If you already know your horoscope, you can also click on the icon to be directed to the info page.
- [ ] On the info page, you can read about your fortune today. You can also click on next to see other horoscope results.
- [ ] If you did not enter your birthday correctly, you will be directed to the error page. Dont worry, just click to go back to the home page and enter again.


## Project Evolution
- During the process of completing this assignment, one of the biggest challenges we encountered was that we could not link the code in app.py, which processes the information about the requesting place, to our designed htmls. It took us a while to figure out the potential causes and the corresponding solutions. Eventually, we found out the bug was due to the function name that we entered unmatch. Another challenge was that we were able to use CSS functions like image and insert image to make our web page more fun. For the assignment, one of the problems we encoutered is that we could not load our website. Every time when we attempted to process it, the browser always returned an error page. It took us quite a long time to figure out the potential cause and the corresponding solution. Eventually, we found out that it was due to the title of one of the folders. The name of that folder was "Code/code", which we basically added another "layer" to the folder. Thus, the code lost track and could not find the template folder where we stored all the indexes (ex. error html). We will be careful with this type of issue when we are going through the term project. Although it was a small problem and we fixed it easily by deleting the folder, it would be very helpful for us to know this ahead of time. So we would not make the same mistake for the term project and spent too much time on a non-technical issue. It was a good opportunity for us to analyze a problem and attempted to solve it through different ways. Moving on, we expect to improve our working efficiency as well as our ability of problem analysis. We realized that our mind should not be bonded by only looking at the technical sides, such as correct usage of API keys or term definition. Details always matter and sometimes soft skill is also crucial during task-solving.

- During the process of completing this assignment, one of the biggest challenges we encountered was that we could not link the code in app.py, which processes the information about the requesting place, to our designed htmls. It took us a while to figure out the potential causes and the corresponding solutions. Eventually, we found out the bug was due to the function name that we entered unmatch. Another one was that we tried to follow the given function names at first, but found out we could not go step by step as the given function name asked. So we changed some of the function names and designed them as our logics. Gladly they both functioned well. A another evolution was that we were able to use CSS functions to make our web page more fun.

-For higher working efficiency, we splitted the work by parts as our proposal suggested. The whole process went well, since we were able to start early and kept communicating with each other on Wechat. We were able to encourage and help each other when facing difficulties, so we successfully completed the project quickly and efficiently.

## More information
For more information on implementation and results, please go to[here](https://docs.google.com/document/d/13ModzsCdd--Y-co1ynOrVpDbNEB4Jx-zQegWjK-XheA/edit?usp=sharing)
