                                 Project Overview


This project shows the use of regular expressions (regex) to extract structured data from realistic raw text input. The program simulates a real-world scenario where text is returned from an external API and must be processed safely and accurately.
The focus of this project is on:

  -Data extraction using regex
  -Handling real-world formatting variations
  -Demonstrating security awareness when processing untrusted input


      The program is implemented using python.
 
                                     
                                  Data Types Extracted

  The program extracts the following data types from the input text:
    -Email Addresses
    -URLs
    -Phone Numbers
    -Credit card
                                   Input Design

The input is stored in a text file (raw-text.txt) and is designed to resemble real-world data, including:

    - Normal sentences and structured text paragraphs
    - Mixed valid and invalid data patterns
    -Multiple formatting variations (such as varied spacing or delimiters)
    -Structural noise and irrelevant background text
    -Malicious input anomalies such as code tags or database command strings

This approach reflects how unstructured text data is commonly received from external APIs or log streams in production environments.

                     Regex Patterns Used (Explanation)

                        ALU Email Regex
Matches valid educational prefixes alongside the three institutional domains specified by the university.
Utilizes explicit word boundaries to reject partial, clipped, or malformed email structures.

                         URL Regex
Matches both secure (https) and unsecure (http) website structures.
Stops matching before trailing punctuation (like periods or commas at the end of a sentence) to avoid false positives.

                          Phone Number Regex
Handles a dynamic country code prefix (+250 or 0) followed by standard digit sequences.
Tolerates variations in human formatting, including voluntary spacing and hyphens.

                         Credit Card Regex
Captures standard 16-digit financial groupings across the raw data field.
Identifies blocks whether they are written continuously or separated by layout spaces and dashes.
Each regex pattern is documented and commented directly within the source code file for clarity.

                         Security Considerations
This project demonstrates awareness that not all input is trustworthy:

 -Script tags (<script>...</script>) are removed before processing to prevent malicious injection.
 -Only well-formed patterns are extracted; malformed data is ignored.
 -Sensitive data such as credit card addresses is partially masked in the output to reduce unnecessary exposure


                                     Output
The extracted data is:
 -Structured into categories
 -Saved automatically into a JSON file (sample_output.json)
 -Printed to the console for verification
 -This makes the output easy to read, store, and reuse.


