import React, { useState,useEffect } from 'react';
import Data from './Data';
import './App.css';
import Button from 'react-bootstrap/Button'
import Alert from 'react-bootstrap/Alert';


const App = () => {
  const [inputText, setInputText] = useState('');
  const [showDescription, setShowDescription] = useState(false);
  const [animal, setAnimal] = useState('');
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false); 

  const handleInputChange = (e) => {
    setInputText(e.target.value);
    setError('');
  };

  const handleShowDescription = () => {
    const enteredAnimal = inputText.toLowerCase();
    if (Data[enteredAnimal]) {
      setAnimal(enteredAnimal);
      setLoading(true); 
      setShowDescription(true);
      setError('');
      setTimeout(() => {
        setLoading(false); 
      }, 10000); // 10 seconds (10000 milliseconds) loading time
    } else {
      setError(`Sorry, no information found for "${enteredAnimal}".`);
    }
  };
  

  const handleHideDescription = () => {
    setShowDescription(false);
    setInputText('');
    setError('');
  };

  const animalDescription = showDescription ? Data[animal]?.description : null;

  return (
    <div className="App">
      <div className="textarea-container">
        <div>
        <h3 className='head'>Enter Your Input Below:👇</h3>
              <textarea
                 className='textarea'
                 rows="4"
                 cols="50"
                 placeholder="Enter Something"
                 value={inputText}
                 onChange={handleInputChange}
               />
                 
       <div className="button-container" style={{display:'flex',flexDirection:'column',border:'3px solid #423F3E' }}>
                      <Button variant="primary" size="lg"  onClick={handleShowDescription} disabled={!inputText || showDescription}>
       
                         Submit
                      </Button>
                      <Button variant="secondary"  size="lg"onClick={handleHideDescription} disabled={!showDescription}>
                         Clear Input
                      </Button>
                    </div>
                    <div style={{display:'flex',flexDirection:'row',marginTop:'30px'}} >
                      <Button variant='light' size="lg" style={{marginLeft:'50px',backgroundColor:''}}>Help?</Button>
                      <Button variant='light' size="lg" style={{marginLeft:'120px'}}>Click to Know More!</Button>
                      </div>

        </div>
       

               <div style={{display:'flex',flexDirection:'column',alignItems:'center'}}>
                      {loading && <div></div>}
                         {error && (
                         <Alert variant="danger" className="error-message">
                         {error}
                         </Alert>
                          )}
                          {animalDescription && (
                      <div className="description-box">
                           <Typewriter text={animalDescription}loading={loading} />
                      </div>
                          )}
              </div>
       </div>

    </div>
  );
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
    }, 50);

    setTimeout(() => {
      setLoading(false); 
    }, 1000); 

    return () => clearInterval(typingInterval);
  }, [isLoading, text]);

  return <div className="typewriter-box">
    {isLoading ? 'Generating...' : text.slice(0, index)}
    </div>;
};

export default App;








