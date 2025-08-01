# Python Learning Space - AI Coding Assistant Instructions

## Project Overview
This is a **Python learning repository** organized around specific language concepts. Each topic gets its own directory with exercises, examples, and documentation. The goal is hands-on learning through practical code examples.

## Project Structure & Patterns
- **Topic-based directories**: Each Python concept lives in its own folder (e.g., `list-comps/`, `unpacking/`)
- **Consistent README structure**: Every topic directory contains a README.md explaining the concept and containing exercises
- **Learning progression**: Start with README explanations, then build practical examples
- **Single entry point**: `main.py` serves as a simple project runner

## Development Environment
- **Python 3.13** (see `.python-version`)
- **Virtual environment**: `.venv/` for isolated dependencies
- **uv/pip**: Dependency management via `pyproject.toml`

## Key Workflows

### Creating New Learning Topics
1. Create new directory: `mkdir new-topic/`
2. Add README with concept explanation: `echo "# Learning [Topic] in Python\n\nIn this folder you will find notes, exercises, snippets, and examples related to [topic] in Python." > new-topic/README.md`
3. Build examples as separate `.py` files within the topic directory

### Running Code
- **Topic examples**: Run individual Python files within topic directories
- **Virtual environment**: Always activate `.venv` before running code

### File Organization
- **Notes**: Use README.md for concept explanations and exercise descriptions


## AI Assistant Guidelines

When helping with this codebase:

1. **Maintain topic isolation**: Keep each concept in its dedicated directory for focused learning
2. **Follow naming patterns**: Use descriptive names that clearly indicate the Python concept being demonstrated
3. **Provide progressive examples**: Start simple, then build complexity within each topic
4. **Include explanatory comments**: Code should be educational with clear comments explaining Python concepts
5. **Update READMEs**: When adding new examples, reference them in the topic's README.md
6. **Use modern Python**: Target Python 3.13 features and best practices

### WORKING WITH THE LEARNING SPACE
- **Build progressively**: Start with README explanations, then move to hands-on coding
- **Run examples**: Use the VS Code terminal to execute code in topic directories with `uv run`

### EXERCISE WORKFLOW INTEGRATION
- **Recognize exercise format**: Understand the standard exercise structure (Exercise description, Instructions, Data, Expected result)
- **Prompt for structured exercises**: When users need new exercises, suggest using agent prompts like `/generate-listcomp-exercise`
- **Guide through exercise steps**: Help users understand the exercise description before they start coding
- **Encourage testing**: Remind users to run their code with `uv run` to check against expected results
- **Support self-assessment**: Guide users to compare their output with expected results and understand differences
- **Suggest exercise variations**: When users complete exercises, suggest modifications to deepen understanding


