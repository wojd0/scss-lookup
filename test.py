import re

string = '--studio-process-category-selector-input-label-error-color: $studio-text-input-label-error-color,--studio-process-category-selector-input-label-error-color: $studio-text-input-label-error-color,'
expression = r'--[a-z-]+'

print(re.findall(expression, string))
print(re.match(expression, ''))