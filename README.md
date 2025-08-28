# 🎓 Python 101 — Interactive Classroom

An all-in-one Streamlit web application designed to teach absolute beginners the core Python concepts through interactive lessons and hands-on examples.

## 📋 Features

- **Interactive Learning**: 7 comprehensive lessons with live code examples
- **Hands-on Practice**: Run Python code directly in your browser
- **Progressive Curriculum**: From basic variables to API calls
- **Mini Quiz**: Test your knowledge with a 6-question assessment
- **Visual Learning**: Data visualization with matplotlib
- **Real-world Examples**: CSV handling and API interactions

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Installation & Setup

1. **Clone or download this repository**
   ```bash
   git clone <your-repo-url>
   cd streamlit-students
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**
   ```bash
   # On macOS/Linux:
   source venv/bin/activate
   
   # On Windows:
   venv\Scripts\activate
   ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the application**
   ```bash
   streamlit run streamlit.py
   ```

6. **Open your browser**
   - The app will automatically open at `http://localhost:8501`
   - If it doesn't open automatically, navigate to the URL shown in your terminal

## 📚 Curriculum Overview

### 1. Python Basics
- Variables and data types
- Type conversion and casting
- Print statements and string formatting

### 2. Lists & Loops
- List creation and manipulation
- Indexing and slicing
- Loops and list comprehensions

### 3. Functions & Errors
- Function definition and calling
- Error handling with try/except
- Raising custom exceptions

### 4. Files & CSV
- Reading CSV data with pandas
- File upload functionality
- Data manipulation and display

### 5. Data Visualization
- Creating charts with matplotlib
- Interactive plotting parameters
- Data visualization best practices

### 6. API Integration
- Making GET requests
- Sending POST requests
- Working with JSON data
- Error handling for network requests

### 7. Mini Quiz
- 6-question assessment
- Immediate feedback
- Progress tracking

## 🛠 Dependencies

The application uses the following key libraries:

- **streamlit**: Web app framework
- **pandas**: Data manipulation and analysis
- **numpy**: Numerical computing
- **matplotlib**: Data visualization
- **requests**: HTTP library for API calls

See `requirements.txt` for the complete list of dependencies.

## 🎯 Usage Tips

- Use the sidebar navigation to jump between lessons
- Each lesson includes expandable code sections with live examples
- Modify input widgets to see how changes affect the output
- Press **R** to rerun the app after making changes
- Take your time with each section before moving to the next

## 🔧 Development

### Project Structure
```
python-101-streamlit/
├── streamlit.py          # Main application file
├── requirements.txt      # Python dependencies
├── README.md            # This file
├── .gitignore          # Git ignore rules
└── venv/               # Virtual environment (created after setup)
```

### Adding New Lessons

To add new lessons, modify the `streamlit.py` file:

1. Add the lesson name to the sidebar radio options
2. Create a new section with the lesson content
3. Use the `show_code()` helper function for interactive examples

### Customization

- Modify the page configuration in `st.set_page_config()`
- Update the lesson content in their respective sections
- Add new interactive widgets as needed
- Customize the styling with Streamlit's theming options

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🆘 Troubleshooting

### Common Issues

**Virtual environment activation fails:**
- Ensure you're in the correct directory
- Check that Python is properly installed
- Try using `python3` instead of `python`

**Dependencies installation fails:**
- Update pip: `pip install --upgrade pip`
- Ensure you're in the activated virtual environment
- Check your internet connection

**Streamlit app won't start:**
- Verify all dependencies are installed
- Check that port 8501 is available
- Try running with `streamlit run streamlit.py --server.port 8502`

**Import errors:**
- Ensure virtual environment is activated
- Reinstall requirements: `pip install -r requirements.txt --force-reinstall`

## 📞 Support

If you encounter any issues or have questions:
1. Check the troubleshooting section above
2. Review the Streamlit documentation: https://docs.streamlit.io
3. Open an issue in this repository

---

Happy learning! 🐍✨