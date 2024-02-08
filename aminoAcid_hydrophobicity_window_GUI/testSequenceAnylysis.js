// Import the assert module for assertion functions
const assert = require('assert');

import { 
  calculateHydrophobicity, 
  overHydrophobicityThresholdTrue, 
  markHighHydrophobicity, 
  markPattern, 
  addBuffer, 
  markPatternsInSequence, 
  markAndRecordHydrophobicityInSequence, 
  patternTrue, 
  analyzeSequence 
} from './sequenceAnalysis.js';

// Define your tests
describe('Protein Sequence Analysis', function() {
  describe('#calculateHydrophobicity()', function() {
    it('should return correct hydrophobicity for a given sequence', function() {
      let sequence = 'VSTNCHQGALPYWLWVSTN';
      let expected = '-0.08';
      assert.equal(calculateHydrophobicity(sequence), expected);
    });
  });

  describe('#overHydrophobicityThresholdTrue()', function() {
    it('should return true if hydrophobicity is over the threshold', function() {
      let hydrophobicity = 2.0;
      let threshold = 1.6;
      assert.equal(overHydrophobicityThresholdTrue(hydrophobicity, threshold), true);
    });

    it('should return false if hydrophobicity is under the threshold', function() {
      let hydrophobicity = 1.0;
      let threshold = 1.6;
      assert.equal(overHydrophobicityThresholdTrue(hydrophobicity, threshold), false);
    });
  });

  describe('#markHighHydrophobicity()', function() {
    it('should add the correct HTML tag for high hydrophobicity', function() {
      let sequence = 'A';
      let threshold = 1.6;
      assert.equal(markHighHydrophobicity(sequence, threshold), '<mark class="high-hydrophobicity">A</mark>');
    });
  });

  describe('#markPattern()', function() {
    it('should add the correct HTML tag for pattern match', function() {
      let sequence = 'ALAAAALW';
      assert.equal(markPattern(sequence), '<mark class="pattern">ALAAAALW</mark>');
    });
  });

  describe('#addBuffer()', function() {
    it('should add the correct buffer to the sequence', function() {
      let sequence = 'ARND';
      assert.equal(addBuffer(sequence), '         ARND         ');
    });
  });

  describe('#markPatternsInSequence()', function() {
    it('should correctly mark patterns in the sequence', function() {
      let sequence = 'ALAAALW';
      let expected = '<mark class="pattern">ALAAALW</mark>';
      assert.equal(markPatternsInSequence(sequence), expected);
    });
  });

  describe('#markAndRecordHydrophobicityInSequence()', function() {
    it('should correctly mark high hydrophobicity in the sequence and record hydrophobicity values', function() {
      let sequence = 'AAAAAAAAACAAAAAAAAA'
      
      let threshold = 1.6;
      let expected = {
        markedHydrophobicitySequence: "AAAAAAA<mark class=\"high-hydrophobicity\">A</mark><mark class=\"high-hydrophobicity\">A</mark><mark class=\"high-hydrophobicity\">C</mark><mark class=\"high-hydrophobicity\">A</mark><mark class=\"high-hydrophobicity\">A</mark>AAAAAAA",
        hydrophobicityArray: [
        "0.98",
        "1.08",
        "1.17",
        "1.27",
        "1.36",
        "1.46",
        "1.55",
        "1.65",
        "1.74",
        "1.84",
        "1.74",
        "1.65",
        "1.55",
        "1.46",
        "1.36",
        "1.27",
        "1.17",
        "1.08",
        "0.98"]  
      };
      console.log(markAndRecordHydrophobicityInSequence(sequence, threshold));
      assert.deepEqual(markAndRecordHydrophobicityInSequence(sequence, threshold), expected);
    });
  });

  describe('#patternTrue()', function() {
    it('should return true if the sequence matches the pattern', function() {
      let sequence = 'ALAAALW';
      assert.equal(patternTrue(sequence), true);
    });

    it('should return false if the sequence does not match the pattern', function() {
      let sequence = 'ARNDALL';
      assert.equal(patternTrue(sequence), false);
    });
  });

  describe('#analyzeSequence()', function() {
    it('should correctly analyze the sequence', function() {
      let sequence = 'ALAAALW';
      let threshold = 1.6;
      let expected = {
        markedPatternSequence: '<mark class="pattern">ALAAALW</mark>',
        markedHydrophobicitySequence: 'ALAAALW',
        hydrophobicityArray: ["0.73",
        "0.73",
        "0.73",
        "0.73",
        "0.73",
        "0.73",
        "0.73"]
      };
      assert.deepEqual(analyzeSequence(sequence, threshold), expected);
    });
  });

  // Add more describe blocks for other functions as needed
});
