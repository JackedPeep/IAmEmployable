
import { 
  analyzeSequence,
  extractSequenceFASTA,
  regularExpressionWindowLength 
} from './sequenceAnalysis.js';

let analysis;

let slider = document.getElementById("hydrophobicityThreshold");
let output = document.getElementById("demo"); 

output.innerHTML = slider.value / 10 - 10; // Display the default slider value

// Update the current slider value (each time you drag the slider handle)
slider.oninput = function() {
  output.innerHTML = (this.value / 10 - 10).toFixed(1);
}

window.updateSliderValue = function(val) {
  let output = document.getElementById("demo"); 
  output.innerHTML = (val / 10 - 10).toFixed(1);
}

window.toggleInput = function(isAccessionSelected) {
  document.getElementById('accession').disabled = !isAccessionSelected;
  document.getElementById('sequence').disabled = isAccessionSelected;
};

document.getElementById('simplePattern').addEventListener('change', function() {
  if (this.checked) {
    document.getElementById('simplePatternMark').style.display = 'block';
    document.getElementById('complexPatternInput').style.display = 'none';
  }
  displayResults(true);  // Display the pattern sequence output
});

document.getElementById('complexPattern').addEventListener('change', function() {
  if (this.checked) {
    document.getElementById('simplePatternMark').style.display = 'none';
    document.getElementById('complexPatternInput').style.display = 'block';
  }
  displayResults(false);  // Display the hydrophobicity sequence output
});

window.togglePatternInput = function(isSimplePatternSelected) {
  document.getElementById('simplePatternMark').style.display = isSimplePatternSelected ? 'block' : 'none';
  document.getElementById('complexPatternInput').style.display = isSimplePatternSelected ? 'none' : 'block';
};

// Trigger the change event for the default checked radio button on page load
window.onload = function() {
  document.getElementById('simplePattern').dispatchEvent(new Event('change'));
};


window.displayResults = function(isPatternSelected) {
  // Get the result div
  const resultDiv = document.getElementById('result');

  // Display the marked pattern sequence or the marked hydrophobicity sequence based on the selected display type
  if (isPatternSelected) {
    resultDiv.innerHTML = `<p>Marked Pattern Sequence:</p> ${analysis.markedPatternSequence}`;
  } else {
    resultDiv.innerHTML = `<p>Marked Hydrophobicity Sequence:</p> ${analysis.markedHydrophobicitySequence}`;
  }
}

window.handleSubmit = async (event) => {
  event.preventDefault(); // Prevent the form from submitting normally
  
  const accessionInput = document.getElementById('accession');
  const sequenceInput = document.getElementById('sequence');
  
  // Use the output value instead of the slider value
  const hydrophobicityThreshold = Number(document.getElementById('demo').innerHTML);
  
  let pattern;
  let patternWindow;

  // Check which pattern option is selected
  let simplePatternOption = document.getElementById('simplePattern');
  let complexPatternOption = document.getElementById('complexPattern');

  console.log('simplePatternOption.checked:', simplePatternOption.checked);
  console.log('complexPatternOption.checked:', complexPatternOption.checked);
  
  

  if (simplePatternOption.checked) {
    // If the simple pattern was selected
    let simplePattern = document.getElementById("simplePatternInput").value;
    console.log('simplePattern:', simplePattern);
    pattern = new RegExp(`${simplePattern}`, 'g');
    patternWindow = simplePattern.length;

  } else if (complexPatternOption.checked) {
    // If the advanced pattern was selected
    let patternStart = document.getElementById("patternStartInput").value;
    let patternMiddle = document.getElementById("patternMiddleInput").value;
    let patternEnd = document.getElementById("patternEndInput").value;
    console.log('patternStart:', patternStart);
    console.log('patternMiddle:', patternMiddle);
    console.log('patternEnd:', patternEnd);
    let patternString = `${patternStart}${patternMiddle}${patternEnd}`;
    pattern = new RegExp(patternString, 'g');
    patternWindow = regularExpressionWindowLength(patternString);
  }

  if (!accessionInput.disabled) {
    const proteinId = accessionInput.value;
    const fastaFile = await fetchFASTA(proteinId);
    console.log(fastaFile);
    const sequence = extractSequenceFASTA(fastaFile);
    console.log(sequence);
    analysis = analyzeSequence(sequence, hydrophobicityThreshold);
  } else if (!sequenceInput.disabled) {
    const sequence = sequenceInput.value;
    analysis = analyzeSequence(sequence, hydrophobicityThreshold);
    console.log(analysis);
  }

  // Display the initial results based on the selected display type
  displayResults(document.getElementById('patternOption').checked);
  
  plotHydrophobicity(analysis.hydrophobicityArray);
};

// Function to plot hydrophobicity
function plotHydrophobicity(hydrophobicityArray) {
  let data = [{
      y: hydrophobicityArray,
      mode: 'lines',
      type: 'scatter'
  }];

  let layout = {
      title: 'Hydrophobicity Plot',
      xaxis: {
          title: 'Residue Position'
      },
      yaxis: {
          title: 'Hydrophobicity Index'
      }
  };

  Plotly.newPlot('hydrophobicityPlot', data, layout);
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

