# Trace Inventory Exporter

This Python script exports your consigned sneaker inventory from **Trace** (a sneaker consignment software platform) into a local CSV file. It authenticates with Trace’s Firebase backend, retrieves the latest inventory, and saves it with a timestamp for reporting or record-keeping.

---

## Features

- Secure login using your Trace credentials
- Supports multiple sneaker consignment stores
- Exports inventory with fields: `status`, `title`, `size`, `price`
- Automatically generates timestamped CSV files
- Output stored in a `History/` folder

---

## Setup Instructions

### 1. Clone the Repository and Install Requirements

First, make sure you have Python 3.7 or later installed. Then run:

```bash
pip install -r requirements.txt
```

### 2. Create a `config.json` File

In the same directory as the script, create a file named `config.json` with your Trace credentials:

```json
{
  "email": "your_email_here",
  "password": "your_password_here"
}
```

### 3. Create the Output Directory

Make a folder to store your CSV exports:

```bash
mkdir History
```

---

## Running the Script

Execute the script from your terminal:

```bash
python main.py
```

You’ll be prompted to select the store whose inventory you want to export. The resulting CSV will be saved in the `History/` folder with a name like:

```
543-kickitnz.com-inventory-2025-07-28.csv
```

---

## Supported Stores

- imyourwardrobe.com  (consign.imyourwardrobe.com)
- cjkicksnz.com  (consign.cjkicksnz.com)
- kickitnz.com  (consign.kickitnz.com)
- basement.nz  (consign.basement.nz)
- priorstoreofficial.com  (sell.priorstoreofficial.com)
- bigboisneakers.com  (consign.bigboisneakers.com)

---

## Requirements

The script requires the following Python packages:

- `requests`
- `json` (built-in)
- `csv` (built-in)

These are listed in the `requirements.txt` file:

```text
requests
```

---

## Notes

- This script uses your Trace email and password to authenticate and retrieve an access token via Firebase.
- The API key used for authentication is specific to Trace and publicly accessible.
- You must have an active consigner account in Trace to retrieve inventory.
- All data is saved locally and is not transmitted elsewhere.

---

## Disclaimer

This script is provided “as is” without warranty or guarantee. It is intended for personal or internal business use only. Use responsibly and in accordance with Trace’s Terms of Service.
