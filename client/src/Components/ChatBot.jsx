const ChatBot = () => {
  const api = import.meta.env.VITE_AZURE_WEB_APP_URL;
  console.log(`S${api}/chatbot`);

  return (
    <div style={{ width: "100vw", height: "100vh", margin: 0 }}>
      <iframe
        // src="http://localhost:8000/chatbot"
        // src="https://ayurvision-server.onrender.com/chatbot/"
        src={`${api}/chatbot`}
        width="100%"
        height="94%"
        style={{ border: "none" }}
        title="chat bot"
        sandbox="allow-same-origin allow-top-navigation"
      ></iframe>
    </div>
  );
};

export default ChatBot;
