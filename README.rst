Inkflow
=======

Inkflow is a lightweight personal writing system built with Flask.

It is designed for simple self-hosted note-taking and writing,
with minimal dependencies and an easy local setup.

The project focuses on clarity, simplicity, and easy deployment
instead of feature complexity.

---

Overview
--------

Inkflow provides a minimal web interface for:

- Writing and managing personal entries
- Viewing entries in a chronological list
- Basic content editing and deletion
- Local database storage (SQLite by default)

No external services are required.

---

Project Structure
------------------

::

    flask_blogging/
        core application logic
    example/
        (removed or simplified in this version)
    test/
        (removed for lightweight deployment)

---

Requirements
------------

- Python 3.9+
- Flask
- SQLAlchemy

Install dependencies:

.. code-block:: bash

    pip install -r Requirements.txt

---

Run Locally
-----------

1. Clone repository:

.. code-block:: bash

    git clone https://github.com/jennica-z/inkflow.git
    cd repo

2. Install dependencies:

.. code-block:: bash

    pip install -r Requirements.txt

3. Start application:

.. code-block:: bash

    python -m flask_blogging

4. Open in browser:

::

    http://localhost:5000

---

Docker Run
----------

Build image:

.. code-block:: bash

    docker build -t inkflow-app .

Run container:

.. code-block:: bash

    docker run -p 5000:5000 inkflow-app

---

Configuration
-------------

Default configuration uses SQLite:

::

    sqlite:///inkflow.db

You can override settings using environment variables if needed.

---

Design Goals
------------

This project is intentionally minimal.

It avoids:

- unnecessary microservices
- external dependencies like Redis or Celery
- complex deployment pipelines
- heavy frontend frameworks

The goal is to keep it readable and easy to maintain
for a single developer.

---

License
-------

This project is licensed under the MIT License.