# Translation Microservice

A lightweight, modular translation microservice using a mock translation API (can be replaced with Google Translate API).

## Features

- Translate text (up to 1000 characters) via POST request
- Support for multiple target languages (ISO codes)
- Input validation and error handling
- Logging of all translation requests to SQLite database
- Health check endpoint
- Support for bulk translations

## Project Structure

The project follows a modular structure with separate modules for routes, services, models, utilities, and database operations.

## Setup and Installation

1. Clone the repository
2. Install dependencies: