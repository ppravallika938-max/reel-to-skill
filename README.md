# Reel2Skill 

**Turn your scrolling into useful technology!**

Reel2Skill is a simple **Streamlit web application** that detects a user's technology interests based on the Reels they have watched. It analyzes selected Reel categories and recommends a useful technology topic to learn next.

## Features

*  Select the Reels you have watched
* Detect your primary technology interest
* 💻 Identify interests such as:

  * Software Engineering
  * Artificial Intelligence
  * Computer Hardware
  * General Technology
*  Get a personalized technology recommendation
*  Shows recommendation category and difficulty
*  Explains why the recommendation was selected
*  Displays confidence level

##  Technologies Used

* **Python**
* **Streamlit**

## Project Structure

```text
Reel2Skill/
│
├── app.py
├── README.md
└── LICENSE
```

##  Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/Reel2Skill.git
cd Reel2Skill
```

### 2. Install dependencies

```bash
pip install streamlit
```

### 3. Run the application

```bash
streamlit run app.py
```

The application will open in your browser.

## 🎯 How It Works

The application provides a list of sample Reels such as:

* Java Meme
* Software Engineer Life
* Coding Interview Joke
* Laptop Comparison
* AI Tutorial
* Gaming Video
* Cricket Video

The selected Reels are mapped to categories such as **Programming, Career, Hardware, AI, Gaming,** and **Entertainment**.

Based on the selected categories, Reel2Skill determines the user's likely interest.

### Example

If a user selects:

* Java Meme
* Coding Interview Joke
* Software Engineer Life

The application detects:

> **Software Engineering**

and recommends:

> **How HashMaps Work**

## 🚀 Future Improvements

* Add more Reel categories
* Use Machine Learning for interest detection
* Connect with YouTube or other learning platforms
* Recommend actual educational videos
* Add user profiles and learning history
* Track learning progress
* Generate personalized learning paths
* Add more advanced difficulty levels

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Commit your changes
5. Push the branch
6. Open a Pull Request

## 📄 License

This project is licensed under the **MIT License**.

## 👨‍💻 Author

Created as a project to demonstrate how entertainment preferences can be converted into useful learning recommendations.
