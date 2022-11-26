## Tools and Languages used in this project
<h5 align="left">Front End:</h5>
<p align="left">
<a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript" target="_blank" rel="noreferrer"> <img 
src="https://raw.githubusercontent.com/devicons/devicon/master/icons/javascript/javascript-original.svg" alt="javascript" 
width="40" height="40"/> </a> <a href="https://reactjs.org/" target="_blank" rel="noreferrer"> <img 
src="https://raw.githubusercontent.com/devicons/devicon/master/icons/react/react-original-wordmark.svg" alt="react" width="40" 
height="40"/> </a> </p>
<h5 align="left">Backend :</h5>
<p align="left">
<a href="https://www.python.org" target="_blank" rel="noreferrer"> <img 
src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" 
height="40"/> </a> 
</p>
<h5 align="left">Databases:</h5>
<p align="left">
<a href="https://www.postgresql.org" target="_blank" rel="noreferrer"> <img 
src="https://raw.githubusercontent.com/devicons/devicon/master/icons/postgresql/postgresql-original-wordmark.svg" 
alt="postgresql" width="40" height="40"/> </a> 
</p>
<h5 align="left">CI/CD:</h5>
<p align="left">
<a href="https://www.gnu.org/software/bash/" target="_blank" rel="noreferrer"><img 
src="https://www.vectorlogo.zone/logos/gnu_bash/gnu_bash-icon.svg" alt="bash" width="40" height="40"/> </a> <a 
href="https://www.docker.com/" target="_blank" rel="noreferrer"> <img 
src="https://raw.githubusercontent.com/devicons/devicon/master/icons/docker/docker-original-wordmark.svg" alt="docker" 
width="40" height="40"/> </a> <a href="https://git-scm.com/" target="_blank" rel="noreferrer"> <img 
src="https://www.vectorlogo.zone/logos/git-scm/git-scm-icon.svg" alt="git" width="40" height="40"/> </a> <a 
href="https://kubernetes.io" target="_blank" rel="noreferrer"> <img 
src="https://www.vectorlogo.zone/logos/kubernetes/kubernetes-icon.svg" alt="kubernetes" width="40" height="40"/> </a> 
</p>

## Project Tree View

    .vscode/
        ├─ launch.json (vscode odoo launch file - DONOT commit(change) this file )
        ├─ settings.json (vscode launch settings file - DONOT commit(change) this file )
    bin/
        ├─ project_name.cfg (odoo config file for dev team - DONOT commit(change) this file )
    code/
        ├─ customer-odoo-apps (project custom modules)/
        ├─ artec-odoo-apps (submodule)/
        ├─ artec-third-party-apps (submodule)/
        ├─ hr-enterprise (hr submodule)/
    doc /
        ├─ doc_code_technical_description.doc (code technical documentation)
    .gitignore (git file to ignore some files or file with specific extensions)
    .gitlab-ci.yml (gitlab .yaml file for code integration and code deployment automation)
    .gitmodule (git submodule path)

## Usage
```bash
# (Method 1) git clone using http
git clone [-b branch_name] http://gitlab.artec-int.local/artec-int/project_name [directory_path]

# (Method 2) git clone using ssh (ssh must be configured in gitlab - ssh-key configuration https://docs.gitlab.com/ee/ssh/)
git clone [-b branch_name] git@gitlab.artec-int.local:artec-int/project_name [directory_path]

# git submodule update
cd project-path/
git submodule init
git submodule update

# (Method 1) Start odoo server using vscode
code project_path/
# Inside vscode Run and Debug - Run

# (Method 2 ) Start odoo server 
source ~/venv/odoo(15-14-13-12..)/bin/activate
~/src/odoo/(15.0-14.0-13.0-12.0..)/odoo-bin -c ~/project/project_name/bin/project_name.cfg
```

## Best Practices

### GIT
```bash

    # Remove files permanently (python git-filter-repo should be installed)
    python3 -m pip install --user git-filter-repo
    git filter-repo --path path/to/big/file.m4v --invert-paths

```


