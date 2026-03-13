# File_Locker

# 🔐 PY_SCAN File Security

A simple file security tool developed with **Python and Batch (.bat)** that allows users to **encrypt and decrypt files using a password**.
This project demonstrates how basic file protection systems work and how encryption logic can be implemented using Python.

---

# 📌 Features

* 🔑 Password-based file encryption
* 🔓 Secure file decryption
* 📂 Works with any file type
* ⚡ Simple command line usage
* 🛡 Uses **AES-based encryption via Fernet**
* 💻 Compatible with Windows (.bat support)

---

# 🛠 Technologies Used

* Python 3
* Batch Script (.bat)
* Cryptography Library

---

# 📦 Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/PY_SCAN.git
cd PY_SCAN
```

Install required dependency:

```bash
pip install cryptography
```

---

# 🚀 Usage

### 🔒 Encrypt a file

```bash
python setup.py lock <file> <password>
```

Example:

```bash
python setup.py lock secret.txt 12345
```

Output:

```
secret.txt.locked
```

The original file will be removed and replaced with the encrypted version.

---

### 🔓 Decrypt a file

```bash
python setup.py unlock <file.locked> <password>
```

Example:

```bash
python setup.py unlock secret.txt.locked 12345
```

The encrypted file will be restored to its original format.

---

# 📂 Project Structure

```
PY_SCAN
│
├── setup.py
├── lock.bat
├── unlock.bat
└── README.md
```

---

# ⚠️ Warning

This project is created **for educational purposes** to demonstrate file encryption concepts.
Do not rely on it for highly sensitive data without further security improvements.

---

# 🔮 Future Improvements

* GUI interface (Tkinter or PyQt)
* Folder encryption
* Brute-force protection
* EXE distribution
* Multi-file encryption support

---

# 👨‍💻 Author

Developed as a learning project to explore **file security and encryption techniques using Python**.
