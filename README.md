# CNIC Eligibility Checker

A small desktop app that tells a person whether they are old enough to apply for a Pakistani CNIC (national identity card). It is a beginner `tkinter` GUI project. It is not an official NADRA tool.

## How it works

1. Enter your name and age.
2. Press **Generate Message** (or hit Enter in the age box).
3. The app shows whether you are eligible (age 18 or older), or how many years remain.

The form clears itself a few seconds after each result so the next person can use it.

## Run it

Requires Python 3.8+. `tkinter` is included with the standard Python installers and no other packages are needed.

```bash
git clone https://github.com/Hammad-Ahmed-hk/CNIC-eligibility.git
cd CNIC-eligibility
python cnic_eligibility_checker.py
```

## Privacy

The app does not save or send the name or age that you enter. Earlier versions wrote entries to a text file; that behavior has been removed.

## Possible improvements

- Support the real eligibility rules (for example, the age at which a first CNIC is issued)
- Unit tests for the age logic, separated from the GUI code

## Author

Hammad Ahmed, [@Hammad-Ahmed-hk](https://github.com/Hammad-Ahmed-hk)
