import React, { useState, useEffect } from 'react';
import Button from 'react-bootstrap/Button';
import Alert from 'react-bootstrap/Alert';
import axios from 'axios';
import './App.css';

const App = () => {
  const [inputText, setInputText] = useState('');
  const [showDescription, setShowDescription] = useState(false);
  const [mainDescription, setmainDescription] = useState('');
  const [error, setError] = useState('');
  
  const handleInputChange = (e) => {
    setInputText(e.target.value);
    setError('');
  };

  const handleShowDescription = async () => {
    try {
      const response = await axios.post('http://localhost:5000/process', {
        inputText: inputText,
        min_word_count: 50,
      });

      setmainDescription(response.data.summary);
      setShowDescription(true);
    } catch (error) {
      console.log("Here We Go !")
      console.error('\n\nerror:', error);
      setError('An error occurred while processing.');
    }
  };

  const handleHideDescription = () => {
    setShowDescription(false);
    setInputText('');
    setError('');
  };

  const Typewriter = ({ text }) => {
    const [isLoading, setLoading] = useState(true);
    const [index, setIndex] = useState(0);

    useEffect(() => {
      const typingInterval = setInterval(() => {
        if (!isLoading) {
          setIndex((prevIndex) => {
            if (prevIndex === text.length - 1) {
              clearInterval(typingInterval);
            }
            return prevIndex + 1;
          });
        }
      }, 15); 

      setTimeout(() => {
        setLoading(false);
      }, 500); 

      return () => clearInterval(typingInterval);
    }, [isLoading, text]);

    return <div className="typewriter-box">
      {isLoading ? 'Generating...' : text.slice(0, index + 1)}
    </div>;
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
          {/* Buttons */}
          <div className="button-container">
            <Button variant="primary" size="lg" onClick={handleShowDescription} disabled={!inputText || showDescription}>
              Submit
            </Button>
            <Button variant="secondary" size="lg" onClick={handleHideDescription} disabled={!showDescription}>
              Clear Input
            </Button>
          </div>
          {/* Help Buttons */}
          <div style={{ display: 'flex', flexDirection: 'row', marginTop: '30px' }}>
            <Button variant='light' size="lg" style={{ marginLeft: '50px', backgroundColor: '' }}>Help?</Button>
            <Button variant='light' size="lg" style={{ marginLeft: '120px' }}>Click to Know More!</Button>
          </div>
        </div>
        {/* Description */}
        <div className="description-container">
          {error && (
            <Alert variant="danger" className="error-message">
              {error}
            </Alert>
          )}
          {mainDescription && (
            <div className="description-box">
              <Typewriter text={mainDescription} />
            </div>
          )}
        </div>
      </div>
    </div>
  );
};

export default App;