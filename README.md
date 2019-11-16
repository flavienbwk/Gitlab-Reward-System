# Gitlab Reward System (Gitlab RS)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A web service which implements a reward system with badges based on statistics using your Gitlab instance API.

**This project is under active development, only the documentation is written. Support this project by adding a star !**

## Getting started

During the installation of Gitlab RS, you will need to have access to a Gitlab user with **admin access** so you can grab the API key with full privileges.

This is needed by Gitlab RS because the reward system need to analyze all users activities.

### Configuration

First, you will need to generate a Gitlab access token key by visiting `https://<your-gitlab>/profile/personal_access_tokens`.  
Make sure to tick all `Scopes` checkboxes and click on `Create personal access token`. It will appear in a message on top : copy it.

_Under construction_

### Run

Simply execute :

```
docker-compose up -d
```

And visit [`localhost:10079`](http://localhost:10079) to access the web application

## Create your own badges

_Under construction_

## Badges list

### Currently implemented

None (under active development).

### To be implemented

Preview | Name | Description | Code name | Properties
--------|------|-------------|------|-----------
_None_ | I am a real {company name} engineer ! | I've commited to the codebase in the last 3 months | present | computed, unique
_None_ | Polyglot 1 | I code in 1 language | polyglot | computed, overlayed
_None_ | Polyglot 2 | I code in 2 languages | polyglot | computed, overlayed
_None_ | Polyglot 4 | I code in 4 languages | polyglot | computed, overlayed
_None_ | Polyglot 6 | I code in 6 languages | polyglot | computed, overlayed
_None_ | Polyglot 8 | I code in 8 languages ! | polyglot | computed, overlayed
_None_ | Polyglot 10+ | I code in at least 10 languages ! | polyglot | computed, overlayed
_None_ | Commit writer | I enjoy writing extensive commit descriptions (>80 characters) | commit-writer | computed, unique
_None_ | Little star | My repos have been stared at least 1 time ! | star-aficionado | computed, overlayed
_None_ | Rising star | My repos have been stared at least 10 times ! | star-aficionado | computed, overlayed
_None_ | Contributor 1  | I've contributed to at least 0.1% of the codebase | contributor | computed, overlayed
_None_ | Contributor 2  | I've contributed to at least 1% of the codebase | contributor | computed, overlayed
_None_ | Contributor 3  | I've contributed to at least 3% of the codebase | contributor | computed, overlayed
_None_ | Contributor 4  | I've contributed to at least 5% of the codebase | contributor | computed, overlayed
_None_ | Contributor 5  | I've contributed to at least 10% of the codebase | contributor | computed, overlayed
_None_ | Superstar | My repos have been stared at least 20 times ! | star-aficionado | computed, overlayed
_None_ | Intern ! | I've once been an intern | contract-type | attributed, cumulative
_None_ | Apprentice ! | I've once been an apprentice | contract-type | attributed, cumulative
_None_ | Full-time employee ! | I've once been a full-time employee | contract-type | attributed, cumulative

:information_source: _attributed_ badges are given by a Gitlab RS administrator through the administration interface (`/admin-dashboard`).

:information_source: _overlayed_ badges are badges that cannot be cummulated. The highest will replace the last one earned.

## Philosophy (how Gitlab RS can help your team)

Reward systems are used in a lot of companies, such as Google or StackOverflow, and take shape as badges that are accessible publicly from the member's profile.

It may look like such system only serves the ego of collaborators, but it has a much more useful intent.

A reward system will :

- Make your team member efforts more valorized
- Improve their skills
- Strengthen the code base

Reward systems are not about ignoring bad behaviour. They are about recognizing and celebrating positive, healthy behavior. 

How can you make sure the system you put into place does this effectively, and encourages your team members to be as efficient as possible ?

### What to consider when creating a reward system

#### 1. Identify the behavior you want to change

Maybe it's your team members inability to follow the optimal Python's coding style or using the continuous integration tools of the team. Maybe it's something else... but pick them !

#### 2. Start a feedback loop

In your system, make sure that you have a way to measure progress or determine whether your team members are engaging in the desired behavior. If, for instance, you want them to commit regularly, how are you going to ensure they do it ?

And when they start to do it consistently, what's the next step ? How can you move forward with this behavior ? Maybe you add specifications in the way they need to commit (extended description, tagging issues in description...). Until they reach all achievments !

Eventually pay them a coffee or give them some goodies ;)

#### 3. Stay fun

Add some funny badges such as "Jeeez, slow down" when comitted continuously during 6 hours. So your team enjoy the reward system more than ever !

## Contributors

Do not hesitate to PR your algorithms of badge ideas ! If approved, it will be added to the official Gitlab RS repository along with your Github username !
