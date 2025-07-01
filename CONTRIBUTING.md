# Contributing to Sud0NetScanner

Thank you for your interest in contributing to Sud0NetScanner! We welcome contributions from the community and appreciate your help in making this tool better.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [Contributing Guidelines](#contributing-guidelines)
- [Submitting Changes](#submitting-changes)
- [Bug Reports](#bug-reports)
- [Feature Requests](#feature-requests)
- [Security Issues](#security-issues)

## Code of Conduct

This project adheres to a Code of Conduct. By participating, you are expected to uphold this code. Please report unacceptable behavior to the project maintainers.

### Our Standards

- Be respectful and inclusive
- Focus on what is best for the community
- Show empathy towards other community members
- Use welcoming and inclusive language
- Be collaborative and constructive

## Getting Started

1. Fork the repository on GitHub
2. Clone your fork locally
3. Create a new branch for your changes
4. Make your changes and test them
5. Submit a pull request

```bash
git clone https://github.com/YOUR-USERNAME/Sud0NetScanner.git
cd Sud0NetScanner
git checkout -b feature/your-feature-name
```

## Development Setup

### Prerequisites

- Python 3.6 or higher
- Git
- A text editor or IDE
- Linux/Unix environment (recommended)

### Local Development

```bash
# Clone the repository
git clone https://github.com/Sud0-x/Sud0NetScanner.git
cd Sud0NetScanner

# Make the script executable
chmod +x netscanner.py

# Test the installation
python3 netscanner.py --help
```

### Testing Your Changes

Before submitting, please test your changes:

```bash
# Basic functionality test
python3 netscanner.py -t 127.0.0.1 -p 80

# Test with different options
python3 netscanner.py -t 127.0.0.1 -p 22,80,443 -v

# Test edge cases (invalid inputs, etc.)
```

## Contributing Guidelines

### Code Style

- Follow PEP 8 Python style guidelines
- Use meaningful variable and function names
- Add comments for complex logic
- Keep functions focused and concise
- Use type hints where appropriate

### Commit Messages

Write clear, descriptive commit messages:

```
[type]: Brief description (50 chars or less)

More detailed explanation if needed. Wrap at 72 characters.
Include the motivation for the change and contrast with previous behavior.

- Use bullet points for multiple changes
- Reference issue numbers if applicable (#123)
```

Types:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes
- `refactor`: Code refactoring
- `test`: Adding or updating tests
- `chore`: Maintenance tasks

### Documentation

- Update README.md if you add new features
- Add docstrings to new functions and classes
- Update CHANGELOG.md with your changes
- Include usage examples for new features

## Submitting Changes

### Pull Request Process

1. **Fork** the repository
2. **Create** a new branch from `main`
3. **Make** your changes
4. **Test** your changes thoroughly
5. **Document** your changes
6. **Submit** a pull request

### Pull Request Template

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Code refactoring
- [ ] Performance improvement

## Testing
- [ ] Tested on local environment
- [ ] All existing tests pass
- [ ] Added tests for new functionality

## Checklist
- [ ] Code follows project style guidelines
- [ ] Self-review completed
- [ ] Documentation updated
- [ ] No breaking changes (or clearly documented)
```

## Bug Reports

When reporting bugs, please include:

### Bug Report Template

```markdown
**Bug Description**
A clear description of the bug

**To Reproduce**
Steps to reproduce the behavior:
1. Run command '...'
2. With options '...'
3. See error

**Expected Behavior**
What you expected to happen

**Actual Behavior**
What actually happened

**Environment**
- OS: [e.g., Kali Linux 2024.1]
- Python Version: [e.g., 3.9.2]
- Sud0NetScanner Version: [e.g., 2.0.0]

**Additional Context**
Any other relevant information
```

## Feature Requests

We welcome feature suggestions! Please provide:

- **Use case**: Why is this feature needed?
- **Description**: What should the feature do?
- **Implementation ideas**: Any thoughts on how to implement it?
- **Examples**: Show how it would be used

### Feature Request Template

```markdown
**Feature Description**
A clear description of the requested feature

**Use Case**
Why is this feature needed? What problem does it solve?

**Proposed Solution**
How should this feature work?

**Alternatives Considered**
Any alternative approaches you've considered

**Additional Context**
Any other relevant information or examples
```

## Security Issues

Please do **NOT** report security vulnerabilities through public GitHub issues. Instead, follow our [Security Policy](SECURITY.md).

## Development Areas

We welcome contributions in these areas:

### High Priority
- Performance optimizations
- Cross-platform compatibility
- IPv6 support
- Advanced scanning techniques
- Error handling improvements

### Medium Priority
- Additional output formats (XML, CSV)
- GUI interface
- Integration with other tools
- Advanced service detection
- Plugin system

### Documentation
- Usage examples
- Video tutorials
- Translation to other languages
- API documentation
- Best practices guide

## Community

- **GitHub Issues**: Bug reports and feature requests
- **Discussions**: General questions and ideas
- **Pull Requests**: Code contributions

## Recognition

Contributors will be recognized in:
- README.md contributors section
- CHANGELOG.md for significant contributions
- Release notes for major contributions

## Questions?

If you have questions about contributing:
- Check existing issues and documentation
- Open a GitHub Discussion
- Contact the maintainers

---

**Thank you for contributing to Sud0NetScanner!** 🚀

Your contributions help make network security tools more accessible and powerful for everyone.
