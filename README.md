# Python Learning Space 🐍

A demonstration of how AI prompts and chat modes can create effective learning environments. This repository showcases how custom instructions and prompts can transform AI assistants into specialized tutors for Python programming.

## 🤖 AI-Powered Learning Demonstration

This project serves as an **example of prompt engineering for educational purposes**. It demonstrates how custom instructions can:

- Transform a general AI assistant into a specialized Python tutor
- Create structured learning environments through clear prompts
- Guide learners without directly providing solutions
- Maintain educational boundaries while providing helpful guidance

## 🎯 Learning Philosophy

The repository structure follows a **concept-focused approach** where each Python topic is isolated in its own directory. This demonstrates how AI can help organize learning materials and maintain educational focus through well-designed prompts and chat modes.

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
   # Run the main entry point
   uv run main.py
   
   # Run specific topic examples
   uv run list-comps/listcomp_1.py
   ```

## 📚 Available Topics

### 🔄 List Comprehensions (`list-comps/`)

Learn to create concise, readable list transformations using Python's list comprehension syntax.

- **Focus**: Syntax, filtering, transformations, nested comprehensions
- **Files**: `listcomp_1.py` - practical examples

### 📦 Unpacking (`unpacking/`)

Master Python's unpacking and destructuring capabilities for cleaner, more expressive code.

- **Focus**: Tuple unpacking, starred expressions, function arguments
- **Status**: Setup complete, examples in progress

## 🎓 Learning Workflow

1. **Start with the README**: Each topic directory contains a README.md explaining the concept
2. **Study the examples**: Review the `.py` files for practical implementations
3. **Practice exercises**: Work through the exercises described in each topic's README
4. **Build your own**: Create additional examples to reinforce learning

## 🛠️ Development Guidelines

### Adding New Topics

1. Create a new directory: `mkdir new-topic/`
2. Add a README with concept explanation:

   ```bash
   echo "# Learning [Topic] in Python

   In this folder you will find notes, exercises, snippets, and examples related to [topic] in Python." > new-topic/README.md
   ```

3. Build examples as separate `.py` files within the topic directory

### Code Organization

- **One concept per directory**: Keep topics isolated for focused learning
- **Descriptive naming**: Use clear names that indicate the Python concept
- **Progressive complexity**: Start simple, build complexity within each topic
- **Educational comments**: Include explanations for learning purposes

## 🔧 Running Examples

### Using uv (Recommended)

```bash
# Run the main entry point
uv run main.py

# Run specific topic examples
uv run list-comps/listcomp_1.py

# Run with activated virtual environment
source .venv/bin/activate
uv run python listcomp_1.py  # from within list-comps/ directory
```
