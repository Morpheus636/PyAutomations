# jmt_cicd Workflow

JMT uses our custom workflow based on github flow (known as jmt_cicd) for our CI/CD projects, as described below.

## Branches:
### main
The main branch is where code can be deployed into the production or staging environment. 

Code in this branch is automatically applied with the `PRODUCTION` tag and deployed to the production environment.
To deploy to other environments, git tags such as `STAGING` can be applied on any branch.

### Feature
Feature branches should be branched from the Production branch. They are where
active development of new features or improvements to existing features should take place.

Feature branches should start with `feature/`, and be followed by the GitHub issue
number and a brief description of the feature to be added. Example:
<br />`feature/#32_rate_limiting`

Feature branches should first be merged into Staging, to test and ensure they will not 
break the rest of the system, then they should be merged into Production, where they
will be deployed. All tests and checks should pass before merging.

### Bugfix
Bugfix branches should be branched from production. They are where bug fixes should be developed.

Bugfix branches should start with `bugfix/`, followed by the GitHub issue number and a brief
description of the bug. Example:
<br /> `bugfix/#33_rate_limit_crashes_client`

Bugfix branches should first be merged into Staging, to test and ensure they will not break
the rest of the system, then they should be merged into Production, where they will be deployed.
All tests and checks should pass before merging.

### Hotfix
Hotfix branches are where especially urgent fixes should be developed, since hotfix branches
are the only way to merge code directly into production without testing it in staging first.

Hotfix branches start with `hotfix/`, followed by the GitHub issue number, and
a brief description of the issue being fixed. Example:
<br /> `hotfix/#34_remote_code_execution`

Hotfixes should be merged directly into production.

## Commit Messages
Commit messages are very important. They tell other developers what you did without
them having to read all the changes you made. Commit messages should be in the form:

`#<GitHub issue number>: <Description of what you did>`

IE:

`#15: Added endpoints for adding/removing users`


## Merging
All merging must be done via a pull request. All pull requests must pass github actions.
All merges to production must have been deployed to staging and tested, except hotfixes.
