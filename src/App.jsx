import readline from 'readline';
import termcolor from 'termcolor';
import settings from './settings';

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
  completer: (line) => {
    const completions = 'help error success info'.split(' ');
    const hits = completions.filter((c) => c.startsWith(line));
    return [hits.length ? hits : completions, line];
  },
});

rl.on('line', (input) => {
  switch (input.trim()) {
    case 'error':
      console.log(termcolor(settings.outputColor.error, 'This is an error message.'));
      break;
    case 'success':
      console.log(termcolor(settings.outputColor.success, 'This is a success message.'));
      break;
    case 'info':
      console.log(termcolor(settings.outputColor.info, 'This is an info message.'));
      break;
    default:
      console.log('Unknown command');
      break;
  }
  rl.prompt();
});

rl.prompt();