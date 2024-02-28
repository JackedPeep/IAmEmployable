
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
});

document.getElementById('complexPattern').addEventListener('change', function() {
  if (this.checked) {
    document.getElementById('simplePatternMark').style.display = 'none';
    document.getElementById('complexPatternInput').style.display = 'block';
  }
});

window.togglePatternInput = function(isSimplePatternSelected) {
  document.getElementById('simplePatternMark').style.display = isSimplePatternSelected ? 'block' : 'none';
  document.getElementById('complexPatternInput').style.display = isSimplePatternSelected ? 'none' : 'block';
};

// Trigger the change event for the default checked radio button on page load
window.onload = function() {
  document.getElementById('simplePattern').dispatchEvent(new Event('change'));
};

document.getElementById('downloadButton').addEventListener('click', async function(event) {
  let accenssionInput = document.getElementById('accession').value;
  
  let fastaData = await fetchFASTA(accenssionInput);

  // Convert the FASTA data to a CSV Blob
  let blob = await fastaToExcel(fastaData);

  // Create an object URL for the Blob
  let url = URL.createObjectURL(blob);

  // Create a link element
  let link = document.createElement("a");

  // Set the link's href to the object URL
  link.href = url;

  // Set the download attribute to the desired file name
  link.download = `NCBI_${accenssionInput}.csv`;

  // Append the link to the body
  document.body.appendChild(link);

  // Programmatically click the link to start the download
  link.click();

  // Remove the link from the body
  document.body.removeChild(link);
});

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

  let displayType;
  if (document.getElementById('patternOption').checked) {
    displayType = 'pattern';
  } else if (document.getElementById('hydrophobicityOption').checked) {
    displayType = 'hydrophobicity';
  } else if (document.getElementById('bothOption').checked) {
    displayType = 'both';
  }

  if (simplePatternOption.checked) {
    // If the simple pattern was selected
    let simplePattern = document.getElementById("simplePatternInput").value;
    if (!simplePattern || !simplePattern.match(/^[ACDEFGHIKLMNPQRSTVWY\[\]\{\}0-9]+$/)) {
      alert('Please enter a valid simple pattern. It should only contain capital letters that align with amino acid single letter abbreviations, brackets [], braces {}, and numbers.');
      return;
    }
    pattern = new RegExp(`${simplePattern}`, 'g');
    patternWindow = regularExpressionWindowLength(simplePattern);

  } else if (complexPatternOption.checked) {
    // If the advanced pattern was selected
    let patternStart = document.getElementById("patternStartInput").value;
    let patternMiddle = document.getElementById("patternMiddleInput").value;
    let patternEnd = document.getElementById("patternEndInput").value;
    let patternString = `${patternStart}${patternMiddle}${patternEnd}`;
    if (!patternString || !patternString.match(/^[ACDEFGHIKLMNPQRSTVWY\[\]\{\}0-9]+$/)) {
      alert('Please enter a valid complex pattern. It should only contain capital letters that align with amino acid single letter abbreviations, brackets [], braces {}, and numbers.');
      return;
    }
    pattern = new RegExp(patternString, 'g');
    patternWindow = regularExpressionWindowLength(patternString);
  }

  let analysis;
  if (!accessionInput.disabled) {
    const proteinId = accessionInput.value;
    if (!proteinId) {
      alert('Please enter a valid accession number.');
      return;
    }
    const fastaFile = await fetchFASTA(proteinId);
    const sequence = extractSequenceFASTA(fastaFile);
    analysis = analyzeSequence(sequence, hydrophobicityThreshold, pattern, patternWindow);
    document.getElementById('downloadButton').style.display = 'block';
  } else if (!sequenceInput.disabled) {
    const sequence = sequenceInput.value;
    if (!sequence || !sequence.match(/^[ACDEFGHIKLMNPQRSTVWY]+$/)) {
      alert('Please enter a valid protein sequence. It should only contain capital letters that align with amino acid single letter abbreviations.');
      return;
    }
    analysis = analyzeSequence(sequence, hydrophobicityThreshold, pattern, patternWindow);
  }

  if (analysis) {
    // Display the initial results based on the selected display type
    displayResults(displayType);
    
    plotHydrophobicity(analysis.hydrophobicityArray);

    clearFields();
  }
};

window.displayResults = function(displayType) {
  // Get the result div
  const resultDiv = document.getElementById('result');

  // Display the marked pattern sequence, the marked hydrophobicity sequence, or both based on the selected display type
  switch (displayType) {
    case 'pattern':
      resultDiv.innerHTML = `<p>Marked Pattern Sequence:</p> ${analysis.markedPatternSequence}`;
      break;
    case 'hydrophobicity':
      resultDiv.innerHTML = `<p>Marked Hydrophobicity Sequence:</p> ${analysis.markedHydrophobicitySequence}`;
      break;
    case 'both':
      resultDiv.innerHTML = `<p>Marked Sequence:</p>${analysis.combinedMarkedSequence}`
      break;
  }
}

function clearFields() {
  document.getElementById('accessionOption').checked = true;
  document.getElementById('simplePattern').checked = true;
}

// Function to plot hydrophobicity
function plotHydrophobicity(hydrophobicityArray) {
  let data = [{
      y: hydrophobicityArray,
      mode: 'lines',
      type: 'scatter'
  }];

  let layout = {
      title: 'Hydrophobicity Plot(Kyte-Doolittle)',
      xaxis: {
          title: 'Residue Position'
      },
      yaxis: {
          title: 'Hydrophobicity Index(Kyte-Doolittle)'
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

function fastaToExcel(fasta) {
  // Split the FASTA string into lines
  let lines = fasta.split('\n');

  // The first line is the identifier and description
  let identifierAndDescription = lines[0].substring(1); // Remove the '>' character

  // Split the identifier and description into separate variables
  let [identifier, ...descriptionParts] = identifierAndDescription.split(' ');
  let description = descriptionParts.join(' ');

  // The rest of the lines make up the sequence
  let sequence = lines.slice(1).join('');

  // Create a CSV string with comma as separator
  let csv = `"Identifier","Description","Sequence"\n"${identifier}","${description}","${sequence}"`;

  // Create a new Blob with the CSV data
  let blob = new Blob([csv], { type: 'text/csv;charset=utf-8;' });

  return blob;
}

