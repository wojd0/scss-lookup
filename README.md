# scss-lookup
Looks up scss variable references in a directory

## Usage
1. Create .env with this structure:
   ```env
   # absolute root path of the project
   ROOT_DIR=""
   # file extension to look for
   EXTENSION="scss"
   # if a variable occurs this amount of times in the entire project, don't log its name
   SKIP_AMOUNT=2
   ```
2. Create varlist.txt file and paste variable names into it (one per line). For speed, a line can have other characters in it.
3. Run using python3