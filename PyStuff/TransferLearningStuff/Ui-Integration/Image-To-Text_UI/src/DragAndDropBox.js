
import React, { useState, useRef } from 'react';
import Button from 'react-bootstrap/Button';

const DragAndDropBox = () => {
  const [image, setImage] = useState(null);
  const [showLoad, setShowLoad] = useState(false);
  const [typingText, setTypingText] = useState('');
  const [showTypewriter, setShowTypewriter] = useState(false);
  const fileInputRef = useRef(null);
  const [isLoading, setIsLoading] = useState(false);

  
  

  const handleDrop = (e) => {
    e.preventDefault();
    const file = e.dataTransfer.files[0];
    handleImage(file);
  };

  const handleDragOver = (e) => {
    e.preventDefault();
  };

  const handleFileInputChange = (e) => {
    const file = e.target.files[0];
    handleImage(file);
  };

  const handleImage = (file) => {
    const reader = new FileReader();

    reader.onloadend = () => {
      setImage(reader.result);
      setShowLoad(false);
    };

    if (file) {
      reader.readAsDataURL(file);
    }
  };

  const handleClearClick = () => {
    setImage(null);
    setTypingText('');
    setShowTypewriter(false);
  };

  const handleChooseFileClick = () => {
    fileInputRef.current.click();
  };

  const handleTypewriterEffect = (text) => {
    let index = 0;
    setShowTypewriter(true);
    const typingInterval = 103; 
  
    const typeNextCharacter = () => {
      if (index < text.length) {
        setTypingText((prevText) => prevText + text.charAt(index));
        index++;
        setTimeout(typeNextCharacter, typingInterval);
      }
    };
  
    typeNextCharacter();
  };

  const handleSubmitClick = () => {
    if (image) {
      setIsLoading(true);
      setTypingText('Creating...');
      setShowTypewriter(true);
  
      setTimeout(() => {
        setTypingText('');
        setIsLoading(false);
        handleTypewriterEffect(
          'TThe typing animation effect has become a popular way to add visual interactivity to web applications. In this blog post, we’ll explore three simple and effective ways to implement typing animations in React'
        );
      }, 5000);
    }
  };
  
  

  return (
    <main className='main'>

          <div style={{display:'flex',flexDirection:'row'}}>
         
           <div style={{display:'flex',flexDirection:'column',alignItems:'center'}}>  
           
           <h1 className='head'>
                      Upload Here:</h1>
         <div
            className="drag-and-drop-box"
            onDrop={handleDrop}
            onDragOver={handleDragOver}
            onClick={handleChooseFileClick}

          >
           
            {image ? (
              <>
                <img src={image} alt="Uploaded" className="uploaded-image"/>
              </>
            ) : (
              <div style={{display:'flex',flexDirection:'column',alignItems:'center',justifyContent:'center',marginTop:'60px'}}>
                <Button variant="default" size="lg" className="drag--btn" style={{background:'#E82155',color:'white',fontWeight:'1000'}}> 
                 Upload Image
                </Button><br/>
                <h5 style={{color:'white'}} >
                  ( or drag the image here ) 
                   </h5>
              </div>
            )}
            <br />
            <input
              type="file"
              accept="image/*"
              ref={fileInputRef}
              style={{ display: 'none' }}
              onChange={handleFileInputChange}
            />
          </div>
          <div>
          {showLoad}
          </div>
          <div style={{display:'flex',flexDirection:'row',paddingTop:'60px',gap:'70px'}}>
          <Button variant="secondary" size="lg" onClick={handleClearClick} className="clear--btn">
                Clear
              </Button>
              <Button variant="primary" size="lg" onClick={handleSubmitClick} className="submit--btn">
                Submit
              </Button>
            </div>
            <div style={{ display:'flex',flexDirection:'column',color:'white',paddingTop:'50px'}}>
            <h1>Note:</h1>
            <p>
              1.please upload (.jpg/.jpeg/.png) 🖼️ files only.<br/>
              2.Be patient ⏳ When AI generates  your solution.<br/>
              3.Upload only one ☝️file at a moment.<br/>
              4.Feel free to contact our service if any ©️<a href=""> yourservice@112.com</a>
            </p>
          </div>
           </div>
          <div style={{display:'flex',flexDirection:'row'}}>
          {isLoading ? (
  <div className="typewriter-box">
    <p>{typingText}</p>
  </div>
) : showTypewriter ? (
  <div className="typewriter-box">
    <p>{typingText}</p>
  </div>
) : null}
          </div>
          </div>
    </main>
  );
};

export default DragAndDropBox;


