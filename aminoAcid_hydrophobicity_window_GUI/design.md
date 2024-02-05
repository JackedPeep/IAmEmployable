Front-End (HTML + JavaScript): Create an HTML form that allows the user to input either the protein sequence or the accession number. You can use JavaScript to handle the form submission and make AJAX calls to the back-end server.
HTML

<form id="proteinForm">
  <label for="accession">Accession Number:</label><br>
  <input type="text" id="accession" name="accession"><br>
  <label for="sequence">Protein Sequence:</label><br>
  <input type="text" id="sequence" name="sequence"><br>
  <input type="submit" value="Submit">
</form>

Back-End (Node.js + Express): Create a back-end server that can receive the AJAX calls from the front-end. If the user inputs an accession number, the server should fetch the protein sequence from the NCBI website. This can be done using a library like axios or node-fetch to make HTTP requests.
JavaScript

const express = require('express');
const axios = require('axios');
const app = express();

app.post('/getProteinSequence', async (req, res) => {
  const { accession, sequence } = req.body;
  let proteinSequence = sequence;

  if (accession) {
    const response = await axios.get(`https://www.ncbi.nlm.nih.gov/sviewer/viewer.fcgi?id=${accession}&db=protein&report=fasta`);
    proteinSequence = response.data;
  }

  // Continue with processing the protein sequence...
});

Protein Sequence Processing: Once you have the protein sequence, you can process it to find all ‘AL???LW’ patterns that are in the high hydrophobicity window. This will involve implementing the Kyte-Doolittle Score Schema and scanning the protein sequence with a sliding window of size 19. If the average score within the window exceeds the threshold of 1.6, check if the pattern ‘AL???LW’ exists within that window.


function findPatterns(sequence) {
  const windowSize = 19;
  const threshold = 1.6;
  const pattern = /AL[A,V,L,I,M,P,F,Y,W,S,T,N,C,H,Q,G]{3}LW/g;
  let patterns = [];

  for (let i = 0; i < sequence.length - windowSize + 1; i++) {
    let window = sequence.substring(i, i + windowSize);
    let score = calculateKyteDoolittleScore(window);

    if (score >= threshold) {
      let match = window.match(pattern);
      if (match) {
        patterns.push(match[0]);
      }
    }
  }

  return patterns;
}

function kyteDoolittle(sequence, windowSize, threshold) {
  // Define the Kyte-Doolittle hydrophobicity values for each amino acid
  var kdValues = {
    'A': 1.8, 'R': -4.5, 'N': -3.5, 'D': -3.5, 'C': 2.5,
    'Q': -3.5, 'E': -3.5, 'G': -0.4, 'H': -3.2, 'I': 4.5,
    'L': 3.8, 'K': -3.9, 'M': 1.9, 'F': 2.8, 'P': -1.6,
    'S': -0.8, 'T': -0.7, 'W': -0.9, 'Y': -1.3, 'V': 4.2
  };

  var scores = [];
  for (var i = 0; i < sequence.length - windowSize + 1; i++) {
    var window = sequence.slice(i, i + windowSize);
    var score = 0;
    for (var j = 0; j < window.length; j++) {
      score += kdValues[window[j]];
    }
    score /= windowSize;
    scores.push(score);
  }

  // TODO: Plot the scores using a library like Chart.js
  // The x-axis should be the position in the sequence
  // The y-axis should be the Kyte-Doolittle score
  // You could highlight the windows with a score above the threshold
}
