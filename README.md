# SQLAlchemy Practice & ORM Examples

A collection of hands-on Python scripts demonstrating core concepts of **SQLAlchemy**, the popular SQL toolkit and Object-Relational Mapper (ORM) for Python. This repository serves as a practical reference for building database-backed applications using SQLite, defining models, managing relationships, and performing CRUD operations.

## Features

- **Declarative Model Definition**: Define database tables as Python classes using `declarative_base`.
- **Database Connection & Session Management**: Create engines, establish connections, and manage sessions with `sessionmaker`.
- **Basic CRUD Operations**: Create, Read, Update, and Delete records through the ORM.
- **Querying & Filtering**: Perform queries with `filter_by`, `filter`, and `like` for precise data retrieval.
- **Relationships**: Implement one-to-many and many-to-one relationships using `relationship` and `ForeignKey`.
- **Cascading Deletes**: Demonstrate `cascade="all, delete"` for maintaining referential integrity.
- **Interactive Examples**: Each script is heavily commented, providing runnable examples and explanations of the executed operations.

## Project Structure

```text
.
├── src/
│   ├── app.py          # Basic Car and Customer models, filtering, and deletion examples
│   ├── app2.py         # Related models (Car/Customer/Student), CRUD helper functions
│   ├── app_3.py        # Relationship traversal (accessing related objects)
│   └── app_4.py        # Student-Course relationship with cascade delete demonstration
└── requirements.txt    # Project dependencies
```

## Requirements

- **Python** 3.8+
- **SQLAlchemy** (see `requirements.txt` for the pinned version)
- **SQLite** (built into Python; no separate installation required)

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/miky619/SQL-Alchemy.git
   cd SQL-Alchemy
   ```

2. **Create and activate a virtual environment** (recommended)
   ```bash
   python -m venv .venv
   # Windows (PowerShell)
   .venv\Scripts\Activate.ps1
   # macOS / Linux
   source .venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
   > If `requirements.txt` is empty or missing, install SQLAlchemy directly:
   > ```bash
   > pip install sqlalchemy
   > ```

## Usage

Run any of the example scripts from the `src` directory. Each script is self-contained and will create a local SQLite database file (e.g., `CarData.db`, `University.db`) in the current working directory.

```bash
python src/app.py
```

### Script Highlights

| Script | Description |
| :--- | :--- |
| **`app.py`** | Defines `Car` and `Customer` models. Demonstrates adding records, querying with `filter_by` and `filter`, and deleting a record. |
| **`app2.py`** | Extends the models with a `Student` table. Provides reusable functions for `add_student`, `get_all_students`, `update_student`, and `delete_student`. Also demonstrates relationship traversal (`customer1.owner`). |
| **`app_3.py`** | Focuses on accessing related objects through relationships (e.g., retrieving a car's customer details). |
| **`app_4.py`** | Models a `Student`–`Course` relationship with `cascade="all, delete"`, showing how to query a student's enrolled courses. |

> **Note**: Many lines in the scripts are commented out to allow you to enable specific examples step-by-step. Uncomment the blocks you wish to execute.

## Database Schemas

The examples use the following SQLite databases:

- **`CarData.db`** – `carinfo` (id, brand, model, price, quantity) and `customerinfo` (id, name, phone, age, gender)
- **`CarData_relation.db`** – `carinfo` and `customerinfo` with a foreign key linking `Car` to `Customer`
- **`University.db`** – `students` (id, name) and `courses` (id, title, unit, student_id)

## Known Limitations

- The scripts are **educational examples** rather than a production-ready application.
- No automated tests, migrations (e.g., Alembic), or configuration management are included.
- The database files are created locally and are not tracked by version control.

## Possible Improvements

- Add a `requirements.txt` with pinned dependency versions.
- Introduce automated tests (e.g., `pytest`) for the CRUD helper functions.
- Refactor the repeated engine/session setup into a reusable module.
- Add support for other database backends (PostgreSQL, MySQL) via environment configuration.

## Technologies

- **Python** – Application logic
- **SQLAlchemy** – ORM and database toolkit
- **SQLite** – Lightweight, file-based database engine

## Author

**Miky**  
GitHub: [@miky619](https://github.com/miky619)

## Repository

[github.com/miky619/SQL-Alchemy](https://github.com/miky619/SQL-Alchemy)
