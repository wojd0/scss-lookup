# scss-lookup
Looks up scss variable references in a directory

## Usage
1. Create .env with this structure:
   ```env
   # absolute root path of the project
   ROOT_DIR=""

   # file extension to look for
   EXTENSION="scss"

   # don't log if the variable occurs exactly this many times
   SKIP_AMOUNT=2

   # don't log if the variable occurs more than this many times
   MAX_AMOUNT=2
   ```
2. Create varlist.txt file and paste changed lines from your scss file.
3. Run 
   ```
   pip3 install -r requirements.txt
   ```
4. Start loop.sh or lookup.py using python3