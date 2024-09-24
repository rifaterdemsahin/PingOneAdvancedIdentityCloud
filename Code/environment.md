To install Python on a RHEL (Red Hat Enterprise Linux) system, you can follow these steps. RHEL typically comes with Python pre-installed, but if you need to install a specific version or if it's not installed, here's how you can do it:

### 1. **Update your system**
First, it's always good practice to update your system before installing new packages. Open a terminal and run:

```bash
sudo yum update
```
![image](https://github.com/user-attachments/assets/45e631b7-a3fd-4a85-a5ab-b4821d6639ae)

### 2. **Enable the EPEL repository (if needed)**
RHEL may not have some packages in its default repositories, so it's a good idea to enable the Extra Packages for Enterprise Linux (EPEL) repository. To do this, run:

```bash
sudo yum install epel-release
```

### 3. **Install Python**
Depending on which version of Python you want to install, follow the appropriate steps below.
![image](https://github.com/user-attachments/assets/c3887e34-c67e-4d3a-9929-8d7d56c0b3e2)

#### For Python 3.8 or newer:
Red Hat provides Python through its AppStream repository. You can install Python 3.8 or newer with:

```bash
sudo yum install python3
```

#### For a specific version of Python:
If you need a specific version, you can use the `dnf` module command, available in newer versions of RHEL:

```bash
sudo yum module list python38
```

Then, to install Python 3.8 for example:

```bash
sudo yum module install python38
```

### 4. **Verify Installation**
Check if Python is installed correctly by running:

```bash
python3 --version
```

### 5. **Set Python 3 as default (optional)**
If you want Python 3 to be the default version when you type `python`, you can create an alias:

```bash
sudo alternatives --set python /usr/bin/python3
```

That’s it! You should now have Python installed on your RHEL system.
