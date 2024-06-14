import readline from 'readline';

const commands = [
  'help',
  'exit',
  'list',
  'show',
  'create',
  'delete',
  'update',
  'search',
  'config',
  'settings',
];

export const initializeAutoComplete = () => {
  readline.createInterface({
    input: process.stdin,
    output: process.stdout,
    completer: (line) => {
      const hits = commands.filter((c) => c.startsWith(line));
      return [hits.length ? hits : commands, line];
    },
  });
};