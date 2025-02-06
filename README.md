# AI Blog Generator with CrewAI

A FastAPI-based web application that uses CrewAI and Google's Gemini model to automatically generate blog topics and outlines.

## Features

- 🤖 Powered by CrewAI and Google's Gemini AI
- 🚀 Fast and efficient with FastAPI
- 💅 Clean and modern UI
- 🔄 Asynchronous processing
- 📝 Generates both topics and detailed outlines

## Prerequisites

- Python 3.12 or higher
- [uv](https://github.com/astral-sh/uv) package manager
- Google Gemini API key

## Quick Start

1. Clone the repository:
   ```bash
   git clone [your-repo-url]
   cd practice_crewai
   ```

2. Set up the Python environment:
   ```bash
   # Create and activate virtual environment using uv
   uv venv .venv
   .\.venv\Scripts\activate  # On Windows
   source .venv/bin/activate  # On Unix/MacOS
   ```

3. Install dependencies:
   ```bash
   uv pip install -e .
   ```

4. Set up your environment variables:
   ```bash
   # Create a .env file and add your Google Gemini API key
   echo "GOOGLE_API_KEY=your_api_key_here" > .env
   ```

5. Set Python path:
   ```bash
   # On Windows PowerShell
   $env:PYTHONPATH = "$PWD\src"
   
   # On Unix/MacOS
   export PYTHONPATH="$PWD/src"
   ```

6. Run the application:
   ```bash
   cd src
   uvicorn myproject.main:app --reload
   ```

7. Open your browser and visit:
   ```
   http://localhost:8000
   ```

## Project Structure

```
practice_crewai/
├── src/
│   └── myproject/
│       ├── main.py          # FastAPI application
│       ├── crew.py          # CrewAI implementation
│       └── templates/
│           └── index.html   # Web interface
├── pyproject.toml          # Project dependencies
├── README.md
└── .gitignore
```

## Usage

1. Visit the web interface at `http://localhost:8000`
2. Click the "Generate New Blog" button
3. Wait for the AI to generate both a topic and outline
4. The results will be displayed on the page

## Development

- The application uses FastAPI for the backend
- Templates are rendered using Jinja2
- AI processing is handled asynchronously
- UI is built with Tailwind CSS

## Troubleshooting

If you encounter any issues:

1. Make sure your virtual environment is activated
2. Verify your PYTHONPATH is set correctly
3. Check that your Google Gemini API key is valid
4. Ensure all dependencies are installed correctly

## License

[Your License Here]

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request
