import React, { useState, useEffect } from 'react';
import Button from 'react-bootstrap/Button';
import Alert from 'react-bootstrap/Alert';
import { RingLoader } from 'react-spinners';
import { css } from '@emotion/react';
import axios from 'axios';
import './App.css';

const override = css`
  display: block;
  margin: 0 auto;
  border-color: red;
`;

const Typewriter = ({ text }) => {
  const [index, setIndex] = useState(0);
  useEffect(() => {
    const typingInterval = setInterval(() => {
      setIndex((prevIndex) => {
        if (prevIndex === text.length - 1) {
          clearInterval(typingInterval);
        }
        return prevIndex + 1;
      });
    }, 10); 
    return () => clearInterval(typingInterval);
  }, [text]);

  return <div className="typewriter-box">
    {text.slice(0, index + 1)}
  </div>;
};


const App = () => {
  const [mainDescription, setMainDescription] = useState('');
  const [isProcessing, setIsProcessing] = useState(false);
  const [minWordCount, setMinWordCount] = useState(75);
  const [error, setError] = useState('');
  const [inputText, setInputText] = useState('');

  useEffect(() => {
    setMainDescription('');
  }, [inputText]);

  const handleInputChange = (e) => {
    setInputText(e.target.value);
    setError('');
  };

  const handleShowDescription = async () => {
    try {
      setIsProcessing(true);
      setError('');
      const response = await axios.post('http://localhost:5000/process', {
        inputText: inputText,
        min_word_count: minWordCount,
      });
      setMainDescription(response.data.summary);
    } catch (error) {
      console.log("Here We Go !");
      console.error('\n\nerror:', error);
      setError('An error occurred while processing.');
    } finally {
      setIsProcessing(false);
    }
  };

  const handleHideDescription = () => {
    setInputText('');
    setError('');
  };

  return (
    <div className="App">
      <div className="textarea-container">
        <div>
          {/* Input Textarea */}
          <textarea
            className='textarea'
            rows="4"
            cols="50"
            placeholder="Enter Something"
            value={inputText}
            onChange={handleInputChange}
          />
          {/* Minimum Word Count Input */}
          <div className="min-word-count-container">
          <label style={{ color: 'white' }}>Minimum Word Count : -</label>
          <input
            type="number"
            value={minWordCount}
            onChange={(e) => {
              const value = parseInt(e.target.value);
              setMinWordCount(Math.max(10, value));
            }}
          />
          </div>
          {/* Buttons */}
          <div className="button-container">
            <Button variant="primary" size="lg" onClick={handleShowDescription} disabled={!inputText || isProcessing}>
              Submit
            </Button>
            <Button variant="secondary" size="lg" onClick={handleHideDescription}>
              Clear Input
            </Button>
          </div>
        </div>
        {/* Description */}
        <div className="description-container">
          {error && (
            <Alert variant="danger" className="error-message">
              {error}
            </Alert>
          )}
          {/* Conditionally render loading spinner */}
          <div className="description-box">
            {isProcessing && (
              <div className="loading-box">
                <RingLoader css={override} size={100} color={'#123abc'} loading={true} />
              </div>
            )}
            {mainDescription && !isProcessing && (
              <Typewriter text={mainDescription} />
            )}
          </div>
        </div>
      </div>
    </div>
  );
};

export default App;