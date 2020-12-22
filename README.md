# saol-wordlist

I needed a Swedish wordlist and noticed that the data file for the SAOL Android app (v.2.0.8.3) was an unencrypted SQLite database, so I wrote a simple script for extracting the words from it.

The script outputs words from SAOL 14 to a text file in all upper-case separated with a newline. The wordlist created by using this script is available in `./output/`.

## Installation

While there is no specific Python package to install to run the script, one needs the `.obb`-file (data file) from the SAOL Android app to run this script.

I guess the simplest way to obtain the data file would be to have an Android phone, but one could emulate an Android phone on the computer and install SAOL...

On one's Android phone, the `.obb`-file can be found in `<shared-storage>/Android/obb/se.svenskaakademien.saol/main.**.se.svenskaakademien.saol.obb` where \*\* is a two digit number depending on the package version.

## Usage

To run this script, one needs to know the path to the copied `.obb`-file for SAOL. The script writes the wordlist to `./output/saol_wordlist.txt`.

Example usage:

```bash
# Given that the path to the data file is ./main.27.se.svenskaakademien.saol.obb
python main.py ./main.27.se.svenskaakademien.saol.obb
```

## Miscellaneous

I excluded prefixes and suffixes available in the database since I wanted only words in my wordlist. Change the query in `main.py` if one wants to include them or such.
