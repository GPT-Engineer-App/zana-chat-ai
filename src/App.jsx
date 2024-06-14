import { useEffect } from 'react';
import { initializeAutoComplete } from './utils/commandAutoComplete';
import { colorText } from './utils/colorOutput';
import { getSetting } from './config/settings';

function App() {
  useEffect(() => {
    if (getSetting('autoComplete')) {
      initializeAutoComplete();
    }
  }, []);

  const handleCommand = (command) => {
    if (getSetting('colorOutput')) {
      console.log(colorText(`Executing command: ${command}`, 'green'));
    } else {
      console.log(`Executing command: ${command}`);
    }
  };

  return (
    <div>
      <h1>Welcome to ZANA</h1>
      <input type="text" onKeyDown={(e) => e.key === 'Enter' && handleCommand(e.target.value)} />
    </div>
  );
}

export default App;