# EXTERNAL-SOURCE-LOAD

## Description

The aim of this project is to create a **load** in an ELT that will have a rest api, then deposit the data in a datalake and finally send a notification to the transfom that a document has been added.

---

## Getting Started

### Prerequisites

List all dependencies and their version needed by the project as :

* IDE used pycharm 2024.3 or later [download](https://www.jetbrains.com/pycharm/download/?section=windows)
* Python 3.13 or later [official doc](https://www.python.org/downloads/)
* Git version 2.47.1 or later [official doc](https://git-scm.com/)

### Configuration

Install requiremenets 
````shell
pip install -r requirements.txt
````

Copy and modify the .env
````shell
cp .env.example .env
````

---

## Development environment

---
### Start

````shell
python main.py
````


### Run test
````shell
pytest tests/aws/test_connection.py
````
````shell
pytest tests/aws/test_load.py
````

## Directory structure

````shell
├───docs                  # Documentations (class, sequence diagram, ...)
├───tests                 # Tests 
├───src
│   ├───cloud_services    # All cloud services (aws, gcp...)
│   │   └───aws_service
│   ├───exceptions        # All exceptions 
│   └───objects           # Objects such as Json
├───.env
├───main.py               # Entry point
└───requirements.md
````


## Collaborate

* Workflow
    * [Gitflow](https://www.atlassian.com/fr/git/tutorials/comparing-workflows/gitflow-workflow#:~:text=Gitflow%20est%20l'un%20des,les%20hotfix%20vers%20la%20production.)
    * [How to commit](https://www.conventionalcommits.org/en/v1.0.0/)
    * [How to use your workflow](https://nvie.com/posts/a-successful-git-branching-model/)

    * Propose a new feature in [Github issues](https://github.com/CPNV-ES-BI1-SBB/EXTERNAL-SOURCE-LOAD-DATALAKE/issues)
    * Pull requests are open to merge in the develop branch.
    * Release on the main branch we use GitFlow and not with GitHub release.
    * Issues are added to the [github issues page](https://github.com/CPNV-ES-BI1-SBB/EXTERNAL-SOURCE-LOAD-DATALAKE/issues)

### Commits
* [How to commit](https://www.conventionalcommits.org/en/v1.0.0/)
```bash
<type>(<scope>): <subject>
```

- **build**: Changes that affect the build system or external dependencies (e.g., npm, make, etc.).
- **ci**: Changes related to integration or configuration files and scripts (e.g., Travis, Ansible, BrowserStack, etc.).
- **feat**: Adding a new feature.
- **fix**: Bug fixes.
- **perf**: Performance improvements.
- **refactor**: Modifications that neither add a new feature nor improve performance.
- **style**: Changes that do not affect functionality or semantics (e.g., indentation, formatting, adding spaces, renaming a variable, etc.).
- **docs**: Writing or updating documentation.
- **test**: Adding or modifying tests.

examples :
```bash
feat(MyClass): add a button in the ...
````
```bash
feat(example.js): change name into username
````

---

## License
MIT

---

## Contact

* If needed you can create an issue on GitHub we will try to respond as quickly as possible.
