# gudlift-registration

## 1. Why

This is a **proof of concept (POC)** of a lightweight version of Güdlft's competition booking platform, aimed at local and regional organizers. It lets club secretaries register athletes for competitions using their club's points (1 point = 1 registration), so organizers spend less time on administration and more on logistics.

Each competition has a limited number of places, and a club can register a maximum of 12 athletes. The goal is to keep things as light as possible and use user feedback to iterate.

## 2. Getting Started

This project uses the following technologies:

* **Python** v3.x+

* **[Flask](https://flask.palletsprojects.com/en/stable/)**
  Whereas Django does a lot of things for us out of the box, Flask allows us to add only what we need.

* **[Virtual environment](https://virtualenv.pypa.io/en/latest/how-to/install.html)**
  This ensures you'll be able to install the correct packages without interfering with Python on your machine.

* **[pytest](https://docs.pytest.org/)**: testing framework.

* **[Locust](https://locust.io/)**: performance testing.

* **[coverage](https://coverage.readthedocs.io/)**: test coverage measurement.

Other dependencies (Click, itsdangerous, Jinja2, MarkupSafe, Werkzeug) are installed automatically with Flask and are listed in `requirements.txt`.

## 3. Installation

1. Clone the repository:

```bash
   git clone <github_repo_url>
```

2. Move into the project directory:

```bash
   cd <repo_name>
```

3. Install `virtualenv` (**only if it is not already installed**):

```bash
   pip3 install virtualenv
```

4. Create the virtual environment in the project directory:

```bash
   virtualenv .
```

5. Activate it. Your command prompt should change to show the name of the folder, meaning packages are now installed here without affecting files outside.

   **macOS / Linux:**

```bash
   source bin/activate
```

   **Windows (CMD):**

```bat
   Scripts\activate
```

   **Windows (PowerShell):**

```powershell
   .\Scripts\Activate.ps1
```

6. Install all the required packages in one step:

```bash
   pip install -r requirements.txt
```

7. Tell Flask which file to run. This variable **only lasts for the current terminal session**, so you will need to set it again each time you open a new terminal.

   **macOS / Linux:**

```bash
   export FLASK_APP=server.py
```

   **Windows (CMD):**

```bat
   set FLASK_APP=server.py
```

   **Windows (PowerShell):**

```powershell
   $env:FLASK_APP = "server.py"
```

   See the [Flask quickstart](https://flask.palletsprojects.com/en/stable/quickstart/#a-minimal-application) for more details.

8. Start the application. It will print an address that you can open in your browser:

```bash
   flask run
```

### Notes

- To leave the virtual environment, type `deactivate` (same command on all systems).
- If you install a new package, update `requirements.txt` so others know about it: `pip freeze > requirements.txt`.

## 4. Current setup for data storage

The app is powered by [JSON files](https://www.tutorialspoint.com/json/json_quick_guide.htm), to avoid needing a database until we actually need one. The main ones are:

* `competitions.json`: list of competitions with their relevant information (e.g., number of places and date).
* `clubs.json`: list of clubs with their relevant information (e.g., points). This is also where you can find the email addresses the app accepts for login.

## 5. Testing

We use [pytest](https://docs.pytest.org/) as our testing framework. All tests live in the `tests/` folder and are grouped by type in separate subfolders: `unit`, `integration`, `functional` .

### Running the tests

Run from the project root, with the virtual environment activated:

```bash
pytest
```

To run only one type of test:

```bash
pytest tests/unit
pytest tests/integration
pytest tests/functional
```

### Measuring coverage

We use [coverage](https://coverage.readthedocs.io/) to show how well the code is tested.

Run the tests through coverage:

```bash
coverage run -m pytest
```

Display the report in the terminal:

```bash
coverage report
```

Or generate a detailed HTML report:

```bash
coverage html
```

