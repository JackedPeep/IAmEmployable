# <tt>Software Development Plan</tt>

## Phase 0: Requirements Specification 

This project involves the development of a graphical user interface (GUI) application for protein sequence analysis. The application will take an amino acid sequence as input from the user and identify specific patterns within the sequence. For each identified pattern, the application will perform a Doolittle hydrophobicity calculation with a sliding window of 19, targeting transmembrane or embedded amino acids.

The requirements of the project are as follows:

- The application should accept user input of an amino acid sequence. 
- The application should identify specific patterns within the input sequence.
- For each identified pattern, the application should perform a Doolittle hydrophobicity calculation with a sliding window of 19.
- The application should return a Doolittle hydrophobicity plot.
- The application should return the original sequence with the search patterns and high hydrophobic amino acids highlighted in distinctive ways.
- The application should return a predicted hydrophobicity plot.
- The application should provide an option to export the information from the database as an Excel file.

To create a well-designed project, it will be necessary to learn about protein sequence analysis, Doolittle hydrophobicity calculations, GUI development, and data visualization. Familiarity with a programming language that supports these tasks, such as Python, will also be required.

## Phase 1: System Analysis 

The big picture programming items for this project could include the following:

1. **Protein Sequence Input Module**: This module will handle user input of the amino acid sequence. It will need to validate the input to ensure it is a valid amino acid sequence.

2. **Pattern Identification Module**: This module will analyze the input sequence and identify specific patterns within it. The output will be the locations of these



## Phase 2: Design 

TODO: the psudo code for your project goes here. Write it as clearly as you can so that others might be able to understand it.

### Define the amino acids and the pattern
amino_acids_hydrophobicity = {
    'A': 1.8,  # Alanine
    'V': 4.2,  # Valine
    'L': 3.8,  # Leucine
    'I': 4.5,  # Isoleucine
    'M': 1.9,  # Methionine
    'P': -1.6, # Proline
    'F': 2.8,  # Phenylalanine
    'Y': -1.3, # Tyrosine
    'W': -0.9, # Tryptophan
    'S': -0.8, # Serine
    'T': -0.7, # Threonine
    'N': -3.5, # Asparagine
    'C': 2.5,  # Cysteine
    'H': -3.2, # Histidine
    'Q': -3.5, # Glutamine
    'G': -0.4  # Glycine
}
pattern_start = 'AL'
pattern_end = 'LW'

### Define the high hydrophobicity window
window_size = 19
threshold = 1.6

### HTML form to get the accession number or protein sequence from the user
def get_input():
    # If the input is an accession number, fetch the protein sequence from NCBI
    # Else, use the input as the protein sequence
    pass

### Function to find all patterns in the sequence
def find_patterns(sequence, pattern_start, pattern_end):
    # pattern_array = []
    # pattern = ""
    # current_char = i
    # next_char = [i + 1]
    # for each char in sequence 
    # If "current_char + next_char" = pattern_start 
      # While "current_char + next_char" != pattern_end
        # pattern += current_char
      # patern += pattern_end
      # pattern_array += pattern
    
    
    pass

### Function to check the hydrophobicity of a window in the sequence
def check_hydrophobicity(sequence, window_size, threshold):
    # Calculate the Kyte-Doolittle Score for each window in the sequence
    # If the score is above the threshold, return True
    pass

### Main function
def main():
    # Get the input from the user
    sequence = get_input()

    # Find all patterns in the sequence
    patterns = find_patterns(sequence, pattern_start, pattern_end)

    # For each pattern, check the hydrophobicity of the window it is in
    for pattern in patterns:
        if check_hydrophobicity(sequence, window_size, threshold):
            print(pattern)

## Phase 3: Implementation 

TODO: Write encountered problems you ran into while implementing your code, and what parts of your code seem to be the weakest.

## Phase 4: Testing & Debugging 

TODO: After debugging your code write the method names for any tests run and what they test for.

## Phase 5: Deployment 

TODO: Wait for bug reports and continue to phase 6.

## Phase 6: Maintenance

TODO: Record all bug fixes to git and as they come. Be nice to the people reporting them.