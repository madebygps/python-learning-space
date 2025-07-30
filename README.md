# Python Learning Space 🐍

A demonstration of how AI prompts and chat modes can create effective learning environments. This repository showcases how [GitHub Copilot instructions](https://code.visualstudio.com/docs/copilot/copilot-customization), [prompts](https://code.visualstudio.com/docs/copilot/copilot-customization) and [chatmodes](https://code.visualstudio.com/docs/copilot/copilot-customization) can transform AI assistants into specialized tutors.

## 🎯 Learning Philosophy

The repository structure follows a **concept-focused approach** where each Python topic is isolated in its own directory. This demonstrates how AI can help organize learning materials and maintain educational focus through well-designed prompts and chat modes.

I recommend structuring the repository folowing your source of truth: book, course, or other educational material. This allows the AI to provide contextually relevant exercises and explanations.

## 🧠 AI Tutor Implementation

### Custom Instructions & Configuration

This repository includes several AI configuration files in the `.github/` directory:

```text
.github/
├── copilot-instructions.md           # Global AI assistant instructions
├── chatmodes/
│   └── python-tutor.chatmode.md     # Specialized Python tutor chat mode
└── prompts/
    └── generate-listcomp-exercise.prompt.md  # Exercise generation prompt
```

#### Key Configuration Files

- **`copilot-instructions.md`**: Sets educational boundaries and tutoring approach
- **`python-tutor.chatmode.md`**: Defines specialized Python tutoring mode with specific tools and behaviors
- **`generate-listcomp-exercise.prompt.md`**: Agent prompt for creating list comprehension exercises

### Chat Mode Configuration

The AI tutor is configured to:

- Explain concepts rather than provide direct answers
- Ask guiding questions to promote understanding
- Suggest debugging approaches without solving problems
- Encourage experimentation and exploration

## 📁 Repository Structure (Learning Example)

```text
python-learning-space/
├── main.py                 # Simple project runner
├── pyproject.toml          # Project configuration and dependencies
├── list-comps/            # List comprehensions topic
│   ├── README.md          # Concept explanation and exercises
│   └── listcomp_1.py      # Example implementations
├── unpacking/             # Unpacking and destructuring topic
│   └── README.md          # Concept explanation and exercises
└── .venv/                 # Virtual environment (isolated dependencies)
```

## 🚀 Getting Started

### Prerequisites

- **Python 3.13** (see `.python-version`)
- **uv** or **pip** for dependency management

### Setup

1. **Clone the repository:**

   ```bash
   git clone <repository-url>
   cd python-learning-space
   ```

2. **Create and activate virtual environment with uv:**

   ```bash
   uv venv
   source .venv/bin/activate  # On macOS/Linux
   # or
   .venv\Scripts\activate     # On Windows
   ```

3. **Install dependencies:**

   ```bash
   uv sync
   ```

4. **Run examples using uv:**

   ```bash
   # Run specific topic examples
   uv run list-comps/listcomp_1.py
   ```

## Adding New Topics

1. Create a new directory: `mkdir new-topic/`
2. Add a README with concept explanation:

   ```bash
   echo "# Learning [Topic] in Python

   In this folder you will find notes, exercises, snippets, and examples related to [topic] in Python." > new-topic/README.md
   ```

3. Build a prompt for generating exercises or examples as needed. See `.github/prompts/` for examples.

Experiment with prompts, chat modes, and configurations to enhance your learning experience.
