
import { 
  analyzeSequence 
} from './sequenceAnalysis.js';

window.handleSubmit = async (event) => {
  event.preventDefault(); // Prevent the form from submitting normally
  
  const accessionInput = document.getElementById('accession');
  const sequenceInput = document.getElementById('sequence');
  console.log('Accession input disabled:', accessionInput.disabled);
  console.log('Sequence input disabled:', sequenceInput.disabled);
  
  if (!accessionInput.disabled) {
    const proteinId = accessionInput.value;
    const data = await fetchProteinSequence(proteinId);
    console.log(data);
  } else if (!sequenceInput.disabled) {
    const sequence = sequenceInput.value;
    const analysis = analyzeSequence(sequence, 1.6);
    console.log(analysis);
  }
};

window.toggleInput = function(isAccessionSelected) {
  document.getElementById('accession').disabled = !isAccessionSelected;
  document.getElementById('sequence').disabled = isAccessionSelected;
};

//Fetch function that gets the fasta file formated protein sequence
const fetchProteinSequence = async (proteinId) => {
  const url = `https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=protein&id=${proteinId}&rettype=fasta&retmode=text`;

  try {
    const response = await fetch(url);
    const data = await response.text();
    return data;
  } catch (error) {
    console.error('Error:', error);
  }
};
