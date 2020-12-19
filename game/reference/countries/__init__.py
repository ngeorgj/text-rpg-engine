from . import (
    London,
    Ireland,
    # Import your countries here
)

# Add the imports here
imports = [London,
           Ireland]

# Auto Select
available_countries = [c for c in imports if c.available]