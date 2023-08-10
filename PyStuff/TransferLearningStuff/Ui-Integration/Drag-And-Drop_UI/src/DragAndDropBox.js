import React, { useState, useRef } from 'react';
import Load from './Load';
import Button from 'react-bootstrap/Button';




const DragAndDropBox = () => {
  const [image, setImage] = useState(null);
  const [showLoad, setShowLoad] = useState(false);
  const fileInputRef = useRef(null);

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
  };

  const handleChooseFileClick = () => {
    fileInputRef.current.click();
  };

  const handleSubmitClick = () => {
    if (image) {
      setShowLoad(true);
    }
  };

  return (
    <div style={{height:'100vh',display:'flex',flexDirection:'row',justifyContent:'center',alignItems:'center',gap:'60px',background:'#171010'}}>
          <div>
            <div>
            <h1 style={{color:'white'}}>Input:</h1>
            </div>
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
            <div style={{display:'flex',flexDirection:'column',alignItems:'center',justifyContent:'center'}}>
              <Button variant="default" size='lg' className='drag--btn' style={{backgroundColor:'black',color:'white'}}>Drag and drop an image  🖼️<h3 style={{color:'grey'}}>(Or)</h3>Click to add file 🖱️</Button>
            </div>
         
          )}
          <input
            type="file"
            accept="image/*"
            ref={fileInputRef}
            style={{ display: 'none' }}
            onChange={handleFileInputChange}
          />
        </div>

        <div style={{display:'flex',flexDirection:'column',gap:'20px',marginTop:'20px',border:'4px solid #423F3E'}}>
        <Button variant="primary"   onClick={handleSubmitClick} className='submit--btn'>
          Submit
        </Button>
           <Button variant="secondary"  onClick={handleClearClick} className='clear--btn'>
           Clear
         </Button>
        </div>
        <div style={{backgroundColor:'#E82155',display:'flex',flexDirection:'column',alignItems:'center',justifyContent:'center',borderRadius:'60%',marginTop:'20px'}}>
          <Button variant='default' style={{color:'white'}} >More Tools</Button>
        </div>
        
</div>
        <div className='loading'>
          {showLoad && <Load imageUrl={image} />}
        </div>
    </div>
  );
};
export default DragAndDropBox;

