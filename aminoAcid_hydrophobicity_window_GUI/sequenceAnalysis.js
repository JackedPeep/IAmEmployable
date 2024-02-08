export {
  calculateHydrophobicity,
  overHydrophobicityThresholdTrue,
  markHighHydrophobicity,
  markPattern,
  addBuffer,
  markPatternsInSequence,
  markAndRecordHydrophobicityInSequence,
  patternTrue,
  analyzeSequence
};


// Get the protein sequence


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
  'V': 4.200,  // Valine
  ' ': 0       // BUFFER VALUE
};


//main loop
function analyzeSequence(sequence, threshold) {
  let markedPatternSequence = markPatternsInSequence(sequence);
  let { markedHydrophobicitySequence, hydrophobicityArray } = markAndRecordHydrophobicityInSequence(sequence, threshold);
  
  return { markedPatternSequence, markedHydrophobicitySequence, hydrophobicityArray };
}

// HELPER FUNCTIONS

// Helper function to mark patterns in the sequence
function markPatternsInSequence(sequence) {
  let patternWindow = 7;
  let markedPatternSequence = '';
  for (let i = 0; i < sequence.length; i++) {
    let patternSubsequence = sequence.slice(i, i + patternWindow);
    if (patternTrue(patternSubsequence)) {
      markedPatternSequence += markPattern(patternSubsequence);
      i += patternWindow - 1; // Skip the rest of the pattern
    } else {
      markedPatternSequence += sequence[i];
    }
  }
  return markedPatternSequence;
}


// Helper function to mark high hydrophobicity in the sequence and record hydrophobicity values
function markAndRecordHydrophobicityInSequence(sequence, threshold) {
  let hydrophobicityWindow = 19;
  let bufferSequence = addBuffer(sequence);
  let halfWindow = Math.floor(hydrophobicityWindow / 2);
  let markedHydrophobicitySequence = '';
  let hydrophobicityArray = [];
  for (let i = halfWindow; i < bufferSequence.length - halfWindow; i++) {
    let hydrophobicitySubsequence = bufferSequence.slice(i - halfWindow, i + halfWindow + 1);
    let hydrophobicity = calculateHydrophobicity(hydrophobicitySubsequence);
    hydrophobicityArray.push(hydrophobicity);
    if (overHydrophobicityThresholdTrue(hydrophobicity, threshold)) {
      markedHydrophobicitySequence += markHighHydrophobicity(bufferSequence[i]);
    } else {
      markedHydrophobicitySequence += bufferSequence[i];
    }
  }
  return { markedHydrophobicitySequence, hydrophobicityArray };
}



// inputs a window of characters in the sequence and returns true if it matches the pattern specified. Returns false otherwise.
function patternTrue(sequence) {
  const pattern = /AL[AVLIMPFYWSTNCHQG]{3}LW/g;
  return pattern.test(sequence);
}

// Function to calculate the average hydrophobicity for a given sequence of amino acids
function calculateHydrophobicity(subsequence) {
  let total = 0;
  for (let i = 0; i < subsequence.length; i++) {
    total += amino_acids_hydrophobicity[subsequence[i]];

  }
  return (total / subsequence.length).toFixed(2);
}

// Function that determines if hydrophobicity is over the threashold
function overHydrophobicityThresholdTrue(hydrophobicity, threashold) {
  if (hydrophobicity >= threashold) {
    return true;
  } else {
    return false;
  }
  
}

// Function to add HTML tags if pattern is found
function markPattern(sequence) {
  return '<mark class="pattern">' + sequence + '</mark>';
}

// Function to add HTML tags 
function markHighHydrophobicity(sequence) {
  return '<mark class="high-hydrophobicity">' + sequence + '</mark>';
}

//adds a buffer to the main sequence for ease of calculating hydrophobicity
function addBuffer(inputString) {
  let buffer = Array(9).fill(' ').join('');
  return buffer + inputString + buffer;
}
