# CLAUDE.md - AI Assistant Guide for unmatchedchecker

## Project Overview

**unmatchedchecker** is a program that validates whether a device is online. This utility performs network connectivity checks to determine device availability status.

## Current State

This repository is in its initial development phase. The project structure and implementation are being established.

### Repository Structure

```
unmatchedchecker/
├── CLAUDE.md          # AI assistant guidelines (this file)
└── README.md          # Project description
```

## Development Guidelines

### Getting Started

1. Clone the repository
2. Check out the appropriate development branch
3. Follow the conventions outlined below when implementing features

### Git Workflow

- **Branch Naming**: Use descriptive branch names (e.g., `feature/ping-checker`, `fix/timeout-handling`)
- **Commits**: Write clear, concise commit messages describing the change
- **Pull Requests**: Include a description of changes and any testing performed

### Code Conventions

When implementing this project, follow these conventions:

1. **Error Handling**: Always handle network errors gracefully; devices may be unreachable for various reasons
2. **Timeouts**: Implement configurable timeouts for connectivity checks
3. **Logging**: Include appropriate logging for debugging connectivity issues
4. **Configuration**: Support configuration via environment variables or config files

### Expected Functionality

The device validation checker should support:

- Ping/ICMP checks for basic connectivity
- TCP port checking for service availability
- Configurable timeout and retry logic
- Clear status reporting (online/offline/unknown)
- Batch checking of multiple devices

## AI Assistant Instructions

### When Working on This Codebase

1. **Read before modifying**: Always read existing files before making changes
2. **Keep it simple**: Implement the minimum necessary for the requested feature
3. **Test connectivity logic**: Network code can fail in many ways; consider edge cases
4. **Handle permissions**: Some network operations (like raw ICMP) may require elevated privileges
5. **Cross-platform**: Consider compatibility across different operating systems if applicable

### Key Considerations for Device Checking

- Network timeouts should be reasonable (not too short, not too long)
- Consider rate limiting when checking many devices
- Respect network policies and firewalls
- Handle DNS resolution failures separately from connectivity failures
- Log enough information for debugging but avoid excessive verbosity

### Security Considerations

- Do not store credentials in code
- Validate and sanitize device addresses/hostnames
- Be cautious with user-provided input that becomes network destinations
- Consider network scanning implications and use responsibly

## Build and Test

*To be defined once the technology stack is chosen.*

Recommended structure when implemented:

```
unmatchedchecker/
├── src/               # Source code
├── tests/             # Test files
├── docs/              # Documentation
├── .gitignore         # Git ignore patterns
├── README.md          # Project documentation
└── CLAUDE.md          # This file
```

## Common Tasks

### Adding a New Check Type

1. Create the check implementation with consistent interface
2. Handle timeouts and errors appropriately
3. Add tests for the new check type
4. Update documentation

### Debugging Connectivity Issues

1. Check network permissions
2. Verify DNS resolution
3. Test with known-good targets
4. Review timeout configuration
5. Check firewall rules

## Notes for Future Development

- Consider async/concurrent checking for multiple devices
- Implement health check history/trending
- Add notification capabilities for status changes
- Support for different network protocols as needed
