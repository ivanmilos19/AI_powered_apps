# AI Powered Apps: Chatbot and Reviews Summarizer

This project hosts two AI-powered apps:

- **Chatbot** – simulates a theme park customer service assistant.
- **Reviews & Summarizer** – displays visitor reviews and generates quick AI summaries of them.

## Setup

### I. Backend

##### 1. Create a Python virtual environment:

```bash
python -m venv venv
```

##### 2. Activate the virtual environment:

- On macOS/Linux:

```bash
source venv/bin/activate
```

- On Windows:

```bash
venv\Scripts\activate
```

##### 3. Install Python dependencies while in the server directory:

```bash
pip install -r requirements.txt
```

##### 4. Database setup:
This project uses Tortoise ORM with Aerich for migrations. You just need to:

- Create a database (MySQL, PostgreSQL, SQLite, etc.)

- Configure the database URL and your OpenAI API key in your .env file.

Then run:

```bash
aerich init -t your_project.settings.TORTOISE_ORM
aerich init-db
aerich migrate
aerich upgrade
```

### II. Frontend

All required Bun files are included, so no global installation is needed. You just need Node.js and TypeScript to run the frontend:

```bash
npm install
npm run dev
```

To launch the applications:

```bash
bun run dev
```

Two apps will start:

- Reviews & Summarizer: http://localhost:5173
- Chatbot: http://localhost:5174