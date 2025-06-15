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

	Add an image named code masters image.png to the project       directory.

3. Run the application-

	main.py


📁 File Overview-

•	File	Description

	main.py- Main - application script
	quiz database.db - SQLite database (auto-created)
	code masters image.png - Home-screen background image



🔄 Flow Summary-


1.	Home screen: Launches start() → prompts sign-up or login



 

















2.	Sign-Up: Collects and stores user info → proceeds to Login



 

















3.	Login: Verifies credentials against SQLite DB → open menu



 



















4.	Menu: Displays greeting + language selection (Python/Java/C)



 













5.	Quiz: 5 timed MCQs per session
Each question: 10-second timer + Submit/Next    



 
















6.	Results: Shows score and pie chart breakdown     



 



✔ To-Do & Enhancements -

•	Store questions in database or JSON for dynamic quizzes

•	Hash passwords for improved security

•	Expand question sets and difficulty ranges

•	Add progress tracking across multiple quiz sessions

📄 License -

•	Distributed under the MIT License. See LICENSE for details.

