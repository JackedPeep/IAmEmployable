
import { 
  analyzeSequence,
  extractSequenceFASTA 
} from './sequenceAnalysis.js';

let analysis;

window.handleSubmit = async (event) => {
  event.preventDefault(); // Prevent the form from submitting normally
  
  const accessionInput = document.getElementById('accession');
  const sequenceInput = document.getElementById('sequence');
  console.log('Accession input disabled:', accessionInput.disabled);
  console.log('Sequence input disabled:', sequenceInput.disabled);
  
  if (!accessionInput.disabled) {
    const proteinId = accessionInput.value;
    const fastaFile = await fetchFASTA(proteinId);
    console.log(fastaFile);
    const sequence = extractSequenceFASTA(fastaFile);
    console.log(sequence);
    analysis = analyzeSequence(sequence, 1.6);
  } else if (!sequenceInput.disabled) {
    const sequence = sequenceInput.value;
    analysis = analyzeSequence(sequence, 1.6);
    console.log(analysis);
  }

  // Display the initial results based on the selected display type
  displayResults(document.getElementById('patternOption').checked);
};

window.toggleInput = function(isAccessionSelected) {
  document.getElementById('accession').disabled = !isAccessionSelected;
  document.getElementById('sequence').disabled = isAccessionSelected;
};

window.displayResults = function(isPatternSelected) {
  // Get the result div
  const resultDiv = document.getElementById('result');

  // Display the marked pattern sequence or the marked hydrophobicity sequence based on the selected display type
  if (isPatternSelected) {
    resultDiv.innerHTML = `<p>Marked Pattern Sequence: ${analysis.markedPatternSequence}</p>`;
  } else {
    resultDiv.innerHTML = `<p>Marked Hydrophobicity Sequence: ${analysis.markedHydrophobicitySequence}</p>`;
  }
}

//Fetch function that gets the fasta file formated protein sequence
const fetchFASTA = async (proteinId) => {
  const url = `https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=protein&id=${proteinId}&rettype=fasta&retmode=text`;

  try {
    const response = await fetch(url);
    const data = await response.text();
    return data;
  } catch (error) {
    console.error('Error:', error);
  }
};