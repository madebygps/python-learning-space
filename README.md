# Python Learning Space 🐍

A demonstration of how AI prompts and chat modes can create effective learning environments. This repository showcases how [GitHub Copilot instructions](https://code.visualstudio.com/docs/copilot/copilot-customization), [prompts](https://code.visualstudio.com/docs/copilot/copilot-customization) and [chatmodes](https://code.visualstudio.com/docs/copilot/copilot-customization) can transform AI assistants into specialized tutors focused on **discovery-based learning**.

## 🎯 Learning Philosophy

**Discovery over Direction**: Students learn by figuring things out themselves rather than following step-by-step instructions. The AI provides context and objectives but lets learners discover the methods.

**Topic-Focused Structure**: Each Python concept lives in its own directory with exercises designed for independent problem-solving and authentic programming challenges.

## 🧠 AI Tutor Implementation

### Core Components

- **`copilot-instructions.md`**: Project-wide educational standards and workflow guidance
- **`python-tutor.chatmode.md`**: Specialized tutoring mode that promotes guided discovery over direct answers  
- **`generate-listcomp-exercise.prompt.md`**: Agent prompt for creating minimal-scaffolding exercises with authentic scenarios

### Key Design Principles

**Minimal Scaffolding**: Exercises provide business context and objectives, but students must discover syntax, approach, and implementation details independently.

**Single-Focus Exercises**: Each exercise teaches exactly one concept through one clear requirement, avoiding cognitive overload.

**Authentic Problems**: Real-world scenarios that naturally require the target programming concept, making learning feel practical and relevant.

## 📁 Repository Structure

```text
python-learning-space/
├── main.py                    # Simple project runner
├── pyproject.toml             # Project configuration and dependencies  
├── list-comps/               # List comprehensions topic
│   ├── README.md             # Concept explanation
│   └── listcomp_*.py         # Discovery-based exercises
├── unpacking/                # Unpacking and destructuring topic
│   └── README.md             # Concept explanation
├── .github/
│   ├── copilot-instructions.md    # Project-wide AI guidance
│   ├── chatmodes/
│   │   └── python-tutor.chatmode.md   # Specialized tutor mode
│   └── prompts/
│       └── generate-listcomp-exercise.prompt.md   # Exercise generator
└── .venv/                    # Virtual environment
```

## 🚀 Getting Started

### Prerequisites

- **Python 3.13** (see `.python-version`)
- **uv** or **pip** for dependency management

### Setup & Usage

```bash
# Clone and setup
git clone <repository-url>
cd python-learning-space
uv venv && source .venv/bin/activate
uv sync

# Run exercises
uv run list-comps/listcomp_2.py

# Generate new exercises using agent prompts
# Use: /generate-listcomp-exercise in Github Copilot Chat
```
