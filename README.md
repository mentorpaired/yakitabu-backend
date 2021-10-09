<p align="center">
  <a href="" rel="noopener">
 <img width=200px height=200px src="https://i.imgur.com/GaiJno0.png" alt="Project logo"></a>
</p>


<h3 align="center">Yakitabu Backend</h3>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
![GitHub issues](https://img.shields.io/github/issues/mentorpaired/yakitabu-backend)
![GitHub pull requests](https://img.shields.io/github/issues-pr/mentorpaired/yakitabu-backend?color=light%20green)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>

---

<p align="center"> 
    <br> 
</p>

## 📝 Table of Contents

- [About](#about)
- [Tech](#tech)
- [Installation](#installation)
- [Running the Tests](#tests)
- [Usage](#usage)
- [Deployment](#deployment)
- [Built Using](#built_using)
- [Authors](#authors)
- [Collaboration](#collaboration)
- [License](#license)
- [Acknowledgments](#acknowledgement)

## 🧐 About <a name = "about"></a>

yakitabu-backend is the backend of <b>Yakitabu</b>, a Peer to Peer Book Loan App.


## 💻 Tech <a name = "tech"></a>
yakitabu-backend is written in [Python 3](https://www.python.org/) and [Flask 2.0.1](https://flask.palletsprojects.com/en/2.0.x/).


## ⚙️ Installation  <a name = "installation"></a>


### Ubuntu 18.04 Users

Please install these packages and set up your environment in the order listed below. Run an upgrade or update if you find that the package is already installed:

- Python 3. Run the 'python3 -V' command to see the version you have installed.

- Create a virtual environment in order to install packages. The README uses [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/install.html#basic-installation) to create this environment. You could use any virtualenv package of your choice or install this wrapper with:

```sh
pip install virtualenvwrapper
```

- Add these lines at the end of your shell startup script (`.bashrc`, `.zshrc`, etc)

```sh
export WORKON_HOME=$HOME/.virtualenvs
export PROJECT_HOME=$HOME/Devel
source /usr/local/bin/virtualenvwrapper.sh
```

- After editing, reload the startup file (e.g., run `source ~/.bashrc`).

- Create a new virtual environment:

```sh
mkvirtualenv <your_preferred_envname>
```

- Install requirements in the virtual environment created:

```sh
pip install -r requirements.txt
```

- Install [PostgreSQL](https://www.postgresql.org/).

- Create a database with PostgresQL, the installation instructions for Ubuntu can be found [here](https://www.postgresql.org/download/linux/ubuntu/). Make sure to note Database name, Database Username and Password and also ensure that the server is running




- Run server to ensure everything is working properly.

```sh
flask run
```


### Windows 10 Users

Please install and set up the following packages first. Upgrade if you find the package is already installed:

- Download [Python 3](https://www.python.org/downloads/). It is advisable to install the python package as an administrator. Click on the 'Add path' checkbox before moving on to the next step of the installation process. Run this command in your terminal to see the version you have installed.

  ```sh
  python3 -V
  ```

- Download [pip](https://pip.pypa.io/en/latest/installing/) and follow the instructions in the link as an installation guide.

- [PostgreSQL](https://www.postgresql.org/download/windows/) (Ensure the server is running).

- It is advisable to install Flask in a virtual environment. The README uses [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/install.html#basic-installation) to create this environment. You could use any virtualenv package of your choice but for Windows, install this wrapper with:

  ```sh
  pip install virtualenvwrapper-win
  ```

- Create a new virtual environment:

  ```sh
  mkvirtualenv <envname>
  ```

- Activate the virtual environment with:

  ```sh
  <envname>\Scripts\activate
  ```
  or use this command
  ```sh 
  & C:/Users/<username>/Envs/<envname>/Scripts/Activate.ps1
  ```

- Install requirements in the virtual environment created:

  ```sh
  pip install -r requirements.txt
  ```

* Run server to ensure everything is running properly.

  ```sh
  flask run
  ```

* Deactivate the virtual environment with:

  ```sh
  deactivate
  ```

- Create a database with PostgreSQL, if you installed it earlier. If not, installation instructions can be found [here](https://www.postgresql.org/download/windows/). Make sure to note database name, database username and password.




## 🔧 Running the tests <a name = "tests"></a>

<b>N/B</b>: This is a ToDo

### Break down into end to end tests
<b>N/B</b>: This is a ToDo

```
Give an example
```

### And coding style tests

<b>N/B</b>: This is a ToDo

```
Give an example
```

## 🎈 Usage <a name="usage"></a>


<b>N/B</b>: This is a ToDo  
Add notes about how to use the system.

## 🚀 Deployment <a name = "deployment"></a>

<b>N/B</b>: This is a ToDo  
Add additional notes about how to deploy this on a live system.


### Python installation instructions for Windows, macOS and other Linux distro Users

- The following may serve as a guide:
  - (https://www.python.org/downloads/)
  - (https://realpython.com/installing-python/)
  - (https://virtualenvwrapper.readthedocs.io/en/latest/install.html)
  - (https://realpython.com/learning-paths/flask-by-example/)



## ⛏️ Built Using <a name = "built_using"></a>

- [Python](https://www.python.org/) - Server Environment
- [Flask](https://flask.palletsprojects.com/en/2.0.x/) - Server Framework
- [PostgreSQL](https://www.postgresql.org/) - Database
- [GitHub Actions](https://github.com/features/actions) - CI/CD
- [Heroku](https://www.heroku.com/) - Deployment


## ✍️ Authors <a name = "authors"></a>

- [Delphine](https://github.com/kylelobo) 
- [Tosin](https://github.com/tosintubi) 
- [Seunfunmi](https://github.com/seun-beta) 
- [Osahon](https://github.com/ausiat1)
- [Brenda](https://github.com/Brenii)

## 🤝 Collaboration <a name = "collaboration"></a>

- You need to have PostgresQL installed and set up on your machine.

- Clone the repository from the `staging` branch and please read the [contributing guide](/CONTRIBUTING.md).

- You may also need to have [Heroku](https://devcenter.heroku.com/articles/heroku-cli).

- Run the `Heroku` login commands in your terminal after installation
  ```sh
  heroku login
  ```

Contact [Seunfunmi](https://github.com/seun-beta), [Tosin](https://github.com/tosintubi) for more details.


## 📝 License <a name = "license"></a>

This project is licensed under the MIT License - see the [LICENSE](/LICENSE) file for more details.


## 🎉 Acknowledgements <a name = "acknowledgement"></a>

Special thanks to [Kosy](https://github.com/kosyfrances) and [Tunde](https://github.com/toystars) for guiding us through the entire app creation process, reviewing our code and unblocking us when we are stuck with an issue, and most especially, for taking the time out of their busy lives to provide free mentorship to us.
