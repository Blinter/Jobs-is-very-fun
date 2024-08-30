**Welcome to Jobs.is-very.fun – Your Ultimate Job Search Companion!**


 [Jobs.is-very.fun](https://jobs.is-very.fun) is designed to be a user-friendly portal for job seekers and professionals eager to discover new opportunities. Our platform offers a wealth of options to help you organize, track, and manage your job search, making your journey as smooth and efficient as possible.

We don’t just pull job listings from popular sites like Indeed, LinkedIn, and Glassdoor; we go beyond that by aggregating jobs from hard-to-reach sources that are often overlooked. Our mission is to bring all these opportunities together in one easy-to-use, accessible platform—completely free for job seekers, with no compensation received from employers.

Built from the ground up with scalability and reliability in mind,  [Jobs.is-very.fun](https://jobs.is-very.fun) ensures that you have the tools you need to stay organized. You can save job listings into customized lists, order them by preference, and even add personal notes to track your application status or any updates from employers.

Navigating the job market can be challenging, but with [Jobs.is-very.fun](https://jobs.is-very.fun), you have a reliable and effective tool to help you every step of the way. Start exploring today and find the job that’s just right for you!


***Developers***

Take your projects to the next level by leveraging the power of our jobs database. With our API, you can style and build your own user interface (UI) without the hassle of managing databases, saving data, or optimizing SQL queries. Focus on crafting an exceptional user experience while we handle the heavy lifting behind the scenes. 

This feature will be added in a future iteration, while we focus on adding more sources to scrape and pull data from. You can view the routes currently accessible from an initial API in the [routes_api.txt](routes_api.txt) file.


**Note from the Programmer**

The code has been well documented, and I've put a lot of grunt-work into the first iteration, which will hopefully improve and speed up progress on new features down the pipeline. The most important aspect of this project are the specialized geospatial search queries and the impressive amount of time spent on administrator and back-end tools to further improve development times further down the road.

---

# Overview


### **Home Page**


![Image](jobs-is-very-fun-homepage.png)

### **Job Search Dashboard**

**Keywords**

Due to the nature of the quality of data from the API's, the searches are only utilizing title scans. There are however, extra tags such as Entry Level, or Senior level, Experience Levels associated with each job listing, but the amount of jobs without the experience level might exclude promising jobs.

Currently, weighted keyword searches on descriptions are in development and in testing.

**Location**

For proper searching of locations, there should be three values separated by commas. It first runs through `pelias-parser` then iterates and tests several times in order to find jobs with locations related to that search query.
### City, State, Country

**(i.e. San Francisco, California, United States)**

*Additionally, **remote** can be searched alone, or can be appended anywhere in the location query.*


![Image](jobs-is-very-fun-job-dashboard.png)


### **Company Search Dashboard**

![Image](jobs-is-very-fun-company-dashboard.png)


### **Registration Page**

![Image](jobs-is-very-fun-email-registration.png)


### **User Dashboard**

![Image](jobs-is-very-fun-user-dashboard.png)


### **View Job Page**

![Image](jobs-is-very-fun-single-job.png)


### **View Company Page**

![Image](jobs-is-very-fun-single-company.png)


### Javascript Libraries

* [Bootstrap v5.3](https://getbootstrap.com/)
* [Popper.js v2.11.8](https://floating-ui.com/)
* [jQuery v3.7.1](https://jquery.com/)
* [Axios v1.7.5](https://github.com/axios/axios)
* [Chart.js v4.4.4](https://github.com/chartjs/Chart.js)
* [Font Awesome](https://fontawesome.com/)

### Python Libraries

- **Flask Framework**: 
	- `Flask`, `Flask-Bcrypt`, `Flask-Cors`, `Flask-Mailman`, `Flask-SQLAlchemy`, `Flask-WTF`

- **Database & ORM**: 
	- `SQLAlchemy`, `Flask-SQLAlchemy`, `GeoAlchemy2`, `psycopg2-binary`, `PyMySQL`

- **Google APIs**: 
	- `google-api-python-client`, `google-auth`, `google-auth-httplib2`, `google-auth-oauthlib`

- **Security & Authentication**: 
	- `bcrypt`, `cryptography`, `PyJWT`, `oauthlib`, `requests-oauthlib`

- **Web Scraping & Parsing**: 
	- `beautifulsoup4`, `bs4`, `lxml`, `soupsieve`, `html5lib`, `html2text`, `selenium`, `undetected-chromedriver`

- **Asynchronous Networking**: `
	- `trio`, `trio-websocket`, `websockets`, `websocket-client`

- **Other Web Technologies**:  
	- `Jinja2`, `MarkupSafe`, `WTForms`, `gunicorn`

- **Utilities & Miscellaneous**: 
	* `pytz`, `requests`

* [Beautiful Soup4](https://pypi.org/project/beautifulsoup4/)
* [html2text](https://github.com/aaronsw/html2text)
* [Google API Python Client](https://github.com/googleapis/google-api-python-client)
* [Undetected Chromedriver](https://github.com/ultrafunkamsterdam/undetected-chromedriver)
* [Selenium](https://www.selenium.dev/)
* [PyMongo](https://www.mongodb.com/docs/languages/python/pymongo-driver/current/)

### Database Software

[MariaDB](https://mariadb.org/)
[PostgresSQL](https://www.postgresql.org/)
[MongoDB](https://www.mongodb.com/)
[MongoDB GridFS](https://www.mongodb.com/docs/drivers/node/v3.6/fundamentals/gridfs/)

**SQL (Location Data)**

[Countries States Cities Database](https://github.com/dr5hn/countries-states-cities-database)

### Node

[Pelias Parser](https://github.com/pelias/parser)


## API's

1. **Indeed Germany** - [Relu Consulting Services](https://rapidapi.com/relu-consultancy-relu-consultancy-default/api/indeed-scraper-api-germany)
2. **Indeed Sweeden**  - [Vuesdata](https://rapidapi.com/user/vuesdata)
3. **Indeed United States** - [Vuesdata](https://rapidapi.com/user/vuesdata)
4. **Indeed Denmark** - [Vuesdata](https://rapidapi.com/user/vuesdata)
5. **Indeed Finland** - [Vuesdata](https://rapidapi.com/user/vuesdata)
6. **Indeed Job Search API** - [jaypat87](https://www.specrom.com/data-marketplace/)
7. **Freelancer API** - [Omar](https://rapidapi.com/omarmohamed0/api/freelancer-api)
8. **Jobwiz** - [PostMan](https://www.postman.com/jobwiz/workspace/jobwiz/collection/28349133-c1e5e44b-296e-41e3-a04b-cd66b545d8c7)
9. **Active Jobs DB** (*Bamboohr, Eightfold, Greenhouse, Lever.co, Oraclecloud, Phenompeople, Recruitee, SmartRecruiters, SuccessFactors, Workable, Workday, Ashby, TeamTailor, Paylocity, Breezy HR, Apple*) - [Fantastic Jobs](https://fantastic.jobs/)
10. **Google Jobs API** (*LinkedIn, Indeed, Jooble, ZipRecruiter, Glassdoor*) - [Patrick](https://rapidapi.com/Pat92/api/jobs-api14)
11. **Google Jobs** (*LinkedIn, Indeed, Glassdoor, ZipRecruiter, Monster*) - [OpenWeb Ninja](https://www.openwebninja.com/)
12. **Job Scanner Data Feed** (*LinkedIn, Indeed, SimplyHired, Careerbuilder, Google, Monster*) - [JayPat87](https://rapidapi.com/jaypat87/api/job-search15)
13. **USA Jobs for IT** (*Indeed, USA Jobs, LinkedIn, Monster, Jobble*) - [BetoAlien](https://rapidapi.com/betoalien/api/usa-jobs-for-it)
14. **Google Jobs** - [DoDocr7](https://rapidapi.com/dodocr7/api/google-jobs)
15. **Glassdoor + Indeed Scraper API** - [Mantiks](https://mantiks.io/)
16. **Real-Time Glassdoor Data** - [OpenWeb Ninja](https://www.openwebninja.com/)
17. **RemoteOK Jobs Portal** - [RemoteOK](https://remoteok.com/)
18. [Remoote Job Search Scraper](https://remoote.app)
19. [**Jobicy**](https://jobicy.com/)
20. [**Jobisite**](https://www.jobisite.com/)
21. **APIJobs** - [APIJobs.dev](https://apijobs.dev/)
22. **Ava Data Services** - [Job Transparency](https://www.jobtransparency.com/)
23. [**Zambian Jobs API**](https://rapidapi.com/JobsAPI2020/api/zambian-jobs-api1)
24. **Remote Jobs API** - [Bareq](https://rapidapi.com/bareq/api/remote-jobs-api1)
25. **Real-Time LinkedIn Scraper** - [RockApis](https://rapidapi.com/rockapis-rockapis-default/api/linkedin-data-api)
26. **LinkedIn Job Search API** - [jaypat87](http://www.jobscanner.org/)
27. **LinkedIn Data Scraper** -[EZ](https://rapidapi.com/mgujjargamingm/api/linkedin-data-scraper)
28. **LinkedIn Jobs Scraper** -[Bebity.io](https://bebity.io) - [RapidAPI](https://rapidapi.com/bebity-bebity-default/api/linkedin-jobs-scraper-api)
29. **LinkedIn Jobs Scraper** - [FreshData](https://rapidapi.com/freshdata-freshdata-default/api/fresh-linkedin-profile-data)
30. **LinkedIn Live Data API** - [Sohail](https://linkifyapi.com/)
31. **Arbeitsagentur** (*Employement Agenc*y) - [Arbeitsagentur](https://rapidapi.com/relu-consultancy-relu-consultancy-default/api/arbeitsagentur-employement-agency)

### Other Resources and Technologies

* [Google Fonts](https://fonts.google.com/)
* [Google reCaptcha v2](https://www.google.com/recaptcha/about/)
* [Obsidian](https://obsidian.md/)
* [Lorem Ipsum](https://loremipsum.io/)
* [Visily](https://www.visily.ai/)

**Software**

* [Linux Containers (LXC)](https://linuxcontainers.org/)
* [Proxmox VE 8.2](https://www.proxmox.com/)
* [Chromium](https://www.chromium.org/chromium-projects/)
* [Insomnia](https://github.com/Kong/insomnia)
* [.NET 9.0 Preview](https://dotnet.microsoft.com/en-us/download/dotnet/9.0)
* [WinSCP](https://winscp.net/eng/index.php)
* [Let's Encrypt](https://letsencrypt.org/)
* [ACME Client](https://letsencrypt.org/docs/client-options/)

**Service Providers**

* [Webshare.io](https://www.webshare.io/)
* [ServaRICA (IAAS)](https://servarica.com)
* [FreeDNS Subdomains](afraid.org)

**LLM's**

* [Phind (LLM)](https://phind.com/)*

**IDE's**

* [Visual Studio 2022 Preview](https://visualstudio.microsoft.com/vs/preview/)
* [PyCharm Community Edition 2024.1](https://www.jetbrains.com/pycharm/)
* [dbForge Studio](https://www.devart.com/dbforge/)
* [MongoDB Compass](https://www.mongodb.com/products/tools/compass)
* [Studio 3T](https://studio3t.com/)


# Schemas

### **MariaDB**

![Image](mariadb_schema.png)

### **MongoDB GridFS**

![Image](mongodb_gridfs.png)

### **PostgresSQL**

![Image](psql_schema.png)


# **Simple Database Flow**

![Image](simple_database_flow.png)

---

# Deployment


**Environment**
> Debian 12 "Bookworm"


**Minimum/Recommended Server Specifications**
- 2 vCPU's
- 2 GB RAM
- 16 GB HDD Space


For the purposes of this setup guide, that latest Debian repositories are used to install and update the latest updates. If you wish to use a different operating system, please find and locate the respective packages that are required.

Additionally, due to the complex nature of this setup guide, you must create and maintain SSL certificates for the `nginx` reverse proxy webserver, and the `postfix` + `dovecot` mail servers.

The user login/registration  and forgot password processes require a Google ReCaptcha v2 key to be supplied, and SSO secrets for Google and GitHub must also be generated and supplied in the credentials file.

Furthermore, for scraping routines to work properly, at least one residential proxy must be configured, and `danted` server or a SOCKS v5 server must be used for querying API's.

Once you have these, I will briefly mention them when configuring the other settings for the deployment.

Use SSH or login to the Server, VPS, or Environment as root.
If you are logging in as an unprivileged user, use these commands into the root user, if not, you may include `sudo` in all of the commands that require superuser access.

```
sudo su -
```

Then enter your root password if required.


**Default Debian Bookworm Sources File**
`/etc/apt/sources.list`

```
deb http://deb.debian.org/debian bookworm main contrib
deb http://deb.debian.org/debian bookworm-updates main contrib
deb http://security.debian.org bookworm-security main contrib
```


**Update the Debian OS with these commands**

```
apt clean;
apt update;
apt upgrade;
apt dist-upgrade;
```


**Install sudo if required**

```
apt install sudo -fy;
```


**Install screen and nano packages for Deployment**

```
apt install screen nano -fy;
```


---
# **Installation of Required Software**



As opposed to using the default Debian repository for the package, we will use the repository provided by **PGDG** (PostgreSQL Global Development Group)
[PostgresSQL Repository Instructions](https://wiki.postgresql.org/wiki/Apt#PostgreSQL_packages_for_Debian_and_Ubuntu)


## PostgreSQL Repository Installation


**Add ca-certificates file, install the PGDG repository keys, then add their repositories**

```
apt install ca-certificates
install -d /usr/share/postgresql-common/pgdg
curl -o /usr/share/postgresql-common/pgdg/apt.postgresql.org.asc --fail https://www.postgresql.org/media/keys/ACCC4CF8.asc
printf \
"deb [signed-by=/usr/share/postgresql-common/pgdg/apt.postgresql.org.asc] https://apt.postgresql.org/pub/repos/apt bookworm-pgdg main\n\
" >> /etc/apt/sources.list.d/pgdg.list
```


**PostgreSQL 16 Installation**

```
apt update;
apt install postgresql -fy;
```


We will use the MongoDB Community Edition and provided repositories provided by the MongoDB Site.
[MongoDB Repository Instructions](https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-debian/)


**Install `gnupg` as necessary**

```
apt install gnupg -fy
```

---

# **MongoDB CE (Community Edition) Repository Installation**


**Add GPG Keys**

```
curl -fsSL https://www.mongodb.org/static/pgp/server-7.0.asc | \
   gpg -o /usr/share/keyrings/mongodb-server-7.0.gpg \
   --dearmor
```


**Add Repository**

```
echo "deb [signed-by=/usr/share/keyrings/mongodb-server-7.0.gpg] http://repo.mongodb.org/apt/debian bookworm/mongodb-org/7.0 main" | tee /etc/apt/sources.list.d/mongodb-org-7.0.list
```


**Install latest version of MongoDB**

```
apt update;
apt install -fy mongodb-org;
```


**Change `ulimit` for open files to 64000.**
[MongoDB ulimit Documentation](https://www.mongodb.com/docs/manual/reference/ulimit/)

**Add this to the bottom of `/etc/security/limits.conf`**

```
*                hard    nofile          64000
*                soft    nofile          64000
```


**Check status of MongoDB Server**

```
systemctl status mongod
```

---

# Install Node.js and npm (Node Package Manager)


[Node.js 22 Repository Instructions](https://github.com/nodesource/distributions?tab=readme-ov-file#using-debian-as-root-nodejs-22)


**Install apt-transport-https as necessary**

```
apt -y install apt-transport-https;
```


**Installation Instructions**

```
cd ~
curl -fsSL https://deb.nodesource.com/setup_22.x -o nodesource_setup.sh
bash nodesource_setup.sh
```


**Install Node.JS**

```
apt-get install -y nodejs
node -v
```

---
# Install pelias-parser node.js Package

[NPM Package](https://www.npmjs.com/package/pelias-parser)


Pelias Parser is used to classify location data and is used to supplement location requests and specifically to process data for some API's that provide incoherent location data.


### Add `pelias` user and group for microservice

```
useradd -M pelias
usermod -L pelias
```


**Verify new User**

```
id pelias
```


**Create Pelias Home Directory and `cd` to it**

```
mkdir /home/pelias;
chown -Rf pelias:pelias /home/pelias;
cd /home/pelias;
```


**Modify the `.bashrc` and update permissions. 
Enter terminal with bash shell as the new user.**

```
printf "cd /home/pelias" >> /home/pelias/.bashrc
chown -Rf pelias:pelias /home/pelias/.bashrc

sudo su pelias --shell /bin/bash
```


**Install `pelias-parser` and required dependencies as new user `pelias`**

```
npm i pelias-parser lodash chalk
```


**Edit `~/node_modules/pelias-parser/server/http.js` for our Deployment**

```
nano ~/node_modules/pelias-parser/server/http.js;
```


**Modify `cpus` to reflect a single core**

```
const cpus = 1
```

Find `const HOST = process.env.HOST || undefined`


**Modify HOST to run on `"localhost"`**

```
const HOST = process.env.HOST || "localhost"
```


**Additional configuration is required**

```
nano ~/node_modules/pelias-parser/debug/DebugOutputBuilder.js
```

**Find**

```
const chalk = require('chalk');
```


**Replace `require` with `import`**

```
const chalk = import('chalk')
```


**Save/Exit the file**


**Initialize a screen and start `pelias-parser`**

```
screen -S 'pelias_parser'

node ./node_modules/pelias-parser/server/http.js
```


*The output should show*

```
parser loading
[master] using 1 cpus
[master] listening on localhost:3000
```


**Exit the screen using the shortcut**

```
CTRL + A + D
```


**Test that the endpoint works by using curl**

```
curl -X GET http://localhost:3000/parser/parse?text=San+Francisco \
-H "Charset: utf8" \
-H "Content-Type: application/json; charset=utf-8" \
-o -
```


**The ouput**

```
{"input":{"body":"San Francisco","start":0,"end":13},"solutions":[{"score":1,"classifications":[{"label":"locality","value":"San Francisco","start":0,"end":13}]}]}
```


*Now that pelias-parser has been configured and the microservice is running, exit the `su` session.*

```
exit;
```

---

# PostgreSQL Server Configuration

Several extensions are used for optimized search queries. The extensions are used for vector keyword, distance and location searches. They are also used to parse different types of location data that are received by API's.

**PostgreSQL Extensions List**
- *plpgsql*
- *pg_trgm*
- *cube*
- *postgis*
- *postgis-topology*
- *earthdistance*

---

# Install Postgis
[PostGIS Website](https://postgis.net/)


**Install PostGIS 3 for PostgreSQL 16**

```
apt -fy install postgresql-16-postgis-3
```


**Make sure that the OS has UTF-8 Encoding enabled so that we can populate the Geolocation data later**

```
localedef -i en_US -f UTF-8 en_US.UTF-8
```

### Login to the `postgres` user


**Verify new User**

```
id postgres
```


**Login**

```
su postgres
```


**Open PostgreSQL Command Line**

```
psql
```

*These commands are completed in the `postgres` shell.*


**Create the `jobs` Username and the `jobs` Database as the `postgres` user**

**Replace `NEWPASSWORDzzzz` with a secure password.**

```
CREATE USER jobs WITH PASSWORD 'NEWPASSWORDzzzz';
CREATE DATABASE jobs WITH ENCODING='UTF8' LC_COLLATE='en_US.UTF-8' LC_CTYPE='en_US.UTF-8' TEMPLATE=template0 OWNER jobs;
```


**Add `jobs` user as superuser and grant privileges**

```
GRANT ALL PRIVILEGES ON DATABASE jobs TO jobs;
ALTER USER jobs with SUPERUSER;
```


Exit the `psql` shell
```
\q
```


**Clear the PostgreSQL command history since it stores plain text commands containing passwords.**

```
rm ~/.psql_history
```


**Exit `su`**

```
exit;
```


As a root user, modify the Postgres Configuration.


**To allow password authentication on the host, the `pg_hba.conf` must be modified.**

```
nano /etc/postgresql/16/main/pg_hba.conf
```


**Find**

```
# "local" is for Unix domain socket connections only
local   all             all                                     peer
```


**Replace `peer` with `trust`**

```
# "local" is for Unix domain socket connections only
local   all             all                                     trust
```


**To prevent a password prompt when accessing the database as `postgres` also change**

```
# Database administrative login by Unix domain socket
local   all             postgres                                md5
```


**Replace `md5` to `trust`**

```
# Database administrative login by Unix domain socket
local   all             postgres                                trust
```

*You can switch `trust` back to `md5` for the `Unix Domain Socket` connections after logging into the database as `postgres`.*


**Reload the Daemon and restart PostgreSQL**

```
systemctl daemon-reload
systemctl restart postgresql
```


*The following commands can be executed as either a root user or a non-privileged user.*


**Now we can enter the PostgreSQL shell as the `jobs` database user.**

```
psql -U jobs -d jobs -W
```

*Input the new password when requested.*


**If the password authentication works and the Postgres shell is visible, then install the extensions.**

```
CREATE EXTENSION IF NOT EXISTS plpgsql;
CREATE EXTENSION IF NOT EXISTS pg_trgm;
CREATE EXTENSION IF NOT EXISTS cube;
CREATE EXTENSION IF NOT EXISTS postgis;
CREATE EXTENSION IF NOT EXISTS postgis_topology;
CREATE EXTENSION IF NOT EXISTS earthdistance;
```


**Verify that the extensions are installed with this command**

```
\dx
```


**The output**

```
------------------+---------+------------+-------------------------------------------------------------------
 cube             | 1.5     | public     | data type for multidimensional cubes
 earthdistance    | 1.1     | public     | calculate great-circle distances on the surface of the Earth
 pg_trgm          | 1.6     | public     | text similarity measurement and index searching based on trigrams
 plpgsql          | 1.0     | pg_catalog | PL/pgSQL procedural language
 postgis          | 3.4.2   | public     | PostGIS geometry and geography spatial types and functions
 postgis_topology | 3.4.2   | topology   | PostGIS topology spatial types and functions
(6 rows)

```


**This query will also show the extensions**

```
SELECT * FROM pg_extension;
```


**Exit the PostgreSQL shell**

```
\q
```

**We will connect back to the PostgreSQL as the `postgres` user.**


**Make sure we are in the `postgres` `su` shell.**

```
su postgres;
```


```
psql
```


**Remove the SUPERUSER role from the `jobs` PostgreSQL database user**

```
ALTER USER jobs WITH NOSUPERUSER;
GRANT CONNECT ON DATABASE jobs TO jobs;
GRANT USAGE ON SCHEMA public TO jobs;
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO jobs;
```


**Verify that the user `jobs` has no SUPERUSER attribute.**

```
\du jobs
```


**Quit the `psql` shell and verify the database user has no *SUPERUSER* access to the `jobs` database.**

```
\q
```


**Access the `jobs` database using psql**

```
psql -U jobs -d jobs -W
```


**Check the privileges**

```
\du
```


The point of adding then removing SUPERUSER roles to the new database user is to allow the user to add all the PostgreSQL extensions.

**PostgreSQL is now configured.**


---
# MariaDB Server Configuration


*We use MariaDB instead of MySQL for the database software.*
[MariaDB Repository Instructions](https://mariadb.com/kb/en/mariadb-package-repository-setup-and-usage/#platform-specific-behavior-on-debian-and-ubuntu)

---

# MariaDB Repository Installation Script


**Install `curl` and `ca-certificates` as necessary**

```
apt install curl ca-certificates -fy;
```


```
curl -LsS https://r.mariadb.com/downloads/mariadb_repo_setup | bash -s -- --skip-maxscale --skip-tools
```

**This script adds the necessary  MariaDB repositories to**
`/etc/apt/sources.list.d/mariadb.list`


**Install MariaDB using `apt`**

```
apt clean;
apt update;
apt -fy install mariadb-server;
```


**Configure MariaDB**

```
mysql_secure_installation
```

**Enter your root password,**

Enter `Y` to use unix_socket authentication.
Enter `N` to skip changing the root password.
Enter `Y` to remove anonymous users.
Enter `N` to allow root login remotely. (If accessing the database using an external tool, this option can be changed.)
Enter `Y` to remove test database and access to it.


**Modify the MariaDB server configuration**

```
nano /etc/mysql/mariadb.conf.d/50-server.cnf
```

**Depending on your server, modify the configuration**


**Uncomment the lines:**

```
user                    = mysql
datadir                 = /var/lib/mysql
tmpdir                  = /tmp
```


**If you want to access the MariaDB server from outside of the server, you can change the `bind-address` to listen on all IP's.**

```
bind-address            = 0.0.0.0
```


**Reload the configuration and restart MariaDB**

```
systemctl daemon-reload
systemctl restart mariadb
```


**Access the MariaDB shell**

```
mariadb -u root;
```


**It should show an output like this**

```
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 1
Server version: 11.5.2-MariaDB-deb12 mariadb.org binary distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]>
```

Create the `jobs` user and the Database `jobs`
Replace `localhost` with `%` if you prefer not to access the database remotely.


**Replace `NEWPASSWORDyyyy` with a secure password.**

```
CREATE USER 'jobs'@'localhost' IDENTIFIED BY 'NEWPASSWORDyyyy';
GRANT ALL PRIVILEGES ON jobs.* TO 'jobs'@'localhost';
FLUSH PRIVILEGES;
```


**Exit the MariaDB Shell**

```
EXIT;
```


**Verify that the user has been created for the server**

```
mariadb -u jobs -p;
```

**Enter the password that was newly created `NEWPASSWORDyyyy`**


The MariaDB shell should show. Now create the database and attempt to select and test the privileges.


**Create the Database `jobs`**

```
CREATE DATABASE `jobs`;
USE jobs;
```


**Test SQL Privileges**

```
CREATE TABLE `jobs`.`Untitled`  (
  `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`)
);
INSERT INTO `jobs`.`Untitled` (`id`) VALUES (NULL);
UPDATE `jobs`.`Untitled` SET `id` = 999999 LIMIT 1;
DELETE FROM `jobs`.`Untitled` WHERE `id` = 999999;
DROP TABLE `jobs`.`Untitled`;

EXIT;
```

**If everything has processed without any errors, then the MariaDB server has been configured correctly.**

---

# MongoDB Server Configuration


**Start MongoDB**

```
systemctl daemon-reload;
systemctl start mongod;
systemctl status mongod;
```

**If you have an error with MongoDB starting**


**Please view the Mongod log file, fix the error(s) and try again**

```
tail /var/log/mongodb/mongod.log
```


**Launch the MongoDB Shell**

```
mongosh
```

*MongoDB does not create databases, rather, you can select the database and begin populating it as needed.*

**Change database to `jobs`**

```
use jobs
```


**Create a new `jobs` user**

**Replace `NEWPASSWORDxxxx` with a secure password.**

```
db.createUser({ user: "jobs", pwd: "NEWPASSWORDxxxx", roles: [{ role: "readWrite", db: "jobs" }] })
```


**If the command is successful, verify then quit.**

```
db.getUsers()
exit
```


**Ensure that MongoDB is configured to require authentication. Uncomment the `security` line and add the following:**

```
security: 
  authorization: "enabled"
```



**If you want to allow remote access to the MongoDB server, edit the `mongod.conf` file.**

```
nano /etc/mongod.conf
```


**Add a comma and a new IP to add additional IP's. Replace `x.x.x.x` with your specified IP**

```
# network interfaces
net:
  port: 27017
  bindIp: 127.0.0.1, x.x.x.x
```

**Restart MongoDB**

```
systemctl stop mongod;
systemctl daemon-reload;
systemctl start mongod;
systemctl status mongod;
```

**Test the authentication**

**Replace `NEWPASSWORDxxxx` with your MongoDB `jobs` account password.**

```
mongosh --username jobs --password NEWPASSWORDxxxx --authenticationDatabase jobs
```

**From MongoSH shell**

**Replace `NEWPASSWORDxxxx` with your MongoDB `jobs` account password.**

```
use jobs
db.auth("jobs", "NEWPASSWORDxxxx")
db.runCommand({ connectionStatus: 1 })
exit
```


**Later, after the Python environment is set up, we will test our database by uploading the `LICENSE` file to the MongoDB using `GridFS`**


---

# All databases should now be configured successfully!


## **Summary**

1. MariaDB default running on port `3306`
2. PostgreSQL default on port `5432`
3. MongoDB default on port `27017`

*Make sure to configure a firewall to these ports for added security if you have enabled remote access.*

---

# Configure the main `jobs` Account

*This username can be changed to reflect a name of your choice. Replace the user commands from `jobs` to `dev` or another name.*

### Add `jobs` user and group

```
useradd -M jobs
usermod -L jobs
```

**Verify new User**

```
id jobs
```

**Create a `jobs` Home Directory and `cd` to it**

```
mkdir /home/jobs;
chown -Rf jobs:jobs /home/jobs;
cd /home/jobs;
```

**Modify the `.bashrc` and update permissions.** 

```
printf "cd /home/jobs" >> /home/jobs/.bashrc
chown -Rf jobs:jobs /home/jobs/.bashrc
```

 **Install `git` a superuser or add `sudo` to each of these commands.**
 
```
apt clean
apt update
apt install git
```

**Enter terminal with bash shell as the new user.**

```
sudo su jobs --shell /bin/bash
```

**Clone the main repository**

```
git clone https://github.com/Blinter/Jobs-is-very-fun
```

---

**Configure the `.gitignore_cleaned` and save it as `.gitignore`**


```
cd Jobs-is-very-fun;
```


**For this deployment, you can rename the repository folder to `jobs` for convenience.**

```
mv Jobs-is-very-fun jobs;
```


```
nano .gitignore_cleaned;
```

If you make any additions that you would like to keep hidden, please add them to the `.gitignore` file.
Additionally, any new directories should also ignore the `__pycache__/` folder.

You should also add a .gitignore to any modified seed file that includes any customized data. Always have a `_cleaned` suffix file with the information blocked out, if you customize a file.

**Configure the `credentials_cleaned.py` file in `secrets_jobs`**

```
cd secrets_jobs/;
nano credentials_cleaned.py;
```

**This file can be customized later if there are changes to the deployment.**

**When done, save as `credentials.py` in `secrets_jobs`**

```
# Administrator Username
admin_list = ["TestAdministrator"]

# If you add Rapid API keys, these must be added with a 'preferred_proxy' host that points to a SOCKS v5 Server. Adding credentials does not work with the current scraping implementation.
rapid_api_keys = []

# API Jobs API Keys
api_jobs_api_keys = []

# Path to the main base directory where you cloned the repository
path_to_base = "/home/jobs/jobs/"

# Path to the secrets directory
path_to_secrets = path_to_base + "secrets_jobs/"

# Please configure this since the user's session will be encrypted with this extra key.
flask_secret = "SECRETFLASKKEYaaaa"

# Email token keys used for providing email registration and forgot password tokens.
# JWT public and private keys generated from ed25519 folder.
# Remember to rotate these keys.
jwt_path_to_public_key = path_to_secrets + """EdDSA_public.pem"""  
jwt_path_to_private_key = path_to_secrets + """EdDSA_private.pem"""

# Database login details
# Accessed throughout the back-end, please configure these to reflect your password/username changes.
# The format is username:password@IP_Address:Port/Database_Name

maria_information_login_details = """mariadb+pymysql://jobs:NEWPASSWORDyyyy@127.0.0.1:3306/jobs?charset=utf8mb4"""

postgres_information_login_details = """postgresql+psycopg2://jobs:NEWPASSWORDzzzz@127.0.0.1:5432/jobs"""

mongodb_information_login_details = """mongodb://jobs:NEWPASSWORDxxxx@127.0.0.1:27017/?authSource=jobs"""

# Please repeat the same database used for MongoDB, PostgreSQL, and MariaDB
mongodb_database_name = """jobs"""  

mariadb_database_name = """jobs"""

postgres_database_name = """jobs"""

# Can be a unix timestamp
last_updated = "1715843424"

# Input the public address of your server
server_address = "0.0.0.0"

# If you configured a proxy, you may add this for leak checks.
# This variable is not used, so it does not need to be set currently.
proxy_public_ip_address_for_leak_check = "0.0.0.0"

# This site is used to test proxy servers and retrieve their IP addresses in the administrator dashboard.
proxy_public_website_check = "https://api.ipify.org"

# If the proxy does not respond successfully, the server can connect to the proxy using this token or password, and run repair scripts. This currently is not implemented so it does not need to be set.
proxy_server_authentication_token = "xxx"  

# This currently is not implemented so it does not need to be set.
proxy_list_location_file_path = "proxycheck/proxylist.txt"  
# This currently is not implemented so it does not need to be set.
cdn_address = "xxx"  

# This currently is not implemented so it does not need to be set.
cdn_relative_path = "/cdn/"  

# This currently is not implemented so it does not need to be set.
cdn_cloudflare_enabled = "0"

# Set proper ownership of these binaries, or copy them to a directory and point to them.
# you can chmod 777 the files after installing them.
# These binaries are used for the scraper.
path_to_chromium_exe = "/usr/bin/chromium"  

path_to_chrome_driver = "/usr/bin/chromedriver"

# Pelias Parser - This points to the microservice we set up and tested earlier
pelias_parser_query_url = "http://localhost:3000/parser/parse"

# Public IP address of the server
# This currently is not implemented so it does not need to be set.
host_public_ip_address = "0.0.0.0"  

# This should be set to your site's public URL
# such as https://jobs.is-very.fun/
# it is used in email templates
website_return_url = "xxxx"

# These options must be set if you are configuring the app to allow email registration.
# This requires a proper email server to be set up and SSL certificates to be maintained.
mail_server_mail_from = ""  
email_server_address = ""  
email_server_port = "465"  
email_server_username = "xxx"  
email_server_password = """xxx"""  
email_server_tls = False  
email_server_ssl = True  
email_server_ssl_verify = True  
email_server_use_localtime = True

# Emails are enabled by default
# This currently is not implemented so it does not need to be set.
email_enabled = "1"

# Your secret Github Key when you have added your deployed website with a callback URL.
sso_github_id = ""  
sso_github_secret = ""  

# Github SSO is enabled by default
# This currently is not implemented so it does not need to be set.
sso_github_enabled = True

# Path to the google secrets file that was provided when you created an SSO token.
sso_google_secrets_path = path_to_secrets + "google_secret.json"  

# This currently is not implemented so it does not need to be set.
sso_google_enabled = False

# The key and secret must be filled out for user login/registration and forgot password requests.
google_recaptcha_v2_key = ""  
google_recaptcha_v2_secret = ""  

# Google reCaptcha v2 is not enabled by default
google_recaptcha_v2_enabled = False
```

**Save this file as credentials.py**

----

# Proxies Configuration

**Configure the `current_proxy_list_cleaned.py` file in `../secrets_jobs`**

```
cd ../
cd secrets_jobs;
nano current_proxy_list_cleaned.py
```

You may add as many proxies as the deployment requires, but certain functions such as the scraper require residential proxies to be used and without any authentication. Datacenter proxies may be used for processing queries.

Find out which available types you can set a proxy in `enums/proxies.py`
Your IDE should also provide an auto-complete list once `ProxyType.` is input.

```
CurrentProxyList = [  
    {        
	    'proxy_address': "0.0.0.0:1080",  
        'proxy_type': ProxyType.PREMIUM_STATIC_RES_SOCKS5,  
        'auth_required': False,  
    },    {        
	    'proxy_address': "0.0.0.0:1080",  
        'proxy_type': ProxyType.OWN_DC_SOCKS5,  
        'auth_required': True,  
        'proxy_username': 'user',  
        'proxy_password': 'pass',  
    }]
```

---

# Email Template Configuration

**Modify email_jobs.py in `email_jobs/` to reflect your deployment Site Address.**

```
nano email_jobs/email_jobs.py;
```

```
# Create the email  
email = EmailMessage(  
    subject="Jobs.is-very.fun | Password Reset Request",
...
  
# Create the email  
email = EmailMessage(  
    subject="Jobs.is-very.fun | New Sign Up Verification",
```

---

# Embedded Text Description


**Modify `base.html` in `general/templates/general` to reflect your deployment.**

```
nano general/templates/general/base.html;
```


```
<meta name="description"
              content="Jobs.is-very.fun is a user-friendly portal for job seekers, offering tools to organize, track, and manage your job search efficiently.">
        <meta name="keywords"
              content="job search, job board, career opportunities, Jobs.is-very.fun">
        <meta name="author" content="Jobs.is-very.fun">
        <meta name="robots" content="index, follow">
        <link rel="canonical" href="{{ url_for('general.home') }}">

        <!-- Open Graph Meta Tags -->
        <meta property="og:title" content="Jobs.is-very.fun | Job Search Portal">
        <meta property="og:description"
              content="Discover a wealth of options to organize, track, and manage your job search efficiently with Jobs.is-very.fun.">
        <meta property="og:image"
              content="{{ url_for('general.static', filename='assets/jobs-is-very-fun-mini_logo.png') }}">
        <meta property="og:image:width" content="120">
        <meta property="og:image:height" content="36">
        <meta property="og:url" content="{{ url_for('general.home') }}">
        <meta property="og:type" content="website">
        <meta property="og:locale" content="en_US">
        <meta property="og:image:alt"
              content="A graphic representing job search on Jobs.is-very.fun">

        <!-- Twitter Card Meta Tags -->
        <meta name="twitter:card" content="summary_large_image">
        <meta name="twitter:title" content="Jobs.is-very.fun | Job Search Portal">
        <meta name="twitter:description"
              content="Discover a wealth of options to organize, track, and manage your job search efficiently with Jobs.is-very.fun.">
        <meta name="twitter:image"
              content="{{ url_for('general.static', filename='assets/search-2911/search-2911.svg') }}">
        <meta name="twitter:url" content="{{ url_for('general.home') }}">

        <!-- Standard favicon -->
        <link rel="icon"
              href="{{ url_for('general.static', filename='assets/fav/favicon.ico') }}"
              type="image/x-icon">
        <meta name="theme-color" content="#ffffff">

        <!-- PNG icons -->
        <link rel="icon" type="image/png" sizes="16x16"
              href="{{ url_for('general.static', filename='assets/fav/favicon-16x16.png') }}">
        <link rel="icon" type="image/png" sizes="32x32"
              href="{{ url_for('general.static', filename='assets/fav/favicon-32x32.png') }}">

        <!-- Apple Touch Icon -->
        <link rel="apple-touch-icon"
              href="{{ url_for('general.static', filename='assets/fav/apple-touch-icon.png') }}">

        <!-- Android Chrome Icons -->
        <link rel="icon" type="image/png" sizes="192x192"
              href="{{ url_for('general.static', filename='assets/fav/android-chrome-192x192.png') }}">
        <link rel="icon" type="image/png" sizes="512x512"
              href="{{ url_for('general.static', filename='assets/fav/android-chrome-512x512.png') }}">

        <!-- Link to Web App Manifest -->
        <link rel="manifest"
              href="{{ url_for('general.static', filename='assets/fav/site.webmanifest') }}">
```

---

### Other files that may require modification

```
email_jobs/templates/email/outgoing_email_forgot_password.html
email_jobs/templates/email/outgoing_email_verification.html

routines/debug/debug_sandbox.py

# Line 4 in <title>
user_jobs/templates/profile/profile_dashboard.html
user_jobs/templates/user/change_password_form.html
user_jobs/templates/user/reset_password_form.html
user_jobs/templates/user/user_forgot_password_form.html
user_jobs/templates/user/user_or_email_login_form.html
user_jobs/templates/user/user_registration_form.html
user_jobs/templates/user/verified_email_registration_form.html

general/templates/general/jobs_board.html
general/templates/general/companies_board.html
general/templates/general/get_started.html
```


**Modify `admin/templates/admin/admin_navigation.html` and `general/templates/general/navigation_base.html` to adjust logo and logo text.**

```
<img class="order-3 order-lg-1 align-self-start align-self-lg-end"
                 style="max-height:48px;"
                 src="{{ url_for('general.static', filename='assets/search-2911/search-2911.svg') }}"
                 alt="Jobs Search Icon" />
            <span class="order-1 order-lg-1"
                  id="logoTextMainFont">Jobs</span><span
                  class="order-2 order-lg-2"
                  id="logoTextSecondaryFont">.is-very.fun</span>
```



---

**For this next portion of the deployment, we must set up a python environment.**

**Exit the `jobs` account session (We were previously in the `jobs` account using `su`)**

---

# Install the Python Environment

```
exit;
apt install python3.11 python3-pip python3-venv -fy;
```

**Enter terminal with bash shell as the `jobs` user**

```
sudo su jobs --shell /bin/bash
```

**Go back to the deployment directory**

```
cd /home/jobs/jobs;
```

**Create a python virtual environment**

```
python3 -m venv venv
```

**Create a `virt_environment.sh` file (Which will be used to load into the `venv` and install python packages)**

```
nano virt_environment.sh;
```

**`virt_environment.sh`**

```
#!/bin/bash
export PYTHONIOENCODING=utf-8
source venv/bin/activate;
echo "To exit, type deactivate";
```

**Save/Exit**

**Set executable permissions to the `virt_environment.sh` file**

```
chmod +x virt_environment.sh
```

**Load up the new `.sh` file**

```
source virt_environment.sh;
```

**Install the required packages for the deployment using `pip3`**

```
pip3 install -r requirements.txt
```

**Now we can continue.**

---


# Generate Ed25519 Private Keys

*These are used to allow the server to encode information into tokens used for user registration and forgot password email requests.*

**Generate Keys, `chmod` (read-only) them, then move them to the `../secrets_jobs` folder.**

```
cd ed25519;
python3 generate_key.py
chmod 400 EdDSA_private.pem EdDSA_public.pem;
mv EdDSA_private.pem ../secrets_jobs;
mv EdDSA_public.pem ../secrets_jobs;
```

**Also set the correct permissions for these key files so that only the `jobs` user can read them.**

---

# **Seeding the Database**


**Replace the PYTHONPATH=/directory/ with your deployment directory, and the 2nd part as well to the correct paths where the seeds/<Database Name>/.py files are located**



### **MongoDB**

**Upload the LICENSE file to the MongoDB Server using GridFS**

```
PYTHONPATH=/home/jobs/jobs python3 /home/jobs/jobs/seeds/mongodb/cache_fs.py
```


**The command output should show**

```
Database seeded successfully!
```

---


### **MariaDB**

```
PYTHONPATH=/home/jobs/jobs python3 /home/jobs/jobs/seeds/mariadb/api_list_feeds.py  
PYTHONPATH=/home/jobs/jobs python3 /home/jobs/jobs/seeds/mariadb/mongo_storage.py  
PYTHONPATH=/home/jobs/jobs python3 /home/jobs/jobs/seeds/mariadb/mongo_scrape_storage.py  
PYTHONPATH=/home/jobs/jobs python3 /home/jobs/jobs/seeds/mariadb/scrape_rate_limit.py  
PYTHONPATH=/home/jobs/jobs python3 /home/jobs/jobs/seeds/mariadb/proxies.py  
PYTHONPATH=/home/jobs/jobs python3 /home/jobs/jobs/seeds/mariadb/resume_text.py  
PYTHONPATH=/home/jobs/jobs python3 /home/jobs/jobs/seeds/mariadb/database_timegraph.py  
  
PYTHONPATH=/home/jobs/jobs python3 /home/jobs/jobs/seeds/mariadb/api_list_url.py  
PYTHONPATH=/home/jobs/jobs python3 /home/jobs/jobs/seeds/mariadb/api_keys.py  
PYTHONPATH=/home/jobs/jobs python3 /home/jobs/jobs/seeds/mariadb/api_endpoints.py  
PYTHONPATH=/home/jobs/jobs python3 /home/jobs/jobs/seeds/mariadb/api_headers.py  
PYTHONPATH=/home/jobs/jobs python3 /home/jobs/jobs/seeds/mariadb/api_endpoint_headers.py  
PYTHONPATH=/home/jobs/jobs python3 /home/jobs/jobs/seeds/mariadb/api_endpoint_params.py  
PYTHONPATH=/home/jobs/jobs python3 /home/jobs/jobs/seeds/mariadb/api_endpoint_bodies.py  
PYTHONPATH=/home/jobs/jobs python3 /home/jobs/jobs/seeds/mariadb/api_endpoint_extras/api_endpoint_extras.py  
PYTHONPATH=/home/jobs/jobs python3 /home/jobs/jobs/seeds/mariadb/api_endpoint_extras/api_endpoint_extras2.py  
PYTHONPATH=/home/jobs/jobs python3 /home/jobs/jobs/seeds/mariadb/api_endpoint_extras/api_endpoint_extras3.py  
PYTHONPATH=/home/jobs/jobs python3 /home/jobs/jobs/seeds/mariadb/api_endpoint_extras/api_endpoint_extras4.py  
PYTHONPATH=/home/jobs/jobs python3 /home/jobs/jobs/seeds/mariadb/api_endpoint_extras/api_endpoint_extras5.py  
PYTHONPATH=/home/jobs/jobs python3 /home/jobs/jobs/seeds/mariadb/api_endpoint_extras/api_endpoint_extras6.py  
PYTHONPATH=/home/jobs/jobs python3 /home/jobs/jobs/seeds/mariadb/api_endpoint_extras/api_endpoint_extras7.py  
PYTHONPATH=/home/jobs/jobs python3 /home/jobs/jobs/seeds/mariadb/api_endpoint_extras/api_endpoint_extras8.py  
PYTHONPATH=/home/jobs/jobs python3 /home/jobs/jobs/seeds/mariadb/api_endpoint_extras/api_endpoint_extras9.py
```

---


### **PostgreSQL**

**These must be populated in order.**

```
PYTHONPATH=/home/jobs/jobs python3 /home/jobs/jobs/seeds/postgres/regions.py  
PYTHONPATH=/home/jobs/jobs python3 /home/jobs/jobs/seeds/postgres/subregions.py  
PYTHONPATH=/home/jobs/jobs python3 /home/jobs/jobs/seeds/postgres/countries.py
```

**The following seeds can be run simultaneously since there is a lot of data to populate.**
**The server may hang if you run all of them at the same time. I've separated them in proposed batches.**
 
 
 **The Table `states` must be completely populated before `cities`**
 
```
PYTHONPATH=/home/jobs/jobs python3 /home/jobs/jobs/seeds/postgres/states/states.py
```

**These next seed files can be run in any order. Make sure they are not run twice, or you will have duplicate rows.**

```
PYTHONPATH=/home/jobs/jobs python3 /home/jobs/jobs/seeds/postgres/states/states2.py &
PYTHONPATH=/home/jobs/jobs python3 /home/jobs/jobs/seeds/postgres/states/states3.py &
PYTHONPATH=/home/jobs/jobs python3 /home/jobs/jobs/seeds/postgres/states/states4.py &
PYTHONPATH=/home/jobs/jobs python3 /home/jobs/jobs/seeds/postgres/states/states5.py &
PYTHONPATH=/home/jobs/jobs python3 /home/jobs/jobs/seeds/postgres/states/states6.py &
PYTHONPATH=/home/jobs/jobs python3 /home/jobs/jobs/seeds/postgres/states/states7.py &
PYTHONPATH=/home/jobs/jobs python3 /home/jobs/jobs/seeds/postgres/states/states8.py &
PYTHONPATH=/home/jobs/jobs python3 /home/jobs/jobs/seeds/postgres/states/states9.py &
PYTHONPATH=/home/jobs/jobs python3 /home/jobs/jobs/seeds/postgres/states/states10.py &
PYTHONPATH=/home/jobs/jobs python3 /home/jobs/jobs/seeds/postgres/states/states11.py &
PYTHONPATH=/home/jobs/jobs python3 /home/jobs/jobs/seeds/postgres/states/states12.py &
PYTHONPATH=/home/jobs/jobs python3 /home/jobs/jobs/seeds/postgres/states/states13.py &
PYTHONPATH=/home/jobs/jobs python3 /home/jobs/jobs/seeds/postgres/states/states14.py &
PYTHONPATH=/home/jobs/jobs python3 /home/jobs/jobs/seeds/postgres/states/states15.py &
PYTHONPATH=/home/jobs/jobs python3 /home/jobs/jobs/seeds/postgres/states/states16.py &
PYTHONPATH=/home/jobs/jobs python3 /home/jobs/jobs/seeds/postgres/states/states17.py &
PYTHONPATH=/home/jobs/jobs python3 /home/jobs/jobs/seeds/postgres/states/states18.py &
PYTHONPATH=/home/jobs/jobs python3 /home/jobs/jobs/seeds/postgres/states/states19.py &
PYTHONPATH=/home/jobs/jobs python3 /home/jobs/jobs/seeds/postgres/states/states20.py &
PYTHONPATH=/home/jobs/jobs python3 /home/jobs/jobs/seeds/postgres/states/states21.py &
```


**`cities` references `states` Table**

```
PYTHONPATH=/home/jobs/jobs python3 /home/jobs/jobs/seeds/postgres/cities/cities.py
```


**These next seed files can be run in any order. Make sure they are not run twice, or you will have duplicate rows.**

```
PYTHONPATH=/home/jobs/jobs python3 /home/jobs/jobs/seeds/postgres/cities/cities2.py &
PYTHONPATH=/home/jobs/jobs python3 /home/jobs/jobs/seeds/postgres/cities/cities3.py &
PYTHONPATH=/home/jobs/jobs python3 /home/jobs/jobs/seeds/postgres/cities/cities4.py &
PYTHONPATH=/home/jobs/jobs python3 /home/jobs/jobs/seeds/postgres/cities/cities5.py &
PYTHONPATH=/home/jobs/jobs python3 /home/jobs/jobs/seeds/postgres/cities/cities6.py &
PYTHONPATH=/home/jobs/jobs python3 /home/jobs/jobs/seeds/postgres/cities/cities7.py &
PYTHONPATH=/home/jobs/jobs python3 /home/jobs/jobs/seeds/postgres/cities/cities8.py &
PYTHONPATH=/home/jobs/jobs python3 /home/jobs/jobs/seeds/postgres/cities/cities9.py &

PYTHONPATH=/home/jobs/jobs python3 /home/jobs/jobs/seeds/postgres/cities/cities10.py &
PYTHONPATH=/home/jobs/jobs python3 /home/jobs/jobs/seeds/postgres/cities/cities11.py &
PYTHONPATH=/home/jobs/jobs python3 /home/jobs/jobs/seeds/postgres/cities/cities12.py &
PYTHONPATH=/home/jobs/jobs python3 /home/jobs/jobs/seeds/postgres/cities/cities13.py &
PYTHONPATH=/home/jobs/jobs python3 /home/jobs/jobs/seeds/postgres/cities/cities14.py &
PYTHONPATH=/home/jobs/jobs python3 /home/jobs/jobs/seeds/postgres/cities/cities15.py &
PYTHONPATH=/home/jobs/jobs python3 /home/jobs/jobs/seeds/postgres/cities/cities16.py &
PYTHONPATH=/home/jobs/jobs python3 /home/jobs/jobs/seeds/postgres/cities/cities17.py &

PYTHONPATH=/home/jobs/jobs python3 /home/jobs/jobs/seeds/postgres/cities/cities18.py &
PYTHONPATH=/home/jobs/jobs python3 /home/jobs/jobs/seeds/postgres/cities/cities19.py &
PYTHONPATH=/home/jobs/jobs python3 /home/jobs/jobs/seeds/postgres/cities/cities20.py &
PYTHONPATH=/home/jobs/jobs python3 /home/jobs/jobs/seeds/postgres/cities/cities21.py &
PYTHONPATH=/home/jobs/jobs python3 /home/jobs/jobs/seeds/postgres/cities/cities22.py &
PYTHONPATH=/home/jobs/jobs python3 /home/jobs/jobs/seeds/postgres/cities/cities23.py &
PYTHONPATH=/home/jobs/jobs python3 /home/jobs/jobs/seeds/postgres/cities/cities24.py &
PYTHONPATH=/home/jobs/jobs python3 /home/jobs/jobs/seeds/postgres/cities/cities25.py &
PYTHONPATH=/home/jobs/jobs python3 /home/jobs/jobs/seeds/postgres/cities/cities26.py &

PYTHONPATH=/home/jobs/jobs python3 /home/jobs/jobs/seeds/postgres/cities/cities27.py &
PYTHONPATH=/home/jobs/jobs python3 /home/jobs/jobs/seeds/postgres/cities/cities28.py &
PYTHONPATH=/home/jobs/jobs python3 /home/jobs/jobs/seeds/postgres/cities/cities29.py &
PYTHONPATH=/home/jobs/jobs python3 /home/jobs/jobs/seeds/postgres/cities/cities30.py &
PYTHONPATH=/home/jobs/jobs python3 /home/jobs/jobs/seeds/postgres/cities/cities31.py &
PYTHONPATH=/home/jobs/jobs python3 /home/jobs/jobs/seeds/postgres/cities/cities32.py &
PYTHONPATH=/home/jobs/jobs python3 /home/jobs/jobs/seeds/postgres/cities/cities33.py &
PYTHONPATH=/home/jobs/jobs python3 /home/jobs/jobs/seeds/postgres/cities/cities34.py &

PYTHONPATH=/home/jobs/jobs python3 /home/jobs/jobs/seeds/postgres/cities/cities35.py &
PYTHONPATH=/home/jobs/jobs python3 /home/jobs/jobs/seeds/postgres/cities/cities36.py &
PYTHONPATH=/home/jobs/jobs python3 /home/jobs/jobs/seeds/postgres/cities/cities37.py &
PYTHONPATH=/home/jobs/jobs python3 /home/jobs/jobs/seeds/postgres/cities/cities37.py &
PYTHONPATH=/home/jobs/jobs python3 /home/jobs/jobs/seeds/postgres/cities/cities38.py &
```


### **Seed the Extra Tables**

**X**

```
PYTHONPATH=/home/jobs/jobs python3 /home/jobs/jobs/seeds/postgres/x_location_ids.py
```

**Glassdoor Locations**

```
PYTHONPATH=/home/jobs/jobs python3 /home/jobs/jobs/seeds/postgres/glassdoor_location_id.py
```

**LinkedIn GeoURNs**

```
PYTHONPATH=/home/jobs/jobs python3 /home/jobs/jobs/seeds/postgres/linkedin_geourns.py
```

---


### **Users Database**

```
PYTHONPATH=/home/jobs/jobs python3 /home/jobs/jobs/seeds/postgres/user.py  
PYTHONPATH=/home/jobs/jobs python3 /home/jobs/jobs/seeds/postgres/profile.py  
PYTHONPATH=/home/jobs/jobs python3 /home/jobs/jobs/seeds/postgres/survey.py  
PYTHONPATH=/home/jobs/jobs python3 /home/jobs/jobs/seeds/postgres/resume.py  
PYTHONPATH=/home/jobs/jobs python3 /home/jobs/jobs/seeds/postgres/listed_job.py  
PYTHONPATH=/home/jobs/jobs python3 /home/jobs/jobs/seeds/postgres/experience_level.py  
PYTHONPATH=/home/jobs/jobs python3 /home/jobs/jobs/seeds/postgres/api_source.py  
PYTHONPATH=/home/jobs/jobs python3 /home/jobs/jobs/seeds/postgres/company.py  
PYTHONPATH=/home/jobs/jobs python3 /home/jobs/jobs/seeds/postgres/location.py  
PYTHONPATH=/home/jobs/jobs python3 /home/jobs/jobs/seeds/postgres/job_type.py  
PYTHONPATH=/home/jobs/jobs python3 /home/jobs/jobs/seeds/postgres/survey_location.py  
PYTHONPATH=/home/jobs/jobs python3 /home/jobs/jobs/seeds/postgres/survey_job_type.py  
PYTHONPATH=/home/jobs/jobs python3 /home/jobs/jobs/seeds/postgres/survey_experience_level.py  
PYTHONPATH=/home/jobs/jobs python3 /home/jobs/jobs/seeds/postgres/listed_job_location.py  
PYTHONPATH=/home/jobs/jobs python3 /home/jobs/jobs/seeds/postgres/listed_job_job_type.py  
PYTHONPATH=/home/jobs/jobs python3 /home/jobs/jobs/seeds/postgres/listed_job_experience_level.py  
PYTHONPATH=/home/jobs/jobs python3 /home/jobs/jobs/seeds/postgres/saved_job.py  
PYTHONPATH=/home/jobs/jobs python3 /home/jobs/jobs/seeds/postgres/saved_company.py
```

---

### The Database should be ready now!


*For Testing,* **Insert the test admin user with this query on the PostgreSQL server.**

**Open a PostgreSQL Shell**

```
psql -U jobs;
```


**Execute the Query**

```
INSERT INTO "public"."users" ("username", "email", "encrypted_password") VALUES ('TestAdministrator', 'test@admin.com', '$2y$10$yAvqUG9gA4Yn9QLggFYpP.noNJNDuBI5uq89bdJ5KwctF/0528nm2');
```

**The test username is: `TestAdministrator` with password `TESTADMINPASSWORDzzzzzz`**

**Update the `credentials.py` in `secrets_jobs`**

```
admin_list = ["TestAdministrator"]
```

**Before we can run our server, double-check the `app/__init__.py` file.**

```
nano app/__init__.py
```

**Make adjustments pertaining to cookies if required, and review the settings depending on your environment. Save the file.**



**Test the deployment by using the Flask Development Server**

```
PYTHONPATH=/home/jobs/jobs python3 /home/jobs/jobs/run.py
```

**Login**

### **Access the Administrator Dashboard**

```
http://site_url:5000/admin
```


If it works, you should see a page like this.

![Image](admin_dashboard_page.png)

*Database Routines, Statistics, and Cached Queries have not been implemented yet, and only the initial templates and design have been generated for Database Routines.*


### **API Endpoints Page**

![Image](api_endpoints_page.png)


The Admin page's manual query endpoint does not populate any extra endpoints past the API selection unless there is an available API key.

It looks like this, with a selection of API, and all enabled endpoints, along with extra documentation and description for each. 

Currently there are over 200 endpoints from over two dozen API's.

Additionally, Automatic API Key selection allows the rotation of multiple API keys using the preferred proxy listed in `credentials.py`


### **Manual Query Page**

![Image](manual_query_page.png)


### **Mongo Storage Page**

![Image](mongo_storage_filters.png)

The filters look like this, and there are two filters which can give you proper results for queries.
Each endpoint is classified properly in the seeds file, and allows easy searching, as well an option to test parsing for data returned by a specific API. See the `routines/parsing` folder for the organization.

**The data can be checked against new parsing updates through the controls button menu**

![Image](mongo_storage_menu_links.png)


The browser will give you a raw look into how the data is parsed, then processed throughout the `process_jobs.py` file in the `routines` folder

This is not a complete break-down of the entire administrator dashboard, but it immensely helps with parsing techniques and makes normalizing data much more efficient.

---

### **Database Routines**


**Currently there are quite a few database routines:**

1. **Process Queries**
	- Parses data from MariaDB's `MongoStorage` and saves the response into MongoDB.

2. **Process Jobs**
	- Parses data from MongoDB and MariaDB's `MongoStorage` Table to generate `ListedJobs` and `Companies`.

3. **Process Companies**
	- Parses data from MongoDB and MariaDB's `MongoStorage` Table to generate Companies and Company Data.

4. **Check Expired Jobs**
	- Parses data from the `ListedJob` and `Company` Tables. Additionally, updates the company count in order to generate properly paginated pages.

5. **Time-graph Generation (For homepage statistics)**
	- Parses data from MongoDB, while referencing `MongoStorage` and pulling queries based on query time as a stand-alone.

6. **Passive Scraper**
	- Also a stand-alone routine, does not rely on any other tables. Parses data from MongoDB and pulls apply links from saved queries. Generates extremely safe rate limits for each unique domain and prevents multiple requests from a single proxy when scraping. Data is stored in the `ScrapeRateLimit` per Residential Proxy enabled, and runs a Chromium browser in a virtual display to load the website's JavaScript in order to scrape the page with a high success rate. The text data is then stored in MongoDB for easy retrieval and object ID is stored in the `MongoScrapeStorage` Table on MariaDB.



The individual files can be found in the `routines` folder, and certain routines have their own respective `handler` which may use checkpoints in time, so that the back-end processes can continue to run without starting from earliest data.


1. **Process Queries**

```
PYTHONPATH=/home/jobs/jobs python3 /home/jobs/jobs/routines/process_queries.py
```


2. **Process Jobs**

```
PYTHONPATH=/home/jobs/jobs python3 /home/jobs/jobs/routines/process_jobs.py
```


3. **Process Companies**

```
PYTHONPATH=/home/jobs/jobs python3 /home/jobs/jobs/routines/process_companies.py
```


4. **Scraper**

```
PYTHONPATH=/home/jobs/jobs python3 /home/jobs/jobs/routines/process_scrape.py
```


5. **Update Expired Job Count (For Companies)**

```
PYTHONPATH=/home/jobs/jobs python3 /home/jobs/jobs/routines/update_expired_job_count.py
```


6. **Generate Time-graph (For Homepage)**

```
PYTHONPATH=/home/jobs/jobs python3 /home/jobs/jobs/routines/generate_timegraph_jobs.py
```

---

### Other Commands


**Running Production**

```
PYTHONPATH=/home/jobs/jobs gunicorn -c gunicorn.conf.py
```


**Viewing Access and Error Logs**

```
tail -f /home/jobs/gunicorn_error.log  
tail -f /home/jobs/gunicorn_access.log
```

---


More features have been planned, and other implementations are currently still in progress.
