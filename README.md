# 🌤 Weather Forecast Application

A real-time weather forecasting web application built with Python and Flask,
powered by the OpenWeatherMap API. This project started as a curiosity-driven
exploration of how real-world weather data can be fetched, processed, and
presented through a clean web interface.

---

## 💡 Why I Built This

Honestly? It was just really hot outside.

I was sweating, constantly checking the weather on my phone, and at some point
I thought, I am literally a computer science student, why am I using someone else's app
for this? That was the moment I closed the weather app and opened VS Code.

I have always been curious about how weather applications work behind the scenes,
how they fetch live data, process it, and display it in a human-readable format.
Instead of just wondering, I decided to build one from scratch.

This project began as a simple terminal-based Python script where I could type
a city name and get the current weather. But I kept pushing further. I wanted
to understand how Python connects to the web, how APIs work in real projects,
and how a backend language like Python can serve a fully functional webpage.
What started as curiosity turned into a full-stack mini project that I am
genuinely proud of.

---

## 🚀 What It Does

- 🔍 Search weather for a **single city** and get a detailed result card
- 🌍 Compare weather across **up to 4 cities** simultaneously in a summary table
- ⚡ Fetches **real-time live data** from the OpenWeatherMap API
- 🌐 Fully accessible through the **web browser** via Flask
- 📊 Displays **temperature, weather condition, humidity, and wind speed**
- ➕ Dynamically **add or remove city inputs** without reloading the page

---

## 🛠 Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core backend logic |
| Flask | Web framework to serve the app in browser |
| OpenWeatherMap API | Live weather data source |
| HTML & CSS | Frontend structure and styling |
| JavaScript | Dynamic city input management |
| Jinja2 | HTML templating engine (comes with Flask) |

---

## 📁 Project Structure
```
Weather_Prediction_Project
  ├── weather.py          # Backend, Flask app and API logic
  ├── templates
  │     └── index.html    # Frontend HTML structure & styling and layout
  └── static
        └── bb.jpg    # Background Image
```

---

## 🔧 How to Run It

**1. Clone the repository**
```bash
git clone https://github.com/PrasidBhusal10/Weather_Prediction_Project.git
cd Weather_Prediction_Project
```

**2. Create and activate virtual environment**
```bash
python -m venv .venv
.venv\Scripts\activate
```

**3. Install dependencies**
```bash
pip install flask requests
```

**4. Set up your API key**

Get a free API key from [openweathermap.org](https://openweathermap.org/api)
then set it as an environment variable in cmd:
```bash
set WEATHER_API_KEY=your_api_key_here
```

> ⚠️ Never share or push your API key to GitHub!

**5. Run the app**
```bash
python weather.py
```

**6. Open in browser**
```
http://127.0.0.1:5000
```

**7. Use the app**
- Type a city name and click **Search** for single city weather
- Click **+ Add City** to compare up to 4 cities at once
- Click **×** to remove a city from the list

> 💡 **Note:** Make sure your virtual environment is always activated
> before running the app. You will see `(.venv)` at the start of your
> terminal line when it is active.

---

## 🌱 What I Learned

- How to make **HTTP requests** to third-party APIs using Python
- How **REST APIs** work and how to handle JSON responses
- How **Flask** works as a web framework and how it connects Python to the browser
- How to use **Jinja2 templating** to dynamically render data in HTML
- How to structure a project with **separated concerns** (backend, frontend, styling)
- How **virtual environments** work and why they matter in Python projects
- How to build a **dynamic UI** using vanilla JavaScript without any frameworks

---

## 🔮 Future Improvements

- Add a **5-day weather forecast** feature
- Include **weather icons** for each condition
- Deploy it online so anyone can use it without running it locally
- Add **geolocation** to auto-detect the user's city

---

## 👨‍💻 Author

Built with curiosity and determination by **Prasid Bhusal**
> *"I didn't just want to use technology — I wanted to understand it by building it."*
