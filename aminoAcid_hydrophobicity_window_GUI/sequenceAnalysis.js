export {
  calculateHydrophobicity,
  overHydrophobicityThresholdTrue,
  markHighHydrophobicity,
  markPattern,
  addBuffer,
  markPatternsInSequence,
  markAndRecordHydrophobicityInSequence,
  patternTrue,
  analyzeSequence,
  extractSequenceFASTA,
  regularExpressionWindowLength
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
function analyzeSequence(sequence, threshold, pattern, patternWindow) {
  let markedPatternSequence = markPatternsInSequence(sequence, pattern, patternWindow);
  let { markedHydrophobicitySequence, hydrophobicityArray } = markAndRecordHydrophobicityInSequence(sequence, threshold);
  let combinedMarkedSequence = combineMarks(markedPatternSequence, markedHydrophobicitySequence).slice(1);

  return { markedPatternSequence, markedHydrophobicitySequence, hydrophobicityArray, combinedMarkedSequence };
}

// HELPER FUNCTIONS

// Helper function to mark patterns in the sequence
function markPatternsInSequence(sequence, pattern, patternWindow) {
  console.log("Pattern window is: " + patternWindow);
  let markedPatternSequence = '';
  for (let i = 0; i < sequence.length; i++) {
    let patternSubsequence = sequence.slice(i, i + patternWindow);
    if (patternTrue(patternSubsequence, pattern)) {
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

function combineMarks(pSequence, hSequence) {
  let combined = "";
  let pMarkStart = "<mark class=\"p\">";
  let hMarkStart = "<mark class=\"h\">";
  let pMarkEnd = "</mark>";
  let hMarkEnd = "</mark>";
  let bMarkStart = "<mark class=\"b\">";
  let bMarkEnd = "</mark>";

  let i = 0;
  let j = 0;
  let inPMark = false;
  let inHMark = false;

  while (i < pSequence.length && j < hSequence.length) {
    if (pSequence.substring(i, i + pMarkStart.length) === pMarkStart) {
      inPMark = true;
      i += pMarkStart.length;
    } else if (pSequence.substring(i, i + pMarkEnd.length) === pMarkEnd) {
      inPMark = false;
      i += pMarkEnd.length;
    } else if (hSequence.substring(j, j + hMarkStart.length) === hMarkStart) {
      inHMark = true;
      j += hMarkStart.length;
    } else if (hSequence.substring(j, j + hMarkEnd.length) === hMarkEnd) {
      inHMark = false;
      j += hMarkEnd.length;
    } else if (inPMark && inHMark) {
      combined += bMarkStart + pSequence[i] + bMarkEnd;
      i++;
      j++;
    } else if (inPMark) {
      combined += pMarkStart + pSequence[i] + pMarkEnd;
      i++;
      j++;
    } else if (inHMark) {
      combined += hMarkStart + hSequence[j] + hMarkEnd;
      i++;
      j++;
    } else {
      combined += pSequence[i];
      i++;
      j++;
    }
  }

  // Append the remaining part of the longer sequence
  if (i < pSequence.length) {
    combined += pSequence.substring(i);
  } else if (j < hSequence.length) {
    combined += hSequence.substring(j);
  }

  return " " + combined;
}

// inputs a window of characters in the sequence and returns true if it matches the pattern specified. Returns false otherwise.
function patternTrue(sequence, pattern) {
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
  return hydrophobicity >= threashold;
  
}

// Function to add HTML tags if pattern is found
function markPattern(sequence) {
  let markedSequence = '';
  for (let i = 0; i < sequence.length; i++) {
    markedSequence += '<mark class="p">' + sequence[i] + '</mark>';
  }
  return markedSequence;
}

// Function to add HTML tags 
function markHighHydrophobicity(sequence) {
  return '<mark class="h">' + sequence + '</mark>';
}

//adds a buffer to the main sequence for ease of calculating hydrophobicity
function addBuffer(inputString) {
  let buffer = Array(9).fill(' ').join('');
  return buffer + inputString + buffer;
}

function extractSequenceFASTA(fastaFileContent) {
  // Split the file content into lines
  let lines = fastaFileContent.split('\n');

  // Filter out the description line and join the rest
  let sequence = lines.filter(line => !line.startsWith('>')).join('');

  return sequence;
}

function regularExpressionWindowLength(regularExpressionString) {
  let insideBrackets = false;
  let insideBrace = false;
  let braceContent = '';
  let count = 0;

  for (let i = 0; i < regularExpressionString.length; i++) {
      if (regularExpressionString[i] === '[') {
          insideBrackets = true;
      } else if (regularExpressionString[i] === ']') {
          insideBrackets = false;
      } else if (!insideBrackets) {
          if (regularExpressionString[i] === '{') {
              insideBrace = true;
              braceContent = '';
          } else if (regularExpressionString[i] === '}') {
              insideBrace = false;
              count += Number(braceContent);
          } else if (insideBrace) {
              braceContent += regularExpressionString[i];
          } else {
              count++;
          }
      }
  }

  return count;
};
