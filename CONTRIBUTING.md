# Contributing to Academic Paper Engineering

Thank you for your interest in contributing to the Academic Paper Engineering Skill! We welcome contributions to improve the parsers, add new templates, or enhance the AI Agent prompts.

## How to Contribute

1. **Report Bugs**: If you find a bug, please open an issue with a detailed description and steps to reproduce.
2. **Add Templates**: 
   - Add the LaTeX template files to `academic-paper-engineering/assets/templates/`.
   - Update `academic-paper-engineering/references/config/system.yaml` to include the new template.
   - Provide a template specification in `academic-paper-engineering/references/prompts/latex/`.
3. **Improve Parsers**: 
   - Modify the scripts in `academic-paper-engineering/src/parsers/` or `academic-paper-engineering/scripts/`.
   - Ensure you add or update tests in `academic-paper-engineering/tests/`.
4. **Enhance Prompts**: 
   - Improve the AI Agent guidance in `academic-paper-engineering/references/prompts/`.

## Development Setup

1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run tests:
   ```bash
   cd academic-paper-engineering/tests && python -m pytest -v
   ```

## Design Principles

Please adhere to the core design principles outlined in the `README.md` and `SKILL.md`:
- **Document IR First**: All processing must use the structured Intermediate Representation.
- **Template-Driven**: Avoid hardcoding journal-specific rules.
- **Data Integrity**: Never fabricate or silently modify scientific data (numbers, formulas, references).

## License

By contributing, you agree that your contributions will be licensed under the project's MIT License.

## Contact

For any questions, suggestions, or collaboration inquiries, please reach out via:

- Email: hongyuanlu9@gmail.com
- GitHub Issues: [Project Issues Page](https://github.com/Hongyuan-Lu/academic-paper-engineering/issues)

Welcome to submit Issues and Pull Requests!
