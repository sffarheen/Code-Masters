Code Master 🎯🧐


Code Master is a desktop quiz application built with Python, Tkinter, SQLite3, and PIL. It allows users to sign up, log in, and take timed quizzes in computer programming languages. The app also tracks scores and visualizes results with a pie chart.

🧠 Features-

•	User Authentication

•	Sign-up and login system with SQLite 3 backend

•	Stores user details

•	Menu & Personalized Greetings

•	Welcome screen after login with greeting (e.g., "Hi! FullName")

•	Language selection: Python, Java, or C

•	Timed Quizzes (10 sec per question)

•	Each quiz has 5 randomly chosen multiple-choice questions

•	Languages: Python, Java, C language

•	10-second countdown per question; auto-advances on timeout

•	Scoring & Visualization

•	Tracks correct answers 

•	Presents final score and pie-chart breakdown using matplotlib

•	Retry & Logout Options

•	Users can retry the quiz or sign out


🛠 Tech Stack-

•	Python 3.x

•	Tkinter – GUI

•	SQLite 3 – Local database storage

•	PIL (Pillow) – Display image on home screen

•	matplotlib – Score pie-chart in results window

•	numpy – calculates the score points


🏁 Getting Started-

•	Prerequisites

        Install the required Python packages:
	Pip install tkinter
	Pip install random
	Pip install sqlite3 
	Pip install time
	Pip install pillow
	Pip install matplotlib
	Pip install numpy

•	Getting the App Running

1.	Clone the report-

	git clone https://github.com/yourusername/code-master.git
	cd code-master

2. Place the home-screen image-

	Add an image named code masters image.png to the project directory.

3. Run the application-

	main.py


📁 File Overview-

•	File	Description

	main.py- Main - application script
	quiz database.db - SQLite database (auto-created)
	code masters image.png - Home-screen background image



🔄 Flow Summary-


1.	Home screen: Launches start() → prompts sign-up or login

   ![Screenshot 2025-06-15 150413](https://github.com/user-attachments/assets/8c694db2-ce87-4232-a3bf-104a087423c8)


2.	Sign-Up: Collects and stores user info → proceeds to Login


    ![Screenshot 2025-06-15 150547](https://github.com/user-attachments/assets/310b0b48-23e6-4b13-bf06-13c5e9d8345b)


3.	Login: Verifies credentials against SQLite DB → open menu


 ![Screenshot 2025-06-15 150752](https://github.com/user-attachments/assets/4d700292-c8b0-49f3-b98c-897fb9c8f982)


4.	Menu: Displays greeting + language selection (Python/Java/C)

 ![Screenshot 2025-06-15 150857](https://github.com/user-attachments/assets/fca90ebc-7b14-420a-a685-e8135b705697)


5.	Quiz: 5 timed MCQs per session
              Each question: 10-second timer + Submit/Next    


![Screenshot 2025-06-15 150914](https://github.com/user-attachments/assets/958b53b6-e46a-47ee-91d9-202faa7c294a)


6.	Results: Shows score and pie chart breakdown     

![Screenshot 2025-06-15 151234](https://github.com/user-attachments/assets/61b187c9-61d4-4d64-bdcb-773dc2d3d09b)


✔ To-Do & Enhancements -

•	Store questions in database or JSON for dynamic quizzes

•	Hash passwords for improved security

•	Expand question sets and difficulty ranges

•	Add progress tracking across multiple quiz sessions

📄 License -

•	Distributed under the MIT License. See LICENSE for details.

