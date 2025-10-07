import ChatBot from './components/chat/ChatBot';
import ReviewList from './components/reviews/ReviewList';

function App() {
   const mode = import.meta.env.VITE_APP_MODE;
   return (
      <div className="p-4 h-screen">
         {mode === 'chatbot' ? <ChatBot /> : <ReviewList productId={2} />}
      </div>
   );
}

export default App;
