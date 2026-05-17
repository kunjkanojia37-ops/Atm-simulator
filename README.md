# Object-Oriented ATM Simulator System

A clean, terminal-based banking ATM simulator engineered in Python using Object-Oriented Programming (OOP) concepts. The application models realistic banking security, transactional accounting rules, dynamic balance state manipulation, and automated input validation wrappers.

## 🔑 Core Features

*   **Secure Authentication Simulation:** Multi-account mapping logic verifying input credentials against structural storage dictionaries (`carddic` / `balance_check`).
*   **Transactional Accounting:** 
    *   **Balance Queries:** Reads current card state memory configurations cleanly.
    *   **Withdrawal Bounds Checking:** Hard verification validation checking for account overdraft conditions, positive integers, and standardized denomination rules (multiples of 100).
    *   **Validated Deposits:** Real-time balance updates wrapped around custom business transaction limits (capped at Rs. 100,000 per transaction).
*   **Security Protocol Management:** Multi-step credential validation processing to rewrite account codes with digit length restrictions (6-digit PIN enforcement).
*   **Robust Exception Handling:** Full `ValueError` wrapping to insulate operations against runtime script crashes from garbage input or non-numeric entries.

---

## 📁 Database Preview (Mock States)

The simulation boots up pre-configured with two active testing card profiles:

| Card Number | Initial PIN | Default Balance (INR) |
| :--- | :--- | :--- |
| `65261645` | `18122006` | Rs. 1,000,000 |
| `12345678` | `123456` | Rs. 50,000 |

---

## 🛠️ Installation & Execution

### Prerequisites
*   Python 3.9+ environment installed on your host machine.

### Execution Instructions
1. Clone this repository or download the source code locally.
2. Open your standard command line or VS Code terminal inside the project directory.
3. Launch the simulator interface by executing the Python file directly:

```bash
python main.py
