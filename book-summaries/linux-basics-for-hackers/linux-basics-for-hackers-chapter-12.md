**SUMMARY OF**
**LINUX BASICS FOR HACKERS**
*(FIRST EDITION) BY OCCUPYTHEWEB*

---

# CHAPTER 12: USING AND ABUSING SERVICES

---

## Starting, Stopping, and Restarting Services

* Manage background daemons with:

  ```bash
  service <name> start|stop|restart
  ```
* Example:

  ```bash
  service apache2 start
  service apache2 stop
  service apache2 restart
  ```

## Creating an HTTP Web Server with Apache

### Starting with Apache

* Installed by default on Kali; otherwise:

  ```bash
  apt-get install apache2
  ```
* Start service or via GUI (Applications » Services » HTTPD).

### Editing the `index.html` File

* Default page at `/var/www/html/index.html`.
* Open and modify with your HTML.

### Adding Some HTML

* Example minimal page:

  ```html
  <html>
    <body>
      <h1>Hackers-Arise Is the Best!</h1>
      <p>If you want to learn hacking, Hackers-Arise.com</p>
      <p>is the best place to learn hacking!</p>
    </body>
  </html>
  ```

### Seeing What Happens

* Browse to `http://localhost/` to view your custom page.

## OpenSSH and the Raspberry Spy Pi

### Setting Up the Raspberry Pi

* Install Raspbian, enable SSH in `raspi-config` (Interfaces → SSH).
* Attach camera module, power on.

### Building the Raspberry Spy Pi

* From Kali:

  ```bash
  service ssh start
  ssh pi@<Pi_IP>
  ```
* Default credentials: `pi` / `raspberry`.

### Configuring the Camera

* On Pi:

  ```bash
  sudo raspi-config    # Enable Camera → Reboot
  ```

### Starting to Spy

* Use `raspistill` to capture images:

  ```bash
  raspistill -v -o firstpicture.jpg
  ls firstpicture.jpg
  ```

## Extracting Information from MySQL/MariaDB

### Starting MySQL or MariaDB

* Start service:

  ```bash
  service mysql start
  ```
* Log in as root (no password by default):

  ```bash
  mysql -u root -p
  ```

### Interacting with SQL

* Core commands: `SELECT`, `INSERT`, `UPDATE`, `DELETE`, etc.

### Setting a Password

* View users:

  ```sql
  SELECT user, host, password FROM mysql.user;
  ```
* Change root password:

  ```sql
  USE mysql;
  UPDATE user SET password=PASSWORD('hackers-arise') WHERE user='root';
  FLUSH PRIVILEGES;
  ```

### Accessing a Remote Database

* Connect to remote host:

  ```bash
  mysql -u root -p 192.168.1.101
  ```

### Connecting to a Database

* Show and select DB:

  ```sql
  SHOW DATABASES;
  USE creditcardnumbers;
  ```

### Database Tables

* List tables:

  ```sql
  SHOW TABLES;
  ```

### Examining the Data

* Describe table:

  ```sql
  DESCRIBE cardnumbers;
  ```
* Dump all rows:

  ```sql
  SELECT * FROM cardnumbers;
  ```

### PostgreSQL with Metasploit

* Install/start Postgres:

  ```bash
  service postgresql start
  msfdb init
  ```
* Create msf\_user and DB:

  ```bash
  su postgres
  createuser msf_user -P
  createdb --owner=msf_user hackers_arise_db
  exit
  ```
* Connect msfconsole → DB:

  ```bash
  db_connect msf_user:password@127.0.0.1/hackers_arise_db
  db_status
  ```

---

## Summary

Linux services run in the background to provide functionality. You mastered service control, deployed Apache for web hosting, used OpenSSH with a Raspberry Pi camera for remote spying, extracted data from MySQL databases, and integrated PostgreSQL with Metasploit—essential skills for both attackers and defenders.

## Exercises

1. Start `apache2` via CLI.
2. Create a simple site in `index.html`.
3. Start SSH service; SSH into Kali from another LAN host.
4. Start MySQL, set root password to `hackers-arise`, and switch to `mysql` DB.
5. Start PostgreSQL; configure it for Metasploit as shown.

---

## Summary author: **Jeremy Ray Jewell**

[GitHub](https://github.com/jeremyrayjewell)
[LinkedIn](https://www.linkedin.com/in/jeremyrayjewell)
