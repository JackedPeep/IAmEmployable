
function patternTrue(sequence) {
  const pattern = /AL[A,V,L,I,M,P,F,Y,W,S,T,N,C,H,Q,G]{3}LW/g;
  
  if (sequence === pattern) {
    return true;
  } else {
    return false;
  }
}

// Function to calculate the average hydrophobicity for a given sequence of amino acids
function calculateHydrophobicity(subsequence) {
  let total = 0;
  for (let i = 0; i < subsequence.length; i++) {
      total += amino_acids_hydrophobicity[subsequence[i]];
  }
  return total / subsequence.length;
}

// Function that determines if hydrophobicity is over the threashold
function overHydrophobicityThresholdTrue(subsequence, threashold) {
  if (calculateHydrophobicity(subsequence) >== threashold) {
    return true;
  } else {
    return false;
  }
  
}

// Function to add HTML tags if pattern is found
function markPattern(sequence) {
  if (patternTrue(sequence)) {
    return '<mark class="pattern">' + sequence + '</mark>';
  } else {
    return sequence;
  }
}

// Function to add HTML tags if hydrophobicity is over the threshold
function markHighHydrophobicity(sequence, threshold) {
  if (overHydrophobicityThresholdTrue(sequence, threshold)) {
    return '<mark class="high-hydrophobicity">' + sequence + '</mark>';
  } else {
    return sequence;
  }
}



// Define the amino acids and their hydrophobicity scores
let amino_acids_hydrophobicity = {
  'A': 1.800,  // Alanine
  'R': -4.500, // Arginine
  'N': -3.500, // Asparagine
  'D': -3.500, // Aspartic Acid
  'C': 2.500,  // Cysteine
  'Q': -3.500, // Glutamine
  'E': -3.500, // Glutamic Acid
  'G': -0.400, // Glycine
  'H': -3.200, // Histidine
  'I': 4.500,  // Isoleucine
  'L': 3.800,  // Leucine
  'K': -3.900, // Lysine
  'M': 1.900,  // Methionine
  'F': 2.800,  // Phenylalanine
  'P': -1.600, // Proline
  'S': -0.800, // Serine
  'T': -0.700, // Threonine
  'W': -0.900, // Tryptophan
  'Y': -1.300, // Tyrosine
  'V': 4.200   // Valine
};


// Defined window size
let window_size = 19;

// Get the protein sequence
let sequence = getSequence(); // You need to define this function

// Main function
function main() {
  // Calculate the hydrophobicity for each amino acid in the sequence
  for (let i = 0; i < sequence.length; i++) {
      // Adjust the window size for the first few amino acids
      let subsequence;
      if (i < window_size / 2) {
          subsequence = sequence.slice(0, i + window_size / 2 + 1);
      } else {
          subsequence = sequence.slice(i - window_size / 2, i + window_size / 2 + 1);
      }
      
      let hydrophobicity = calculateHydrophobicity(subsequence);
      console.log('Hydrophobicity for amino acid ' + (i+1) + ': ' + hydrophobicity);
  }
}