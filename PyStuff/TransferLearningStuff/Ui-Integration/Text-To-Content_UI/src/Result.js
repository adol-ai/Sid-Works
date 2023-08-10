import React, { useState } from "react";
import Button from 'react-bootstrap/Button';

export default function App() {
  const [inputValue, setInputValue] = useState("");
  const [content, setContent] = useState(null);
  const [loading, setLoading] = useState(false);
  const [clearInput, setClearInput] = useState(false); 

  const handleInputChange = (event) => {
    setInputValue(event.target.value);
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    setLoading(true); // Show loading spinner before generating content

    // Simulate a delay of 5 seconds before generating content
    setTimeout(() => {
      if (inputValue.toLowerCase() === "music") {
        const audioSources = ["music.mp3", "music2.mp3"];
        const randomIndex = Math.floor(Math.random() * audioSources.length);
        const randomAudioSrc = audioSources[randomIndex];

        setContent(<audio controls><source src={randomAudioSrc} type="audio/mpeg" /></audio>);
      } else if (inputValue.toLowerCase() === "video") {
        setContent(<iframe 
          width="600" 
          height="300"
          src="dance.mp4"
          title="Video"
        />);
      } else if (inputValue.toLowerCase() === "image") {
        setContent(<img src="logo512.png" alt="Text Image" style={{ width: "300px", height: "200px" }} />);
      } else {
        setContent(null);
      }

      setLoading(false); // Hide loading spinner after content generation
    }, 5000); // 5000 milliseconds (5 seconds)
  };

  const handleClearInput = () => {
    setInputValue("");
    setClearInput(true);
  };

  React.useEffect(() => {
    if (clearInput) {
      setInputValue("");
      setClearInput(false);
    }
  }, [clearInput]);

  return (
    <div>
      <div className="headline">
        <h1 className="h1">Content Generator</h1>
      </div>

      <div className="main" style={{display:'flex',flexDirection:'column', height:'100vh',justifyContent:'center',alignItems:'center'}}>
        <div className="content" style={{display:'flex',flexDirection:'column'}}>
          <div className="input--text" style={{paddingLeft:'209px',display:'flex',flexDirection:'row',color:'black',height:'50px'}}>
            <div className="input">
              <h2>Your Input: </h2>
            </div>
            <div className="out" style={{marginLeft:'437px',color:'white'}}>
              <h2>⬇ Your Output Will Be Generated Here:</h2>
            </div>
          </div>
          <form onSubmit={handleSubmit}>
            <textarea
              style={{marginLeft:'50px',cursor:'default'}}
              placeholder="Enter your Thoughts"
              className="text"
              value={inputValue}
              onChange={handleInputChange}
            ></textarea>
            <Button
              type="submit"
              variant="success"
              className="submit--btn"
              size="lg"
            >
              Submit
            </Button>

            <Button variant="secondary"  onClick={handleClearInput} className='clear--btn' size="lg">
              Clear
            </Button>
            <div className="output">
              {loading ? (
                <div className="loader"></div>
              ) : (
                content
              )}
            </div>
          </form>
        </div>
      </div>

      <div className="guide">
        <h1 style={{marginLeft:'20px'}}>Guidance:</h1>
        <p>
          1. You can retrieve img/mp3/mp4 Files.
          <br/>
          2. It will automatically start generating when you click 'submit'.
          <br/>
          3. Wait for a while when AI is generating the solution.
        </p>
      </div>

    </div>
  );
}
